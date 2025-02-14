# Container image that runs your code
FROM python:3.12.5-alpine3.20

#Install the required python modules to the container
RUN pip install --no-cache pyyaml PyGithub
RUN pip install pyfiglet

WORKDIR /usr/solution

#Copies code files from the actions repository to the container
COPY solution .

#Code file to execute when teh docker container starts up
ENTRYPOINT [ "python", "/usr/solution/main.py" ]
