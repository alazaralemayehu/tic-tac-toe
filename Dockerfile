FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# install dependences
RUN pip install -r requirements.txt

# copy project file
COPY . /app

# configure the container to run in an executed manner 
ENTRYPOINT [ "python" ]

CMD ["app.py"]