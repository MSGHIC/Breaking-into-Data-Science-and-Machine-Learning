# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:04:52 2018

@author: MSG
"""

#required libraries
import json 
import pygal

#functions
def SaveAsJson(jsonfilename, listname):
    """saves list of dicts data to json file"""
    with open(jsonfilename+'.json', 'w') as f:
     json.dump(listname, f, indent = 2)    

#initialize empty  list 

#*********IDES STUDENTS USE***************
IDEs = []
#******Hosted Notebooks Students use **********
hosted_notebooks = []  
#****CLOUD COMPUTING SERVICES STUDENTS USE***********     
cloud_computing_services = []  
#****SPECIFIC PROGRAMMING LANGUAGE STUDENTS USE MOST OFTEN ***********    
programming_languages = [] 
#****MACHINE LEARNING FRAMEWORKS THEY USE ***********     
machine_learning_frameworks = []     
#****ML LIBRARY STUDENTS USE MOST OFTEN ***********    
ml_libraries = []  
#****DATA VISUALIZATION LIBRARY STUDENTS USE MOST OFTEN ***********     
visualization_libraries = [] 
#****PRIMARY TOOL THEY USE TO ANALYSE DATA ***********     
tools = []     


#populate  lists
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
        #populate IDEs list
        for i in range(1, 16):
            ide = value['Q13_Part_'+str(i)]
            if ide:
                #populate education_level list
                if ide not in IDEs:
                    IDEs.append(ide)  
        #populate hosted notebooks list
        for i in range(1, 12):
            notebook = value['Q14_Part_'+str(i)]
            if  notebook:
                #populate hosted_notebooks list
                if notebook not in hosted_notebooks:
                    hosted_notebooks.append(notebook)
        #populate cloud_computing_services list
        for i in range(1, 8):
            service = value['Q15_Part_'+str(i)]
            if service:
                #populate cloud_computing_services list
                if service not in cloud_computing_services:
                    cloud_computing_services.append(service)
        #populate programming_languages list
        prog_lang = value['Q17']
        if prog_lang:
            #populate programming_languages list
            if prog_lang not in programming_languages:
                programming_languages.append(prog_lang)
        #populate machine_learning_frameworks list
        for i in range(1, 20):
            framework = value['Q19_Part_'+str(i)]
            if framework:
                #add it to list
                if framework not in machine_learning_frameworks:
                    machine_learning_frameworks.append(framework)
        #populate ml_libraries list
        library = value['Q20']
        if library:
            if library not in ml_libraries:
                ml_libraries.append(library)
        #populate visualization_libraries list
        visual_library = value['Q22']
        if visual_library:
            #populate libraries list
            if visual_library not in visualization_libraries:
                visualization_libraries.append(visual_library)
        #populate tools list
        tool = value['Q12_MULTIPLE_CHOICE']
        if tool:
            #populate tools list
            if tool not in tools:
               tools.append(tool)
               
#count the scores for each  item in a given list
#each item gets score of 1 if it was voted by student 
#store scores in lists               
IDE_Scores = []
hosted_notebooks_Scores = []
services_Scores = []
language_Scores = []
frameworks_Scores = []
library_Scores = []
visual_library_Scores = []
tools_Scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update IDE_Scores list
    for i in range(0, len(IDEs)):
        score = 0
        for key, value in json_dataset.items():
           for k in range(1, 16):
               ide = value['Q13_Part_'+str(k)]
               if ide:
                   #update ide score   
                   if IDEs[i] ==  ide:
                       score += 1                
        score_dict = {"IDE" :IDEs[i], "Score":score} 
        IDE_Scores.append(score_dict) 
    #update notebook_Scores list
    for i in range(0, len(hosted_notebooks)):
        score = 0
        for key, value in json_dataset.items():
           for k in range(1, 12):
               notebook = value['Q14_Part_'+str(k)]
               if notebook:
                   #update ide score   
                   if hosted_notebooks[i] ==  notebook:
                       score += 1                
        score_dict = {"notebook" :hosted_notebooks[i], "Score":score} 
        hosted_notebooks_Scores.append(score_dict)        
    #update services_Scores list
    for i in range(0, len(cloud_computing_services)):
        score = 0
        for key, value in json_dataset.items():
           for k in range(1, 8):
               service = value['Q15_Part_'+str(k)]
               if  service:
                   #update  service score   
                   if cloud_computing_services[i] ==  service:
                       score += 1                
        score_dict = {"cloud_computing_services" :cloud_computing_services[i], "Score":score} 
        services_Scores.append(score_dict)
    #update language_Scores list
    for i in range(0, len(programming_languages)):
        score = 0
        for key, value in json_dataset.items():
            prog_lang = value['Q17']
            if prog_lang:
                #update  language score   
                if programming_languages[i] ==  prog_lang:
                    score += 1                
        score_dict = {"programming_language" :programming_languages[i], "Score":score} 
        language_Scores.append(score_dict)   
    #update frameworks_Scores list
    for i in range(0, len(machine_learning_frameworks)):
        score = 0
        for key, value in json_dataset.items():
           for k in range(1, 20):
               framework = value['Q19_Part_'+str(k)]
               if framework:
                   #update  framework score   
                   if machine_learning_frameworks[i] ==  framework:
                       score += 1                
        score_dict = {"framework" :machine_learning_frameworks[i], "Score":score} 
        frameworks_Scores.append(score_dict) 
    #update library_Scores list
    for i in range(0, len(ml_libraries)):
        score = 0
        for key, value in json_dataset.items():
            library = value['Q20']
            if library:
                #update  library score   
                if ml_libraries[i] ==  library:
                    score += 1                
        score_dict = {"library" : ml_libraries[i], "Score":score} 
        library_Scores.append(score_dict) 
    #update library_Scores list
    for i in range(0, len(visualization_libraries)):
        score = 0
        for key, value in json_dataset.items():
            visual_library = value['Q22']
            if visual_library:
                #update  library score   
                if visualization_libraries[i] ==  visual_library:
                    score += 1                
        score_dict = {"library" : visualization_libraries[i], "Score":score} 
        visual_library_Scores.append(score_dict)        
    #update tools_Scores list
    for i in range(0, len(tools)):
        score = 0
        for key, value in json_dataset.items():
            tool = value['Q12_MULTIPLE_CHOICE']
            if tool:
                #update  tool score   
                if tools[i] ==  tool:
                    score += 1               
        score_dict = {"tool" : tools[i], "Score":score} 
        tools_Scores.append(score_dict)        


#save as json lists  for future use
SaveAsJson('IDEs_Scores', IDE_Scores)
SaveAsJson('hosted_notebooks_Scores', hosted_notebooks_Scores) 
SaveAsJson('cloud_computing_services_Scores', services_Scores) 
SaveAsJson('programming_languages_Scores', language_Scores)
SaveAsJson('machine_learning_frameworks_Scores', frameworks_Scores) 
SaveAsJson('ML Libraries_Scores', library_Scores)   
SaveAsJson('DATA VISUALIZATION Libraries_Scores', visual_library_Scores) 
SaveAsJson('primary data analysis tools _Scores',  tools_Scores)  

#VISUALIZE DATA

#*********IDES STUDENTS USE********************
with open('IDE_Scores.json', 'r') as m:
        IDE_Scores = json.load(m)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per IDE "
        for item in  IDE_Scores:
            pie_chart.add(item['IDE'], [{'value': item['Score'], 'label': item['IDE']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('IDEs used by Students.svg')

#*****Hosted Notebooks Students use********
with open('hosted_notebooks_Scores.json', 'r') as n:
        notebook_Scores = json.load(n)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Hosted Notebook "
        for item in  notebook_Scores:
            pie_chart.add(item['notebook'], [{'value': item['Score'], 'label': item['notebook']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('Hosted Notebooks Students use.svg')

#****CLOUD COMPUTING SERVICES****************
with open('cloud_computing_services_Scores.json', 'r') as g:
        services_Scores = json.load(g)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Cloud Computing Service "
        for item in  services_Scores:
            pie_chart.add(item['cloud_computing_services'], [{'value': item['Score'], 'label': item['cloud_computing_services']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('cloud_computing_services Students use.svg')
        
#****SPECIFIC PROGRAMMING LANGUAGES ****************
with open('programming_languages_Scores.json', 'r') as f:    
        languages_Scores = json.load(f)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Programming Language "
        for item in  languages_Scores:
            pie_chart.add(item['programming_language'], [{'value': item['Score'], 'label': item['programming_language']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('programming_languages Students use.svg')
        
#*****ML Libraries**************
with open('ML Libraries_Scores.json', 'r') as l:    
        libraries_Scores = json.load(l)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Machine Learning Library "
        for item in   libraries_Scores:
            pie_chart.add(item['library'], [{'value': item['Score'], 'label': item['library']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('Machine Learning Libraries Students use.svg')   

#****machine learning frameworks************
with open('machine_learning_frameworks_Scores.json', 'r') as j:    
        framework_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Machine Learning Framework "
        for item in   framework_Scores:
            pie_chart.add(item['framework'], [{'value': item['Score'], 'label': item['framework']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('Machine Learning frameworks Students use.svg')   

#****Data Visualization Libraries use************
with open('DATA VISUALIZATION Libraries_Scores.json', 'r') as j:    
        library_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per Data Visualization Library "
        for item in   library_Scores:
            pie_chart.add(item['library'], [{'value': item['Score'], 'label': item['library']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('Data Visualization Libraries Students use.svg')      
        
#****Primary data analysis tools************
with open('primary data analysis tools _Scores.json', 'r') as j:    
        tools_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Number of Students per primary data analysis tool used "
        for item in   tools_Scores:
            pie_chart.add(item['tool'], [{'value': item['Score'], 'label': item['tool']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('primary data analysis tools Students use.svg')        