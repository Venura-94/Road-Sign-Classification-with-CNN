# Road Sign Classification with Convolutional Neural Networks

- Here is the old school architecture for understanding
  ![image](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/6e0b12ee-1d02-4662-bc09-438a46cecb74)

#### Note :: Data set is too large to add to the Github 

In this project, I have trained deep learning models known as Convolutional Neural Networks (CNNs) to classify 43 traffic sign images. 
This project has practical applications, particularly in the realm of self-driving cars.

1. Import libraries and datasets.
2. Visualize images.
3. Convert images to grayscale and perform normalization.
4. Build a deep learning model.
5. Compile and train the deep learning model.
6. Assess the trained model's performance.

## Learning Objectives

By completing this project,

- Understand the theory and intuition behind Convolutional Neural Networks (CNNs).


- Apply Python libraries to import and visualize dataset images.

  ![1](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/15fe588c-8b25-41f8-9795-f5b617701efb)


- Perform image normalization and convert images from color-scaled to grayscale.

  ![2](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/27bf7cdc-4a1f-4168-ac29-61f3db2319a5)


- Build a Convolutional Neural Network using Keras with Tensorflow 2.0 as a backend.

  ![3](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/a30e51e9-a115-4238-a480-e21f0a19339c)



- Compile and fit the Deep Learning model to training data.
  ![4](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/99fb1594-9092-4366-8a3a-bb16d4c4381c)



- Assess the performance of the trained CNN using various key performance indicators (KPIs) such as accuracy, precision, and recall.


![output](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/b8fb4d00-4b88-4ec5-9301-3596e3ae8dbe)


![2](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/5874cf04-cf2a-4945-83c9-bd05f39d8374)


## Docker Work in Step Wise

- Save the model according to the tensorflow serving models

- Pull image from the docker hub and create tensorflow serving image

- Then execute docker run
   - run docker container with tensorflow serving image
   - then mount model directory to tensorflow model in to container
   - add environment variables
 
    ![Docker_Container](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/43a9c53d-9aaf-4594-8267-e135ecac7d4d)


- Then at last can access the model endpoint to get prediction

## Summary to Tensorflow Serving Docker Container

![image](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/4ea86e60-41d8-4548-b446-82dc825ce26e)


## Predictions from User APP 

30Mph - Class - 1 - Correct 

![correct prediction](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/dc94fd37-127e-4db8-8571-cdbfa06669da)


50Mph - Class wrongly predicted due to different data set, not from the same distributions. Because model has made for different environment , therefore to improve this model need to look for different images and different techniques of optimizations.


![50 error analysis](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/f62da88b-1564-4b9f-8c32-cac43f0aebb7)


- Final Model Prediction

  ![final predictions](https://github.com/Venura-94/Road-Sign-Classification-with-CNN/assets/137409412/7b3ace88-8c2d-4f82-94b7-108e7c1bb659)

## Classes

| Class ID | Sign Description          |
|----------|---------------------------|
| 0        | Speed limit (20km/h)      |
| 1        | Speed limit (30km/h)      |
| 2        | Speed limit (50km/h)      |
| 3        | Speed limit (60km/h)      |
| 4        | Speed limit (70km/h)      |
| 5        | Speed limit (80km/h)      |
| 6        | End of speed limit (80km/h)|
| 7        | Speed limit (100km/h)     |
| 8        | Speed limit (120km/h)     |
| 9        | No passing                |
| 10       | No passing for vehicles over 3.5 metric tons|
| 11       | Right-of-way at the next intersection|
| 12       | Priority road             |
| 13       | Yield                     |
| 14       | Stop                      |
| 15       | No vehicles               |
| 16       | Vehicles over 3.5 metric tons prohibited|
| 17       | No entry                  |
| 18       | General caution           |
| 19       | Dangerous curve to the left|
| 20       | Dangerous curve to the right|
| 21       | Double curve              |
| 22       | Bumpy road                |
| 23       | Slippery road             |
| 24       | Road narrows on the right |
| 25       | Road work                 |
| 26       | Traffic signals           |
| 27       | Pedestrians               |
| 28       | Children crossing         |
| 29       | Bicycles crossing         |
| 30       | Beware of ice/snow        |
| 31       | Wild animals crossing     |
| 32       | End of all speed and passing limits|
| 33       | Turn right ahead          |
| 34       | Turn left ahead           |
| 35       | Ahead only                |
| 36       | Go straight or right      |
| 37       | Go straight or left       |
| 38       | Keep right                |
| 39       | Keep left                 |
| 40       | Roundabout mandatory      |
| 41       | End of no passing         |
| 42       | End of no passing by vehicles over 3.5 metric tons|

Each class corresponds to a specific type of traffic sign
