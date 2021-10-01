import json
import matplotlib.pyplot as plt
import numpy as np

class Data_manipulation:
    def __init__(self):
    
        self.data_population = []
        self.data_continent = []
        self.data_lifeexpectancy = []
        self.data_surface_area = []
        self.data_tupples = []
        self.europe_pop = 0
        self.oceania_pop = 0
        self.asia_pop = 0
        self.africa_pop = 0
        self.sAmerica_pop = 0
        self.nAmerica_pop = 0
        self.population_sum = 0

    def create_data(self):
        with open('countries_population.json') as json_file:
            self.data_population= json.load(json_file)

        with open('countries_continent.json') as json_file2:
            self.data_continent = json.load(json_file2)

        with open('countries_life-expectancy.json') as json_file3:
            self.data_lifeexpectancy = json.load(json_file3)

        with open('countries_by_surface_area.json') as json_file4:
            self.data_surface_area = json.load(json_file4)

    def arrange_data(self):
        for c_pop in self.data_population:
            for c_cont in self.data_continent:
                if c_pop['country'] == c_cont['country']:
                    self.data_tupples.append([c_pop['country'], c_pop['population'], c_cont['continent']])
                
        
    def calculate_percentages(self):
        for country in self.data_tupples:
            continent = country[2]
            if continent == 'Oceania':
                self.oceania_pop += country[1]
            elif continent == 'Europe':
                self.europe_pop += country[1]
            elif continent == 'Asia':
                self.asia_pop += country[1]
            elif continent == "South America":
                self.sAmerica_pop += country[1]
            elif continent == "North America":
                self.nAmerica_pop += country[1]
            elif continent == "Africa":
                self.africa_pop += country[1]

        self.population_sum = self.europe_pop + self.asia_pop + self.oceania_pop + self.africa_pop + self.sAmerica_pop + self.nAmerica_pop
        print (self.population_sum)
        pop_sum = self.population_sum
        self.europe_pop_percentage = (self.europe_pop/pop_sum)*100
        self.asia_pop_percentage = (self.asia_pop/pop_sum)*100
        self.africa_pop_percentage = (self.africa_pop/pop_sum)*100
        self.oceania_pop_percentage = (self.oceania_pop/pop_sum)*100
        self.sAmerica_pop_percentage = (self.sAmerica_pop/pop_sum)*100
        self.nAmerica_pop_percentage = (self.nAmerica_pop/pop_sum)*100

    def return_population_percentages(self):
        self.percentage_list = [self.europe_pop_percentage, self.africa_pop_percentage, self.asia_pop_percentage, self.oceania_pop_percentage, self.sAmerica_pop_percentage, self.nAmerica_pop_percentage]

        print(sum(self.percentage_list))
        return self.percentage_list

   
