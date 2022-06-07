# Base image
FROM python:3.7


# Creating work directory in docker
WORKDIR /app

# Copying files to docker 

COPY requirements.txt ./requirements.txt


# Installing requirements
RUN apt-get update && pip install -r requirements.txt

EXPOSE 8501

ADD . /app 

# Starting application
ENTRYPOINT ["streamlit", "run"]

CMD ["frontend.py"]
