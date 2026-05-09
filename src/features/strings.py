

def character_vocabulary_from_dataset(dataset: list[str], minimum_set: list[str] = None) -> list[str]:
    """
    Extracts the unique characters present in all samples of the given dataset.

    :param dataset: List of strings representing the samples.
    :param minimum_set: List of characters to include in the vocabulary even if they are missing from the dataset.
    :return: Sorted list of unique characters.
    """
    if minimum_set is None:
        minimum_set = []

    complete_str = "".join(minimum_set + dataset)
    characters = list(set(complete_str))
    return sorted(characters)
