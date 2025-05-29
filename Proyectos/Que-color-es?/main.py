from models.insolation_forest import AnomalyCleaner
from models.mlp import ColorClassifier
from models.svm import SVMColorClassifier
from models.random_forest import RandomForestColorClassifier
from scripts.global_var import *
from scripts.etl import ETL
from models.kmeans import KMeansColorClassifier
import argparse

etl = ETL(DATA_NOT_PROCESSED)
anomaly = AnomalyCleaner()
mlp = ColorClassifier()
rf = RandomForestColorClassifier()
kmeans = KMeansColorClassifier(DATA_PROCESSED)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Color classification with optional anomaly detection.")
    parser.add_argument("--detect-anomalies", action="store_true", help="Enable anomaly detection step")
    args = parser.parse_args()
    etl.save_json(DATA_PROCESSED) # Save the processed data to a JSON file

    if args.detect_anomalies:
        anomaly.load_data(DATA_PROCESSED)  # Load the processed data
        anomaly.train_model("Color")  # Train the anomaly detection model
        anomaly.show_anomalies()  # Show detected anomalies
        anomaly.export_clean_json(DATA_CLEANED)  # Export cleaned data to JSON

        mlp.load_data(DATA_CLEANED)  # Load cleaned data
        mlp.train_model("Color")  # Train the MLP model
        print(mlp.predict_color([109, 124, 117, 359, 86]))  # Predict color using MLP
        svm = SVMColorClassifier(DATA_CLEANED)
        svm.train_model("Color")  # Train the SVM model
        sample = {
            "Red": 110,
            "Green": 120,
            "Blue": 115,
            "Clear": 360,
            "Lux": 85
        }
        print(svm.predict_color(sample))  # Predict color using SVM

        rf.train_model("Color",DATA_CLEANED)  # Train the Random Forest model
        rf.predict_color({"Red": 109, "Green": 124, "Blue": 117, "Clear": 359, "Lux": 86})

        kmeans = KMeansColorClassifier(DATA_PROCESSED)
        kmeans.visualize_clusters("Color")  # Visualize clusters using K-Means
        print(kmeans.check_cluster_Var("Cluster", "Color"))  # Check cluster variance
    else:
        mlp.load_data(DATA_PROCESSED)  # Load cleaned data
        mlp.train_model("Color")  # Train the MLP model
        print(mlp.predict_color([109, 124, 117, 359, 86]))  # Predict color using MLP
        svm = SVMColorClassifier(DATA_PROCESSED)
        svm.train_model("Color")  # Train the SVM model
        sample = {
            "Red": 110,
            "Green": 120,
            "Blue": 115,
            "Clear": 360,
            "Lux": 85
        }
        print(svm.predict_color(sample))  # Predict color using SVM

        rf.train_model("Color",DATA_PROCESSED)  # Train the Random Forest model
        rf.predict_color({"Red": 109, "Green": 124, "Blue": 117, "Clear": 359, "Lux": 86})

        kmeans = KMeansColorClassifier(DATA_PROCESSED)
        kmeans.visualize_clusters("Color")  # Visualize clusters using K-Means
        print(kmeans.check_cluster_Var("Cluster", "Color"))  # Check cluster variance





