import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/romantic/{place}"
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
bali_romantic = ["Tegallalang Rice Terraces", "Ancient Temples", "Beaches", "Rafting on Ayung River", "Climbing Mount Batur", "Sunset at Tanah Lot Temple", "Kuta Beach", "Balinese Massage", "Diving in Tulamben", "Bali Swing", "Bali Safari Marine Park", "Uluwatu Temple", "Dolphin Watching Activity", "Cruise to Nusa Lembongan", "Sacred Monkey Forest Sanctuary", "Campuhan Ridge Walk", "Pura Tirta Empul", "Waterbom Bali", "Water Sports in Sanur"]
coorg_romantic = ["Raja's Seat", "Golden Temple", "Abbey Falls, Coorg (Madikeri)", "Irupu Falls", "Iguthappa Temple", "Madikeri Fort", "Talakaveri", "Honnamana Kere Lake", "Mallalli Falls", "Somwarpet", "River Rafting in Coorg", "Honey Valley"]
gulmarg_romantic = ["Gulmarg Biosphere Reserve", "Gulmarg Gondola Ride", "Alpather Lake", "Gulmarg Golf Course", "St. Mary's Church", "Strawberry Valley", "Shrine of Baba Reshi", "Khilanmarg", "Buta Pathri", "Durung Waterfall", "Seven Springs"]
havelock_romantic = ["Barren Island", "Museum Circuit in Port Blair", "Anthropological Museum", "Samudrika Naval Marine Museum", "Fisheries Museum", "Chidiya Tapu"]
lakshadweep_romantic = ["Andretti", "Agatti", "Minicoy", "Kadmath", "Kalpeni", "Bangaram", "Kiltan In Lakshadweep", "Chetlat Island Lakshadweep", "Bitra Island Lakshadweep", "Thinnakara Island Lakshadweep", "Amini Island Lakshadweep", "Kavaratti"]
manali_romantic = ["Manikaran Sahib", "Hidimba Devi Temple", "Rohtang Pass", "Manu Temple", "Solang Valley", "Old Manali", "Naggar Castle Near Manali", "Arjun Gufa", "Sethan Valley", "Atal Tunnel", "Vashisht Hot Water Springs", "Nehru Kund", "Old Manali Snow Point", "Himvalley Amusement & Cultural Park", "Shoja, Himachal Pradesh", "Jalori Jot, Himachal Pradesh", "Jibhi, Himachal Pradesh", "Cafe 1947"]
munnar_romantic = ["Echo Point Near Munnar", "Eravikulam National Park", "Pothamedu View Point", "Photo Point", "Attukal Waterfalls", "Chinnakanal Waterfalls", "Kundala Dam Lake", "Lockheart Gap"]
ooty_romantic = ["Botanical Garden", "Pykara Waterfalls", "Doddabetta Peak", "Elk Hill Murugan Temple", "Ooty Lake", "Fernhills Palace", "Tea Museum", "Mudumalai National Park, Tamil Nadu"]


romantics = {
    "bali": bali_romantic,
    "coorg": coorg_romantic,
    "gulmarg": gulmarg_romantic,
    "havelock": havelock_romantic,
    "lakshadweep": lakshadweep_romantic,
    "manali": manali_romantic,
    "munnar": munnar_romantic,
    "ooty": ooty_romantic
}


for romantic in romantics.keys():
    list_places = romantics[romantic]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, romantic)
        print(loc, "Done")
