#Dockerfile for eggify deployment

#FROM directive instructing base image to build upon
FROM python:3.5-jessie

#ENV directive sets environmental variable for direct terminal output
ENV PYTHONUNBUFFERED 1

#RUN create root directory for project with mkdir
RUN mkdir /eggify

#WORKDIR set working directory to project root
WORKDIR /eggify

#COPY app components into container's workdir
ADD . /eggify

#RUN install required python packages with pip
RUN pip install -r requirements.txt
