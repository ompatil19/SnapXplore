import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/adventure/{place}"
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
        image_filename = f"{location.replace(' ', '_').lower()}_{i}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        with open(image_path, 'wb') as img_file:
            img_file.write(response.content)

    return urls

# ...

base_url = "https://www.makemytrip.com/tripideas/attractions/"
leh_adventure = ["Leh Palace", "Shanti Stupa", "Gurudwara Pathar Sahib", "Spituk Gompa", "Stok Palace Museum", "Alchi Monastery Near Leh", "Magnetic Hill"]
rishikesh_adventure = ["Laxman Jhula", "Rajaji National Park", "Triveni Ghat", "Neelkanth Mahadev Temple", "Parmarth Niketan", "Vashishtha Guha Temple", "The Beatles Ashram", "Tera Manzil", "Little Buddha Cafe", "Kaudiyala", "Ram Jhula", "Neergarh Waterfall", "Vashistha Cave", "Kunjapuri Devi Temple"]
neemrana_adeventure = ["Day Trip to Neemrana Fort-Palace", "Go Zip-lining", "Enjoy Camel Rides", "Explore the Neemrana Baori"]
kutch_adventure = ["Kutch Museum", "Vijaya Vilas Palace", "Aina Mahal", "Bhadreshwar Jain Temple", "Kalo Dungar", "Great Rann Of Kutch", "Lakhpat", "Kutch Desert Wildlife Sanctuary", "Craft Villages"]
manikaran_adventure = ["Seek Blessings at Gurudwara Shri Manikaran Sahib", "Manikaran Hot Springs", "Shop at the Kasol Market", "Walk by the Parvati River", "Camp in the Parvati Valley", "Trek from Malana to Waichin Valley", "Star Gazing in Kasol", "Pin Parvati Pass Trek", "Buddha Place", "Tosh", "Stone Garden Cafe", "Barshaini", "Sar Pass Trek", "Stargazing at Kasol", "Magic Valley", "Fishing Activity in Naggar"]
gulmarg_adventure = ["Gulmarg Biosphere Reserve", "Gulmarg Gondola Ride", "Alpather Lake", "Gulmarg Golf Course", "St. Mary's Church", "Strawberry Valley", "Shrine of Baba Reshi", "Khilanmarg", "Buta Pathri", "Durung Waterfall", "Seven Springs"]
andaman_adventure = ["Cellular Jail", "Radhanagar Beach", "Elephant Beach", "Ross Island", "Kalapathar Beach", "Mount Harriet National Park Near Havelock", "Neil's Cove", "Barren Island"]

adventures = {
    "leh": leh_adventure,
    "rishikesh": rishikesh_adventure,
    "neemrana": neemrana_adeventure,
    "kutch": kutch_adventure,
    "manikaran": manikaran_adventure,
    "gulmarg": gulmarg_adventure,
    "andaman": andaman_adventure
}

for adventure in adventures.keys():
    list_places = adventures[adventure]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, adventure)
        print(loc, "Done")
