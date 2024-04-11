# NBA 3 Point Percentage Impact on Winning
Over the past decade NBA offenses have shifted to primarily relying on the 3 point shot to score points. Certain players and teams have greatly impacted this shift. Stephen Curry and the Golden State Warriors are among some of the pioneers for this new approach. This project will analyze NBA 3 point percetage data from 2015 to 2023. We will be looking for the potential impact that 3 point shooting percentage has on winning NBA games.

## Project Set Up and Installation
In order complete this project successfully you will need to register the dataset provided in the /data folder of this repository. This is a custom dataset for this project.

**Udacity Note**
I am using the provided lab for this project.

## Dataset

### Overview
The dataset we are using was supplied from Kaggle [Link](https://www.kaggle.com/datasets/wyattowalsh/basketball). Within that database is a table that stores all game related data. All relevant team stats and the outcome of each game. From that I was able to extract a condensed dataset with SQL that has 3 point shooting percetages for each team as well as the winning team and the highest 3 point percentage between both teams.

### Task
With this dataset we will be evaluating whether or not a high 3 point shooting percentage has an impact on the outcome of a game or not.

### Access
I will be registering this dataset within the workspace and accessing it via URL when needed. You can see how I registered the dataset with the following code:
```
# workspace setup
ws = Workspace.from_config()
print(ws)

# dataset key info
key = 'nba_3pt_data'
data_desc = 'NBA game data from 2015 to 2023 containing 3 point percentages.'

# checking if dataset is already registered
if key in ws.datasets.keys():
    nba_dataset = ws.datasets[key]
else:
    # get data from url
    nba_data_url = 'https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/data/nba_3pt_data.csv'
    nba_dataset = Dataset.Tabular.from_delimited_files(nba_data_url)        
    # register dataset
    nba_dataset = nba_dataset.register(workspace=ws,
                               name=key,
                               description=data_desc)
```
There are several ways you can register a dataset but I chose via the Azure ML SDK in this case.

## Automated ML
For the AutoML experiment I will be using a classification experiment type to find the best possible model in an automated fashion. I'm looking for the most accurate model and evaluating the column containing the outcome for the highest 3 point shooting percentage between both teams.

### Results
The AutoML experiment returned Voting Ensemble as the best model with a very high accuracy.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/automl_rundetails.png)

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/automl_best_model_trained.png)

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/automl_best_model_metrics.png)

## Hyperparameter Tuning
For the hyperparameter tuning experiment I chose to do a logistic regression model. Logistic regressions can offer both efficiency and ease of interpretability. I was hoping to easily understand the experiment so that I could compare it to the AutoML experiment. I chose a large range of C and max iteration variables for the regression to use, in hopes of getting a good sampling of results.

### Results
The results were not as good as the AutoML model experiment. The best accuracy that the model was able to get was 0.70 which paled in comparison to the AutoML model which had a best accuracy of 0.99. I would choose a different model entirely for the hyper parameter experiment since the logistic regression performed so poorly. I'm not a data scientist though and would consult with data scientists on my team to find the best possible for this dataset.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/hyperdrive_run_details.png)

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/screenshots/hyperdrive_best_model.png)

## Model Deployment
I deployed the AutoML experiment since it was the best performer. I deployed it with an Azure Container Instance to an endpoint within. I was then able to send data to that endpoint to get a result from the model back. You can query the endpoint with a simple python json http request.

Here's a sample data request:
```
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
```
## Project Improvements
There's a couple of steps that could be taken to improve this project.
- Getting a more robust dataset that includes more games would help the experiments have more to work with.
- Having another figure in the dataset that accounts for 3 point volume as well to get a bigger picture of how 3 point shooting volume and percentage are coupled and can impact a game outcome.
- Running different types of AutoML experiments and choosing a different hyperparameter tuning experiment. For instance we could choose an AutoML time series analysis to predict how well a team will shoot against a certain opponent based on past meetings. In the case of the hyperparameter experiment we could try a grid search instead of a random search in order to explore every passed combination of variables. I would also consider swapping the model type over to a decision tree instead of a logistic regression to see the differences between the two.
- Giving the AutoML experiment more time to complete it's analysis would also help. I limited the AutoML runs to 30 minutes I would expand that to ensure it's a more exhaustive experiment. The same goes for the hyperdrive experiment, I limited it to 40 runs. Expanding that would ensure a more exhaustive experiment.
- Ideally if this were done in a work setting I would work closely with a data scientist to get an idea of which model type would be best based on the data itself.

## Screen Recording
[Screen Recording Link](https://youtu.be/jNaVuzxc684)
