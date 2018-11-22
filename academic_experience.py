# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:34:30 2018

@author: MSG
"""
"""Script to extract high level of eductaion and undergraduate majors
    from dataset_student.json
"""
#import require libraries
import json 
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#functions
def SaveAsJson(jsonfilename, listname):
    """saves list of dicts data to json file"""
    with open(jsonfilename+'.json', 'w') as f:
     json.dump(listname, f, indent = 2)  

#***high level of eductaion*****
#create lists for high level of eductaion and majors
education_level = []
majors =[]

#populate education_level and major lists
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
        level= value['Q4']
        major = value['Q5']
         #populate education_level list
        if level not in education_level:
            education_level.append(level)
        #populate majors list    
        if major not in majors:
            majors.append(major)
  
#count the occurance of each level of eductaion, and each major
# and store as key value pairs ie Masterâ€™s degree : 235
students_per_level = []
students_per_major = []

#populate students_per_level list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update education_level dict
    for i in range(0, len(education_level)):
        number = 0
        for key, value in json_dataset.items():
            level = value['Q4']                     
            if education_level[i] ==  level:
                number += 1                
        level_dict = {"Level" :education_level[i], "Number of Students":number} 
        students_per_level.append(level_dict)
#save lists in json for future use
SaveAsJson('students_per_level', students_per_level)             
                
#populate students_per_major list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update education_level dict
    for i in range(0, len(majors)):
        number = 0
        for key, value in json_dataset.items():
            major = value['Q5']           
            if majors[i] ==  major:
                number += 1                
        major_dict = {"major" :majors[i] , "Number of Students":number} 
        students_per_major.append(major_dict)
#save lists in json for future use
SaveAsJson('students_per_major', students_per_major)               
                    
      
#VISUALIZING DATA
 
#High level of education by survey takers
#store each level of education ,and its corresponding numbers of students
with open("students_per_level.json", "r") as d:
    students_per_level = json.load(d)         
    levels = []
    level_plot_dicts = []   
    for i in range(0, len(students_per_level)):
        level_dict  = students_per_level[i]
        levels.append(level_dict['Level'])       
        level_plot_dict = {
                            'value': level_dict['Number of Students'],
                            'label':  str(level_dict['Level']),                             
                        }
        level_plot_dicts.append(level_plot_dict)    
#make visualisation
my_style = LS('#087631', base_style=LCS)
#creating a configuration object that contains all of our customizations to pass to Bar():
my_config = pygal.Config()
my_config.x_label_rotation = 25
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 20
my_config.show_y_guides = False
my_config.width = 1000
hist = pygal.Bar(my_config, style=my_style)
hist.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.       Category: Highest education level for survey takers(students) "
hist.x_labels = levels
hist.x_title = "High level of eductaion"
hist.y_title = "Number of Students"
hist.add(' ', level_plot_dicts)
hist.render_to_file("Kaggle 2018 Survey for Data Science & ML Community(Education-level).svg")


#survey takers'  majors
#store each major ,and its corresponding numbers of students
with open("students_per_major.json", "r") as d:
    students_per_major = json.load(d)           
    majors_list = []
    major_plot_dicts = []    
    for i in range(0, len(students_per_major)):
        major_dict  = students_per_major[i]
        majors_list.append(major_dict['major'])       
        major_plot_dict = {
                            'value': major_dict['Number of Students'],
                            'label':  str(major_dict['major']),                             
                        }
        major_plot_dicts.append(major_plot_dict)
#make visualisation
my_style = LS('#108123', base_style=LCS)
#creating a configuration object that contains all of our customizations to pass to Bar():
my_config = pygal.Config()
my_config.x_label_rotation = 25
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 20
my_config.show_y_guides = False
my_config.width = 1000
hist = pygal.Bar(my_config, style=my_style)
hist.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.       Category: Majors contribution to DS & ML Community "
hist.x_labels = majors
hist.x_title = "Major"
hist.y_title = "Number of Students"
hist.add(' ', major_plot_dicts)
hist.render_to_file("Kaggle 2018 Survey for Data Science & ML Community(Majors).svg")


