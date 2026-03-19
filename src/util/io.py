import os


def load_name_dataset(directory: str) -> tuple[list[str], list[str]]:
    """
    Loads a name dataset (X, y) consisting of all names provided in .txt files in the given directory.
    The .txt files are expected to contain 1 name per line.
    The label is the name of the file without the extension.

    Example:
    Given 2 files CHANGELING.txt and HUMAN_MALE.txt in data/names:
    load_name_dataset("data/names") -> ["Vaks", "Alveth Marshrunner"], ["CHANGELING", "HUMAN_MALE"]

    :param directory: Directory to search for .txt files containing names.
    :return: List of names and list of their respective labels.
    """
    X, y = [], []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if not os.path.isfile(file_path) or not file.endswith(".txt"):
            continue

        with open(file_path, "r") as f:
            names = f.read().splitlines()
        X.extend(names)
        y.extend([file[:-4]] * len(names))
    return X, y
