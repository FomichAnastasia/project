# Project Fomich - ML model for flat price prediction

## Data

[Data](https://drive.google.com/file/d/1FZV6YH3k_-uiMv32GfsGaByE5D2CMUhZ/view?usp=sharing) was taken from [Yandex.Realty] https://realty.ya.ru/sankt-peterburg/ and contains information about sale and rent announcements. Here the brief description of the dataset:

![image](https://github.com/FomichAnastasia/project/assets/114520431/1ecc5577-0b58-4fcf-b31f-74602558a774)

In the [file](https://github.com/FomichAnastasia/project/blob/main/HW1%20(4).ipynb) all necessary operations and visualizations are given

[Here](https://github.com/FomichAnastasia/project/blob/main/HW2%20(3).ipynb) all model creation steps are presented. What is important here is that in the result xgboost model was chosen. Cathegorical featrues were not transformed to dummy variables to simplify the interface and error without dummies didn't increase significantly. 

## Install instructions and run app with virtual environment

### Check ports

As we specified ports in the [app](https://github.com/FomichAnastasia/project/blob/master/app.py) - , we need to specify port in the the remote VM port with following commands:
```
sudo apt install ufw # if you don't have it already
sudo ufw allow 5444 
```

## Information about Dockerfile and describe it's content

### Dockerfile
 
Our [dockerfile](https://github.com/FomichAnastasia/project/blob/master/Dockerfile) contains the following data:
 
 ```
FROM ubuntu:20.04 # open source operating system on Linux
MAINTAINER st062944 # author (me)
RUN apt-get update -y # update all packages
COPY . /opt/gsom_predictor # copy content of the directory (current) to gsom_predictor folder 
WORKDIR /opt/gsom_predictor # set working directory
run apt install -y python3-pip # install pip
run pip install -r requirements.txt # install all necessary labs from [requirements](https://github.com/FomichAnastasia/project/blob/master/requirements.txt) file 
cmd python3 app.py # run the [app](https://github.com/FomichAnastasia/project/blob/master/app.py)
 ```
 
### What files are inside our docker? 

Here you can see all content of the working directory but we don't need all of the files to be added to docker
 
![image](https://github.com/FomichAnastasia/project/assets/114520431/7dae5499-6a7f-49cd-a705-b93674c4ba3d)

So, we specified what files should be excluded from docker with [dockerignore](https://github.com/FomichAnastasia/project/blob/master/.dockerignore) file
 

How to open the port in your remote VM
	
How to run app using docker and which port it uses
