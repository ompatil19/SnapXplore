import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = "images/heritage/"
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
kasol_mountains = ["Seek Blessings at Gurudwara Shri Manikaran Sahib", "Manikaran Hot Springs", "Walk by the Parvati River", "Camp in the Parvati Valley", "Trek from Malana to Waichin Valley", "Star Gazing in Kasol", "Pin Parvati Pass Trek", "Buddha Place", "Tosh", "Stone Garden Cafe", "Barshaini", "Sar Pass Trek", "Stargazing at Kasol", "Stargazing at Kasol"]
lansdowne_mountains = ["Bhulla Tal", "Darwan Singh Museum", "St Marys Church Lansdowne", "Durga Devi Temple", "Garhwal Rifles Regimental War Memorial", "Santoshi Mata Mandir", "Garhwali Mess", "Kanvashram", "St Johns Church", "Tarkeshwar Mahadev Temple"]
dalhousie_mountains =  ["Panchpula", "Dainkund Peak Near Dalhousie", "Kalatop Wildlife Sanctuary", "Ganji Pahari", "Chamera Lake", "Khajjiar", "Rock Garden Dalhousie", "Sach Pass", "Subhash Baoli", "Bakrota Hills", "St Patricks Church", "Indo Tibetan Market", "Satdhara Falls", "St Johns Church Dalhousie", "St Francis Church"]
shimla_mountains =  ["Christ Church", "Viceregal Lodge", "Kalibari Temple", "The Ridge of Shimla", "Green Valley", "Jhakoo Hill", "Johnnie's Wax Museum", "Annandale"]
wayanad_mountains = ["Edakkal Caves", "Thirunelli Temple", "Chembra Peak", "Muthanga Wildlife Sanctuary", "Kuruva Island", "Pookode Lake", "Banasura Sagar Dam"]
leh_mountains =  ["Leh Palace", "Shanti Stupa", "Gurudwara Pathar Sahib", "Spituk Gompa", "Stok Palace Museum", "Alchi Monastery Near Leh", "Magnetic Hill"]
pahalgam_mountains = ["Pahalgam Golf Course", "Betaab Valley", "Aru Valley", "Lidderwat", "Baisaran Hills", "Overa-Aru Wildlife Sanctuary", "Panchtarni", "Skiing in Pahalgam", "Trekking in Pahalgam", "River Rafting in Pahalgam", "Chandanwari", "Lidder Amusement Park"]
gulmarg_mountains = ["Gulmarg Biosphere Reserve", "Gulmarg Gondola Ride", "Alpather Lake", "Gulmarg Golf Course", "St. Mary's Church", "Strawberry Valley", "Shrine of Baba Reshi", "Khilanmarg", "Buta Pathri", "Durung Waterfall", "Seven Springs"]
coonoor_mountains = ["Sim’s Park", "Dolphins Nose", "St Georges Church Coonoor", "Lambs Rock", "Ralliah Dam", "Droog Fort"]
lavasa_mountains = ["Natural Trail in Lavasa", "Water Sports", "Unwind at Dasvino Country Club", "Bird Watching at Dasvae Point", "Chilling at Lakeside Promenade", "Get Creative at Bamboosa"]
ananthagiri_hills = ["Musi River", "Ananthagiri Temple", "Ananthagiri Forest", "Vikarabad"]



for loc in ananthagiri_hills:
    test = loc.lower()
    l = test.split(" ")
    endpoint = "-".join(l)
    newurl = base_url + endpoint
    print(newurl)
    image_urls = image_scraping(newurl, loc)
    print(loc, "DOon")




