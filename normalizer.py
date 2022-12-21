def normalize_lyrics(data):
    deletion = ["[Verse]", "[Verse 1]", "[Verse 2]", "[Verse 3]", "[Verse 4]",
                "Verse 1:", "Verse 2:", "Verse 3:", "Verse 4:",
                "[Chorus]", "[Chorus 1]", "[Chorus 2]", "[Chorus 3]",
                "[Pre-Chorus]", "[Pre-Chorus 1]", "[Pre-Chorus 2]", "[Pre-Chorus 3]",
                "[Intro]", "[Post-Chorus]", "[Bridge]", "[Outro]",
                "Intro:", "Chorus:", "Pre-Chorus:", "Post-Chorus:", "Bridge:", "Outro:",
                ".", ",", ":", "(", ")", "!", "?", "[", "]", '"', "„", "“", "/", "\\", "&", ";"]

    for el in deletion:
        data = data.replace(el, "")

    data = data.lower()

    contractions_dict = {
        "case": ["'m", "'ve", "'ll", "can't", "won't", "n't", "'d", "'s", "'re", "'til", "in'", "'cause", "'em",
                 "’m", "’ve", "’ll", "can’t", "won’t", "n’t", "’d", "’s", "’re", "’til", "in’", "’cause", "’em"],
        "alias": [" am", " have", " will", "cannot", "will not", " not", " had", " is", " are", "until", "ing",
                  "because", "them",
                  " am", " have", " will", "cannot", "will not", " not", " had", " is", " are", "until", "ing",
                  "because", "them"]
    }

    for i in range(len(contractions_dict["case"])):
        data = data.replace(contractions_dict["case"][i], contractions_dict["alias"][i])

    data = data.strip()
    data = data.replace(' - ', ' ')
    data = data.replace(u'\xa0', u' ')
    data = data.replace(u'\u2005', u' ')
    return data
