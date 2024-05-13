## Train model
Train sklearn DecisionTreeClassifier model and save it to `model.pkl`
`python train_iris_model.py`

## Run serving app locally
`python iris_app.py`

```
curl -X POST -H "Content-Type: application/json" -d '{
"data": [
[5.1, 3.5, 1.4, 0.2],
[6.3, 3.3, 6.0, 2.5],
[6.0, 2.2, 4.0, 1.0]
]
}' http://localhost:5000/predict
```


## Build Docker container
`docker build -t iris-app .`

## Run Docker image
`docker run -p 5000:5000 iris-app`

## Run app with Kubernetes

