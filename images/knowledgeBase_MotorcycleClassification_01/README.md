# knowledgeBase_MotorcycleClassification_01

Docker image providing trained AI and OLS models for motorcycle classification.

---

## Purpose

This image stores the trained machine learning models for motorcycle classification. It contains both:
- **AI Model** (ANN): Deep learning model trained with TensorFlow/Keras
- **MnLogit Model**: Statistical baseline model trained with Statsmodels

These models can classify motorcycles into categories (naked bikes, sport bikes, enduro, etc.) based on performance specifications such as horsepower, weight, engine 

The trained models are made available at `/tmp/knowledgeBase/` for use by the codeBase image during inference.

---

## Authors

- **Alexander Breuer**
- **David Brockmeyer**

---

## Course Information

This image was created as part of the course **"Advanced AI-based Application Systems"** by the **Junior Chair for Business Information Systems, esp. AI-based Application Systems** at the **University of Potsdam**, supervised by **M. Grum, Chairholder**.

---

## Data Origin

**Dataset**: The dataset used for AI training was scraped by Victor Megir from Bikez.com and contains approximately 38,000 motorcycle models. The dataset was published on Kaggle.com and subsequently transformed and adapted for this project's specific classification purposes.

**Original Data Source**: https://www.kaggle.com/datasets/victormegir/bikes-from-bikezcom

---

## Docker Usage

### Pull the Image

```bash
docker pull yourusername/knowledgebase_motorcycleclassification
```

### Run the Image

```bash
docker run -v ai_system:/tmp yourusername/knowledgebase_motorcycleclassification
```

---

## Image Contents

- **currentAiSolution_ann.h5**: Trained ANN model (TensorFlow/Keras format)
- **currentSolution_mnl.pkl**: Trained OLS model (Pickle format)
- **label_encoder.pkl**: Encoding the categorys for model usage
- **README.md**: This documentation file

### Model Location

The trained models are provided at:
```
/tmp/knowledgeBase/
```

---

## License

This image and its contents are licensed under the **AGPL-3.0 License**.

---

## 🔗 Related Resources

- **Main Project Repository**: https://github.com/DavidBroson/MotorcycleClassification
- **Docker Hub Profile**: https://hub.docker.com/repository/docker/dbrockmeyer/knowledgebase_motorcycleclassification/
- **Original AI-CPS Framework**: https://github.com/MarcusGrum/AI-CPS

---
