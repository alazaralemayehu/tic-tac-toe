#!/bin/bash

sudo docker build -t flask-application .
sudo docker run -p 5000:5000 -d flask-application