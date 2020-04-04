#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas for data manipulation
import pandas as pd


# In[2]:


# Read in the most recent data
covid_cases = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')


# In[3]:


# Feel for the data
covid_cases.head()


# In[4]:


covid_cases[['cases', 'deaths']].describe()


# In[5]:


covid_cases.info()


# In[6]:


# Grouping data by country or territory
grouped_countries = covid_cases.groupby('countriesAndTerritories')


# In[7]:


# Data for US
grouped_countries.get_group('United_States_of_America')


# In[8]:


# Gets data for each of the 7 countries I will be looking at (China, US, Italy, Poland, Spain, United Kingdom, and South Korea)
China_data = grouped_countries.get_group('China')
US_data = grouped_countries.get_group('United_States_of_America')
Italy_data = grouped_countries.get_group('Italy')
Poland_data = grouped_countries.get_group('Poland')
Spain_data = grouped_countries.get_group('Spain')
UK_data = grouped_countries.get_group('United_Kingdom')
SK_data = grouped_countries.get_group('South_Korea')


# In[9]:


# Getting the countries with the highest number of cases
grouped_county_data = covid_cases.groupby('countriesAndTerritories').cases.sum().reset_index()


# In[10]:


# Displaying most cases by country desc
grouped_county_data.sort_values('cases', ascending = False)


# In[11]:


grouped_county_data['cases'].max()


# In[12]:


# All countries that can be explored in the data
covid_cases['countriesAndTerritories'].unique()


# In[13]:


# Sorting the countries we want to look at by year, month, and day to get sequential data
data_us = US_data.sort_values(['year', 'month', 'day'])
data_uk = UK_data.sort_values(['year', 'month', 'day'])
data_poland = Poland_data.sort_values(['year', 'month', 'day'])
data_spain = Spain_data.sort_values(['year', 'month', 'day'])
data_italy = Italy_data.sort_values(['year', 'month', 'day'])
data_china = China_data.sort_values(['year', 'month', 'day'])
data_sk = SK_data.sort_values(['year', 'month', 'day'])


# In[278]:


# Importing in plotly express for the first line graph for the US
import plotly.express as px
fig = px.line(data_us, x='dateRep', y='cases')

fig.update_layout(title='New Coronavirus Cases Each Day in the US',
                  xaxis_title='Date',
                  yaxis_title='Cases',
                  template='plotly_dark')

fig.show()


# In[293]:


# Importing graph_objects from Plotly to be used to graph multiple countries on the same graph
import plotly.graph_objects as go

# Adding each of the lines to the graph
fig = go.Figure()
fig.add_trace(go.Scatter(x=data_us['dateRep'], y=data_us['cases'], name='United States',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=data_italy['dateRep'], y=data_italy['cases'], name='Italy',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=data_spain['dateRep'], y=data_spain['cases'], name='Spain',
                         line=dict(color='#DD99FF', width=2)))
fig.add_trace(go.Scatter(x=data_poland['dateRep'], y=data_poland['cases'], name='Poland',
                         line=dict(color='#E60000', width=2)))
fig.add_trace(go.Scatter(x=data_uk['dateRep'], y=data_uk['cases'], name='United Kingdom',
                         line=dict(color='#6699FF', width=2)))
fig.add_trace(go.Scatter(x=data_china['dateRep'], y=data_china['cases'], name='China',
                         line=dict(color='#ffffff', width=2)))
fig.add_trace(go.Scatter(x=data_sk['dateRep'], y=data_sk['cases'], name='South Korea',
                         line=dict(color='#FF6699', width=2)))

# Adding title and axis titles
fig.update_layout(title='New Coronavirus Cases Each Day',
                  xaxis_title='Date',
                  yaxis_title='Cases',
                  annotations=[dict(
                      x="09/03/2020",
                      y=int(data_italy['cases']
                            [data_italy['dateRep'] == '09/03/2020']),
                      xref="x",
                      yref="y",
                      text="Italy Quarantine",
                      showarrow=True,
                      arrowhead=7,
                      ax=-50,
                      ay=-70, clicktoshow='onout', bgcolor='royalblue'
                  )])

fig.add_annotation(
    x="31/01/2020",
    y=int(data_spain['cases'][data_spain['dateRep'] == '31/01/2020']),
    text="First Spanish Case",
    arrowhead=7, ax=10, ay=-60, clicktoshow='onout', bgcolor='#DD99FF', arrowcolor='#DD99FF')

fig.add_annotation(
    x="04/03/2020",
    y=int(data_poland['cases'][data_poland['dateRep'] == '04/03/2020']),
    text="First Polish Case",
    arrowhead=7, ax=-50, ay=-50, clicktoshow='onout', bgcolor='#E60000', arrowcolor='#E60000')

