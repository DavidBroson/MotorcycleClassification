####################
import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pickle
import os

# Pfad des aktuellen Scripts (App01.py)
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

# FIX: Extract the actual data values, not column names
X_test = df.drop(columns=[y])  # This gives you the DataFrame without the 'Category' column
y_test = df[y]  # Removed the quotes - this is now active

print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")


# ================== 1. MODELL UND LABEL ENCODER LADEN ==================

# Keras/TensorFlow Modell laden
model_path = os.path.join(path, 'knowledgeBase', 'CurrentSolution_ann.h5')
model = keras.models.load_model(model_path)
print("Model geladen")

# LabelEncoder laden (falls du kategoriale Labels hast)
with open(os.path.join(path, 'knowledgeBase', 'label_encoder.pkl'), 'rb') as f:
    le = pickle.load(f)
print("LabelEncoder geladen")


# ================== 2. VORHERSAGE ==================

# Predict probabilities
y_pred_proba = model.predict(X_test)  # Gibt Wahrscheinlichkeiten zurück
print(f"Prediction probabilities shape: {y_pred_proba.shape}")

# Get class predictions
y_pred = np.argmax(y_pred_proba, axis=1)  # Klasse mit höchster Wahrscheinlichkeit

# Decode predictions back to original labels
y_pred_labels = le.inverse_transform(y_pred)

print(f"\nErste 10 Vorhersagen:")
print(y_pred_labels[:10])