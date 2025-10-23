import os
import utils

class TrainingCorpus:
    @staticmethod
    def get_data(file_path):
        """
        Load training data from the specified file path. If the path is a directory,
        read all files and their classifications from '!truth.txt'. If the path is a single file,
        return its contents with a default label of 'OK'.

        Parameters:
        file_path (str): Path to a directory containing training files or a single file.

        Returns:
        tuple: A tuple of two lists:
            - texts: List of file contents as strings.
            - labels: Corresponding list of labels ('SPAM' or 'OK') for each file.
        """
        texts = []
        labels = []

        # Check if the given path is a directory
        if os.path.isdir(file_path):
            # Path to the classification file '!truth.txt'
            classification_file = os.path.join(file_path, "!truth.txt")
            if os.path.exists(classification_file):
                # Read classifications from '!truth.txt'
                classifications = utils.read_classification_from_file(classification_file)

                # Iterate over all files in the directory
                for filename in os.listdir(file_path):
                    # Skip the classification file itself
                    if filename != "!truth.txt":
                        full_path = os.path.join(file_path, filename)
                        # Ensure the item is a file before reading
                        if os.path.isfile(full_path):
                            with open(full_path, 'r', encoding='utf-8') as f:
                                # Read and store the file contents
                                text = f.read()
                                texts.append(text)
                                # Get the corresponding label or default to 'OK'
                                labels.append(classifications.get(filename, "OK"))
        else:
            # If the path is a single file, read and assign a default label
            with open(file_path, 'r', encoding='utf-8') as f:
                texts = [f.read()]
                labels = ["OK"]

        return texts, labels
