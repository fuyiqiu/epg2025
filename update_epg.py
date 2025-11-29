import gzip
import requests

EPG_URL = "https://epg.pw/xmltv/epg.xml.gz"
OUTPUT = "public/epg.xml.gz"

def download_epg():
    print("Downloading latest EPG from epg.pw...")
    r = requests.get(EPG_URL, timeout=30)
    r.raise_for_status()
    with open(OUTPUT, "wb") as f:
        f.write(r.content)
    print("EPG downloaded and saved to public/epg.xml.gz")

if __name__ == "__main__":
    download_epg()
  
