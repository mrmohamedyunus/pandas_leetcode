import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips=trips[(trips['request_at']>='2013-10-01') &
    (trips['request_at']<='2013-10-03')]
    trips=trips.merge(
        users[['users_id','banned']],
        left_on='client_id',
        right_on='users_id',
        how='left'
    ).rename(columns={'banned':'client_banned'})

    trips=trips.merge(
        users[['users_id','banned']],
        left_on='driver_id',
        right_on='users_id',
        how='left'
    ).rename(columns={'banned':'driver_banned'})

    trips=trips[(trips['client_banned']=='No')&
    (trips['driver_banned']=='No')]

    trips['is_cancelled']=trips['status']!='completed'

    result=(
        trips.groupby('request_at')
        .agg(
            **{'Cancellation Rate':('is_cancelled',
            lambda x: round(x.mean(), 2))}
        )
        .reset_index()
        .rename(columns={'request_at': 'Day'})
    )
    return result

  