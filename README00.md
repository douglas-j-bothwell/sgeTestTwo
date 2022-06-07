https://docs.docker.com/language/python/build-images/#tag-images

docker run -d -p 8000:5000 python-docker

docker build --tag dbothwell/python-docker:1.0.0 .

https://medium.com/codex/push-docker-image-to-docker-hub-acc978c76ad

docker login

docker tag python-docker:latest python-docker:v1.0.0

docker push dbothwell/python-docker:1.0.0


1.0.0 -- added the last line to Dockerfile

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

this is equivalent to running:

python3 -m flask run --host=0.0.0.0
