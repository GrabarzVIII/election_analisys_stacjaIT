from .const import DTYPES_DICT,CANDIDATES,NUM_COLUMNS
import pandas as pd

def prepare_results_data2020(filepath: str) -> pd.DataFrame:
    
    df = pd.read_csv(filepath ,sep=';', low_memory=False, converters=DTYPES_DICT)
    df = df[df['Typ obwodu'] == 'stały'].reset_index(drop=True)

    for c in df.columns:
        if c in NUM_COLUMNS:
            df[c].fillna(0)
            df[c] = pd.to_numeric(df[c], errors='coerce').astype(int)
        if any(candidate in c for candidate in CANDIDATES):
            df[c].fillna(0)
            df[c] = pd.to_numeric(df[c], errors='coerce').astype(int)

    df.rename(
        columns={
            'W tym z powodu postawienia znaku „X" obok nazwiska dwóch lub większej liczby kandydatów':'x_multi',
            'W tym z powodu niepostawienia znaku „X" obok nazwiska żadnego kandydata':'x_zero'
        }
    )
    
    return df


def prepare_trusttee_presence_data2020(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath, converters=DTYPES_DICT)