class BaseFilter:
    def __init__(self):
        pass

    def train(self, training_data):
        pass

    def test(self, test_data_path):
        pass

    def predict(self, test_data):
        pass

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
