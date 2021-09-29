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
            data_tupples.append((c_pop['country'], c_pop['population'], c_cont['continent']))

print(data_tupples)