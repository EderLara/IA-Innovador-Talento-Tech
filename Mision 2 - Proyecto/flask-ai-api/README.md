# Flask AI API

Este es un proyecto API-REST basado en Flask, utilizado para generar predicciones a partir de un modelo entrenado

## Estructura del Proyecto

```
flask-ai-api
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models
│   │   └── model.pkl
│   ├── services
│   │   └── prediction_service.py
│   ├── static
│   └── templates
├── tests
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. **Clone el repositorio:**
   ```
   git clone <repository-url>
   cd flask-ai-api
   ```

2. **Crear un virtual environment: (Opcional)**
   ```
   python -m venv venv
   source venv/bin/activate  # linux - mac
   # On Windows use `venv\Scripts\activate`
   ```

3. **Instalar Librerías:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   flask run
   ```

## Uso

Once the application is running, you can access the API endpoints to generate predictions. 

### Ejemplo Request

To get a prediction, send a POST request to the `/predict` endpoint with the required input data in JSON format.

```json
{
    "input_data": [/* your input data here */]
}
```

### Ejemplo Response

The API will return a JSON response with the prediction result.

```json
{
    "prediction": /* predicted value */
}
```

## Testing

To run the tests, ensure you are in the virtual environment and execute:

```
pytest
```

## Licencia

This project is licensed under the MIT License.