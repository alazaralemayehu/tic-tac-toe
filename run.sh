#!/bin/bash

exec docker build -t flask-application .
exec docker run -p 5000:5000 -d flask-application