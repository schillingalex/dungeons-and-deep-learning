import re


def character_vocabulary_from_dataset(dataset: list[str], minimum_set: list[str] = None,
                                      include_whitespace: bool = False) -> list[str]:
    """
    Extracts the unique characters present in all samples of the given dataset.

    :param dataset: List of strings representing the samples.
    :param minimum_set: List of characters to include in the vocabulary even if they are missing from the dataset.
        Optional, default: None.
    :param include_whitespace: Determines whether to include whitespace characters in the vocabulary. Optional,
        default: False.
    :return: Sorted list of unique characters.
    """
    if minimum_set is None:
        minimum_set = []

    complete_str = "".join(minimum_set + dataset)
    if not include_whitespace:
        complete_str = re.sub(r"\s", "", complete_str)
    characters = list(set(complete_str))
    return sorted(characters)


def count_words_in_string(string: str) -> int:
    """
    Counts the number of words in a given string based on a simple whitespace split.

    Examples:
        Hello world -> 2 words
        23-year-old -> 1 word

    :param string: Input string to count the words in.
    :return: Number of words in input string.
    """
    return len(string.split())
