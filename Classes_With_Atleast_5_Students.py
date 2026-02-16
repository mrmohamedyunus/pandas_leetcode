import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = (
        courses.groupby('class')
        .size()
        .reset_index(name = 'student_count')
    )
    return courses[courses['student_count']>=5][['class']]