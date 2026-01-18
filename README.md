# 🏍️ AI-based Motorcycle Classification System

An intelligent system for classifying motorcycles into categories (naked bikes, sport bikes, enduro, etc.) based on performance data such as horsepower, weight, and other technical specifications.

---

## The Authors

- **Alexander Breuer, alexander.breuer@uni-potsdam.de**
- **David Brockmeyer, david.brockmeyer.1@uni-potsdam.de**
---

## Project Overview

This project implements an AI-based classification system that predicts motorcycle categories using performance and technical specifications. The system leverages both Artificial Neural Networks (ANN) and Ordinary Least Squares (OLS) regression models to compare traditional statistical methods with modern deep learning approaches.

**Course**: Advanced AI-based Application Systems  
**Institution**: University of Potsdam, Junior Chair for Business Information Systems, esp. AI-based Application Systems  
**Instructor**: M. Grum  
**Academic Year**: 2025/2026


**Note**: This repository is a fork of the AI-CPS repository and has been customized for motorcycle classification purposes as part of the course requirements.


**Dataset**: The dataset used for AI training was scraped by Victor Megir from Bikez.com and contains approximately 38,000 motorcycle models. The dataset was published on Kaggle.com and subsequently transformed and adapted for this project's specific classification purposes.

**Original Data Source**: https://www.kaggle.com/datasets/victormegir/bikes-from-bikezcom

**Data Processing**:
- Original dataset: 38k motorcycle models from Bikez.com
- Data cleaning: Outlier removal and normalization
- Feature selection: Performance specifications relevant for category classification
- Data split: 80% training, 20% testing



## 🔗 Related Links

- **Docker Hub Profile**: https://hub.docker.com/repositories/dbrockmeyer
- **Original AI-CPS Repository**: https://github.com/MarcusGrum/AI-CPS
---


## Project Goals

1. **Data Collection**: Scrape motorcycle performance data from the Internet
2. **Data Preparation**: Clean, normalize, and split data for training and testing
3. **Model Development**: Create and train both ANN and MLN models
4. **Model Evaluation**: Compare performance metrics and visualizations
5. **Containerization**: Provide Docker images for reproducible deployment
6. **Application**: Enable real-time motorcycle classification

---

##  Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git installed

### Clone the Repository

```bash
git clone https://github.com/YourUsername/motorcycle-classification.git
cd /MotorcycleClassification
```

### Pull Docker Images from Docker Hub

```bash
# Pull all required images
docker pull dbrockmeyer/activationbase_motorcycleclassification
docker pull dbrockmeyer/learningbase_motorcycleclassification
docker pull dbrockmeyer/knowledgebase_motorcycleclassification
docker pull dbrockmeyer/codebase_motorcycleclassification
```
### Create Docker Volume
First, create the shared volume for data exchange between containers:
```bash
docker volume create ai_system
```

### Run the Application with pulled images

```bash
docker-compose up
```
### Install images locally and run afterwards
```bash
docker-compose up --build
```
---

## License
This project is licensed under the **AGPL-3.0 License** - see the [LICENSE] file for details.

---
