import os 
import requests 
image_url ="https://drive.google.com/uc?id=13gb1qr6qNW_wYuCgu3B9M-XJjmDZh31K"
response = requests.get(image_url)
image_folder = "Web Scraping"
image_filename = "hello.jpg"
image_path = os.path.join(image_folder, image_filename)
with open(image_path, 'wb') as img_file:
    img_file.write(response.content)