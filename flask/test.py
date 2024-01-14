from io import BytesIO
from flask import Flask, request, jsonify, render_template
import requests
from PIL import Image
#from FinalModel import classify, get_bottleneck_features, get_distance, load_data
from ImageFunctions import get_color_description, load_image
import numpy as np
import tensorflow as tf
from keras.models import load_model, Model
from keras.applications import vgg16

import pandas as pd
import numpy as np
# import pickle5 as pickle
import pickle
import urllib.request
import scipy.spatial.distance
import tensorflow as tf

# img load and show
from PIL import Image
import matplotlib.pyplot as plt

import re
# models
from keras.models import load_model, Model
from keras.applications import vgg16

#load cnn model
from tensorflow import keras
import os
import pickle

# color distributions
# from ImageFunctions import get_color_description, histogram
import cv2
import imutils
import sklearn.preprocessing as preprocessing

#img load
import requests
# !pip install fake_useragent
from fake_useragent import UserAgent 
from io import BytesIO
from PIL import Image   

res = []

app = Flask(__name__)

# create vgg model with correct input size
inputs = (150, 150, 3)
vgg = vgg16.VGG16(include_top=False, weights='imagenet', 
                                     input_shape=inputs)

output = vgg.layers[-1].output
output = keras.layers.Flatten()(output)
vgg_model = Model(vgg.input, output)

#dont want model weights to change durring training
vgg_model.trainable = False
for layer in vgg_model.layers:
    layer.trainable = False


# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

# Function to preprocess the image
def preprocess_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # Convert the image to RGB
    img = img.convert("RGB")
    
    img = img.resize((150, 150))
    img_array = np.array(img)
    
    # Ensure the correct shape (1, 150, 150, 3)
    img_array = np.expand_dims(img_array, axis=0)
    img_std = img_array / 255.0
    img_std_copy = img_std.squeeze()

    return img_std_copy



def show_recommendations(groups, atts):
    '''
    show 3 images for each recommended attraction
    '''
    for idx, group in enumerate(groups):
        df = pd.DataFrame(group).reset_index()
        imgs = [df.loc[1,'url'], df.loc[25,'url'], df.loc[19,'url']]
        fig = plt.figure()
        fig.suptitle(atts[idx], fontsize="x-large")
        for i in range(3):
            res.append([imgs[i]])
            a=fig.add_subplot(1,3,i+1)
            image = load_image(imgs[i])
            plt.imshow(image,cmap='Greys_r')
            plt.axis('off')
# Function to get recommendations
def get_recommendations(img_class,img_array, img_vgg):
    '''
    get df of top attractions and siplay 3 images from top attractions
    '''
    # df = load_data()
    # load df with color and vgg descriptions
    df = load_data(img_class)
    print(df)


    #get color distribution feature vector
    bins = [8,8,8]
    img_color_des = get_color_description(img_array, bins)

    # get distances between color vectors of all imgs in class and distances between vgg vectors
    df['color_feats'] = df.apply(lambda row: get_distance(img_color_des, row[3]), axis=1)
    df['vgg_feats'] = df.apply(lambda row: get_distance(img_vgg, row[4]), axis=1)

    # create color and vgg vectors and standardize 
    min_max_scaler = preprocessing.MinMaxScaler()
    color_array = df['color_feats'].values.astype(float).reshape(-1,1)
    scaled_color_array = min_max_scaler.fit_transform(color_array)
   
    vgg_array = df['vgg_feats'].values.astype(float).reshape(-1,1)
    scaled_vgg_array = min_max_scaler.fit_transform(vgg_array)
    

    # drop color and vgg columns
    df.drop(['color_feats','vgg_feats'], axis=1, inplace=True)

    # combine arrays, weighing vgg vector depending on class
    if img_class in ['beaches/ocean']:
        total_distance =  0.5*scaled_vgg_array + scaled_color_array
    elif img_class in ['gardens/zoo']:
        total_distance =  10*scaled_vgg_array + scaled_color_array
    elif img_class in ['entertainment', 'landmarks', 'museums']:
        total_distance =  20*scaled_vgg_array + scaled_color_array
    else:
        total_distance =  1* scaled_vgg_array + scaled_color_array
   
    # add new distance column
    df['distance'] = total_distance

    # groupb attractions and find mean distance
    grouped_df = df.groupby(['name', 'location'])['distance'].mean()
    grouped_df = pd.DataFrame(grouped_df).reset_index()

    # remove attractins with no locations
    grouped_df['length'] = grouped_df.location.str.len()
    grouped_df = grouped_df[grouped_df.length > 3]

    # sort by distance ascending
    grouped_df.sort_values(by=['distance'], ascending=True, inplace=True)

    # get top 3 attractions
    top_df = grouped_df[:3].reset_index()
    atts = [top_df.loc[0,'name'], top_df.loc[1,'name'], top_df.loc[2,'name']]

    # groupp by attraction, and get groups for top 3 attractions
    grouped = df.groupby('name')
    groups = []
    for attraction in atts:
        groups.append(grouped.get_group(attraction))
    show_recommendations(groups, atts) #show recommendations

    return top_df

# Flask route to handle requests
@app.route('/get_recommendations', methods=['GET'])
def get_recommendations_endpoint():
    # Get the URL parameter from the request
    image_url = request.args.get('image_url')

    # Preprocess the image
    img_array = preprocess_image(image_url)

    # Get bottleneck features
    img_vgg = get_bottleneck_features(vgg_model, img_array)
    img_vgg_flattened = img_vgg.flatten().reshape(1, -1)

    # Classify with the CNN model
    label = classify(img_vgg_flattened, model)

    # Get recommendations
    recommendations_df = get_recommendations(label, img_array, img_vgg)

    # Convert DataFrame to dictionary
    recommendations_dict = recommendations_df.to_dict(orient='split')

    # Add label to the dictionary
    recommendations_dict['label'] = label

    # Create a JSON response
    response_data = {
        'success': True,
        'data': recommendations_dict
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)