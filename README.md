
# 🩺 Diabetes Prediction ML Pipeline with DVC

*A Machine Learning pipeline for predicting diabetes using DVC (Data Version Control) for reproducibility and organization. The pipeline automates data preprocessing, model training, evaluation, and version control to ensure reproducibility and scalability.*

---

## 🌟 Features

- 1️⃣*End-to-End Pipeline* from data preprocessing to model evaluation.
- 2️⃣*Structured Project Layout* with clear separation of data, models, source code, and configurations.
- 3️⃣*DVC Integration* for data versioning, pipeline tracking, and reproducibility.
- 4️⃣*Preprocessing* including data cleaning, feature engineering, and train-test splitting.
- 5️⃣*Configurable Parameters* via params.yaml for easy experimentation.
- 6️⃣*Model Training & Evaluation* with metrics tracking.

---

## 🗂 Project Structure

```bash
piyushbhavsar22-diabetes-ml-pipeline-with-dvc/
├── README.md               # Project documentation
├── dvc.lock                # DVC pipeline lock file
├── dvc.yaml                # DVC pipeline stages
├── params.yaml             # Configuration parameters
├── requirements.txt        # Python dependencies
├── data/
│   ├── processed/          # Processed datasets (e.g., train/test splits)
│   └── raw/                # Raw dataset (versioned with DVC)
├── models/                 # Trained model artifacts
├── src/                    # Source code
│   ├── preprocess.py       # Data preprocessing script
│   ├── train.py            # Model training script
│   └── evaluate.py         # Model evaluation script
└── .dvc/                   # DVC internal configurations
    ├── config
    └── .gitignore
```

## ⚡ Quick Start
📋 Prerequisites
- Python 3.7+
- DVC (pip install dvc)

## 🚀 Run the Pipeline
Execute the entire pipeline with DVC:
```
dvc repro
```


## ⚙ Configuration (params.yaml)
- *preprocess:*
  - test_size: 0.2
  - random_state: 42

- *train:*
  - model_type: "random_forest"
  - n_estimators: 100
  - max_depth: 5

- *evaluate:*
  - metrics: ["accuracy", "precision", "recall"]
