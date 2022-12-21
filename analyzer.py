import pandas as pd
import math


def get_tfidf(df):
    res_df = {"song_id": [], "word": [], "tf-idf": []}
    for i in df.index.values.tolist():
        s = set(df.iloc[i]["lyrics"].split(" "))
        try:
            s.remove('')
        except:
            pass
        for e in s:
            res_df["song_id"].append(i)
            res_df["word"].append(e)

    collection_size = res_df["song_id"][-1]
    for i in range(len(res_df["song_id"])):
        lyrics = list(filter(('').__ne__, df.iloc[res_df["song_id"][i]]["lyrics"].split(" ")))
        tf = lyrics.count(res_df["word"][i]) / len(lyrics)

        count = 0
        for j in df.index.values.tolist():
            if df.iloc[j]["lyrics"].find(res_df["word"][i]) != -1:
                count += 1

        idf = math.log((collection_size / count))
        res_df["tf-idf"].append(tf * idf)

    return pd.DataFrame(res_df)
