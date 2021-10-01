import numpy
import matplotlib.pyplot as plt
import json
import data_manipulation as dm

class Chart:
   def __init__(self):
      #self.type = type
      pass

   def create_objekt(self):
      objekt = dm.Data_manipulation()
      objekt.create_data()
      objekt.arrange_data()
      objekt.calculate_percentages()

      return objekt
 
   def create_pie_chart(self):
      #get percentages
      values = self.create_objekt().return_population_percentages()
      #prepare axis and labels
      fig = plt.figure()
      ax = fig.add_axes([0,0,1,1])
      ax.axis('equal')
      langs = ['Europe', 'Africa', 'Asia', 'Oceania', 'South America', 'North America']

      #draw the chart
      ax.pie(values, labels = langs,autopct='%1.2f%%')
      plt.show()