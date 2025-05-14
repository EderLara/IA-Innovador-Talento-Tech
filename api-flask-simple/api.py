from flask import Flask, request, jsonify


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG) # Configurar logging básico

#
@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint para recibir una imagen y devolver la predicción del modelo."""
    logging.info(f"Solicitud POST recibida en /predict desde {request.remote_addr}")
    if 'imagen' not in request.files:
        logging.warning("Solicitud recibida sin archivo en el campo 'imagen'.")
        return jsonify({'error': 'No se proporcionó ninguna imagen en el campo "imagen"'}), 400

    image_file = request.files['imagen']
    logging.debug(f"Archivo recibido: {image_file.filename}, Tipo: {image_file.content_type}")

    try:
        # Leer los bytes del archivo
        image_bytes = image_file.read()
        if not image_bytes:
             logging.warning("El archivo recibido está vacío.")
             return jsonify({'error': 'El archivo de imagen está vacío'}), 400

        # Preprocesar la imagen (incluye la inversión CONDICIONAL)
        processed_image = preprocess_image(image_bytes)

        # Realizar la predicción
        logging.debug("Realizando predicción con el modelo...")
        predictions = model.predict(processed_image)
        logging.debug(f"Predicciones crudas (logits/probabilidades): {predictions}")

        # Obtener la clase predicha (índice con mayor probabilidad) y la confianza
        predicted_class = np.argmax(predictions[0])
        confidence = np.max(predictions[0])

        logging.info(f"Predicción: Clase={predicted_class}, Confianza={confidence:.4f}")

        # Devolver el resultado como JSON
        return jsonify({
            'predicted_class': int(predicted_class),        # Convertir a int para JSON
            'confidence': float(confidence) * 100           # Convertir a porcentaje
        })

    except FileNotFoundError as fnf_error:
          logging.error(f"Error crítico: {fnf_error}", exc_info=True)
          return jsonify({'error': 'Error interno del servidor: Falta archivo de modelo'}), 500
    except Exception as e:
        logging.error(f"Error durante la predicción o preprocesamiento: {e}", exc_info=True)

        return jsonify({'error': 'Error interno al procesar la imagen o realizar la predicción'}), 500

if __name__ == '__main__':
    # Usar host='0.0.0.0' para que sea accesible desde fuera del contenedor
    # debug=False es generalmente recomendado para producción/staging
    app.run(host='0.0.0.0', port=5000, debug=False)