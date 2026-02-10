import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=employee.merge(
        department, left_on='departmentId',right_on='id',how='inner'
    )
    df['rank']=df.groupby('name_y')['salary'].rank(
        method='dense',
        ascending=False
    )
    df=df[df['rank']<=3]

    return df[["name_y","name_x","salary"]].rename(
        columns={
            "name_y":"Department",
            "name_x":"Employee",
            "salary":"Salary"
        }
    )