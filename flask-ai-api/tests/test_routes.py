from flask import json
from app import create_app

app = create_app()

def test_prediction_route(client):
    response = client.post('/predict', json={'data': [1, 2, 3]})
    assert response.status_code == 200
    assert 'prediction' in response.json

def test_prediction_route_invalid_data(client):
    response = client.post('/predict', json={'data': 'invalid'})
    assert response.status_code == 400
    assert 'error' in response.json

def test_prediction_route_missing_data(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert 'error' in response.json