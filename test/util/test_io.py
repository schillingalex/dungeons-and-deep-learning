import os

import pytest

from util.io import load_name_dataset


def test_load_name_dataset_simple():
    X, y = load_name_dataset(os.path.join(os.path.dirname(__file__), "data", "names"))
    assert len(X) == len(y) == 6, "X and y should have length 6"
    assert len(set(y)) == 3, "There should be 3 unique labels"
    assert "Vaks" in X, "The name Vaks should appear in X"
    assert "HUMAN" in y, "The label HUMAN should appear in y"


def test_load_name_dataset_no_txt_files():
    with pytest.raises(ValueError):
        _ = load_name_dataset(os.path.join(os.path.dirname(__file__), "data"))
