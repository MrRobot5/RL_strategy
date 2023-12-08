
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))

df.to_csv("foo.csv")

read_df = pd.read_csv("foo.csv")
print(read_df)