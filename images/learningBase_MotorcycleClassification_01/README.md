# learningBase_MotorcycleClassification_01

Docker image providing training and validation datasets for motorcycle classification model development.

---

## Purpose

This image provides the complete dataset split for training and testing machine learning models for motorcycle classification. It contains:
- **Training data** (80% of the dataset) for model training
- **Test/Validation data** (20% of the dataset) for model evaluation

The data is structured to enable reproducible model development and performance evaluation.

The datasets are made available at:
- `/tmp/learningBase/train/training_data.csv`
- `/tmp/learningBase/validation/test_data.csv`

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
docker pull dbrockmeyer/learningbase_motorcycleclassification
```

### Run the Image

```bash
docker run -v ai_system:/tmp yourusername/learningbase_motorcycleclassification
```


---

##  Image Contents

- **training_data.csv**: Training dataset (80% of total data)
- **test_data.csv**: Validation/testing dataset (20% of total data)
- **README.md**: This documentation file

### Data Locations

```
/tmp/learningBase/train/training_data.csv
/tmp/learningBase/validation/test_data.csv
```

---

## License

This image and its contents are licensed under the **AGPL-3.0 License**.

---

## Related Resources

- **Main Project Repository**: https://github.com/DavidBroson/MotorcycleClassification
- **Docker Hub Profile**:https://hub.docker.com/repository/docker/dbrockmeyer
- **Original AI-CPS Framework**: https://github.com/MarcusGrum/AI-CPS

---
