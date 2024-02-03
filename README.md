# Machine Learning Project: Text Classification

## Introduction

This repository contains my first machine learning project submitted for the course CSCI315: Web Application Development. The project focuses on building a Text Classification Model using a Multinomial Naive Bayes classifier.

## Project Structure

- **MachineLearningProject:** Project directory.
- **Machine Learning Project.pptx:** Project presentation slides.
- **Model1.ipynb:** Jupyter Notebook for Model 1 implementation.
- **Model2.ipynb:** Jupyter Notebook for Model 2 implementation.

## README.md

### Problem

The objective of this project is to create a solution that processes user-provided descriptions and suggests the appropriate Linux or CMD command based on the context of the request. The goal is to offer users an efficient and user-friendly means to obtain the relevant command corresponding to their described task or query.

### Choose Model

The employed model is a Multinomial Naive Bayes classifier, operating within the realm of supervised learning, specifically tailored for text classification.

### Build Model

The initial dataset was sourced from Kaggle, comprising command listings for CMD, Linux, macOS, and VBScript. Each command is associated with six distinct descriptions, contributing to the model's capacity to discern patterns within the text data.

Two models were implemented:

#### Model 1:
- Utilizes TfidfVectorizer for text vectorization.
- Calculates and prints accuracy on the entire dataset.
- Further trains the model on the test set.
- Takes user input, classifies it, and outputs the top 5 predictions with probabilities.

#### Model 2:
- Employs TfidfVectorizer for text vectorization.
- Calculates and prints accuracy on the entire dataset.
- Saves the trained model using joblib for future use.
- Takes user input, classifies it, and outputs the top 5 predictions with probabilities.

#### Additional Components:
- **venv:** Serves the purpose of creating an isolated environment for a Python project.
- **text_classifier_model.joblib:** Storage file for the trained model and vectorizer.

### Evaluate Model

Limitations & Improvement Strategies:

1. **Time Constraint:** The time constraint prevented the inclusion of the entire dataset for model training.
2. **Synthetic Descriptions:** The dataset is populated with synthetic descriptions rather than real human-generated ones.
3. **Fixed Number of Descriptions:** Each command has a fixed number of descriptions (6), potentially limiting the model's exposure to varied contexts.

### Improvement Strategies

- Consider allocating additional time to incorporate the entire dataset, ensuring comprehensive model coverage.
- Gather human-generated descriptions to enhance the authenticity and diversity of the dataset.
- Allow users to contribute additional descriptions for commands through the interface, promoting a richer dataset.
- Expand the interface functionality to enable users to provide their own command descriptions, fostering user engagement and dataset enrichment.
- Explore alternative model architectures or methods, such as deep learning approaches, to assess their effectiveness in capturing complex relationships within the dataset.

Feel free to explore the project and provide any feedback!
