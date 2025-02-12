*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Your Project Title Here

The goal of this project is to build models using both autoML and hyperparameter to predict the average sleepiness of a given region thus giving us inishgt into the likelyhood of a lack-of-sleep related car crash within the bounds of said region. 

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The dataset I am using is a custom dataset build from sourced data from the government's statistics of car crashes, and a survey asking people their self-reported levels of sleepiness. I randomly selected a subset of these datasources to cut down on processing time, leaving us with cleandata.csv.

### Task
Sleep is an often highly undervalued remedy to a variety of conditions. And to me, it's always been a very interesting topic. I was curious to see if people's chronic lack of sleep in a general area has any correlation to the number and severity of car accients. 

### Access
The data is uploaded as a csv and referenced directly. 

## Automated ML
We're using a classification task with a primary metric of accuracy attempting to predict the number of crashes per year based on a given state. I used these parameters as my overall goal is being able to classify whether a particular crash as--at least in part--was due to sleepiness. Classification/accuracy autoML will try a ton of different models in order to find the best one for this particular scenario. 

### Results
My results all around were relatively dissapointing. My best autoML model only managed to get an accuracy of 0.12678. Certainly nothing too great. In the future, this could be improved by allowing the autoML to run longer. However, I think a major bottleneck is actually in my dataset itself. The % at night and % at day fields sometimes appear to contridict themselves due to being an aggregation of data. I suspect these fields are leading to issues in accuracy down the line. In the future, I'd want to simply my data source by removing fields where are not required or may be reducing the accuracy such as these % at night and % at day fields. Additionally, it may be interesting to experiment with other types of autoML configurations. While I expected Classification to be the best, maybe it will surprise me with other configs.

<img width="1184" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/1b8aae69-9b74-492e-9d4e-b89226801d84">
<img width="818" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/ac483c59-cda4-408a-8ba2-8e38ce246ce3">

## Hyperparameter Tuning
Following the same line of logic from the AutoML project, I used a Logistic Regression model with varying degrees in C and max_iter. I believe this model to be the best for predicting the data (and specifically the avg_crashes field). 

### Results
This model performed worse than the autoML model. With a best case scenario of only 0.008771930. I think this model could be improved by deploying it with a different type of regression. Perhaps linear would perform better for non-boolean values. 

<img width="1185" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/fbf08f49-982a-4cab-9d57-2eb4cc5851b6">
<img width="853" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/872b0121-f160-49ba-aabe-ddda1972b743">

Best model parameters & run ID
<img width="1177" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/f434f865-445b-4cc7-8e21-a33fd7295145">


## Model Deployment
The deployed model takes the following input parameters:
```json
"data": [
    {
      "Avg_Crash_Severity": 1.0,
      "Avg_Sleepiness": "36%",
      "People_Queried_About_Sleep": 1000,
      "Percent_Evening_Crashes": "50%",
      "Percent_Morning_Crashes": "50%",
      "raw_Crashes_per_Year": 1.0
    }
  ],
  "method": "predict"
}
```

Simply send this (filled out with whatever parameters you are interested in predicting for) and the model will return the likelyhood of a crash given these parameters.

<img width="1110" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/bd4bb805-d518-4103-ab41-8304dc7e1fb1">


## Screen Recording
[https://imgur.com/a/C323Vbo](https://i.imgur.com/L5i54cf.mp4)
There is audio. Make sure it is unmuted in the top right

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
