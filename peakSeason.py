import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
import os 


# Beaches 
goa_beaches = ["Anjuna Beach", "Baga Beach", "Calangute Beach", "Candolim Beach", "Colva Beach", "Vagator Beach", "Palolem Beach", "Miramar Beach", "Benaulim Beach", "Majorda Beach", "Varca Beach", "Sinquerim Beach", "Arambol Beach", "Morjim Beach", "Querim Beach (Keri Beach)"]
maldives_beaches = ["Underwater Restaurant", "Sun Island", "Huvahendhoo Island", "Maldives Glowing Beach", "Fihalhohi Island", "Maafushi", "Artificial Beach", "Maamigili"]
lakshwadeep_beaches = ["Andretti", "Agatti", "Minicoy", "Kadmath", "Kalpeni", "Bangaram", "Thinnakara Island Lakshadweep", "Amini Island Lakshadweep", "Kavaratti"]
pondicherry_beaches = ["Promenade Beach", "Paradise Beach Near Puducherry", "Chunnambar Boat House", "Tranquebar Tamil Nadu", "Serenity Beach"]
alibaug_beaches = ["Varsoli Beach", "Mandwa Beach", "Nagaon Beach", "Alibaug Beach"]
kovalam_beaches = ["Hawa Beach", "Lighthouse Beach"]
gokarna_beaches = ["Om Beach", "Paradise Beach", "Half Moon Beach", "Gokarna Beach", "Kudle Beach"]
varkala_beach = ["Varkala Beach", "Thiruvambady Beach"]

beaches_dict = {"goa": goa_beaches, "maldives": maldives_beaches, "lakshwadeep": lakshwadeep_beaches, "pondicherry": pondicherry_beaches, "alibaug": alibaug_beaches, "kovalam": kovalam_beaches, "gokarna": gokarna_beaches, "varkala": varkala_beach}

# Heritage 

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


heritage_dict  = {"gwalior": gwalior_places, "jodhpur": jodhpur_places, "mathura": mathura_places, "bhubaneswar": bhubaneswar_places, "udaipur": udaipur_places, "vrindavan": vrindavan_places, "aurangabad": aurangabad_places, "lucknow": lucknow_places, "mysore":mysore_places, "kochi":kochi_places, "pushkar":pushkar_places, "rishikesh": rishikesh_places}
# Honeymoon Places 
havelock_honeymoon = ["Cellular Jail", "Radhanagar Beach", "Elephant Beach", "Ross Island", "Kalapathar Beach", "Mount Harriet National Park Near Havelock", "Neil's Cove", "Barren Island"]
goa_honeymoon = ["Aguada Fort", "Basilica of Bom Jesus", "Dudhsagar Waterfalls", "Baga beach, Goa", "Our Lady of the Immaculate Conception Church", "Calangute Beach", "Se Cathedral", "Chapora Fort", "Anjuna Flea Market", "Anjuna Beach", "Candolim Beach", "Vagator Beach", "Palolem Beach", "Salaulim Dam", "Morjim Beach", "Baina Beach", "Querim Beach", "Majorda Beach", "Agonda Beach", "Varca Beach", "Butterfly Beach", "Netravali Bubbling Lake", "Bhagwan Mahaveer Wildlife Sanctuary", "Indian Naval Aviation Museum", "Arambol Beach"]
manali_honeymoon = ["Manikaran Sahib", "Hidimba Devi Temple", "Rohtang Pass", "Manu Temple", "Solang Valley", "Old Manali", "Naggar Castle Near Manali", "Arjun Gufa", "Sethan Valley", "Atal Tunnel", "Vashisht Hot Water Springs", "Nehru Kund", "Old Manali Snow Point", "Himvalley Amusement & Cultural Park", "Shoja, Himachal Pradesh", "Jalori Jot, Himachal Pradesh", "Jibhi, Himachal Pradesh", "Cafe 1947"]
srinagar_honeymoon = ["Mughal Gardens", "Nishat Bagh", "Shalimar Bagh", "Achabal Bagh", "Chashma Shahi", "Pari Mahal", "Verinag", "Dal Lake", "Shankaracharya Hill Srinagar", "Nigeen Lake", "Wular Lake", "Hari Parbat", "Shri Pratap Singh Museum", "Lal Chowk and Polo View", "Doodhpathri, Kashmir", "Hazratbal Shrine", "Chashme Shahi", "Shalimar Bagh", "Shikara Ride in Srinagar"]
munnar_honeymoon = ["Echo Point Near Munnar", "Eravikulam National Park", "Pothamedu View Point", "Photo Point", "Attukal Waterfalls", "Chinnakanal Waterfalls", "Kundala Dam Lake", "Lockheart Gap", "Trek to the Anamudi Peak", "Chandys Windy Woods", "Avondale Cottage", "Talayar Bungalow", "Dream Catcher Plantation", "Munnar Discovery Tent Stay", "Boating in Mattupetty Dam", "Visit the Tea Museum", "Go for Rock Climbing", "Elephant Safari at Carmelagiri Park", "Relishing Kerala Sadhya", "Eravikulam National Park", "Trek to the Anamudi Peak", "Tea Tales", "Relishing Kerala Sadhya", "Hotel Gurubhavan", "Hotel Sri Nivas Restaurant", "Copper Castle", "Vattavada", "Kanthalloor", "Seetha Devi Lake", "Marayur", "Pampadum Shola National Park", "Kolukkumalai Tea Estate", "Boating in Mattupetty Dam", "Go for Rock Climbing", "Elephant Safari at Carmelagiri Park", "Munnar Discovery Tent Stay"]
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



