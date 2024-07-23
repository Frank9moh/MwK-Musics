
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://edge.mixlr.com/channel/rwumx")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '5620568130',"1256293459")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '6789249'))
    CHAT = int(os.environ.get("CHAT", "2205437057"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "2205437057")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    DURATION_LIMIT=int(os.environ.get("DUR", 15))
    API_HASH = os.environ.get("API_HASH", "b0e83186601cc8a8953673d327cb5265")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7458060169:AAG7-MfOXwzUqiNNdA2X2tckOik0_XQWnRo") 
    SESSION = os.environ.get("SESSION_STRING", "BABnmIEAEQuP_r6sudRiL504i0ShWj4qmlQbI_CuAawhWiijUYf28FGzV7K3FqzQF_TdI6Q78sGxvkLvkIQE5yJwUhxADbTl9sH1Nz_hJHo1JaPTWv9NfLzdVWrVkBOFF_pFdAhQHcYlkoOpxQCEI5-mE0GqwzH0fD9DxWhRJ527KHI8vWo3fYGDLJ6S0jU4seQjzwQsD1gMC8PAHE5YdAyaZe_V_SdQ4Sp49-u-bKD8imyBHw_Ty9VKJm8wdpFVBJEngg9Wmpiq-nTEJtHO5nXLg-YZbU7nLPG5dEAFfWJymdILYwCtR_hKGvZBeLXDMeGmLpELLSIJzmfLmlehh7zlL3iAAAAAFPAxBCAA")
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    playlist=[]
    msg = {}
