"""Run a held-out evaluation of the dress recommendation coursework."""

import argparse

import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="CSV FILES/Attribute DataSet.csv")
    data = pd.read_csv(parser.parse_args().csv)
    features = data.drop(columns=["Dress_ID", "Recommendation"])
    labels = data["Recommendation"]
    train, test, y_train, y_test = train_test_split(
        features, labels, test_size=0.25, random_state=42, stratify=labels
    )
    categorical = features.select_dtypes(exclude="number").columns.tolist()
    numeric = features.select_dtypes(include="number").columns.tolist()
    preprocess = make_column_transformer(
        (make_pipeline(SimpleImputer(strategy="most_frequent"),
                       OneHotEncoder(handle_unknown="ignore")), categorical),
        (SimpleImputer(strategy="median"), numeric),
    )
    models = {
        "Majority baseline": DummyClassifier(strategy="most_frequent"),
        "Logistic regression": make_pipeline(
            preprocess, LogisticRegression(max_iter=1000)
        ),
    }
    print(f"Train rows: {len(train)}. Test rows: {len(test)}.")
    for name, model in models.items():
        predicted = model.fit(train, y_train).predict(test)
        print(
            f"{name}: accuracy={accuracy_score(y_test, predicted):.4f}, "
            f"balanced accuracy={balanced_accuracy_score(y_test, predicted):.4f}, "
            f"confusion matrix={confusion_matrix(y_test, predicted).tolist()}"
        )
