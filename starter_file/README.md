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
We're using a classification task with a primary metric of accuracy attempting to predict the number of crashes per year based on a given state. 

### Results
My results all around were relatively dissapointing. My best autoML model only managed to get an accuracy of 0.12678. Certainly nothing too great. In the future, this could be improved by allowing the autoML to run longer. However, I think a major bottleneck is actually in my dataset itself. The % at night and % at day fields sometimes appear to contridict themselves due to being an aggregation of data. I suspect these fields are leading to issues in accuracy down the line.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.
<img width="1184" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/1b8aae69-9b74-492e-9d4e-b89226801d84">
<img width="818" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/ac483c59-cda4-408a-8ba2-8e38ce246ce3">

## Hyperparameter Tuning
Following the same line of logic from the AutoML project, I used a Logistic Regression model with varying degrees in C and max_iter. I believe this model to be the best for predicting the data (and specifically the avg_crashes field). 

### Results
This model performed worse than the autoML model. With a best case scenario of only 0.008771930. I think this model could be improved by deploying it with a different type of regression. Perhaps linear would perform better for non-boolean values. 

<img width="1185" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/fbf08f49-982a-4cab-9d57-2eb4cc5851b6">
<img width="853" alt="image" src="https://github.com/ThinPotato/nd00333-capstone/assets/41706121/872b0121-f160-49ba-aabe-ddda1972b743">

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
