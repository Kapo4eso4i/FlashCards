#!/usr/bin/env python
import pandas as pd

data = pd.read_csv("~/PycharmProjects/FlashCards/data/ro_en_1-1999.csv")

row = data.sample(ignore_index=True)


print(row.at[0,"ro"])
