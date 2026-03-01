import requests
import random
from tqdm import tqdm

def GetVoix(texte:str, voix:str):
    assert type(texte) == str, "Attention, le texte doit être une chaine de caractères"
    assert type(voix) == str, "Attention, le nom de la voix doit être une chaine de caractères"
    assert not texte == "", "Attention, le texte ne doit pas être vide !"
    assert not voix == "", "Attention, on doit avoir une voix dedans !"

    url = "https://h-ir-ssd-1.acapela-group.com/webservices/1-60-00/UrlMaker.json"
    data = {
        "cl_login": "AcapelaGroup",
        "cl_app": "AcapelaGroup_WebDemo_HTML",
        "session_start": "1760963977",
        "session_time": "10800", 
        "session_key": "2096218979-75468671b540b39f684614122761b08065374b5f5951bad8336a9e0655586a0d",
        "req_voice": voix,
        "req_text": f".\n\n{texte}"
    }
    
    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "459",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "h-ir-ssd-1.acapela-group.com",
    "Origin": "https://www.acapela-group.com",
    "Referer": "https://www.acapela-group.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
    }
    
    response = requests.post(url, data=data, headers=headers)
    json = None
    
    try:
        json = response.json()
    except ValueError:
        print(response.text)
        
    print(json)
        
    soundUrl = json["snd_url"]
    
    sndResponse = requests.get(soundUrl, stream=True)
    sndResponse.raise_for_status()
    nomFichier = f"temp\File{random.randint(1,999999)}.mp3"
    
    # f"temp\File{random.randint(1,999999)}"
    with requests.get(soundUrl, stream=True) as r:
        r.raise_for_status()
        taille_totale = int(r.headers.get('content-length', 0))
        bloc = 1024  # 1 Ko par itération
    
        # Configure la barre de progression
        with open(nomFichier, 'wb') as f, tqdm(
            total=taille_totale,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            desc=nomFichier,
            initial=0,
            ascii=True,
            colour='green'
        ) as barre:
            for chunk in r.iter_content(chunk_size=bloc):
                if chunk:
                    f.write(chunk)
                    barre.update(len(chunk))

    print(f"\n✅ Téléchargement terminé : {nomFichier}")
    return nomFichier