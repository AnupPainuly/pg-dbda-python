from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv('housing.csv')
long=df['longitude']
lat=df['latitude']
house_age=df['housing_median_age']
plt.scatter(long,lat,label="House Age",c=house_age).set_xlabel("Latitude") #For a sequence of values to be color-mapped, use the 'c' argument instead.
plt.title("Latitude & Longitude differntiated with house age")
plt.ylabel("Longitude")
plt.xlabel("Latitude")
plt.legend()
plt.style.use('ggplot')
plt.show()

"""

#OOP way of doing the above
fig is canvas and ax is axis
fig,ax=plt.subplots()
ax.scatter(long,lat,c=house_age)
ax.set_xlabel("Latitude")
plt.show()

"""
