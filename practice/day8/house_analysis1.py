import pandas as pd
df=pd.read_csv('housing.csv')
#filtering data from with total_bedrooms and ocean_proximity columns
filtered_df=df[(df.total_bedrooms==4) & (df.ocean_proximity=="NEAR OCEAN")]
print(filtered_df)
#gets the number of rows from the data frame .shape[1] is for columns
print(filtered_df.shape[0])
