# pythongraphQL
## Without docker
### Run app
```
python3 app.py
```
## With docker
### Build container
```
docker image build -t flask .
```
### Run container
```
docker container run -p 5000:5000 flask
```