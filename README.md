# minimal-flask-docker

docker build -t flaskimage

docker run -it --name flaskcontainer --rm -p 8000:5000 flaskimage

then run
`python post.py`