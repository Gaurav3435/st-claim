import pandas as pd

# Read JSON data into a Pandas DataFrame
df = pd.read_json('data.json')
df.set_index("pmid")
print(list(df.index))
# Display the DataFrame
print("DataFrame from JSON:")
print(df)
