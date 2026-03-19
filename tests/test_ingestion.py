import pytest
import pandas as pd

from app.services import ingestion

def test_create_chunks():
    data = {
        "DATE ": ["2024-01-01"],
        "CATEGORY": ["Shopping"],
        "AMOUNT": [101]
    }
    df = pd.DataFrame(data)
    chunks = ingestion.create_chunks_from_df(df)
    assert len(chunks) == 1
    assert "Shopping" in chunks[0]
    assert "101" in chunks[0]
    assert "Date" in chunks[0]

def test_data_validation():
    data = {
        "DATE ": ["2024-01-01"],
        "CATEGORY": ["Shopping"]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        ingestion.create_chunks_from_df(df)



    