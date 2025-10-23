import pickle

def save_object(obj, filename):
    """
    Save a Python object to a file using pickle.

    Parameters:
    obj (any): The Python object to be serialized.
    filename (str): The file path where the object should be saved.
    """
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def load_object(filename):
    """
    Load a Python object from a pickle file.

    Parameters:
    filename (str): The file path from which the object should be loaded.

    Returns:
    any: The deserialized Python object.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)

def read_classification_from_file(filepath: str):
    """
    Read classifications from a file and return them as a dictionary.

    Parameters:
    filepath (str): The path to the classification file.

    Returns:
    dict: A dictionary with filenames as keys and their corresponding labels as values.
    """
    classification_dict = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                filename, label = parts
                classification_dict[filename] = label
    return classification_dict
