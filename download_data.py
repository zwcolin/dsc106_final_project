import requests
import re
from bs4 import BeautifulSoup
import zipfile
import os
from tqdm import tqdm

if not os.path.exists("data"):
	os.mkdir("data")
r = requests.get("https://s3.amazonaws.com/baywheels-data/")
files = re.findall("([0-9]+-baywheels-tripdata.csv.zip)",r.text)
for f in tqdm(files):
    r = requests.get("https://s3.amazonaws.com/baywheels-data/" + str(f))
    open(f, 'wb').write(r.content)
    with zipfile.ZipFile(f, 'r') as zip_ref:
        zip_ref.extractall("data/")
    os.remove(f)