import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd 
def make_data()-> pd.DataFrame:

   return kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "adilshamim8/student-depression-dataset",
    "student_depression_dataset.csv"
    )
    