fig.add_annotation(
    x="21/01/2020",
    y=int(data_us['cases'][data_us['dateRep'] == '21/01/2020']),
    text="First Confirmed US Case",
    arrowhead=7, ax=20, ay=-90, clicktoshow='onout', bgcolor='firebrick', arrowcolor='firebrick')

fig.add_annotation(
    x="13/03/2020",
    y=int(data_spain['cases'][data_spain['dateRep'] == '13/03/2020']),
    text="Spain Quarantine",
    arrowhead=7, ax=40, ay=-60, clicktoshow='onout', bgcolor='#DD99FF', arrowcolor='#DD99FF')

fig.add_annotation(
    x="31/01/2020",
    y=int(data_italy['cases'][data_italy['dateRep'] == '31/01/2020']),
    text="First Italian Case",
    arrowhead=7, ax=-50, clicktoshow='onout', bgcolor='royalblue', arrowcolor='royalblue')

fig.add_annotation(
    x="20/01/2020",
    y=int(data_sk['cases'][data_sk['dateRep'] == '20/01/2020']),
    text="First South Korean Case",
    arrowhead=7, ax=-60, clicktoshow='onout', bgcolor='#FF6699', arrowcolor='#FF6699')

fig.add_annotation(
    x="12/03/2020",
    y=int(data_poland['cases'][data_poland['dateRep'] == '12/03/2020']),
    text="Polish Lockdown",
    arrowhead=7, ax=0, ay=-100, clicktoshow='onout', bgcolor='#E60000', arrowcolor='#E60000')

fig.update_layout(hovermode='x', template='plotly_dark')

fig.show()


# In[16]:


# Generating the cumulative sum up to each day for each country since the data keeps track of new cases
spaindata = data_spain.cumsum()
polanddata = data_poland.cumsum()
ukdata = data_uk.cumsum()
chinadata = data_china.cumsum()
italydata = data_italy.cumsum()
unitedstatesdata = data_us.cumsum()


# In[17]:


# New dataframes to keep track of dates, cases, and deaths for each of the countries
uscase_death = pd.DataFrame(
    {'Date': data_us['dateRep'], 'Total Cases': unitedstatesdata['cases'], 'Total Deaths': unitedstatesdata['deaths']})
italycase_death = pd.DataFrame(
    {'Date': data_italy['dateRep'], 'Total Cases': italydata['cases'], 'Total Deaths': italydata['deaths']})
spaincase_death = pd.DataFrame(
    {'Date': data_spain['dateRep'], 'Total Cases': spaindata['cases'], 'Total Deaths': spaindata['deaths']})
ukcase_death = pd.DataFrame(
    {'Date': data_uk['dateRep'], 'Total Cases': ukdata['cases'], 'Total Deaths': ukdata['deaths']})
polandcase_death = pd.DataFrame(
    {'Date': data_poland['dateRep'], 'Total Cases': polanddata['cases'], 'Total Deaths': polanddata['deaths']})
chinacase_death = pd.DataFrame(
    {'Date': data_china['dateRep'], 'Total Cases': chinadata['cases'], 'Total Deaths': chinadata['deaths']})
skcase_death = pd.DataFrame(
    {'Date': data_sk['dateRep'], 'Total Cases': SK_data['cases'], 'Total Deaths': SK_data['deaths']})


# In[292]:


# Generates line graph for Total Cases
fig = go.Figure()
fig.add_trace(go.Scatter(x=uscase_death['Date'], y=uscase_death['Total Cases'], name='United States',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=italycase_death['Date'], y=italycase_death['Total Cases'], name='Italy',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=spaincase_death['Date'], y=spaincase_death['Total Cases'], name='Spain',
                         line=dict(color='#DD99FF', width=2)))
fig.add_trace(go.Scatter(x=polandcase_death['Date'], y=polandcase_death['Total Cases'], name='Poland',
                         line=dict(color='#E60000', width=2)))
fig.add_trace(go.Scatter(x=ukcase_death['Date'], y=ukcase_death['Total Cases'], name='United Kingdom',
                         line=dict(color='#6699FF', width=2)))
fig.add_trace(go.Scatter(x=chinacase_death['Date'], y=chinacase_death['Total Cases'], name='China',
                         line=dict(color='#ffffff', width=2)))
fig.add_trace(go.Scatter(x=skcase_death['Date'], y=skcase_death['Total Cases'], name='South Korea',
                         line=dict(color='#FF6699', width=2)))

