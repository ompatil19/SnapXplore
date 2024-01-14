import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

def image_scraping(url, loc, place):
    driver = webdriver.Chrome()
    driver.get(url)
    location = loc 
    image_folder = f"Web Scraping/images/weekend/{place}"
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
neemrana_weekend = ["Day Trip to Neemrana Fort-Palace", "15th Century Fort Palace", "Go Zip-lining", "Popular Adventure Activity", "Enjoy Camel Rides", "Fun Activity in Rajasthan", "Explore the Neemrana Baori", "An Ancient Stepwell"]
lonavala_weekend = ["Karla and Bhaja caves", "Buddhist Rock-Cut Caves", "Bhushi Lake", "Peaceful Lake", "Kune Waterfalls", "Picturesque Waterfalls", "Rajmachi Fort", "Two Citadels", "Duke's Nose", "Excellent Sunset Point", "Tiger's Point", "Amazing Vantage Point", "Lohagad Fort", "Historical Citadel"]
jaipur_weekend = ["Amer Fort", "A Majestic Hilltop Fort", "Hawa Mahal", "A Five-Storeyed Historic Landmark", "Nahargarh Fort", "The majestic abode of tigers!", "City Palace", "The Residence of the Royal family.", "Birla Mandir", "Discover Peace at Birla Mandir", "Jantar Mantar Near Jaipur", "A Popular Astronomical Observatory", "Jal Mahal", "The Gem of Man Sagar Lake"]
shantiniketan_weekend = ["Chhatimtala", "The Birthplace of Shantiniketan", "Rabindra Bhavana", "Dedicated Tagore Museum", "Khoai Sonajhuri Forest", "Clean Green Forest", "Amar Kutir", "Historic Independence Cooperative", "Singha Sadan", "Heritage Bell Tower", "Cheena Bhavana", "Chinese Cultural Centre", "Kala Bhavana (Nandan Museum)", "Fine Arts Museum"]
gwalior_weekend = ["Sun Temple", "Modern-Time Architectural Wonder", "Gwalior Fort", "A Majestic Hilltop Citadel", "Gwalior Zoo", "Home of the White Tiger", "Saas Bahu Temple", "Lord Vishnu Temple", "Tansen Memorial", "Tribute to the Famous Musician", "Teli ka Mandir", "Highest Building in Gwalior", "Gujari Mahal Museum", "The Queen's Abode"]
kasauli_weekend = ["Sunset Point", "Popular Scenic Viewpoint", "Gurkha Fort", "Ancient Landmark Fort", "Sunrise Point", "Serene Sunrise Point", "Christ Church Near Kasauli", "19th Century Church", "Sanjeevni Hanuman Temple", "Holy Hanuman Temple", "Baba Balak Nath Temple", "Holy Shiva Temple", "Gurudwara Shri Guru Nanakji", "Revered Sikh Shrine"]
pondicherry_weekend = ["Sri Aurobindo Ashram", "Peaceful Ashram", "Basilica Of The Sacred Heart Of Jesus Pondicherry", "Beautiful Gothic Church", "Promenade Beach", "Stunning Rocky Beach", "Paradise Beach, Pondicherry", "Lively & Gorgeous Beach", "Chunnambar Boat House", "Ideal for Boating", "Tranquebar, Tamil Nadu", "Popularly known as the Land of Singing Waves", "Auroville", "Unique Experimental Township", "Serenity Beach"]
kabini_weekend = ["Nagarhole National Park Near Kabini", "Wildlife Getaway", "Kutta Village", "Enchanting Village", "Kabini Dam", "Picturesque Dam", "Kabini Backwater Viewpoint", "Popular Vantage Point", "Kabini River", "Mesmerizing River"]
hampi_weekend = ["Coracle Ride", "Ride Across Tungabhadra River", "Virupaksha Temple", "Oldest Temple in Hampi", "Vittala Temple", "Iconic Temple Ruins", "Rock Climbing", "Climb Giant Boulders", "Sasivekalu Ganesha Temple", "8-Feet Statue of Lord Ganesha", "Pattabhirama Temple", "Known for Intricate Architecture", "Hampi Bazaar", "Locally Known as Virupaksha Bazaar"]
gokarna_weekend = ["Mahabaleshwar Temple Near Gokarna", "Classical Dravidian Architecture", "Food Tour", "Popular Shacks and Cafes", "Om Beach", "Shaped Like the ‘OM’ Symbol", "Paradise Beach", "Also Called Full Moon Beach", "Half Moon Beach", "Beautiful Small Beach", "Koti Tirtha", "Sacred Man-Made Lake", "Gokarna Beach", "Serene Beach", "Kudle Beach", "Secluded Beach", "Beach Yoga", "Rejuvenating Experience"]
diu_weekend = ["Diu Fort", "Enrapturing Fort", "Explore labyrinthine Naida Caves", "Mazy Caves", "Nagao Beach", "Swaying Palm Trees", "St. Paul Church", "Gothic Architectural Delight", "Gorge on Portuguese Delicacies", "Tantalizing Food Tour", "Church of St Francis of Assisi", "Venerate Church", "Spend time at Ghoghla Beach", "Pristine Beach"]

weekends = {
    "neemrana": neemrana_weekend,
    "lonavala": lonavala_weekend,
    "jaipur": jaipur_weekend,
    "shantiniketan": shantiniketan_weekend,
    "gwalior": gwalior_weekend,
    "kasauli": kasauli_weekend,
    "pondicherry": pondicherry_weekend,
    "kabini": kabini_weekend,
    "hampi": hampi_weekend,
    "gokarna": gokarna_weekend,
    "diu": diu_weekend
}

for weekend in weekends.keys():
    list_places = weekends[weekend]
    
    for loc in list_places:
        test = loc.lower()
        l = test.split(" ")
        endpoint = "-".join(l)
        newurl = base_url + endpoint
        print(newurl)
        image_urls = image_scraping(newurl, loc, weekend)
        print(loc, "Done")
