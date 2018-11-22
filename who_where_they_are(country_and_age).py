# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:13:37 2018

@author: MSG
"""
#this scipt loads the dataset_student.json dataset
#we analyse it to understand
#Who are they?
#by extracting  country, and age range

#import required libraries
import json 
import pygal
from country_codes import get_country_code


#functions
def SaveAsJson(jsonfilename, listname):
    """saves list of dicts data to json file"""
    with open(jsonfilename+'.json', 'w') as f:
     json.dump(listname, f, indent = 2) 
     
#create lists for countries and age_ranges
countries = []
age_range =[]
#populate countries and age_range lists
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items(): 
        country = value['Q3']
        age = value['Q2']
        #populate countries list
        if country not in countries:
            countries.append(country)
        #populate age_range list
        if age not in age_range:
            age_range.append(age)
#create dict of countries 
#and their respective number of students
#per age bracket           
students_per_country_per_age = [] 
for country in countries:
    for age in age_range:
        number = 0
        for key, value in json_dataset.items(): 
            if value['Q3'] == country and age == value['Q2']:
                number += 1
        student_popn = {"Country":country , "age_range": age,  "number": number}
        students_per_country_per_age.append(student_popn)
#save lists in json for future use
SaveAsJson('students_per_country_per_age', students_per_country_per_age)
 

filename = 'students_per_country_per_age.json'
#load the data into a list
with open(filename) as f:
    student_data = json.load(f)
#create dict of countries 
#and their respective number of students
students_per_country = [] 
# Print the number of students   for each country.
for country in countries:
    number = 0
    for country_dict in student_data:
        if country == country_dict['Country']:
            number += country_dict['number']         
    student_num = {"Country":country ,  "number": number}
    students_per_country.append(student_num)
#save lists in json for future use
SaveAsJson('students_per_country', students_per_country)


#VISUALIZE DATA 

#Pygal uses  codes   
# Viasialize  total number of students per country    
#Build a dictionary of student_data.
#Grouping Countries by student_number
#three  levels:
# lessthan 100, between 100 and 1000, and more than 1000
numbers_L100 = {}
numbers_B100_1000 = {}
numbers_1000plus = {}

filename = 'students_per_country.json'

#load the data into a list
with open(filename) as f:
    student_numbers = json.load(f)

# Print the number of students  for each country.
for country_dict in student_numbers:
    country = country_dict['Country']
    number = country_dict['number']
    if country == "Russia" :
        country = "Russian Federation"
    if country == "South Korea" :
        country = "Korea, Rep."
    if country == "Republic of Korea":
        country = "Korea, Dem. Rep."
    if country == "United States of America":
        country = "United States"
    if country == "United Kingdom of Great Britain and Northern Ireland":
        country = "United Kingdom"
    if country == "Iran, Islamic Republic of...":
        country = "Iran, Islamic Rep."    
               
    code = get_country_code(country)
    #we consider only countries with code in the world map
    if code:
        if number < 100:
            numbers_L100[code] = number
        elif number < 1000:
            numbers_B100_1000[code] = number
        else:
            numbers_1000plus[code] = number
        
        print('Country:'+country +
              ' Country Code :'+ str(code) +
              ' Number of Students :'+str(number))   
        print(" ")
    else:
        print('ERROR: '+country)        
        
#Building a World Map
wmt = pygal.maps.world.World()
wmt.title = 'Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Students residing in different countries and breaking into Data Science & ML Field. '
wmt.add('Less than 100', numbers_L100)
wmt.add('Between 100 to 1000', numbers_B100_1000)
wmt.add('Over 1000', numbers_1000plus)
wmt.render_to_file('New Data Scientists.svg')


#Visualize students per age bracket per country of residence
#Build a dictionary of student_data.
#Grouping Countries by student_number
#three  levels:
# lessthan 10, between 10 and 100, and more than 100
numbers_L10 = {}
numbers_B10_100 = {}
numbers_100plus = {}

# Print the number of students aged 22-24  for each country.
for country_dict in student_data:
    if country_dict['age_range'] == '22-24': #change range to get maps for different age_ranges
        country = country_dict['Country']
        number = country_dict['number']
        if country == "Russia" :
            country = "Russian Federation"
        if country == "South Korea" :
            country = "Korea, Rep."
        if country == "Republic of Korea":
            country = "Korea, Dem. Rep."
        if country == "United States of America":
            country = "United States"
        if country == "United Kingdom of Great Britain and Northern Ireland":
            country = "United Kingdom"
        if country == "Iran, Islamic Republic of...":
            country = "Iran, Islamic Rep."    
                   
        code = get_country_code(country)
        #we consider only countries with code in the world map
        if code:
            if number < 10:
                numbers_L10[code] = number
            elif number < 100:
                numbers_B10_100[code] = number
            else:
                numbers_100plus[code] = number
            
            print('Country:'+country +
                  ' Country Code :'+ str(code) +
                  ' Number of Students :'+str(number))   
            print(" ")
        else:
            print('ERROR: '+country)
            
            
#Building a World Map
wm = pygal.maps.world.World()
wm.title = 'Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Students(aged  80+) ,residing in different countries and breaking into Data Science & ML Field. '
wm.add('Less than 10', numbers_L10)
wm.add('Between 10 to 100', numbers_B10_100)
wm.add('Over 100', numbers_100plus)
wm.render_to_file('New Data Scientists(aged 80+).svg')


