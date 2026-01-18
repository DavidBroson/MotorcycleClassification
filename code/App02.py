import os
import pandas as pd
import pickle
from scipy import stats
import statsmodels.api as sm
import statsmodels
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Pfad des aktuellen Scripts
script_path = os.path.abspath(__file__)
print(f"Script Pfad: {script_path}")

# Verzeichnis des Scripts (code/)
current = os.path.dirname(script_path)
print(f"Script Verzeichnis: {current}")

# Parent-Verzeichnis (MotorcycleClassification/)
path = os.path.dirname(current)
print(f"Parent Verzeichnis: {path}")


# ================== 0. Activation Data LADEN ==================

df = pd.read_csv(os.path.join(path, "activationBase", "activation_data.csv"))
y = 'Category'

X = df.drop(columns=[y])
y_test = df[y]

numeric_values = ['Displacement ccm', 'Fuel capacity liters', 'Power HP']

# ================== 1. Models LADEN ==================

# LabelEncoder laden 
with open(os.path.join(path, 'knowledgeBase', 'label_encoder.pkl'), 'rb') as f:
    le = pickle.load(f)
print("LabelEncoder geladen")

# MNLogit Modell laden
with open(os.path.join(path, 'knowledgeBase', 'currentSolution_mnl.pkl'), 'rb') as f:
    model_mnl = pickle.load(f)
print("MNLogit Modell geladen")

# Keras/TensorFlow Modell laden
model_path = os.path.join(path, 'knowledgeBase', 'currentSolution_ann.h5')
model_ann = keras.models.load_model(model_path)
print("ANN Modell geladen")

# ================== 2. VORHERSAGEN MNLogit ==================

# Vorhersagen machen (gibt Wahrscheinlichkeiten zurück)
predictions_proba_mnl = model_mnl.predict(X[numeric_values])

# Die Klasse mit der höchsten Wahrscheinlichkeit auswählen
predictions_mnl = predictions_proba_mnl.idxmax(axis=1).values

# Vorhersagen dekodieren
predicted_labels_mnl = le.inverse_transform(predictions_mnl)

# ================== 3. VORHERSAGEN ANN ==================

# Vorhersagen machen mit TensorFlow
predictions_proba_ann = model_ann.predict(X[numeric_values])

# Die Klasse mit der höchsten Wahrscheinlichkeit auswählen
predictions_ann = np.argmax(predictions_proba_ann, axis=1)

# Vorhersagen dekodieren
predicted_labels_ann = le.inverse_transform(predictions_ann)

# ================== 4. AUSGABE ==================

print("\n" + "="*100)
print("Vorhersage der Modelle:")
print("="*100)
print(f"{'Motorrad':<12} | {'Tatsächlich':<20} | {'MNLogit':<20} | {'ANN (TensorFlow)':<20}")
print("-"*100)

for i, (actual, pred_mnl, pred_ann) in enumerate(zip(y_test, predicted_labels_mnl, predicted_labels_ann), 1):
    print(f"Motorrad {i:<3} | {actual:<20} | {pred_mnl:<20} | {pred_ann:<20}")