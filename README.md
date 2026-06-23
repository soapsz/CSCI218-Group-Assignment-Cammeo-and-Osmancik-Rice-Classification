# Rice Classification Pipeline: Cammeo vs. Osmancik

## Overview
This repository contains a machine learning pipeline developed to classify two distinct species of rice (Cammeo and Osmancik) based on their morphological features. The project focuses on end-to-end data processing, addressing dataset imbalance, and evaluating multiple classification algorithms to determine the most optimal model.

## Technologies Used
* **Language:** Python
* **Libraries:** Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
* **Techniques:** Feature Selection, SMOTE (Synthetic Minority Over-sampling Technique), Cross-Validation

## Methodology
The pipeline processes morphological image data (like area, perimeter, and eccentricity) and applies six different machine learning models to classify the rice grains. 

Key steps in the pipeline included:
1. **Exploratory Data Analysis:** Visualising feature distributions and identifying class imbalances.
2. **Data Preprocessing:** Standardising features and applying SMOTE to synthesise data for the minority class, ensuring the models train without bias.
3. **Model Implementation:** Trained and tuned six distinct algorithms:
   * K-Nearest Neighbors (KNN)
   * Naive Bayes
   * Logistic Regression
   * Random Forest
   * Support Vector Machine
   * Multi-Layer Perceptron
4. **Evaluation:** Comparing models based on Accuracy, Precision, Recall, and F1-Score.

## Key Results
* **Best Performing Model:** Logistic Regression
* **Top Accuracy:** 0.9278
