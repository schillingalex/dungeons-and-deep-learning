from features.strings import character_vocabulary_from_dataset, count_words_in_string


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


def test_count_words_in_string_simple():
    n_words = count_words_in_string("Hello World")
    assert n_words == 2


def test_count_words_in_string_empty_string():
    n_words = count_words_in_string("")
    assert n_words == 0


def test_count_words_in_string_symbols():
    n_words = count_words_in_string("The 23-yeal-old Orc Krag'Thal")
    assert n_words == 4
