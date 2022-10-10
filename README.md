# 🏖️ Tourist Package Prediction

## Problem Statement and Solution Proposed 

This project aims to solve the problem of tourism sector where they can predict if a tourist is likely to buy a tourism package or not, the model training is done using Sklearn's supervised machine learning techniques. It is a classification problem and training are carried out on dataset. Several classification techniques have been studied, the model has been finalized with Random Forest Classifier and XGB Classifier in pipeline.

For Detailed EDA and Feature engineering Check out notebook directory 

Their performances were compared in order to determine which one works best with our dataset and used them to predict if tourist will buy a package or not from user input from Fast API application.

## 👨‍💻 Tech Stack Used

1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## 🌐 Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)

## Project Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)


## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)

### Step 1: Clone the repository
```bash
git clone https://github.com/Machine-Learning-01/TouristPackagePrediction
```
```
cd TouristPackagePrediction
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.7.6 -y
```

```bash
conda activate venv
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the  environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL=<MONGODB_URL>

```

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image

```
docker run -d -p 8080:8080 <IMAGEID>
```
## Models Used 
- Logistic Regression
- KNeighbors Classifier
- XGB Classifier
- CatBoost Classifier
- SVC
- AdaBoost Classifier
- RandomForest Classifier

From these above models after hyperparameter optimization we selected Top two models which were XGBClassifier and Random Forest Classifier and used the following in Pipeline.

GridSearchCV is used for Hyperparameter Optimization in the pipeline.

`toursim` is the main package folder which contains all codes.


## Conclusion 
This project can be used in real-life by tourism companies to predict if the user has chance to buy the tourism package or not.