fig.update_layout(title='Total Coronavirus Cases',
                  xaxis_title='Date',
                  yaxis_title='Cases',
                  template='plotly_dark')


fig.show()


# In[288]:


# Line graph for Total Deaths
fig = go.Figure()
fig.add_trace(go.Scatter(x=uscase_death['Date'], y=uscase_death['Total Deaths'], name='United States',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=italycase_death['Date'], y=italycase_death['Total Deaths'], name='Italy',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=spaincase_death['Date'], y=spaincase_death['Total Deaths'], name='Spain',
                         line=dict(color='#DD99FF', width=2)))
fig.add_trace(go.Scatter(x=polandcase_death['Date'], y=polandcase_death['Total Deaths'], name='Poland',
                         line=dict(color='#E60000', width=2)))
fig.add_trace(go.Scatter(x=ukcase_death['Date'], y=ukcase_death['Total Deaths'], name='United Kingdom',
                         line=dict(color='#002B80', width=2)))
fig.add_trace(go.Scatter(x=chinacase_death['Date'], y=chinacase_death['Total Deaths'], name='China',
                         line=dict(color='#ffffff', width=2)))

fig.update_layout(title='Total Coronavirus Deaths',
                  xaxis_title='Date',
                  yaxis_title='Deaths', template='plotly_dark')

fig.show()


# In[20]:


# Calculates the mortality rate
spaincase_death['Death Rate'] = spaincase_death['Total Deaths'] /     spaincase_death['Total Cases']
uscase_death['Death Rate'] = uscase_death['Total Deaths'] /     uscase_death['Total Cases']
ukcase_death['Death Rate'] = ukcase_death['Total Deaths'] /     ukcase_death['Total Cases']
italycase_death['Death Rate'] = italycase_death['Total Deaths'] /     italycase_death['Total Cases']
polandcase_death['Death Rate'] = polandcase_death['Total Deaths'] /     polandcase_death['Total Cases']
chinacase_death['Death Rate'] = chinacase_death['Total Deaths'] /     chinacase_death['Total Cases']


# In[294]:


# Line graph of the mortality rate as a percentage
fig = go.Figure()
fig.add_trace(go.Scatter(x=uscase_death['Date'], y=uscase_death['Death Rate'] * 100, name='United States',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=italycase_death['Date'], y=italycase_death['Death Rate'] * 100, name='Italy',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=spaincase_death['Date'], y=spaincase_death['Death Rate'] * 100, name='Spain',
                         line=dict(color='#DD99FF', width=2)))
fig.add_trace(go.Scatter(x=polandcase_death['Date'], y=polandcase_death['Death Rate'] * 100, name='Poland',
                         line=dict(color='#E60000', width=2)))
fig.add_trace(go.Scatter(x=ukcase_death['Date'], y=ukcase_death['Death Rate'] * 100, name='United Kingdom',
                         line=dict(color='#6699FF', width=2)))
fig.add_trace(go.Scatter(x=chinacase_death['Date'], y=chinacase_death['Death Rate'] * 100, name='China',
                         line=dict(color='#ffffff', width=2)))

fig.update_layout(title='Coronavirus Death Rates as a Percentage',
                  xaxis_title='Date',
                  yaxis_title='Death Rate', template='plotly_dark')

fig.show()


# In[295]:


# Line graph of cases per 100,000 people
fig = go.Figure()
fig.add_trace(go.Scatter(x=uscase_death['Date'], y=uscase_death['Total Cases'] * 100000 / data_us['popData2018'], name='United States',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=italycase_death['Date'], y=italycase_death['Total Cases'] * 100000 / data_italy['popData2018'], name='Italy',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=spaincase_death['Date'], y=spaincase_death['Total Cases'] * 100000 / data_spain['popData2018'], name='Spain',
                         line=dict(color='#DD99FF', width=2)))
fig.add_trace(go.Scatter(x=polandcase_death['Date'], y=polandcase_death['Total Cases'] * 100000 / data_poland['popData2018'], name='Poland',
                         line=dict(color='#E60000', width=2)))
fig.add_trace(go.Scatter(x=ukcase_death['Date'], y=ukcase_death['Total Cases'] * 100000 / data_uk['popData2018'], name='United Kingdom',
                         line=dict(color='#6699FF', width=2)))
fig.add_trace(go.Scatter(x=chinacase_death['Date'], y=chinacase_death['Total Cases'] * 100000 / data_china['popData2018'], name='China',
                         line=dict(color='#ffffff', width=2)))

fig.update_layout(title='Coronavirus Cases per 100,000 People',
                  xaxis_title='Date',
                  yaxis_title='Cases', template='plotly_dark')

fig.show()


# In[ ]:




