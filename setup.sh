#!/bin/bash

#Script to setup virtual environment and install all the dependencies.

module load Python/3.6.3-intel-2017a
virtualenv nlp_env
source nlp_env/bin/activate

ipython kernel install --user --name=nlp_env

pip install -r requirements.txt --user

