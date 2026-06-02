# XAI-Depression-Detection

Depression Severity Detection from Social Media using Natural Language Processing (NLP) and Explainable Artificial Intelligence (XAI).

## Overview

This project aims to automatically detect and classify the severity of depression from social media text into four categories:

* None
* Mild
* Moderate
* Severe

The system combines traditional machine learning, deep learning, and transformer-based approaches while providing interpretable predictions through Explainable AI techniques.

## Features

* Multi-class depression severity classification
* TF-IDF + Logistic Regression baseline
* DistilBERT-based text classification
* Explainable AI (XAI) support
* Django web interface for prediction
* Social media text preprocessing pipeline

## Technologies Used

* Python
* Django
* Scikit-learn
* Transformers (Hugging Face)
* DistilBERT
* Pandas
* NumPy



## Model Performance

| Model               | Accuracy | Weighted F1 |
| ------------------- | -------- | ----------- |
| Logistic Regression | 0.68     | 0.68        |
| SVM                 | 0.67     | 0.67        |
| BiLSTM              | 0.63     | 0.63        |
| DistilBERT          | 0.67     | 0.67        |

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Django Server

```bash
python manage.py runserver
```

### Open in Browser

```text
http://127.0.0.1:8000/
```

## Future Work

* Bangla language support
* SHAP-based explanations
* Clinical dataset validation
* Real-time monitoring pipeline

## Authors

* Afia Mahmud Roshni

