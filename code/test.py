from bs4 import BeautifulSoup
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import numpy as np




#response = requests.get("https://github.com/MarcusGrum/AIBAS/blob/main")
#response = requests.get("https://www.kaggle.com/datasets/victormegir/bikes-from-bikezcom/data")

#doc = BeautifulSoup(response.text, "html.parser")

#article = doc.find("article")

#print(doc)
#print("testpush")
#table = article.find("table")

# df = pd.read_html(str(table))[0].copy()
# print(df)


"""
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "bikes.csv"

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "victormegir/bikes-from-bikezcom",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

import kagglehub

# Download latest version
path = kagglehub.dataset_download("victormegir/bikes-from-bikezcom")

print("Path to dataset files:", path)
"""

current=os.path.dirname(os.path.abspath(__file__))
parent=parent_dir = os.path.dirname(current)

df=pd.read_csv(parent_dir+"/datasets/victormegir/bikes-from-bikezcom/versions/4/bikes.csv")

##---------------Sichere Auswahl mit DropNA---------------------##

kat_selection_safe=["Category","Engine type","Transmission type,final drive","Displacement ccm","Fuel capacity liters","Power HP","Front brakes","Rear brakes"]
kat_selection_all=["Category","Engine type","Transmission type,final drive","Displacement ccm","Fuel capacity liters","Power HP","Front brakes","Rear brakes","Starter","Seat height mm","Dry weight kg","Overall length mm","Wheelbase mm","Top speed km/h"]

df_selected_safe=df[kat_selection_safe].copy()
df_selected_all=df[kat_selection_all].copy()

#print(df_all.shape)

df_clean=df_selected_safe.dropna().copy()
df_all_0=df_selected_all.fillna(0).copy()

print(df_all_0.head())
#print(df_clean.head())
##-------Bis zum Punkt steht doppel/Single etc-------------##
df_clean["Front brakes"]=df_clean['Front brakes'].str.split('.').str[0]
df_clean["Rear brakes"]=df_clean['Rear brakes'].str.split('.').str[0]

# mindest Wert denn eine Art haben muss an Datensatzhäufigkeit
min_count = 100

# Häufigkeiten zählen
value_counts = df_clean['Category'].value_counts()
#print(value_counts)

# Kategorien mit genug Vorkommen identifizieren
valid_categories = value_counts[value_counts >= min_count].index
#print(valid_categories)

# DataFrame filtern
df_clean = df_clean[df_clean['Category'].isin(valid_categories)].copy()
print(df_clean.shape)
print(df_clean)


numeric_columns = df_clean.select_dtypes(include=['number']).columns.tolist()

def removeOutliers(data, col):
    Q3 = np.quantile(data[col], 0.75)
    Q1 = np.quantile(data[col], 0.25)
    IQR = Q3 - Q1

    print("IQR value for column %s is: %s" % (col, IQR))
    global outlier_free_list
    global filtered_data

    lower_range = Q1 - 1.5 * IQR
    upper_range = Q3 + 1.5 * IQR
    outlier_free_list = [x for x in data[col] if (
        (x > lower_range) & (x < upper_range))]
    filtered_data = data.loc[data[col].isin(outlier_free_list)] #entsprechende Outlier free rows setzen

counter=0
for i in numeric_columns:
    if counter == 0:
      removeOutliers(df_clean, i)
      counter=counter+1 # einaml mit anfangs df rein, danach mit arbeist variable
    else: 
      removeOutliers(filtered_data, i)

df_clean=filtered_data
print(df_clean.shape)

text_columns = df_clean.select_dtypes(include=['object', 'string']).columns.tolist()

print(f"Filtere folgende Text-Spalten: {text_columns}\n")

# Für jede Text-Spalte filtern
for col in text_columns:
    print(f"Verarbeite Spalte: {col}")
    
    # Häufigkeiten zählen
    value_counts = df_clean[col].value_counts()
    print(f"  Vorher: {len(value_counts)} unique values, {len(df_clean)} Zeilen")
    
    # Kategorien mit genug Vorkommen identifizieren
    valid_categories = value_counts[value_counts >= min_count].index
    
    # Entfernte Kategorien anzeigen
    removed = value_counts[value_counts < min_count]
    if len(removed) > 0:
        print(f"  Entferne {len(removed)} Kategorien mit < {min_count} Vorkommen:")
        print(f"  {removed.to_dict()}")
    
    # DataFrame filtern
    df_clean = df_clean[df_clean[col].isin(valid_categories)].copy()
    
    print(f"  Nachher: {df_clean[col].nunique()} unique values, {len(df_clean)} Zeilen\n")

print(f"\nFinale Anzahl Zeilen: {df_clean}")



