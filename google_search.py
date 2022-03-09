from googlesearch import search
from bs4 import BeautifulSoup
import requests, lxml

query = input("What do you want to search for? ")
how_many_search_results = input("How many search results you want me to display? ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def get_product_results_data(soup):
    ## TODO CREATE A FUNCTION THAT LOOKS FOR A SPECIFIC ITEM IN THE soup
    ## THEN RETURNS IF IT IS IN STOCK OR NOT.

for j in search(query, num_results=int(how_many_search_results)):
    response = requests.get(j, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    
