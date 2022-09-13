import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from pprint import pprint

import webbrowser
import pandas as pd
from tempfile import NamedTemporaryFile

def df_window(df: pd.DataFrame):
    with open("presentation.html", "w") as f:
        df.to_html(f)
    f = open("presentation.html", "r")

for file in os.listdir("data"):
    print(file)

train_dataset = pd.read_csv("data/train.csv")
test_dataset = pd.read_csv("data/test.csv")

all_data = pd.concat([test_dataset, train_dataset], )

#all_data = pd.concat([train_dataset, test_dataset])
print(train_dataset.shape)
print(test_dataset.shape)

all_data["Survived"].fillna("test_entry", inplace=True)

print(all_data.columns)

pprint([(column, all_data[column].isna().sum()) for column in all_data.columns])

all_data["Ticket"] = all_data["Ticket"].apply(len)

all_data["Age_na"] = all_data["Age"].isna()
all_data["Age"].fillna(all_data["Age"].mean(), inplace=True)

all_data = pd.concat([all_data, pd.get_dummies(all_data["Sex"])], axis=1)

df_window(all_data)
webbrowser.open("presentation.html")




