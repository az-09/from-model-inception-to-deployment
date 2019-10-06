Note:

    Changed proxy_pass from http://localhost:5000 to http://api:5000 in nginx.conf

    Nginx:

    $ curl --header "Content-Type: application/json" --request POST --data '[{"sepal_length":6.3,"sepal_width":2.3,"petal_length":4.4,"petal_width":1.0}]' http://localhost:8080/predict
        {
            "predictions": {
                "prediction_0": 1
            }
        }

    Gunicorn:
    
    $ curl --header "Content-Type: application/json" --request POST --data '[{"sepal_length":6.3,"sepal_width":2.3,"petal_length":4.4,"petal_width":1.0}]' http://localhost:8080/predict
        {
            "predictions": {
                "prediction_0": 1
            }
        }

Reference:

    https://medium.com/datadriveninvestor/from-model-inception-to-deployment-adce1f5ed9d6
    https://dev.to/ishankhare07/nginx-as-reverse-proxy-for-a-flask-app-using-docker-3ajg

