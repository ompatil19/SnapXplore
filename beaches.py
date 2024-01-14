import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = "images/beaches/varkala"
    driver.implicitly_wait(10)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    driver.quit()

    # Find all img tags with alt containing the location
    elements = soup.find_all('img', alt=lambda value: value and location.lower() in value.lower())
    
    urls = []
    for i, element in enumerate(elements, start=1):
        image_url = element.get('src')
        urls.append(image_url)

        # Create the images folder if it doesn't exist
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # Download and save the image
        response = requests.get(image_url)
        image_filename = f"{location}_{i}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        with open(image_path, 'wb') as img_file:
            img_file.write(response.content)

    return urls

# ...

base_url = "https://www.makemytrip.com/tripideas/attractions/"
goa_beaches = ["Anjuna Beach", "Baga Beach", "Calangute Beach", "Candolim Beach", "Colva Beach", "Vagator Beach", "Palolem Beach", "Miramar Beach", "Benaulim Beach", "Majorda Beach", "Varca Beach", "Sinquerim Beach", "Arambol Beach", "Morjim Beach", "Querim Beach (Keri Beach)"]
maldives_beaches = ["Underwater Restaurant", "Sun Island", "Huvahendhoo Island", "Maldives Glowing Beach", "Fihalhohi Island", "Maafushi", "Artificial Beach", "Maamigili"]
lakshwadeep_beaches = ["Andretti", "Agatti", "Minicoy", "Kadmath", "Kalpeni", "Bangaram", "Thinnakara Island Lakshadweep", "Amini Island Lakshadweep", "Kavaratti"]
pondicherry_beaches = ["Promenade Beach", "Paradise Beach Near Puducherry", "Chunnambar Boat House", "Tranquebar Tamil Nadu", "Serenity Beach"]
alibaug_beaches = ["Varsoli Beach", "Mandwa Beach", "Nagaon Beach", "Alibaug Beach"]
kovalam_beaches = ["Hawa Beach", "Lighthouse Beach"]
gokarna_beaches = ["Om Beach", "Paradise Beach", "Half Moon Beach", "Gokarna Beach", "Kudle Beach"]
varkala_beach = ["Varkala Beach", "Thiruvambady Beach"]
for loc in varkala_beach:
    test = loc.lower()
    l = test.split(" ")
    endpoint = "-".join(l)
    newurl = base_url + endpoint
    print(newurl)
    image_urls = image_scraping(newurl, loc)
    print(loc, "DOon")




