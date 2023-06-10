# Project Fomich - ML model for flat price prediction

## Data

[Data](https://drive.google.com/file/d/1FZV6YH3k_-uiMv32GfsGaByE5D2CMUhZ/view?usp=sharing) was taken from [Yandex.Realty] https://realty.ya.ru/sankt-peterburg/ and contains information about sale and rent announcements. Here the brief description of the dataset:

![image](https://github.com/FomichAnastasia/project/assets/114520431/1ecc5577-0b58-4fcf-b31f-74602558a774)

We will predict with this project the prices of **selling**! 

In the [file](https://github.com/FomichAnastasia/project/blob/main/Statistics.ipynb) all necessary operations and visualizations are given

[Here](https://github.com/FomichAnastasia/project/blob/main/Models.ipynb) all model creation steps are presented. What is important here is that in the result **xgboost model was chosen**. Cathegorical featrues were not transformed to dummy variables to simplify the interface and error without dummies didn't increase significantly. 


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

## Install instructions and run app with virtual environment

### How to start work with VM

Firstly, create your own VM. We will use [Yandex VM](https://console.cloud.yandex.ru/folders/b1gbrh8lv3mtr0l2eo47/compute/instances). 

Make the connection to your VM and go to the VM

```
ssh-rsa your_key
ssh login@vm_address
```

### How to open the port in your remote VM

As we specified ports in the [app](https://github.com/FomichAnastasia/project/blob/master/app.py) - , we need to specify port in the the remote VM port with following commands:

```
sudo apt install ufw 
sudo ufw allow 5444 
```
![image](https://github.com/FomichAnastasia/project/assets/114520431/46dda731-462a-4f7b-be99-a5be9d37cabe)

### How to add data to the VM

Firstly, if you don't have docker, please follow the instructions from the official [site](https://docs.docker.com/engine/install/ubuntu/)

As you have docker installed, we can start working with project.

add project to your VM
```
git clone --branch master https://github.com/FomichAnastasia/project.git 
```

## How to run app using docker

Go to the project folder
```
cd project 
```
You can check the last version of the docker image with **docker images** command

Run the current latest version of the docker
```
docker run --network host -d st062944/gsom_predictor:v.0.2 
```
Check that it is working with  **docker ps** command - output should not be empty

Go to the [Postman](https://web.postman.co/), create an account if you need -> **Workspaces** -> **Your workspace**, create the new one of ypu need -> add in the **Get** the following request

```
vm_address:5444/prediction_test?floor=5&rooms=2&area=64&kitchen_area=23&living_area=30&agent_fee=0&price_per_sq_m=10000&house_price_sqm_median_cleaned=300000&house_price_sqm_median_cleaned=35000&days_exposition=130&price_for_rent=23000
```
You can change request with different imputs of variables (numbers after =)

The example of the Postman interface is below

![image](https://github.com/FomichAnastasia/project/assets/114520431/373a9b49-d17d-41da-ad36-9dcbac01c762)

### Close docker

To end work with docker file, find the name of the docker with 
```
docker ps
docker stop NAMES
```



