import pandas as pd

df = pd.read_csv(iris_data.csv)

a = pd.Series(data = sample_id)

b = pd.Series(data = species)

c = pd.Series(data = petal_length)

d = pd.Series(data = petal_width)

e = pd.Series(data = sepal_length)

f = pd.Series(data = sepal_width)

#combine the datasets
combined_data = pd.concat([a, b, c, d, e, f])
print(combined_data)

df = pd.DataFrame(data = combined_data)
print(df)

#calculate the correlation
print(df.corr)

#calculate the average
print(df.mean)

#calculate the median 
print(df.median)

#calculate the standard deviation
print(df.std)

#Which species of irises are most similar/are least similar?
#virginia and versicolor are most similar based on the measurements given
#virginia and setosa are the least similar based on the measurements given