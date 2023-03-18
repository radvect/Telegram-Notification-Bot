from bs4 import BeautifulSoup
import requests

def connect(url):
    page = requests.get(url)
    print((page.status_code))
    return page

def form_url(status_list):
    base_url = "https://www.yad2.co.il/realestate/rent"
    criteria_url = "?"
    price_url = ("price=-1-"+ str(status_list[4]))