import pandas as pd # pyright: ignore[reportMissingModuleSource]
from config import BEST_MODEL_MAE

def test_data_shape():
    data = pd.read_csv("data/cleaned_data.csv")
    assert data.shape == (1000, 9), "Data shape is incorrect"

def test_mae_value():
    assert BEST_MODEL_MAE <= 6.0, "MAE is too high"

