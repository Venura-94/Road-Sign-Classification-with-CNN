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
