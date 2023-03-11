# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The main objective of this project was to deploy a model onto the cloud that can take in data about an individual and predict wheter they will be approved for a loan or not
## Hypothesis
- Individuals who are married will have a higher chance of getting approved
- Level of education might impact approval
- Urban areas with high growth prospects might impact the decision

## EDA 
- Married and Educated individuals have a greater ratio of Loans approved 
- Higher ratio of Loans approved for homes in Semiurban areas
- Married people tend to look for homes in urban/semiurban areas



## Process
- During EDA, I tried to test out my hypothesis by plotting different visualizations from my data and various pivot tables
- The data cleaning step was integrated into the pipeline
- For numeric variables I imputed null values with the mean
    - For Loan Amount I imputed null values with the mean of Loan Amount accoridng to each Property Area
- For categorical variables I imputed null values with the mode
- Using a pipleine I tested different models that gave me the best accuracy score for my data
- After I found th ebest model I created another pipeline that found the best hyperparameters and feature selection for thta model using GridSearchCV
- Once I was satisfied with my models performance, I deployed to to the cloud using an API I created

## Results/Demo
- My LogisticRegression model gave me the best performace with an accuracy score of 0.811
- After hyperparamter tuning and feature selection I improved my accuracy to 0.812
- The app api I created was just a simple one that takes in json data and outputs a prediction of weather a Loan would be approved or not (1 for approved, 0 for rejected)
- Run the test.py file in the command line to see the prediction of the model

## Challanges 
- Couldn't really do much feature engineering because all of the custom classes and function transformers I created gave me an error when fit into the pipeline
- Unfortunately I downloaded the outdated python packages into my EC2 instance before the project, so I couldnt really run the model I trained in the newer versions of python in the cloud

## Future Goals
- Create custom classes and function transformers that allow more feature engineering possibilities which might improve my model
- My model might be overfitting my training data, need to see how accurately it predicts on unseen data
    - Will try to implement the train test split method and see how my model performs on the testing data