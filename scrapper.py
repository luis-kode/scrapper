import requests
from bs4 import BeautifulSoup

# page routes
MAIN_URL = "https://www.bancalavorofitness.com/"
PROVINCES_URL = "provincia/"

# html classes
PROVINCES_CLASS = {"tag": "select", "className": "ddl_province"}
TRAINER_NAMES = {"tag": "td", "className": "td_nome_cognome"}
TRAINER_PHONE_NUMBERS = {"tag": "td"}
TRAINER_EMAILS = {"tag": "input", "id": "hf_email"}

page = requests.get(MAIN_URL)
data = BeautifulSoup(page.content, "html.parser")

# trainer's data
provinces = []
names = []
emails = []
phoneNumbers = []
trainersCount = 0


def getUrlFormated(trainerName):
    trainerName.lower()
    return trainerName.replace(" ", "-")


# getting names by provinces
print(data.find_all(TRAINER_NAMES["tag"], _class=TRAINER_NAMES["className"]))

# getting trainer email and phones
for name in names:
    page = requests.get(MAIN_URL + getUrlFormated(name))
    print(MAIN_URL + getUrlFormated(name))
    data = BeautifulSoup(page.content, "html.parser")
    email = ""
    phone = ""
    try:
        email = data.find(TRAINER_EMAILS["tag"], {"id": TRAINER_EMAILS["id"]}).attrs['value']
    except:
        email = "none"

    try:
        phone = data.select(".tabella_pagina_studente td")[1].getText()
    except:
        phone = "nd"

    phoneNumbers.append(phone)
    emails.append(email)

for user in phoneNumbers:
    print(user)