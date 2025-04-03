from abc import ABCMeta, abstractmethod
class TransformationInterface(metaclass=ABCMeta):
    @abstractmethod
    def change_to_datetime(self, column_name):
        pass

    @abstractmethod
    def round_to_hours(self, column_name):
        pass

    @abstractmethod
    def calculate_auxiliary_columns(self, column_name):
        pass

    @abstractmethod
    def merge_with(self, other_csv, on_columns=None, how='outer'):
        pass

    @abstractmethod
    def save_to_folder(self, path):
        pass
