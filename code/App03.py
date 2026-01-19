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

# Verzeichnis des Scripts (code/)
current = os.path.dirname(script_path)

# Parent-Verzeichnis (MotorcycleClassification/)
path = os.path.dirname(current)


# ================== 0. Activation Data LADEN ==================

df = pd.read_csv(os.path.join(path, "activationBase", "activation_data.csv"))
y = 'Category'

X = df.drop(columns=[y])

# ================== 1. Models LADEN ==================

# LabelEncoder laden 
with open(os.path.join(path, 'knowledgeBase', 'label_encoder.pkl'), 'rb') as f:
    le = pickle.load(f)

# Keras/TensorFlow Modell laden
model_path = os.path.join(path, 'knowledgeBase', 'currentSolution_ann.h5')
model_ann = keras.models.load_model(model_path)

# ================== 2. VORHERSAGEN ANN ==================

# Vorhersagen machen mit TensorFlow
predictions_proba_ann = model_ann.predict(X)

# Die Klasse mit der höchsten Wahrscheinlichkeit auswählen
predictions_ann = np.argmax(predictions_proba_ann, axis=1)

# Vorhersagen dekodieren
predicted_labels_ann = le.inverse_transform(predictions_ann)

# ================== 3. AUSGABE ==================

print("\n" + "="*40)
print("Vorhersage TensorFlow Modell:")
print("="*40)
print(f"{'Motorrad':<12} | {'Prediction':<20}")
print("-"*40)

for i, pred_ann in enumerate(predicted_labels_ann, 1):
    print(f"Motorrad {i:<3} | {pred_ann:<20}")