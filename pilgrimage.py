import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/pilgrimage/{place}"
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
mathura_pilgrims = ["Prem Mandir", "Krishna Janmasthan Temple Complex", "Dwarkadhish Temple", "Mathura Museum", "Radha Vallabh Mandir", "Jai Gurudev Mandir", "Lathmar Holi", "Banke Bihari Temple", "Potara Kund", "Kokilavan", "Vaishno Devi Mandir", "Jama Masjid Near Mathura", "Kansa Qila"]
vrindavan_pilgrims = ["Prem Mandir", "Krishna Janmasthan Temple Complex", "Dwarkadhish Temple", "Mathura Museum", "Radha Vallabh Mandir", "Jai Gurudev Mandir", "Lathmar Holi", "Banke Bihari Temple", "Potara Kund", "Kokilavan", "Vaishno Devi Mandir", "Jama Masjid Near Mathura", "Kansa Qila", "Radha Raman Temple", "Keshi Ghat", "Prem Mandir Near Vrindavan", "Banke Bihari Mandir in Vrindavan", "Nidhivan"]
allahbad_pilgrims = ["Manakameshwar Temple", "Allahabad Fort", "Khusrau Bagh", "Bade Hanuman Ji Temple", "All Saints Cathedral", "Swaraj Bhavan", "Ulta Qila", "Kalyani Devi Temple"]
pushkar_pilgrims = ["Brahma Temple", "Apteshwar Temple", "Savitri Temple", "Pushkar Lake Near Pushkar", "Rangji Temple", "Varaha Temple"]
amristar_pilgrims = ["Golden Temple, Amritsar", "Gobindgarh Fort", "Jallianwala Bagh", "Sri Durgiana Temple", "Partition Museum", "Hall Bazaar", "Ram Tirth Temple", "Katra Jaimal Singh Bazaar"]
dwarka_pilgrims = ["Dwarkadhish Temple Near Dwarka", "Nageshwar Jyotirlinga", "ISKCON Dwarka", "Bet Dwarka", "Sudama Setu", "Swaminarayan Temple", "Gita Temple", "Gomti Ghat", "Bhadkeswar Mahadev Temple"]
varanasi_pilgrims = ["Dashashwamedh Ghat", "Manikarnika Ghat", "Panchganga Ghat", "Assi Ghat", "Shivala Ghat", "Shri Satyanarayan Tulsi Manas Mandir", "Nepali Museum", "Ganga River", "Vindham Waterfalls", "Bharat Kala Bhavan Museum", "Gyan Vapi Well"]
tirupati_pilgrims = ["Sri Venkateswara Temple", "Sri Venkateswara National Park", "Sri Kapileswara Swamy Temple", "Swami Pushkarini Lake", "Silathoranam", "TTD Gardens", "Vedadri Narasimha Swamy Temple", "Horsley Hills, Andhra Pradesh", "ISKCON Tirupati", "Akasaganga Teertham", "Talakona Waterfall", "Kapila Teertham", "Sri Venkateswara Dhyana Vignan Mandiram", "Rock Garden Tirupati", "Sri Padmavathi Ammavari Temple", "Papavinasanam"]
guwahati_pilgrims = ["Assam State Zoo cum Botanical Garden", "Kamakhya Temple Guwahati", "Umananda Temple", "Regional Science Centre", "Guwahati Planetarium", "Kaziranga National Park", "Botanical Garden Guwahati", "Manas National Park", "Dipor Bil", "Dispur", "Guwahati War Memorial", "Chandubi Lake", "ISKCON Guwahati", "Umananda Island", "Guwahati Zoo", "Haflong, Assam", "Srimanta Sankardev Kalakshetra"]
haridwar_pilgrims = ["Shantikunj Ashram", "Har Ki Pauri", "Rajaji National Park Near Haridwar", "Mansa Devi Temple", "Bharat Mata Temple", "Sapt Rishi Ashram", "Pawan Dham Temple"]
kedarnath_pilgrims = ["Kedarnath Temple", "Vasuki Tal", "Sonprayag", "Chorabar Tal", "Bhairavanath Temple", "Gauri Kund", "Vishwanath Temple"]

puri_pilgrims = ["Shree Jagannath Temple", "Sakshigopal Temple", "Swargadwar Market", "Gundicha Mandir", "Puri Beach", "Pipli", "Konark"]
rameswaram_pilgrims = ["Kalam National Memorial", "Gandamadana Parvatham", "Ramanathaswamy Temple", "Pamban Bridge", "Agnitheertham", "Jada Theertham", "Ram Setu", "Villoondi Theertham Beach", "Thiruppullani", "Five Faced Hanuman Temple", "Lakshmana Tirtham", "Arulmigu Ramanathaswamy", "Dhanushkodi", "Panchamukhi Hanuman Temple"]


pilgrims = {
    "mathura": mathura_pilgrims,
    "vrindavan": vrindavan_pilgrims,
    "allahabad": allahbad_pilgrims,
    "pushkar": pushkar_pilgrims,
    "amristar": amristar_pilgrims,
    "dwarka": dwarka_pilgrims,
    "varanasi": varanasi_pilgrims,
    "tirupati": tirupati_pilgrims,
    "guwahati": guwahati_pilgrims,
    "haridwar": haridwar_pilgrims,
    "kedarnath": kedarnath_pilgrims,
    "puri": puri_pilgrims,
    "rameswaram": rameswaram_pilgrims
}

for pilgrim in pilgrims.keys():
    list_places = pilgrims[pilgrim]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, pilgrim)
        print(loc, "Done")
