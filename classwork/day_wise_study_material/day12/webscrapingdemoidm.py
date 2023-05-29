# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:39:33 2020

@author: anilk
"""
print("Hello World!");



#import libraries
#pip install requests
#pip install bs4

#request module helps to send request to web site and retirve html page
import requests  
from bs4 import BeautifulSoup
import re

url = 'http://www.imdb.com/search/title?release_date=2021&sort=num_votes,desc&page=1'
response = requests.get(url)
print(response.content)
#print(response.text[:500])


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
print(html_soup)

#data=html_soup.find_all("a")
#print(len(data))

#find_all  ------ all matching element
#find  ---- first matching element

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))


#to get name and movie number of first movie


first_movie=movie_containers[0]
print(first_movie)
# to retrieve movie name
#print(first_movie.find_all('a'))

h3=first_movie.h3.find_all("a")
h3[1]
print(first_movie.h3)
print(first_movie.h3.a)
print(first_movie.h3.a.text)

#to find the year
s=first_movie.find('span', class_ = 'lister-item-year text-muted unbold')
print(s)
print(s.text)




print(first_movie.strong.text)


second_movie=movie_containers[1]
print(second_movie.h3.a.text)

#to add all movinames in a list
names=[]
rating=[]
years=[]
for movie in movie_containers:
    names.append(movie.h3.a.text)
    rating.append(movie.strong.text)
    s=movie.find('span', class_ = 'lister-item-year text-muted unbold')
    years.append(s.text)
print(names)
print(rating)
print(years)


data={"name":names,"ratings":rating,"years":years}
import pandas as pd
df=pd.DataFrame(data)

df["ratings"].max()



#to print the rating
print(first_movie.strong.text)

#to find year test
print(first_movie.h3)
#print(first_movie.h3.find_all('span'))

#to find first year

first_year = first_movie.find('span', class_ = 'lister-item-year text-muted unbold')

print(first_year.text)

#To retrieve rating
print(first_movie.strong)
first_imdb = float(first_movie.strong.text)


names = []
years = []
ratings = []
for movie in movie_containers:
    #to retrieve movie name
    names.append(movie.h3.a.text)
    yr=movie.find('span', class_ = 'lister-item-year text-muted unbold').text 
    years.append(yr)
    ratings.append(movie.strong.text)   
d={"name":names,"year":years,"ranting":ratings}
import pandas as pd
df=pd.DataFrame(d)
print(df.info())







#to find metascore
first_mscore = first_movie.find('span', class_ = 'metascore favorable')  #to find based on class
first_mscore = int(first_mscore.text)
print(first_mscore)

#to find all movie names
for ob in movie_containers:
    print(ob.h3.a.text)



first_year= first_movie.find('span',class_="lister-item-year text-muted unbold")
print(first_year.text)

print(first_movie.strong.text)

first_metascore=first_movie.find('span',class_='metascore favorable')
print(type(first_metascore))
print(int(first_metascore.text))





#to find votes
print(first_movie)
first_votes = first_movie.find('span', attrs = {'name':'nv'}) #to find  element based on attribute
print(first_votes.text) #to retrieve tag contents
print(first_votes['data-value'])  #to retrieve value of attribute

# to retrieve the rating
first_rating=first_movie.find("strong")
print(first_rating.text)


#------------------------------------
#to find data for all movies
# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
# Extract data from individual movie container
for container in movie_containers:
# If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
# The name
        name = container.h3.a.text
        names.append(name)
    # The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
    # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
    # The Metascore
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))
    # The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

#to average rating of all movies
#to find year of movies with highest vote
#to analyze data convert into Dataframe
import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(test_df.info())
test_df
