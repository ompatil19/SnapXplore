import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/treks/{place}"
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
coonoor_treks = ["Sims Park", "Dolphins Nose", "St Georges Church Coonoor", "Lambs Rock", "Ralliah Dam", "Droog Fort"]
dalhousie_treks = ["Panchpula", "Dainkund Peak Near Dalhousie", "Kalatop Wildlife Sanctuary", "Ganji Pahari", "Chamera Lake", "Khajjiar", "Rock Garden Dalhousie", "Sach Pass", "Subhash Baoli", "Bakrota Hills", "St Patricks Church", "Indo Tibetan Market", "Satdhara Falls", "St Johns Church Dalhousie", "St Francis Church"]
kasauli_treks = ["Sunset Point", "Gurkha Fort", "Sunrise Point", "Christ Church Near Kasauli", "Sanjeevni Hanuman Temple", "Baba Balak Nath Temple", "Gurudwara Shri Guru Nanakji"]
shillong_treks  = ["Elephant Falls", "Laitlum Canyons", "Don Bosco Museum Shillong", "Double-Decker Bridge", "Umiam Lake", "David Scott Trail", "All Saints Church", "Shillong Peak", "Ziro Valley, Arunachal Pradesh", "Mawlynnong", "Spread Eagle Falls", "Sweet Falls", "Air Force Museum", "Malki Forest", "Rhino Heritage Museum", "Lady Hydari Park", "Wards Lake", "Police Bazaar"]
nandihills_treks = ["Bhoga Nandishwara Temple", "Brahmashram", "Tipu's Drop", "Amrita Sarovar", "Tipu's Summer Residence", "Muddenahalli"]
leh_treks = ["Leh Palace", "Shanti Stupa", "Gurudwara Pathar Sahib", "Spituk Gompa", "Stok Palace Museum", "Alchi Monastery Near Leh"]
lansdowne_treks = ["Bhulla Tal", "Darwan Singh Museum", "St Marys Church Lansdowne", "Durga Devi Temple", "Garhwal Rifles Regimental War Memorial", "Santoshi Mata Mandir", "Garhwali Mess", "Kanvashram", "St Johns Church", "Tarkeshwar Mahadev Temple"]
mahabaleshwar_treks = ["Pratapgarh Fort", "Arthur's Seat", "Mahabaleshwar Temple", "Wilson Point (Sunrise Point)", "Venna Lake", "Elephant's Head Point", "Lingmala Waterfall", "Dhobi Waterfall"]
kasol_treks = ["Gurudwara Shri Manikaran Sahib", "Manikaran Hot Springs", "Shop at the Kasol Market", "Walk by the Parvati River", "Camp in the Parvati Valley", "Trek from Malana to Waichin Valley", "Star Gazing in Kasol", "Pin Parvati Pass Trek", "Buddha Place", "Tosh", "Stone Garden Cafe", "Barshaini", "Sar Pass Trek", "Stargazing at Kasol", "Magic Valley", "Fishing Activity in Naggar"]
ladakh_treks = ["Pangong Tso", "Diskit Monastery", "Thiksey Gompa", "Leh Palace Near Leh", "Tso Moriri", "Stok Palace"]

treks = {"coonoor": coonoor_treks, "dalhousie": dalhousie_treks, "kasauli": kasauli_treks, "shillong": shillong_treks, "nandhihills": nandihills_treks, "leh": leh_treks, "lansdowne": lansdowne_treks, "mahabaleshwar": mahabaleshwar_treks, "kasol": kasol_treks, "ladhakh": ladakh_treks}


for trek in treks.keys():
    list_places = treks[trek]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, trek)
        print(loc, "Done")
