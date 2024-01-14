import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/honeymoon/{place}"
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
# havelock_honeymoon = ["Cellular Jail", "Radhanagar Beach", "Elephant Beach", "Ross Island", "Kalapathar Beach", "Mount Harriet National Park Near Havelock", "Neil's Cove", "Barren Island"]
# goa_honeymoon = ["Aguada Fort", "Basilica of Bom Jesus", "Dudhsagar Waterfalls", "Baga beach, Goa", "Our Lady of the Immaculate Conception Church", "Calangute Beach", "Se Cathedral", "Chapora Fort", "Anjuna Flea Market", "Anjuna Beach", "Candolim Beach", "Vagator Beach", "Palolem Beach", "Salaulim Dam", "Morjim Beach", "Baina Beach", "Querim Beach", "Majorda Beach", "Agonda Beach", "Varca Beach", "Butterfly Beach", "Netravali Bubbling Lake", "Bhagwan Mahaveer Wildlife Sanctuary", "Indian Naval Aviation Museum", "Arambol Beach"]
# manali_honeymoon = ["Manikaran Sahib", "Hidimba Devi Temple", "Rohtang Pass", "Manu Temple", "Solang Valley", "Old Manali", "Naggar Castle Near Manali", "Arjun Gufa", "Sethan Valley", "Atal Tunnel", "Vashisht Hot Water Springs", "Nehru Kund", "Old Manali Snow Point", "Himvalley Amusement & Cultural Park", "Shoja, Himachal Pradesh", "Jalori Jot, Himachal Pradesh", "Jibhi, Himachal Pradesh", "Cafe 1947"]
# srinagar_honeymoon = ["Mughal Gardens", "Nishat Bagh", "Shalimar Bagh", "Achabal Bagh", "Chashma Shahi", "Pari Mahal", "Verinag", "Dal Lake", "Shankaracharya Hill Srinagar", "Nigeen Lake", "Wular Lake", "Hari Parbat", "Shri Pratap Singh Museum", "Lal Chowk and Polo View", "Doodhpathri, Kashmir", "Hazratbal Shrine", "Chashme Shahi", "Shalimar Bagh", "Shikara Ride in Srinagar"]
# munnar_honeymoon = ["Echo Point Near Munnar", "Eravikulam National Park", "Pothamedu View Point", "Photo Point", "Attukal Waterfalls", "Chinnakanal Waterfalls", "Kundala Dam Lake", "Lockheart Gap", "Trek to the Anamudi Peak", "Chandys Windy Woods", "Avondale Cottage", "Talayar Bungalow", "Dream Catcher Plantation", "Munnar Discovery Tent Stay", "Boating in Mattupetty Dam", "Visit the Tea Museum", "Go for Rock Climbing", "Elephant Safari at Carmelagiri Park", "Relishing Kerala Sadhya", "Eravikulam National Park", "Trek to the Anamudi Peak", "Tea Tales", "Relishing Kerala Sadhya", "Hotel Gurubhavan", "Hotel Sri Nivas Restaurant", "Copper Castle", "Vattavada", "Kanthalloor", "Seetha Devi Lake", "Marayur", "Pampadum Shola National Park", "Kolukkumalai Tea Estate", "Boating in Mattupetty Dam", "Go for Rock Climbing", "Elephant Safari at Carmelagiri Park", "Munnar Discovery Tent Stay"]
alleppey_honeymoon = ["Ambalapuzha Sree Krishna Temple Alleppey", "Visit Alappuzha Lighthouse", "Tour Krishnapuram Palace", "Explore the Backwaters", "Relax at the Alleppey Beach", "Enjoy Soothing Ayurvedic Therapies", "Visit St Marys Forane Church", "Kuttanad, Kerala", "Shopping Spree In Alleppey"]
gangtok_honeymoon = ["Tsomgo Lake", "Rumtek Monastery", "Nathu La Pass", "Do-Drul Chorten", "Enchey Monastery", "Namgyal Institute of Tibetology", "Seven Sisters Waterfall", "Ganesh Tok Temple Gangtok Sikkim", "Khangchendzonga National Park, Sikkim", "Ravangla, Sikkim", "Pelling, Sikkim"]
coorg_honeymoon = ["Raja's Seat", "Golden Temple", "Abbey Falls, Coorg (Madikeri)", "Irupu Falls", "Iguthappa Temple", "Madikeri Fort", "Talakaveri", "Honnamana Kere Lake", "Mallalli Falls", "Somwarpet", "River Rafting in Coorg", "Honey Valley"]
shimla_honeymoon = ["Christ Church", "Viceregal Lodge", "Kalibari Temple", "The Ridge of Shimla", "Green Valley", "Jhakoo Hill", "Johnnie's Wax Museum", "Annandale"]
ooty_honeymoon = ["Botanical Garden", "Pykara Waterfalls", "Doddabetta Peak", "Elk Hill Murugan Temple", "Ooty Lake", "Fernhills Palace", "Tea Museum", "Mudumalai National Park, Tamil Nadu"]
gulmarg_honeymoon = ["Gulmarg Biosphere Reserve", "Gulmarg Gondola Ride", "Alpather Lake", "Gulmarg Golf Course", "St. Mary's Church", "Strawberry Valley", "Shrine of Baba Reshi", "Khilanmarg", "Buta Pathri", "Durung Waterfall", "Seven Springs"]
darjeeling_honeymoon = ["Padmaja Naidu Himalayan Zoological Park Darjeeling", "Batasia Loop", "Japanese Peace Pagoda", "Himalayan Mountaineering Institute", "Tiger Hill", "Ghoom Monastery", "Sandakphu, Darjeeling", "Lepchajagat, West Bengal", "Dhirdham Temple"]
dalhousie_honeymoon = ["Panchpula", "Dainkund Peak Near Dalhousie", "Kalatop Wildlife Sanctuary", "Ganji Pahari", "Chamera Lake", "Khajjiar", "Rock Garden Dalhousie", "Sach Pass", "Subhash Baoli", "Bakrota Hills", "St Patricks Church", "Indo Tibetan Market", "Satdhara Falls", "St Johns Church Dalhousie", "St Francis Church"]
auli_honeymoon = ["Artificial Lake Auli", "Kwani Bugyal Auli", "Experience Skiing amidst Snow-Clad Mountains", "Visit Nanda Devi National Park", "Trek to Gurso Bugyal", "Seek Blessings at Narsimha Temple", "Experience the Ropeway Cable Car Ride"]
udaipur_honeymoon = ["City Palace, Udaipur", "Saheliyon Ki Bari", "Fateh Sagar Lake", "Lake Pichola", "Jag Mandir Palace", "Crystal Gallery Udaipur", "Udaipur City Palace Museum", "Sajjangarh Wildlife Sanctuary", "Moti Magri", "Vintage Car Museum Udaipur", "Gulab Bagh Zoo", "Jaisamand Lake", "Mansapurna Karni Ropeway", "Ambrai Ghat"]
mussoorie_honeymoon = ["Kempty Falls", "George Everests House", "Lal Tibba", "Clouds End Mussoorie", "Benog Wildlife Sanctuary", "Camels Back Road", "Gun Hill", "Landour", "Mussoorie Lake", "Mall Road"]
jaipur_honeymoon = ["Amer Fort", "Hawa Mahal", "Nahargarh Fort", "City Palace", "Birla Mandir", "Jantar Mantar Near Jaipur", "Jal Mahal"]
shillong_honeymoon = ["Elephant Falls", "Laitlum Canyons", "Don Bosco Museum Shillong", "Double-Decker Bridge", "Umiam Lake", "David Scott Trail", "All Saints Church", "Shillong Peak", "Ziro Valley, Arunachal Pradesh", "Mawlynnong", "Spread Eagle Falls", "Sweet Falls", "Air Force Museum", "Malki Forest", "Rhino Heritage Museum", "Lady Hydari Park", "Wards Lake", "Police Bazaar"]
pondicherry_honeymoon = ["Sri Aurobindo Ashram", "Basilica Of The Sacred Heart Of Jesus Pondicherry", "Promenade Beach", "Paradise Beach, Pondicherry", "Chunnambar Boat House", "Tranquebar, Tamil Nadu", "Auroville", "Serenity Beach"]
wayanad_honeymoon = ["Edakkal Caves", "Thirunelli Temple", "Chembra Peak", "Muthanga Wildlife Sanctuary", "Kuruva Island", "Pookode Lake", "Banasura Sagar Dam"]


honeymoons = {
    "alleppey": alleppey_honeymoon,
    "gangtok": gangtok_honeymoon,
    "coorg": coorg_honeymoon,
    "shimla": shimla_honeymoon,
    "ooty": ooty_honeymoon,
    "gulmarg": gulmarg_honeymoon,
    "darjeeling": darjeeling_honeymoon,
    "dalhousie": dalhousie_honeymoon,
    "auli": auli_honeymoon,
    "udaipur": udaipur_honeymoon,
    "mussoorie": mussoorie_honeymoon,
    "jaipur": jaipur_honeymoon,
    "shillong": shillong_honeymoon,
    "pondicherry": pondicherry_honeymoon,
    "wayanad": wayanad_honeymoon
}

for honeymoon in honeymoons.keys():
    list_places = honeymoons[honeymoon]
    print(honeymoon)
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, honeymoon)
        print(loc, "Done")
