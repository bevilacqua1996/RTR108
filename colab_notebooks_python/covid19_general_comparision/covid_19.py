# -*- coding: utf-8 -*-
"""covid_19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q1Lw2QAG9CylQ28k2Px7B3YrTXQouAXm
"""

import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

csv_covid_19 = pd.read_csv('./covid_19_data.csv')
csv_covid_19.head()
country1 = "Lithuania"
country2 = "Latvia"

csv_covid_19.describe()

covid_19_country1 = csv_covid_19.where(csv_covid_19["Country/Region"]==country1).sort_values(by='ObservationDate')
covid_19_country1.head()

covid_19_country2 = csv_covid_19.where(csv_covid_19["Country/Region"]==country2).sort_values(by='ObservationDate')
covid_19_country2.head()

list_dates = [];
list_dates = csv_covid_19['ObservationDate']
list_dates = list_country.drop_duplicates()

list_final_date = [];

for date in list_dates:
  num = int(date[3:5])
  list_final_date.append(date[3:5] + '/' + date[0:2])
  
def plot_graph_confirmed_cases(graph, title):
  chart = graph;
  chart.set_xticklabels(list_final_date, rotation=45, horizontalalignment='right');
  chart.set_ylabel('Confirmed Cases');
  chart.set_xlabel('Date');
  chart.grid(1);
  chart.set_title(title);

plt.figure(figsize=(20,5))
plot_graph_confirmed_cases(sbn.lineplot(x='ObservationDate', y='Confirmed', hue='Country/Region', marker='o', data=covid_19_country1), 'Confirmed Cases in ' + country1);

plt.figure(figsize=(20,5))
plot_graph_confirmed_cases(sbn.lineplot(x='ObservationDate', y='Confirmed', hue='Country/Region', marker='o', data=covid_19_country2), 'Confirmed Cases in ' + country2)

covid_19_compare = csv_covid_19[(csv_covid_19['Country/Region']==country1) | (csv_covid_19['Country/Region']==country2)]
covid_19_compare.sort_values(by='ObservationDate').head()

plt.figure(figsize=(20,5))
plot_graph_confirmed_cases(sbn.lineplot(x='ObservationDate', y='Confirmed', hue='Country/Region', marker='o', data=covid_19_compare), 'Comparision between ' + country1 + ' and ' + country2)