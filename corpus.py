import os


class Corpus:
    @staticmethod
    def get_data(file_path):
        """
        Load data from the specified file path. If the path is a directory,
        read all files except '!truth.txt' and '!prediction.txt' and store their contents.
        If the path is a single file, read its contents.

        Parameters:
        file_path (str): Path to a directory or a single file.

        Returns:
        dict: A dictionary where keys are filenames and values are file contents as strings.
        """
        result = {}

        # Check if the given path is a directory
        if os.path.isdir(file_path):
            # Iterate over all files in the directory
            for filename in os.listdir(file_path):
                # Skip special files '!truth.txt' and '!prediction.txt'
                if filename != "!truth.txt" and filename != "!prediction.txt":
                    full_path = os.path.join(file_path, filename)
                    # Ensure the item is a file before reading
                    if os.path.isfile(full_path):
                        with open(full_path, 'r', encoding='utf-8') as f:
                            # Read and strip contents, storing in the result dictionary
                            result[filename] = f.read().strip()
        else:
            # If the path is a single file, read and store its contents
            with open(file_path, 'r', encoding='utf-8') as f:
                result[os.path.basename(file_path)] = f.read().strip()

        return result
