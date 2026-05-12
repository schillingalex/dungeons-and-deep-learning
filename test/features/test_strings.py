from features.strings import character_vocabulary_from_dataset


def test_character_vocabulary_from_dataset_simple():
    chars = character_vocabulary_from_dataset(["abc", "abd", "aaa"])
    assert chars == ["a", "b", "c", "d"]


def test_character_vocabulary_from_dataset_empty_strings():
    chars = character_vocabulary_from_dataset(["", ""])
    assert chars == []


def test_character_vocabulary_from_dataset_empty_dataset():
    chars = character_vocabulary_from_dataset([])
    assert chars == []


def test_character_vocabulary_from_dataset_minimum():
    chars = character_vocabulary_from_dataset(["aaa"], minimum_set=["c", "b", "a"])
    assert chars == ["a", "b", "c"]


def test_character_vocabulary_from_dataset_whitespace():
    chars = character_vocabulary_from_dataset(["a b c"])
    assert chars == ["a", "b", "c"]


def test_character_vocabulary_from_dataset_include_whitespace():
    chars = character_vocabulary_from_dataset(["a b\tc\n"], include_whitespace=True)
    assert chars == ["\t", "\n", " ", "a", "b", "c"]
