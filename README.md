# LauzHack2018 
### Project submission available on [devpost](https://devpost.com/software/kang)

## Inspiration
There is a lot of suspicious financial activity happening every day. These suspicious transactions are used for different activities like money laundering, funding terrorism, etc. Banks need to investigate both for the greater good and also for compliance reasons. Due to the high volume of transactions, it is hard to do these investigations manually. So, we need a better & automated way to identify the limited suspicious activities which can then be investigated by human operators.

A lot of the financial irregularities are leading to increased funds for terrorist activities & drug trades which are harmful to the entire society. 

We use machine learning to identify the suspicious transactions which can then be investigated by the human operators. 

## What it does
We built a machine learning model based on the dataset provided by CreditSuisse to detect the accounts having suspicious behaviour.

## How we built it
* We built hundreds of models using different frameworks & platforms like Pega Prediction Studio. We tried to optimize the different hyperparameters, features, sampling & thresholds for the models. 
* We ran the Pega Prediction Studio to figure out the important features for the machine learning models. After

## Challenges we ran into
* The dataset was highly imbalanced leading to overfitting of the models. It took some time to try different ways to balance the dataset & trying different approaches. 
* The PEGA platform for training the models was not meant for the production loads which caused some issues for the PEGA team as well. 

## What we tried that did not work
* We tried to make use of auto-encoder to learn about the representation of non-suspicious accounts. This would provide a way to distinguish them from the suspicious accounts. Unfortunately, in the end it took long time to train and did not give great results.

## Accomplishments that we're proud of
* We managed to learn how to run machine learning models on imbalanced datasets after reading the different state of the art research papers.
* Managed to get the predictions for a limited number of inputs for the model trained by Pega platform despite lots of issues.

## What we learned
* Working with imbalanced datasets


## What's next for KaNG
* Run our model in production at scale on the CreditSuisse production environment!


