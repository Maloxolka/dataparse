import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

client_access_token = "qW9weoP_qiHLAKPqebtnIlDe5P7PEbmwNwlkRAT5ZIB-7LOjVL0jn4cQBhjQyyUA"


def find_songs_by_api(text):
    songs = []
    url = f"http://api.genius.com/search?q={text}&access_token={client_access_token}"

    res = requests.get(url)

    body = res.json()

    for hit in body["response"]["hits"]:
        songs.append("https://genius.com" + hit["result"]["path"])

    return songs


def find_songs_by_selenium(text):
    songs = []
    text = text.replace(" ", "%20")

    url = "https://genius.com/search?q=" + text

    driver = webdriver.Edge()

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    driver.command_executor.set_timeout(50)
    driver.quit()

    links = soup.findAll('a', class_="mini_card")

    for link in links:
        if link['href'].find("lyrics") != -1 and link['href'].find("annotated") == -1:
            songs.append(link['href'])

    return songs
