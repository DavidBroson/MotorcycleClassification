import os
import pandas as pd
import pickle
from scipy import stats
import statsmodels.api as sm
import statsmodels
from sklearn.preprocessing import LabelEncoder

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
# ==================Models LADEN ==================

# LabelEncoder laden 
with open(os.path.join(path, 'knowledgeBase', 'label_encoder.pkl'), 'rb') as f:
    le = pickle.load(f)
#print("LabelEncoder geladen")
with open(os.path.join(path, 'knowledgeBase', 'currentSolution_mnl.pkl'), 'rb') as f:
    model_mnl = pickle.load(f)

# Vorhersagen machen (gibt Wahrscheinlichkeiten zurück)
predictions_proba = model_mnl.predict(X[numeric_values])

# Die Klasse mit der höchsten Wahrscheinlichkeit auswählen
predictions = predictions_proba.idxmax(axis=1).values

# Vorhersagen dekodieren
predicted_labels = le.inverse_transform(predictions)

# Ausgabe in CLI
print("\nVorhersage von MNLogit-Model:")
for i, label in enumerate(predicted_labels, 1):
    print(f"Motorrad {i}: {label}")

# from sklearn.metrics import classification_report
# # Classification Report
# print("\n" + "="*60)
# print("Classification Report:")
# print("="*60)
# print(classification_report(y_test, predicted_labels))

# print("\n====================================================================\n")

# # Ausgabe in CLI
# print("\nVorhersage von MNLogit-Model:")
# print("="*60)
# for i, (actual, predicted) in enumerate(zip(y_test, predicted_labels), 1):
#     print(f"Motorrad {i}: Tatsächlich: {actual:20s} | Vorhergesagt: {predicted}")



