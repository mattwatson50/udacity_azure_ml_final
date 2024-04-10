*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# NBA 3 Point Percentage Impact on Winning
Over the past decade NBA offenses have shifted to primarily relying on the 3 point shot to score points. Certain players and teams have greatly impacted this shift. Stephen Curry and the Golden State Warriors are among some of the pioneers for this new approach. This project will analyze NBA 3 point percetage data from 2015 to 2023. We will be looking for the potential impact that 3 point shooting percentage has on winning NBA games.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The dataset we are using was supplied from Kaggle [Link](https://www.kaggle.com/datasets/wyattowalsh/basketball). Within that database is a table that stores all game related data. All relevant team stats and the outcome of each game. From that I was able to extract a condensed dataset with SQL that has 3 point shooting percetages for each team as well as the winning team and the highest 3 point percentage between both teams.

### Task
With this dataset we will be evaluating whether or not a high 3 point shooting percentage has an impact on the outcome of a game or not.

### Access
I will be registering this dataset within the workspace and accessing it via URL when needed.

## Automated ML
For the AutoML experiment I will be using a classification experiment type to find the best possible model in an automated fashion. I'm looking for the most accurate model and evaluating the column containing the outcome for the highest 3 point shooting percentage between both teams.

### Results
The AutoML experiment returned Voting Ensemble as the best model with a very high accuracy.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/automl_rundetails.png)

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

For the hyperparameter tuning experiment I chose to do a logistic regression model. Logistic regressions can offer both efficiency and ease of interpretability. I was hoping to easily understand the experiment so that I could compare it to the AutoML experiment. I chose a large range of variables for the regression to use, in hopes of getting a good sampling of results.

### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

The results were not as good as the AutoML model experiment. The best accuracy that the model was able to get was 0.70 which paled in comparison to the AutoML model which had a best accuracy of 0.98. I would choose a different model entirely for the hyper parameter experiment since the logistic regression performed so poorly.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

I deployed the AutoML experiment since it was the best performer. I deployed it with an Azure Container Instance to an endpoint within. I was then able to send data to that endpoint to get a result from the model back. You can query the endpoint with a simple python json http request.

Here's a sample data request:
`
data = {"data":
           [
              {
                'season_id': 22015,
                'matchup_home': 'ATL vs. DET',
                'season_type': 'Regular Season',
                'min': 240,
                'team_name_home': 'Atlanta Hawks',
                'fg3m_home': 8,
                'fg3a_home': 27,
                'fg3_pct_home': 0.296,
                'wl_home': 'L',
                'team_name_away': 'Detroit Pistons',
                'fg3m_away': 12,
                'fg3a_away': 29,
                'fg3_pct_away': 0.414,
                'wl_away': 'W',
                'highest_3pp': 0.414
      },
   ]
}
`

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
