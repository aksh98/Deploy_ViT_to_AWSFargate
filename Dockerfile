# Base image
FROM python:alpine

# Running every next command wih this user
USER root
EXPOSE 8501

# Installing Flask App
RUN pip install streamlit==1.9
RUN pip install -r requirements.txt

# Creating work directory in docker
WORKDIR /app

# Copying files to docker
COPY . '/app'

# Starting application #["python", "app.py"]
CMD streamlit run frontend.py