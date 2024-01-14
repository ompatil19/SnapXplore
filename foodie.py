import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/foodie/{place}"
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
amritsar_foodie = ["Golden Temple, Amritsar", "Gobindgarh Fort", "Jallianwala Bagh", "Sri Durgiana Temple", "Partition Museum", "Hall Bazaar", "Ram Tirth Temple", "Katra Jaimal Singh Bazaar"]
agra_foodie = ["Taj Mahal", "Agra Fort", "Akbar's Tomb", "Moti Masjid", "Itmad-ud-Daulah's Tomb", "Mehtab Bagh", "Fatehpur Sikri"]
kolkata_foodie = ["Dakshineshwar Kali Temple", "Maidan", "Belur Math", "Howrah Bridge", "Victoria Memorial", "Indian Museum", "Netaji Bhawan", "Prinsep Ghat", "Jorasanko Thakur Bari", "Maulana Azad Museum Kolkata", "Dalhousie Square"]
malvan_foodie = ["Rock Garden", "Malvan Marine Sanctuary", "Sindhudurg Fort", "Tarkarli Beach Near Tarkarli", "Tsunami Island", "Rameshwar Temple", "Achara Beach", "Shri Sateri Temple"]
hyderabad_foodie = ["Charminar", "Golconda Fort Near Hyderabad", "Nehru Zoological Park", "Chowmahalla Palace", "Salar Jung Museum", "Moula Ali Dargah", "Hussain Sagar Lake", "Qutb Shahi Tombs"]
delhi_foodie = ["Sri Gurudwara Bangla Sahib", "Akshardham Temple", "India Gate", "Lotus Temple", "Jantar Mantar In Delhi", "Humayun's Tomb", "Jama Masjid in Delhi", "Red Fort (Lal Quila)", "Qutub Minar, Delhi", "Madame Tussauds Museum Delhi", "Connaught Place", "Khan Market", "Lodhi Garden", "Rashtrapati Bhawan", "National Zoological Park", "Swatantrata Sangrama Sangrahalaya Delhi", "Swatantrata Senani Museum Delhi", "Teen Murti Bhavan & Nehru Planetarium", "Musuem of Illusion", "National Railway Museum", "Champa Gali"]
baroda_foodie = ["Sayaji Baug", "EME Temple", "Ajwa World", "Laxmi Vilas Palace", "Kirti Mandir", "Sursagar Lake", "Baroda Prints"]

foodies = {
    "amritsar": amritsar_foodie,
    "agra": agra_foodie,
    "kolkata": kolkata_foodie,
    "malvan": malvan_foodie,
    "hyderabad": hyderabad_foodie,
    "delhi": delhi_foodie,
    "baroda": baroda_foodie
}

for foodie in foodies.keys():
    list_places = foodies[foodie]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, foodie)
        print(loc, "Done")
