from flask import Blueprint, request, jsonify
from app.services.prediction_service import PredictionService

api = Blueprint('api', __name__)
prediction_service = PredictionService()

@api.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    input_data = data['input']
    prediction = prediction_service.predict(input_data)
    
    return jsonify({'prediction': prediction})