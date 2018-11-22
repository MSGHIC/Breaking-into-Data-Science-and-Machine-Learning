# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:21:54 2018

@author: MSG
"""
#this script loads original dataset ,
# filters out survey takers who are students
# and saves thier data as dataset_student.csv
#and dataset_student.json

#part1:

#import original dataset
import pandas as pd
dataset = pd.read_csv('multipleChoiceResponses.csv')

#Create dataframe for students only    
dataset_student = dataset.where(dataset['Q6'] == 'Student') 
#drop only if ALL columns are NaN (not student) 
dataset_student = dataset_student.dropna(how='all')

#save dataset_student in csv format
dataset_student.to_csv("dataset_student.csv",  encoding='utf8') 

#part2:

#store each student's record(dict) as an item in the data list
data = []
import csv
with open('dataset_student.csv') as f:
    for row in csv.DictReader(f):
        data.append(row)

#create a dict of dicts(each dict is student's survey data)
student_data = {}        
for i in range(len(data)):
    student_data.update({i : data[i]}) 
    
#save as json for future analysis
import json 
with open('dataset_student.json', 'w') as f:
     json.dump(student_data, f, indent = 2)
