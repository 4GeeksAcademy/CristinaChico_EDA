from utils import db_connect
engine = db_connect()


# your code here
import pandas as pd

total_data = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv")
total_data.head()

total_data.shape

total_data.info()

total_data.drop("id", axis = 1).duplicated().sum()

total_data = total_data.drop_duplicates(subset = total_data.columns.difference(['id']))
print(total_data.shape)
total_data.head()

if total_data.duplicated().sum():
    total_data = total_data.drop_duplicates()
print(total_data.shape)
total_data.head()