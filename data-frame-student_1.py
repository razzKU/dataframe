import pandas

data = pandas.read_csv('student - Sheet1.csv')

print(data.to_string(), "\n")

for column in data.columns[2:]:
    max_value = data[column].max()
    df2 = data.loc[data[column] == max_value, 'name']
    print(f"Student who got highest mark in {column} is {df2.values} and the mark is {max_value}")
