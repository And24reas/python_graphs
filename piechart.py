import numpy
import matplotlib.pyplot as plt
import json


data_population = []
data_continent = []

data_tupples = []

with open('countries_population.json') as json_file:
    data_population= json.load(json_file)
    """
    for x in data:
        print (x['country'], "\t\t", x['population'] )
    """
with open('countries_continent.json') as json_file2:
    data_continent = json.load(json_file2)

for c_pop in data_population:
    for c_cont in data_continent:
        if c_pop['country'] == c_cont['country']:
            data_tupples.append([c_pop['country'], c_pop['population'], c_cont['continent']])



europe_pop = 0
oceania_pop = 0
asia_pop = 0
africa_pop = 0
sAmerica_pop = 0
nAmerica_pop = 0
pop_sum = 0
for country in data_tupples:
    continent = country[2]
    if continent == 'Oceania':
        oceania_pop += country[1]
    elif continent == 'Europe':
        europe_pop += country[1]
    elif continent == 'Asia':
        asia_pop += country[1]
    elif continent == "South America":
        sAmerica_pop += country[1]
    elif continent == "North America":
        nAmerica_pop += country[1]
    elif continent == "Africa":
        africa_pop += country[1]

pop_sum = europe_pop + asia_pop + oceania_pop + africa_pop + sAmerica_pop + nAmerica_pop

print (pop_sum)

europe_pop_percentage = (europe_pop/pop_sum)*100
asia_pop_percentage = (asia_pop/pop_sum)*100
africa_pop_percentage = (africa_pop/pop_sum)*100
oceania_pop_percentage = (oceania_pop/pop_sum)*100
sAmerica_pop_percentage = (sAmerica_pop/pop_sum)*100
nAmerica_pop_percentage = (nAmerica_pop/pop_sum)*100

percentage_list = [europe_pop_percentage,africa_pop_percentage,asia_pop_percentage,oceania_pop_percentage,sAmerica_pop_percentage,nAmerica_pop_percentage]

print(sum(percentage_list))

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Europe', 'Africa', 'Asia', 'Oceania', 'South America', 'North America']

ax.pie(percentage_list, labels = langs,autopct='%1.2f%%')
plt.show()
