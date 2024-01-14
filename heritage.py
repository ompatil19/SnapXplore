import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/heritage/{place}"
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

gwalior_places = ["Sun Temple", "Gwalior Fort", "Gwalior Zoo", "Saas Bahu Temple", "Tansen Memorial", "Teli ka Mandir", "Gujari Mahal Museum"]
jodhpur_places = ["Mehrangarh Fort", "Umaid Bhawan Palace", "Mandore Garden", "Jaswant Thada", "Clock Tower Market", "Rao Jodha Desert Rock Park", "Toorji Ka Jhalra", "Camel Safari", "Phalodi Jodhpur", "Khejarla Fort", "Balsamand Lake", "Sardar Market", "Bishnoi Village Tour", "Sardar Government Museum", "Fort Chanwa"]
mathura_places  = ["Prem Mandir", "Krishna Janmasthan Temple Complex", "Dwarkadhish Temple", "Mathura Museum", "Radha Vallabh Mandir", "Jai Gurudev Mandir", "Lathmar Holi", "Banke Bihari Temple", "Potara Kund", "Kokilavan", "Vaishno Devi Mandir", "Jama Masjid Near Mathura", "Kansa Qila"]
bhubaneswar_places = ["Nandankanan Zoological Park", "Lingaraj Temple", "Odisha State Museum", "Museum of Tribal Arts & Artefacts", "Kedargouri Temple", "Rajarani Temple", "Ekamra Kanan", "Chilika, Odisha"]
udaipur_places = ["City Palace, Udaipur", "Saheliyon Ki Bari", "Fateh Sagar Lake", "Lake Pichola", "Jag Mandir Palace", "Crystal Gallery Udaipur", "Udaipur City Palace Museum", "Sajjangarh Wildlife Sanctuary", "Moti Magri", "Vintage Car Museum Udaipur", "Gulab Bagh Zoo", "Jaisamand Lake", "Mansapurna Karni Ropeway", "Ambrai Ghat"]
vrindavan_places = ["Radha Raman Temple", "Keshi Ghat", "Prem Mandir Near Vrindavan", "Banke Bihari Mandir in Vrindavan", "Nidhivan"]
aurangabad_places = ["Ellora Caves", "Ajanta Caves", "Bibi Ka Maqbara Aurangabad", "Bhadra Maruti Temple", "Valley of the Sufi Saints", "Grishneshwar Temple Jyotirlinga, Aurangabad", "Aurangabad Caves", "Khuldabad Aurangabad", "Jain Caves Ellora", "Jama Masjid Aurangabad", "Dargah of Pir Ismail", "Buddhist Caves Aurangabad", "Bani Begum Garden", "Himayat Bagh", "Tomb of Aurangzeb", "Kailasa Temple", "Salim Ali Lake", "Siddharth Garden"]
lucknow_places = [    "Bara Imambara","Chhota Imambara","Rumi Darwaza","Tomb of Saadat Ali Khan","Satkhanda","Begum Hazrat Mahal Park"]
mysore_places = ["Mysore Palace","St. Philomena's Cathedral","Brindavan Gardens","Jagmohan Palace","Mysore Zoo","Mysore Sand Sculpture Museum","Chamundi Hills"]
hampi_places  = ["Coracle Ride","Virupaksha Temple","Vittala Temple","Rock Climbing","Sasivekalu Ganesha Temple","Pattabhirama Temple","Hampi Bazaar"]
kochi_places = ["Hill Palace Museum","The Mattancherry Palace","Santa Cruz Basilica","Paradesi Synagogue","Willingdon Island","Vypeen Island","Princess Street","Muziris, Kerala"]
pushkar_places = ["Brahma Temple","Apteshwar Temple","Savitri Temple","Pushkar Lake Near Pushkar","Rangji Temple","Varaha Temple","Merta City"]
rishikesh_places = ["Laxman Jhula","Rajaji National Park","Triveni Ghat","Neelkanth Mahadev Temple","Parmarth Niketan",    "Vashishtha Guha Temple","The Beatles Ashram","Tera Manzil","Little Buddha Cafe","Kaudiyala","Ram Jhula","Neergarh Waterfall","Vashistha Cave","Kunjapuri Devi Temple"]

places  = {"gwalior": gwalior_places, "jodhpur": jodhpur_places, "mathura": mathura_places, "bhubaneswar": bhubaneswar_places, "udaipur": udaipur_places, "vrindavan": vrindavan_places, "aurangabad": aurangabad_places, "lucknow": lucknow_places, "mysore":mysore_places, "kochi":kochi_places, "pushkar":pushkar_places, "rishikesh": rishikesh_places}

for place in places.keys():
    list_places = places[place]
    print(place)
    print(list_places)

    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, place)
        print(loc, "Done")
