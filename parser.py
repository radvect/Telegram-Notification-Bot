from bs4 import BeautifulSoup
import requests

cities = {"Tel_Aviv":"topArea = 2 & area = 1 & city = 5000",
          "Rishon":"topArea=2&area=9&city=8300",
          "Holon":"topArea=2&area=11&city=6600",
          "Haifa": "topArea=25&area=5&city=4000",
          "Ramat_Gan":"topArea=2&area=3&city=8600",
          "Eilat":"topArea=43&area=24&city=2600"}

def connect(url):
    page = requests.get(url)
    print((page.status_code))
    return page

def form_url(status_list):
    base_url = "https://www.yad2.co.il/realestate/rent"
    criteria_url = "?"
    url_and = "&"
    price_url = ("price=-1-"+ str(status_list[4]))
    rooms_url = ("rooms="+ str(status_list[6]) + "--1")
    city_url = cities[status_list[2]]
    url = base_url + criteria_url+ price_url + url_and + rooms_url + url_and + city_url
    return url

def BS_parser(page):
    soup = BeautifulSoup(page.text, "html.parser")
    return soup