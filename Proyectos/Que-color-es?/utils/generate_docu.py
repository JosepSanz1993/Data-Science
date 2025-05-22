from abc import ABC, abstractmethod
class TrainingResultDocument(ABC):
    @abstractmethod
    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        pass