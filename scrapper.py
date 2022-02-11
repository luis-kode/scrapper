import os
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
websites = []
facebookProfiles = []
twitterProfiles = []
youtubeChannels = []
linkedinProfiles = []
trainerPages = []

# getting provinces
provinces = [
    "agrigento",
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


def getTrainerInfo(data, infoType):
  if infoType == "email":
    try:
      info = data.find(TRAINER_EMAILS["tag"], {"id": TRAINER_EMAILS["id"]})
      return info.attrs["value"]
    except:
      return "email"
  elif infoType == "phone":
    if len(data.select(".tabella_pagina_studente td")) > 1:
      return data.select(".tabella_pagina_studente td")[1].getText()
    else:
      return "phone"
  elif infoType == "website":
    info = data.select(".tabella_pagina_studente tr td")[5]
    if not info.getText() == "nd":
      return info.find("a").attrs["href"]
    else:
      return info.getText()
  elif infoType == "facebook":
    info = data.select(".tabella_pagina_studente tr td")[7]
    if info.getText() != "nd" and info.getText() != "n.d.":
      return info.find("a").attrs["href"]
    else:
      return "nd"
  elif infoType == "twitter":
    info = data.select(".tabella_pagina_studente tr td")[9]
    if info.getText() != "nd" and info.getText() != "n.d.":
      return info.find("a").attrs["href"]
    else:
      return "nd"
  elif infoType == "youtube":
    info = data.select(".tabella_pagina_studente tr td")[11]
    if info.getText() != "nd" and info.getText() != "n.d.":
      return info.find("a").attrs["href"]
    else:
      return "nd"
  elif infoType == "linkedin":
    info = data.select(".tabella_pagina_studente tr td")[13]
    if info.getText() != "nd" and info.getText() != "n.d.":
      return info.find("a").attrs["href"]
    else:
      return "nd"

for province in provinces:
  page = requests.get(MAIN_URL + "/provincia/" + province)
  data = BeautifulSoup(page.content, "html.parser")
  print(MAIN_URL + "/provincia/" + province)

  # getting names
  for name in data.find_all(TRAINER_NAMES["tag"], TRAINER_NAMES["className"]):
      trainerPages.append(name.find(href=True).attrs["href"])
      names.append(name.getText())

  # getting trainer email and phones
  for url in trainerPages:

      page = requests.get(MAIN_URL + url)
      data = BeautifulSoup(page.content, "html.parser")

      emails.append(getTrainerInfo(data, "email"))
      phoneNumbers.append(getTrainerInfo(data, "phone"))
      websites.append(getTrainerInfo(data, "website"))
      facebookProfiles.append(getTrainerInfo(data, "facebook"))
      twitterProfiles.append(getTrainerInfo(data, "twitter"))
      youtubeChannels.append(getTrainerInfo(data, "youtube"))
      linkedinProfiles.append(getTrainerInfo(data, "linkedin"))

  try:
    os.remove('trainers_' + province + '.txt')
  except:
    print("file not exists")
  
  file = open('trainers_' + province + '.txt', 'w')

  for i in range(0, len(trainerPages) - 1):
    print(names[i])
    print(emails[i])
    print(phoneNumbers[i])
    print(websites[i])
    print(facebookProfiles[i])
    print(twitterProfiles[i])
    print(youtubeChannels[i])
    print(linkedinProfiles[i])
    print("-----------------")
    line = names[i] + ";" + emails[i] + ";" + phoneNumbers[i] + ";" + websites[i] + ";" + facebookProfiles[i] + ";" + twitterProfiles[i] + ";" + youtubeChannels[i] + ";" + linkedinProfiles[i] + ";"
    file.write(line)

  file.close()