honeymoon_dict = {
    "havelock": havelock_honeymoon,
    "goa": goa_honeymoon,
    "manali": manali_honeymoon,
    "srinagar": srinagar_honeymoon,
    "munnar": munnar_honeymoon,
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


# Adventure Category

leh_adventure = ["Leh Palace", "Shanti Stupa", "Gurudwara Pathar Sahib", "Spituk Gompa", "Stok Palace Museum", "Alchi Monastery Near Leh", "Magnetic Hill"]
rishikesh_adventure = ["Laxman Jhula", "Rajaji National Park", "Triveni Ghat", "Neelkanth Mahadev Temple", "Parmarth Niketan", "Vashishtha Guha Temple", "The Beatles Ashram", "Tera Manzil", "Little Buddha Cafe", "Kaudiyala", "Ram Jhula", "Neergarh Waterfall", "Vashistha Cave", "Kunjapuri Devi Temple"]
neemrana_adeventure = ["Day Trip to Neemrana Fort-Palace", "Go Zip-lining", "Enjoy Camel Rides", "Explore the Neemrana Baori"]
kutch_adventure = ["Kutch Museum", "Vijaya Vilas Palace", "Aina Mahal", "Bhadreshwar Jain Temple", "Kalo Dungar", "Great Rann Of Kutch", "Lakhpat", "Kutch Desert Wildlife Sanctuary", "Craft Villages"]
manikaran_adventure = ["Seek Blessings at Gurudwara Shri Manikaran Sahib", "Manikaran Hot Springs", "Shop at the Kasol Market", "Walk by the Parvati River", "Camp in the Parvati Valley", "Trek from Malana to Waichin Valley", "Star Gazing in Kasol", "Pin Parvati Pass Trek", "Buddha Place", "Tosh", "Stone Garden Cafe", "Barshaini", "Sar Pass Trek", "Stargazing at Kasol", "Magic Valley", "Fishing Activity in Naggar"]
gulmarg_adventure = ["Gulmarg Biosphere Reserve", "Gulmarg Gondola Ride", "Alpather Lake", "Gulmarg Golf Course", "St. Mary's Church", "Strawberry Valley", "Shrine of Baba Reshi", "Khilanmarg", "Buta Pathri", "Durung Waterfall", "Seven Springs"]
andaman_adventure = ["Cellular Jail", "Radhanagar Beach", "Elephant Beach", "Ross Island", "Kalapathar Beach", "Mount Harriet National Park Near Havelock", "Neil's Cove", "Barren Island"]

adventure_dict = {
    "leh": leh_adventure,
    "rishikesh": rishikesh_adventure,
    "neemrana": neemrana_adeventure,
    "kutch": kutch_adventure,
    "manikaran": manikaran_adventure,
    "gulmarg": gulmarg_adventure,
    "andaman": andaman_adventure
}
#foodie 
amritsar_foodie = ["Golden Temple, Amritsar", "Gobindgarh Fort", "Jallianwala Bagh", "Sri Durgiana Temple", "Partition Museum", "Hall Bazaar", "Ram Tirth Temple", "Katra Jaimal Singh Bazaar"]
agra_foodie = ["Taj Mahal", "Agra Fort", "Akbar's Tomb", "Moti Masjid", "Itmad-ud-Daulah's Tomb", "Mehtab Bagh", "Fatehpur Sikri"]
kolkata_foodie = ["Dakshineshwar Kali Temple", "Maidan", "Belur Math", "Howrah Bridge", "Victoria Memorial", "Indian Museum", "Netaji Bhawan", "Prinsep Ghat", "Jorasanko Thakur Bari", "Maulana Azad Museum Kolkata", "Dalhousie Square"]
malvan_foodie = ["Rock Garden", "Malvan Marine Sanctuary", "Sindhudurg Fort", "Tarkarli Beach Near Tarkarli", "Tsunami Island", "Rameshwar Temple", "Achara Beach", "Shri Sateri Temple"]
hyderabad_foodie = ["Charminar", "Golconda Fort Near Hyderabad", "Nehru Zoological Park", "Chowmahalla Palace", "Salar Jung Museum", "Moula Ali Dargah", "Hussain Sagar Lake", "Qutb Shahi Tombs"]
delhi_foodie = ["Sri Gurudwara Bangla Sahib", "Akshardham Temple", "India Gate", "Lotus Temple", "Jantar Mantar In Delhi", "Humayun's Tomb", "Jama Masjid in Delhi", "Red Fort (Lal Quila)", "Qutub Minar, Delhi", "Madame Tussauds Museum Delhi", "Connaught Place", "Khan Market", "Lodhi Garden", "Rashtrapati Bhawan", "National Zoological Park", "Swatantrata Sangrama Sangrahalaya Delhi", "Swatantrata Senani Museum Delhi", "Teen Murti Bhavan & Nehru Planetarium", "Musuem of Illusion", "National Railway Museum", "Champa Gali"]
baroda_foodie = ["Sayaji Baug", "EME Temple", "Ajwa World", "Laxmi Vilas Palace", "Kirti Mandir", "Sursagar Lake", "Baroda Prints"]

foodie_dict = {
    "amritsar": amritsar_foodie,
    "agra": agra_foodie,
    "kolkata": kolkata_foodie,
    "malvan": malvan_foodie,
    "hyderabad": hyderabad_foodie,
    "delhi": delhi_foodie,
    "baroda": baroda_foodie
}


# List of directories 
honeymoon = os.listdir("images/honeymoon")
adventure = os.listdir("images/adventure")
beaches = os.listdir("images/beaches")
foodie = os.listdir("images/foodie")
heritage = os.listdir("images/heritage")
# Function 1 
def checkPlaces(s):
    res = []
    if s in honeymoon:
        list_of_values = honeymoon_dict[s]
        res.extend(list_of_values)
    
    elif s in beaches:
        list_of_values = beaches_dict[s]
        res.extend(list_of_values)
    elif s in foodie:
        list_of_values = foodie_dict[s]
        res.extend(list_of_values)
    elif s in heritage:
        list_of_values = heritage_dict[s]
        res.extend(list_of_values)
    elif s in adventure:
        list_of_values = adventure_dict[s]
        res.extend(list_of_values)
    
    return res 

# Function 2 
def make_requests(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    season_class = "BestTimeToVisitstyles__SeasonItemHdrLft-sc-1kzpf8k-3 cpjepR"

    element1 = soup.find_all(class_=season_class)
    res = []
    for element in element1:
        for child in element.children:
            if hasattr(child, 'string') and child.string:
                res.append(child.string)
    
    if res:
        str_res1 = res[0] + " "+ res[2]
        str_res2 = res[3]+ " " + res[5]
        str_res3 = res[6] + " " + res[8]
        return [str_res1, str_res2, str_res3]

l = beaches + honeymoon + adventure + beaches + foodie + heritage
dict1 = {}
s = set(l)

for place in s:
    dict1[place] = [[], [], [], []]

for key in dict1.keys():
    url = "https://www.makemytrip.com/tripideas/{}/best-time-to-visit".format(key)
    ans = checkPlaces(key)
    dict1[key][0].extend(ans)
    res = make_requests(url)
    if res:
        dict1[key][1] = res[0]
        dict1[key][2] = res[1]
        dict1[key][3] = res[2]

    print(dict1[key])

df = pd.DataFrame.from_dict(dict1)
print(df.T)
df1 = df.T
df1.to_csv('suggestions.csv')


