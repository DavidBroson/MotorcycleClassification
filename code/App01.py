####################
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
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

# df = pd.read_csv(os.path.join(path, "activationBase", "activation_data.csv"))

# y = 'category'

# X_test = df.columns.drop(y)
# y_test = df[y]



# # ================== 1. MODELL UND LABEL ENCODER LADEN ==================

# # Keras/TensorFlow Modell laden
# model = keras.models.load_model(path+'/knowledgeBase/CurrentSolution_ann.h5')
# print("Modell geladen")

# # LabelEncoder laden (falls du kategoriale Labels hast)
# with open(path+'/knowledgeBase/label_encoder.pkl', 'rb') as f:
#     le = pickle.load(f)
# print("LabelEncoder geladen")

# # ================== 2. PREDICTIONS AUSFÜHREN ==================

# # Prediction auf X (deine Feature-Matrix)
# y_pred_proba = model.predict(X_test)  # Gibt Wahrscheinlichkeiten zurück

# # Klasse mit höchster Wahrscheinlichkeit wählen
# y_pred = np.argmax(y_pred_proba, axis=1)  # [0, 1, 2, ...] encoded labels

# # Falls du LabelEncoder hast: Zurück zu echten Namen
# if le:
#     y_pred_labels = le.inverse_transform(y_pred)
#     y_test_labels = le.inverse_transform(y_test) if isinstance(y_test[0], (int, np.integer)) else y_test
#     categories = le.classes_
# else:
#     y_pred_labels = y_pred
#     y_test_labels = y_test
#     categories = np.unique(y_test)

# print(y_pred)






# # ================== 3. CLASSIFICATION REPORT ==================

# print("\n" + "="*60)
# print("CLASSIFICATION REPORT")
# print("="*60 + "\n")

# # Mit Kategorienamen
# report = classification_report(y_test, y_pred, target_names=categories)
# print(report)

# # Accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f"\nTest Accuracy: {accuracy:.4f}")

# # ================== 4. CONFUSION MATRIX VISUALISIEREN UND SPEICHERN ==================

# cm = confusion_matrix(y_test, y_pred)

# plt.figure(figsize=(12, 10))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
#             xticklabels=categories,
#             yticklabels=categories,
#             cbar_kws={'label': 'Count'})
# plt.xlabel('Predicted Category', fontsize=13)
# plt.ylabel('Actual Category', fontsize=13)
# plt.title(f'Confusion Matrix (Accuracy: {accuracy:.4f})', fontsize=15)
# plt.xticks(rotation=45, ha='right', fontsize=10)
# plt.yticks(rotation=0, fontsize=10)
# plt.tight_layout()

# # Speichern
# plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
# print(f"\n✓ Confusion Matrix gespeichert als: confusion_matrix.png")

# plt.show()

# # ================== OPTIONAL: ZUSÄTZLICHE METRIKEN ==================

# from sklearn.metrics import precision_recall_fscore_support

# precision, recall, f1, support = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# print(f"\nWeighted Metrics:")
# print(f"  Precision: {precision:.4f}")
# print(f"  Recall:    {recall:.4f}")
# print(f"  F1-Score:  {f1:.4f}")