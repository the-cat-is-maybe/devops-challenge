FROM alpine:latest
##?## Seperate run commands for clairty purposes. Use \ new lines for clarity purposes

##?## Install both python3.10 and py3-pip instead of just py3-pip for better human comprehension
RUN apk update && \
    apk add python3 py3-pip

##?## Make and upload necessary files to docker image
RUN mkdir -p /app/devops-challenge 
ADD ./ /app/devops-challenge

##?## Pip install requirements
WORKDIR /app/devops-challenge
RUN pip install -r requirements.txt

##?## Expose application
EXPOSE 8080

##?## Set default command
CMD ["python3", "app.py"]

##!## docker build -f application.Dockerfile -t devops-challenge . ; docker run -it -e MONGO_URI=mongodb://devopsC:dev0psUs3r@localhost:27017/devops-challenge-db devops-challenge 