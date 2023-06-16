# %%
print("My name is rahul")

# %%
rahul="HelloVai"


# %%

import pandas as pd

data1 = {"Name": ["Alice", "Bob", "Charlie"],
         "Age": [20, 18, 19]}
df1 = pd.DataFrame(data1)

data2 = {"Name": ["David", "Eve", "Frank"],
         "Age": [21, 22, 20]}
df2 = pd.DataFrame(data2)

appended_df = pd.concat([df1, df2], ignore_index=True)

print(appended_df)


