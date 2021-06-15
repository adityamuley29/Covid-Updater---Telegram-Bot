import requests
import json


covid_api_url = requests.get("https://api.covid19india.org/data.json")

api = json.loads(covid_api_url.content)

state_search = api["statewise"]

# a = str(input("enter"))


def searchedData(state_name):

    for i in state_search:
        if i["state"].lower() == state_name.lower():
            return i['active'], i['confirmed'], i['deaths'], i['recovered'], i['lastupdatedtime']


def indiacases():
    india = api["statewise"][0]

    return india['active'], india['confirmed'], india['deaths'], india['recovered'], india['lastupdatedtime']
