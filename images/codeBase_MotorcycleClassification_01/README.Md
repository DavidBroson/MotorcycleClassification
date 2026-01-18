# codeBase_MotorcycleClassification_01

Docker image executing the motorcycle classification application.

---

## Purpose

This image contains the Python application code that performs motorcycle classification inference. It:
- Loads activation data from the activationBase image
- Loads trained models from the knowledgeBase image
- Executes the classification algorithm
- Outputs prediction results

The codeBase orchestrates the entire inference pipeline, connecting data sources with trained models to produce motorcycle category predictions based on performance specifications.

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
docker pull yourusername/codebase_motorcycleclassification_01
```

**Note**: Standalone run not recommended, because Data from KnowledgeBase and ActivationBase is required.

---

## Image Contents

- **App01.py**: Main application script for classification
- **requirements.txt**: Python dependencies
- **README.md**: This documentation file

### Expected Data Paths

The application expects data at:
- Input: `/tmp/activationBase/activation_data.csv`
- Models: `/tmp/knowledgeBase/...

---

## License

This image and its contents are licensed under the **AGPL-3.0 License**.

---

## Related Resources

- **Main Project Repository**: https://github.com/DavidBroson/MotorcycleClassification
- **Docker Hub Link**: https://hub.docker.com/repository/docker/dbrockmeyer/codebase_motorcycleclassification
- **Original AI-CPS Framework**: https://github.com/MarcusGrum/AI-CPS

---

