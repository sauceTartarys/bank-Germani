import requests
import json

valcode = "PLN"
date = "20230204"

a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")


if a.status_code == 200:
    data = json.loads(a.text)
    print(data[0]["txt"], data[0]["rate"])