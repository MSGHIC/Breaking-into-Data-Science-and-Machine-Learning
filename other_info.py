# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:45:12 2018

@author: MSG
"""
#import rewuired libraries
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#functions
def SaveAsJson(jsonfilename, listname):
    """saves list of dicts data to json file"""
    with open(jsonfilename+'.json', 'w') as f:
     json.dump(listname, f, indent = 2)  
     
#*****programming language would you recommend an aspiring data scientist to learn first*****
#initialize empty  list for programming languages
languages = []   
#populate programming_languages  list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
            language = value['Q18']
            if language:
                #populate languages list
                if language not in languages:
                    languages.append(language)
#count the scores for each  programming language
#each language gets score of 1 if was voted by student
language_scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update language_scores list
    for i in range(0, len(languages)):
        score = 0
        for key, value in json_dataset.items():
            language = value['Q18']
            if language:
                #update  language score   
                if languages[i] ==  language:
                    score += 1             
        score_dict = {"language" :languages[i], "Score":score} 
        language_scores.append(score_dict)        
#save list in json for future use
SaveAsJson('recommended_languages_Scores', language_scores)   

 
#******Time spent by Students coding*********
#initialize empty  list for time spent
time_spent = []    
#populate time_spent  list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
            time = value['Q23']
            if time:
                #populate time_spent list
                if time not in time_spent:
                    time_spent.append(time)
#count the scores for each  programming language
#each language gets score of 1 if was voted by student
time_scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update time_scores list
    for i in range(0, len(time_spent)):
        score = 0
        for key, value in json_dataset.items():
            time = value['Q23']
            if time:
                #update time score   
                if time_spent[i] ==  time:
                    score += 1                
        score_dict = {"time" :time_spent[i], "Score":score} 
        time_scores.append(score_dict)        
#save list in json for future use
SaveAsJson('time_spent_Scores', time_scores)        


#******Experience in writing code *********
#initialize empty  list for time spent
experience = []      
#populate time_spent  list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
            period = value['Q24']
            if  period:
                #populate time_spent list
                if period not in experience:
                    experience.append(period)
#count the scores for each period
#each period gets score of 1 if was voted by student
period_scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update period_scores list
    for i in range(0, len(experience)):
        score = 0
        for key, value in json_dataset.items():
            period = value['Q24']
            if  period:
                #update period score   
                if experience[i] ==  period:
                    score += 1                
        score_dict = {"time" :experience[i], "Score":score} 
        period_scores.append(score_dict)        
#save list in json for future use
SaveAsJson('experience_Scores', period_scores)      


#******Experience in using ML methods *********
#initialize empty  list for time spent
experience_ml = []      
#populate time_spent  list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
            period = value['Q25']
            if  period:
                #populate time_spent list
                if period not in experience_ml:
                    experience_ml.append(period)
#count the scores for each period
#each period gets score of 1 if was voted by student
ml_period_scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update period_scores list
    for i in range(0, len(experience_ml)):
        score = 0
        for key, value in json_dataset.items():
            period = value['Q25']
            if  period:
                #update period score   
                if experience_ml[i] ==  period:
                    score += 1                
        score_dict = {"time" :experience_ml[i], "Score":score} 
        ml_period_scores.append(score_dict)        
#save list in json for future use
SaveAsJson('ml_experience_Scores',  ml_period_scores)        


#********data that you currently interact with most often***********
#initialize empty  list for time spent
data_types = []      
#populate time_spent  list
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    for key, value in json_dataset.items():
            data_type = value['Q32']
            if  data_type:
                #populate time_spent list
                if data_type not in data_types:
                    data_types.append(data_type)
#count the scores for each period
#each period gets score of 1 if was voted by student
data_type_scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update period_scores list
    for i in range(0, len(data_types)):
        score = 0
        for key, value in json_dataset.items():
            data_type = value['Q32']
            if  data_type:
                #update period score   
                if data_types[i] ==  data_type:
                    score += 1                
        score_dict = {"type" :data_types[i], "Score":score} 
        data_type_scores.append(score_dict)        
#save list in json for future use
SaveAsJson('data_type_scores', data_type_scores)            


#******Public dataset sources students use **********
#initialize empty  list for   data_sources
data_sources = []    
#populate data_sources list
with open("dataset_student.json", "r") as n:
    json_dataset = json.load(n)
    for key, value in json_dataset.items():
        for i in range(1, 12):
           source = value['Q33_Part_'+str(i)]
           if source:
                #populate data_sources list
                if source not in data_sources:
                    data_sources.append(source)
#count the scores for each  data source
#data source gets score of 1 if was voted by student
source_Scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update notebook_Scores list
    for i in range(0, len(data_sources)):
        score = 0
        for key, value in json_dataset.items():
           for k in range(1, 12):
                source = value['Q33_Part_'+str(k)]
                if source:
                   #update source score   
                   if data_sources[i] ==  source:
                       score += 1                
        score_dict = {"source" :data_sources[i], "Score":score} 
        source_Scores.append(score_dict)        
#save list in json for future use
SaveAsJson('Public dataset sources students use', source_Scores)


#*****online platforms where students undertake data science courses*******
#initialize empty  list for   online platforms
online_courses_platforms = []    
#populate data_sources list
with open("dataset_student.json", "r") as n:
    json_dataset = json.load(n)
    for key, value in json_dataset.items():
        for i in range(1, 14):
           platform = value['Q36_Part_'+str(i)]
           if  platform:
                #populate data_sources list
                if  platform not in online_courses_platforms:
                    online_courses_platforms.append(platform)
#count the scores for each  platform
#platform gets score of 1 if was voted by student
platform_Scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update notebook_Scores list
    for i in range(0, len(online_courses_platforms)):
        score = 0
        for key, value in json_dataset.items():
          for k in range(1, 14):
              platform = value['Q36_Part_'+str(k)]
              if  platform:
                   #update platform score   
                   if online_courses_platforms[i] ==  platform:
                       score += 1                
        score_dict = {"platform" :online_courses_platforms[i] , "Score":score} 
        platform_Scores.append(score_dict)        
#save list in json for future use
SaveAsJson('online_data_science_learning_platforms',  platform_Scores)  


#********tools and methods students use to make their work easy to reproduce ***********
tools_for_reproduction = []  
#populate data_sources list
with open("dataset_student.json", "r") as n:
    json_dataset = json.load(n)
    for key, value in json_dataset.items():
        for i in range(1, 13):
           method = value['Q49_Part_'+str(i)]
           if  method:
                #populate data_sources list
                if  method not in tools_for_reproduction:
                    tools_for_reproduction .append(method)
#count the scores for each  method
#method gets score of 1 if was voted by student
method_Scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update notebook_Scores list
    for i in range(0, len(tools_for_reproduction)):
        score = 0
        for key, value in json_dataset.items():
          for k in range(1, 13):
              method= value['Q49_Part_'+str(k)]
              if  method:
                   #update method score   
                   if tools_for_reproduction[i] ==  method:
                       score += 1                
        score_dict = {"method" :tools_for_reproduction[i]  , "Score":score} 
        method_Scores.append(score_dict)        
#save list in json for future use
SaveAsJson('methods_students_use_to_make_their_work_easy_to_reproduce', method_Scores)  


#*****What barriers prevent you from making your work even easier to reuse and reproduce?*****
barriers = []   
#populate barriers list
with open("dataset_student.json", "r") as n:
    json_dataset = json.load(n)
    for key, value in json_dataset.items():
        for i in range(1, 9):
           barrier = value['Q50_Part_'+str(i)]
           if  barrier:
                #populate data_sources list
                if  barrier not in barriers:
                    barriers.append(barrier)
#count the scores for each  barrier
#barrier gets score of 1 if was voted by student
barriers_Scores = []
with open("dataset_student.json", "r") as d:
    json_dataset = json.load(d)
    #update notebook_Scores list
    for i in range(0, len(barriers)):
        score = 0
        for key, value in json_dataset.items():
          for k in range(1, 9):
              barrier = value['Q50_Part_'+str(k)]
              if  barrier:
                   #update barrier score   
                   if barriers[i] ==  barrier:
                       score += 1                
        score_dict = {"barrier" :barriers[i], "Score":score} 
        barriers_Scores.append(score_dict)        
#save list in json for future use
SaveAsJson('barriers_in_work_reuse', barriers_Scores)
          
     
#VISUALIZE DATA

#visualize recommended programming languages 
with open('recommended_languages_Scores.json', 'r') as j:    
        tools_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Programming languages as recommended to aspiring data scientists "
        for item in   tools_Scores:
            pie_chart.add(item['language'], [{'value': item['Score'], 'label': item['language']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('recommended languages for new data scientists.svg')   


#visualize how time is spent by students coding
#store each major ,and its corresponding numbers of students
with open("time_spent_Scores.json", "r") as d:
    time_spent = json.load(d)          
    time_list = []
    time_plot_dicts = []   
    for i in range(0, len(time_spent)):
        time_dict  = time_spent[i]
        time_list.append(time_dict['time'])      
        time_plot_dict = {
                            'value': time_dict['Score'],
                            'label':  str(time_dict['time']),                             
                        }
        time_plot_dicts.append(time_plot_dict)         
#make visualisation
my_style = LS('#698614', base_style=LCS)
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
hist.x_labels = time_list
hist.x_title = "time spent coding"
hist.y_title = "Number of Students"
hist.add(' ', time_plot_dicts)
hist.render_to_file("Kaggle 2018 Survey for Data Science & ML Community(Coding Time Spent).svg")


#visualize students' experience in using ML methods
with open("ml_experience_Scores.json", "r") as d:
    time_spent = json.load(d)      
    time_list = []
    time_plot_dicts = []
    for i in range(0, len(time_spent)):
        time_dict  = time_spent[i]
        time_list.append(time_dict['time'])
        time_plot_dict = {
                            'value': time_dict['Score'],
                            'label':  str(time_dict['time']),                            
                        }
        time_plot_dicts.append(time_plot_dict)          
hist = pygal.Bar(my_config, style=my_style)
hist.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.       Category: students' experience in using ML methods "
hist.x_labels = experience_ml
hist.x_title = "experience in using ml methods"
hist.y_title = "Number of Students"
hist.add(' ', time_plot_dicts)
hist.render_to_file("Kaggle 2018 Survey for Data Science & ML Community(experience in using ml methods).svg")


#visualize online learning platforms for data science
with open("online_data_science_learning_platforms.json", "r") as d:
    data = json.load(d)         
    platforms_list = []
    platforms_plot_dicts = []   
    for i in range(0, len(data)):
        platform_dict  = data[i]
        platforms_list.append(platform_dict ['platform'])       
        platform_plot_dict = {
                            'value': platform_dict['Score'],
                            'label':  str(platform_dict['platform']),                             
                        }
        platforms_plot_dicts.append(platform_plot_dict)          
hist = pygal.Bar(my_config, style=my_style)
hist.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.       Category: online platforms where students undertake data science courses "
hist.x_labels = platforms_list
hist.x_title = "online learning platform"
hist.y_title = "Number of Students"
hist.add(' ', platforms_plot_dicts)
hist.render_to_file("Kaggle 2018 Survey for Data Science & ML Community(online learning platform).svg")


# visualize experience in data science and ML
with open('experience_Scores.json', 'r') as f:
        experiences = json.load(f)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Students' experience in data science and ML "
        for item in  experiences:
            pie_chart.add(item['time'], [{'value': item['Score'], 'label': item['time']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file("Students' experience in data science and ML.svg")   
 
      
#visualize data students interact with most
with open('data_type_scores.json', 'r') as j:    
        tools_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: data types stduents interact with most often "
        for item in   tools_Scores:
            pie_chart.add(item['type'], [{'value': item['Score'], 'label': item['type']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('data types stduents interact with most often.svg')   
 
       
#visualize public data sources students use
with open('Public dataset sources students use.json', 'r') as j:    
        source_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Public dataset sources students use "
        for item in   source_Scores:
            pie_chart.add(item['source'], [{'value': item['Score'], 'label': item['source']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('Public dataset sources students use.svg')   


#*****methods_students_use_to_make_their_work_easy_to_reproduce******
with open('methods_students_use_to_make_their_work_easy_to_reproduce.json', 'r') as j:    
        tools_Scores = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: tools and methods students use to make their work easy to reproduce "
        for item in   tools_Scores:
            pie_chart.add(item['method'], [{'value': item['Score'], 'label': item['method']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('methods_students_use_to_make_their_work_easy_to_reproduce.svg')         
 
       
#****What barriers prevent you from making your work even easier to reuse and reproduce?*****
with open('barriers_in_work_reuse.json', 'r') as j:    
        barriers = json.load(j)
        pie_chart = pygal.Pie()
        pie_chart.title = "Kaggle-Survey-2018 for Data Science and Machine Learning Community.  Category: Barriers thet prevent students from making their work easier to reuse and reproduce "
        for item in  barriers:
            pie_chart.add(item['barrier'], [{'value': item['Score'], 'label': item['barrier']}])
        pie_chart.value_formatter = lambda x: "%.0f" % x
        pie_chart.render_to_file('barriers_in_work_reuse.svg')         
       