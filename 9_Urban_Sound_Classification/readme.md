My solution to solve a simple practice Audio classification challenge on Analytics Vidhya's website - [Urban Sound classification](https://datahack.analyticsvidhya.com/contest/practice-problem-urban-sound-classification/). Here is where I stand with few hours of hacking - 
![alt text](./img/website_capture.PNG "Snapshot from leaderboard")

## Problem statement - 
Audio classification in 10 different classes.

## Data
This dataset contains 8732 labeled sound excerpts (<=4s) of urban sounds from 10 classes: air_conditioner, car_horn, children_playing, dog_bark, drilling, enginge_idling, gun_shot, jackhammer, siren, and street_music.

## Approach
Using [fastaiaudio](https://github.com/fastaudio/fastaudio) to convert audio into Mel Spectorgram and then use a pretrained Resnet18 model to classify in 10 different categories. Refer to the UrbanSoundClassification.ipynb notebook.