*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# NBA 3 Point Percentage Impact on Winning
Over the past decade NBA offenses have shifted to primarily relying on the 3 point shot to score points. Certain players and teams have greatly impacted this shift. Stephen Curry and the Golden State Warriors are among some of the pioneers for this new approach. This project will analyze NBA 3 point percetage data from 2015 to 2023. We will be looking for the potential impact that 3 point shooting percentage has on winning NBA games.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The dataset we are using was supplied from Kaggle [Link](https://www.kaggle.com/datasets/wyattowalsh/basketball). Within that database is a table that stores all game related data. All relevant team stats and the outcome of each game. From that I was able to extract a condensed dataset with SQL that has 3 point shooting percetages for each team as well as the winning team and the highest 3 point percetage between both teams.

### Task
With this dataset we will be evaluating whether or not a high 3 point shooting percetage has an impact on the outcome of a game or not.

### Access
I will be registering this dataset within the workspace and accessing it via URL when needed.

## Automated ML
For the AutoML experiment I will be using a classification experiment type to find the best possible model in an automated fashion. I'm looking for the most accurate model and evaluating the column containing the outcome for the highest 3 point shooting percentage between both teams.

### Results
The AutoML experiment returned Voting Ensemble as the best model with a very high accuracy.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
