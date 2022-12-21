import pandas as pd
import matplotlib.pyplot as plt


def show_important_words(id):
    df = pd.read_csv('datasets/songs.csv')
    tfidf_df = pd.read_csv('datasets/tf-idf.csv')

    song = tfidf_df[tfidf_df["song_id"] == id].sort_values(by=["tf-idf"], ascending=False).head(10)
    song.plot(x='word', y='tf-idf', kind="bar")
    plt.title(df.iloc[id]["song"])
    plt.subplots_adjust(bottom=0.25)
    plt.show()
