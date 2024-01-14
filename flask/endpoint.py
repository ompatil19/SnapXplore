from flask import Flask, render_template, request, jsonify
from PIL import Image
import pandas as pd
# from FinalModel import get_color_description
import numpy as np
import requests
from io import BytesIO
from keras.models import load_model
#from FinalModel import get_recommendations
from ImageFunctions import get_bottleneck_features, load_image, show_image,get_color_description
import scipy.sparse
import sklearn.preprocessing as preprocessing
import matplotlib.pyplot as plt
import requests
import os 
import re

import pandas as pd
import numpy as np
# import pickle5 as pickle
import pickle
import urllib.request
import scipy.spatial.distance

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

ans = []
app = Flask(__name__)

model = load_model('C:/Users/prakruthimadhav/Documents/code red/trip/lets_take_a_trip-main/Notebooks/final_vgg_cnn.h5')

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

def load_data(img_class):
    # Load your DataFrame from the pickle file
    # Assuming you have a pickle file named 'img_att_loc_topics.pkl'
    df = pd.read_pickle('C:/Users/prakruthimadhav/Documents/code red/travel/Data/img_att_loc_topics_df.pkl')

    # Filter DataFrame based on the provided category (img_class)
    filtered_df = df[df['category'] == img_class]


    return filtered_df
# def preprocess_image(img_path):
#     img = Image.open(img_path)
#     img = img.resize((150, 150))
#     img_array = np.array(img) / 255.0
#     return img_array

# def preprocess_image_url(img_url):
#     response = requests.get(img_url)
#     img = Image.open(BytesIO(response.content))
#     img = img.resize((150, 150))
#     img_array = np.array(img) / 255.0
#     return img_array

def classify(img_vgg, model):
    cats = ['beaches/ocean', 'entertainment', 'gardens/zoo', 'landmarks', 'museums','parks']
    predictions = np.array(model.predict(img_vgg))
    pred = np.argmax(predictions)
    return cats[pred] 

def get_distance(img_feats, feats):
    '''
    Get distance between vectors.
    '''
    try:
        # Extract numeric features from the URLs or use the appropriate column
        # Replace this line with the correct logic based on your DataFrame structure
        numeric_feats = [float(x) for x in re.findall(r'\d+\.\d+|\d+', feats)]

        # Convert lists to NumPy arrays and flatten
        img_feats_flat = np.array(img_feats).astype(float).flatten()
        feats_flat = np.array(numeric_feats).astype(float).flatten()

        # Check if arrays are empty
        if img_feats_flat.size == 0 or feats_flat.size == 0:
            raise ValueError("One or both arrays are empty.")

        # Compute cosine distance
        return scipy.spatial.distance.cosine(img_feats_flat, feats_flat)
    except Exception as e:
        print(f"Error in get_distance: {e}")

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
            ans.append([imgs[i]])
            a=fig.add_subplot(1,3,i+1)
            image = load_image(imgs[i])
            plt.imshow(image,cmap='Greys_r')
            plt.axis('off')

def get_recommendations(img_class, img_array, img_vgg):

    df = load_data(img_class)
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


@app.route('/')
def hello():
    return 'Hello, Flask!'
@app.route('/predict', methods=['GET'])
def predict():
    try:
        if 'url' in request.form:
            img_url = request.form['url']
            response = requests.get(img_url)
            img_filename = f"test.jpg"
            img_folder = os.getcwd() 
            img_path = os.path.join(img_folder, img_filename)
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)

            image = Image.open(img_path) 
            img = image.resize((150, 150))
            # Ensure 3 color channels for RGB images
            img_array = np.array(img)
            if len(img_array.shape) == 2:  # If the image is grayscale, convert to RGB
                img_array = np.stack((img_array,) * 3, axis=-1)
            elif img_array.shape[-1] != 3:  # If the image has a different number of channels, raise an error
                return jsonify({'error': 'Invalid number of image channels'})
            img_std = img_array / 255.0
            img_std = np.expand_dims(img_std, axis=0)
            img_std_copy = img_std.squeeze()
            return img_std_copy
            # Ensure the correct shape (1, 150, 150, 3)
            # img_array = np.expand_dims(img_array, axis=0)
        else:
            return jsonify({'error': 'No URL provided'})

        img_vgg = get_bottleneck_features(vgg_model, img_std)
        
        # Classify function expects 2D input
        # img_vgg_flattened = img_vgg.flatten().reshape(1, -1)

        label = classify(img_vgg, model)
        df = get_recommendations(label, img_array, img_vgg)

        # Convert data to JSON format
        dict1 = {}
        n = len(df)
        for i in range(n):
            name = df.iloc[i, 1]
            dict1[name] = ans[i:i + 3]
        response_data = {
            'label': label,
            'recommendations': dict1,
            'image_urls_list': ans
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
