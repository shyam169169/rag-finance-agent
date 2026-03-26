import pandas as pd
from typing import List
from fastapi import UploadFile

REQUIRED_COLUMNS = ["date", "category", "amount"]

async def process_csv(file: UploadFile) -> List[str]:
    df = pd.read_csv(file.file)
    chunks = create_chunks_from_df(df)
    return chunks

def create_chunks_from_df(df: pd.DataFrame) -> List[str]:
    """
    Convert dataframe into list of text chunks.
    """
    df = normalize_columns(df)
    validate_columns(df)

    chunks = []

    for _, row in df.iterrows():
        chunk = row_to_chunk(row)
        chunks.append(chunk)
    
    return chunks

def row_to_chunk(row: pd.Series) -> str:
    """
    Convert a single row into a text chunk.
    """
    return (
        f"[TRANSACTION]\n"
        f"Date: {row.get('date')}\n"
        f"Category: {row.get('category')}\n"
        f"Amount: {row.get('amount')}\n"
        f"Description: {row.get('description', '')}"
    )

def normalize_columns(df: pd.DataFrame):
    """
    Normalize column names to lowercase.
    """
    df.columns = [col.strip().lower() for col in df.columns]
    return df

def validate_columns(df: pd.DataFrame) -> None:
    """
    Ensure required columns exist.
    """

    print(f"df columns = {df.columns}")
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")