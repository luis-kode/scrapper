import requests
from bs4 import BeautifulSoup

# page routes
MAIN_URL = "https://www.bancalavorofitness.com"
PROVINCES_URL = "provincia/"

# html classes
PROVINCES_CLASS = {"tag": "select", "className": "ddl_province"}
TRAINER_NAMES = {"tag": "td", "className": "td_nome_cognome"}
TRAINER_PHONE_NUMBERS = {"tag": "td"}
TRAINER_EMAILS = {"tag": "input", "id": "hf_email"}

# trainer's data
names = []
emails = []
phoneNumbers = []
trainersCount = 0
trainerPages = []

# getting provinces
provinces = [
    "agriento",
    "alessandria",
    "ancona",
    "aosta",
    "arezzo",
    "ascoli-piceno"
    "avellino",
    "bari",
    "barletta-andria-trani",
    "belluno",
    "benevento",
    "bergamo",
    "biella",
    "bologna",
    "brescia",
    "brindisi",
    "cagliari",
    "caltanissetta",
    "campobasso"
    "caserta",
    "catania",
    "catanzaro",
    "chieti",
    "como",
    "cosenza",
    "cremona",
    "crotone",
    "cuneo",
    "enna",
    "fermo",
    "ferrara",
    "firenze",
    "foggia",
    "forli-cesena",
    "frosinone",
    "genova",
    "gorizia",
    "grosseto",
    "imperia"
    "isernia",
    "l-aquila",
    "la-spezia",
    "latina",
    "lecce",
    "lecco",
    "livorno",
    "lodi",
    "lucca",
    "macerata",
    "mantova",
    "massa-carrara",
    "matera",
    "messina",
    "milano",
    "modena",
    "monza-brianza",
    "napoli",
    "novara",
    "nuoro",
    "oristano",
    "padova",
    "palermo",
    "parma",
    "pavia",
    "perugia",
    "pesaro-urbino",
    "pescara",
    "piacenza",
    "pisa",
    "pistoia",
    "pordenone",
    "potenza",
    "prato",
    "ragusa",
    "ravenna",
    "reggio-emilia",
    "rieti",
    "rimini",
    "roma",
    "rovigo",
    "salerno",
    "sassari",
    "savona",
    "siena",
    "sondrio",
    "sud-sardegna",
    "taranto",
    "teramo",
    "terni",
    "torino",
    "trapani",
    "trento",
    "treviso",
    "trieste",
    "udine",
    "varese",
    "venezia",
    "verbano-cusio-ossola",
    "vercelli",
    "verona",
    "vibo-valentia",
    "vinceza",
    "viterbo"
]

page = requests.get(MAIN_URL + "/provincia/" + provinces[0])
data = BeautifulSoup(page.content, "html.parser")
print(MAIN_URL + "/provincia/" + provinces[0])

# getting names
for name in data.find_all(TRAINER_NAMES["tag"], TRAINER_NAMES["className"]):
    trainerPages.append(name.find(href=True).attrs["href"])
    names.append(name.getText())

# getting trainer email and phones
for url in trainerPages:

    page = requests.get(MAIN_URL + url)
    data = BeautifulSoup(page.content, "html.parser")
    email = ""
    phone = ""

    try:
        email = data.find(TRAINER_EMAILS["tag"], {
                          "id": TRAINER_EMAILS["id"]}).attrs['value']
    except:
        email = "none"

    try:
        phone = data.select(".tabella_pagina_studente td")[1].getText()
    except:
        phone = "nd"

    phoneNumbers.append(phone)
    emails.append(email)

    for i in range(len(trainerPages) - 1):
        print(names[i] + " - " + emails[i] + " - " + phoneNumbers[i])
