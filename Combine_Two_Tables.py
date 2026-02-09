import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df_mrg = pd.merge(person, address, on='personId', how='left')
    return df_mrg[['firstName', 'lastName', 'city', 'state']]