# activationBase_MotorcycleClassification_01

Docker image providing activation data for motorcycle classification inference.

---

## Purpose

This image provides sample activation data (`activation_data.csv`) that can be used to test and demonstrate the motorcycle classification system. The activation data contains a single motorcycle entry with performance specifications that will be classified by the trained AI/OLS models.

The data is made available at the path `/tmp/activationBase/` for consumption by the codeBase image during model inference.

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

## 
Docker Usage

### Pull the Image

```bash
docker pull yourusername/activationbase_motorcycleclassification
```

### Run the Image

```bash
docker run -v ai_system:/tmp yourusername/activationbase_motorcycleclassification
```



##  Image Contents

- **activation_data.csv**: Sample motorcycle data for classification
- **README.md**: This documentation file


---

## 📝 License

This image and its contents are licensed under the **AGPL-3.0 License**.

---

## 🔗 Related Resources

- **Main Project Repository**: [\[GitHub Repository Link\]](https://github.com/DavidBroson/MotorcycleClassification)
- **Docker Hub Link**: https://hub.docker.com/repository/docker/dbrockmeyer/activationbase_motorcycleclassification
- **Original AI-CPS Framework**: https://github.com/MarcusGrum/AI-CPS

---
