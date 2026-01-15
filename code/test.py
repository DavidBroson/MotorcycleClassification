from bs4 import BeautifulSoup
import pandas as pd
import requests

#response = requests.get("https://github.com/MarcusGrum/AIBAS/blob/main")
response = requests.get("https://www.kaggle.com/datasets/victormegir/bikes-from-bikezcom/data")

doc = BeautifulSoup(response.text, "html.parser")

#article = doc.find("article")

print(doc)
print("testpush")
#table = article.find("table")

# df = pd.read_html(str(table))[0].copy()
# print(df)