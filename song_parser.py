from bs4 import BeautifulSoup
import requests
import pandas as pd

from analyzer import get_tfidf
from normalizer import normalize_lyrics
from searcher import find_songs_by_api, find_songs_by_selenium


def get_song_list(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    songs = []
    links = soup.findAll('a', class_="mini_card")

    for link in links:
        songs.append(link['href'])
    return songs


def get_song_lyrics(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    lyrics = soup.find('div', class_="Lyrics__Container-sc-1ynbvzw-6 YYrds")
    songname = url[:-7]
    songname = songname[19:]

    return lyrics.get_text(separator=" "), songname


def create_dataset(search_list):
    data = {"song": [], "lyrics": []}
    for group in search_list:
        search = find_songs_by_selenium(group)
        for song in search:
            lyrics, name = get_song_lyrics(song)
            data["song"].append(name)
            data["lyrics"].append(normalize_lyrics(lyrics))

    return pd.DataFrame(data)


def analyse_songs():
    search_list = ["The Beatles", "Imagine Dragons", "Linkin Park", "Fall Out Boys", "The Rolling Stones", "Nirvana",
                   "Queen", "Pink Floyd", "Lana Del Ray", "Rihanna", "Ariana Grande", "Twenty One Pilots", "Shakira",
                   "Solence", "The Offspring"]

    df = create_dataset(search_list)
    df.to_csv('datasets/songs.csv')

    tfidf_df = get_tfidf(df)
    tfidf_df.to_csv('datasets/tf-idf.csv')
