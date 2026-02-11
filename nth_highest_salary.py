import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sort_sal = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(sort_sal)<N or N<=0:
        result = [None]
    else:
        result=[sort_sal.iloc[N-1]]

    return pd.DataFrame({f'getNthHighestSalary({N})': result})