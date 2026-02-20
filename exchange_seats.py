import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    df=seat.copy()
    max_id=df['id'].max()
    df['id']=df['id'].apply(
        lambda x:x+1 if x%2==1 and x != max_id
        else x-1 if x%2==0
        else x
    )
    return df.sort_values('id')