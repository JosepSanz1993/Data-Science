from models.trainmodel import model_train
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
from trainmodel import pl
class KMeansColorClassifier(model_train):
    def __init__(self, data_path):
        self.model = None
        self.data = self.load_data(data_path)
    
    def train_model(self, target_column):
        X = self.data.drop(target_column)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        self.model = KMeans(n_clusters=5, random_state=42)
        clusters = self.model.fit_predict(X_scaled)
        self.data = self.data.with_columns(pl.Series("Cluster", clusters))
        self.data.to_pandas().to_json('data/processed/kmeans.json', orient='records')
        return X_scaled

    def visualize_clusters(self, target_column):
        X_scaled = self.train_model(target_column)
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        plt.figure(figsize=(8, 6))
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=self.data["Cluster"], cmap="Set2")
        plt.title("Clustering amb K-Means")
        plt.xlabel("PCA 1")
        plt.ylabel("PCA 2")
        plt.colorbar(label="Cluster")
        plt.show()

    def check_cluster_Var(self,cluster,var):
        return pd.crosstab(self.data[cluster],self.data[var])
    