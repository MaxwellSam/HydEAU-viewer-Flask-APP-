# HydrEAUviwer Flask APP

HydrEAUviewer is a Web application developed in python with FLASK. This APP is composed by an overlayer API, which organise the hydrological data recovery from HubEAU, an online API for water related data ([hubEAU](https://hubeau.eaufrance.fr/)). An interface use the API and allow to visualize data recorded by hydrological stations through a map and graphics. 

## Setup

### Install requirements

#### With virtualenv

```
virtualenv .venv
source ./.venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

#### or with conda

```
conda create --prefix ./venv python=3.8
conda activate ./.venv
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Run the app 

```
python3 APP/APP.py
```

## Python Dependancies

This programme use some python modules. Please make sure you to have installed the following packages: 
-  API and Web interface
   -  Flask
   -  Requests
