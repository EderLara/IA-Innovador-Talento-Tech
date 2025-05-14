import numpy as np
import tensorflow as tf
import io
import os
import logging # Añadir logging
# from sklearn.externals import joblib Tambien podemos usar esta librería

# Cargar el modelo 
MODEL_PATH = './modelo/modelo.pkl'                  # Asumiendo que sea pkl, recuerda que puedes usar otra técnica para guardar el modelo
if not os.path.exists(MODEL_PATH):
    logging.error(f"Error Crítico: Modelo no encontrado en {MODEL_PATH}")
    # Considera una forma más robusta de manejar esto si la API no puede funcionar sin el modelo
    exit() # O manejar el error de forma diferente

try:
    model = tf.keras.models.load_model(MODEL_PATH)              # Tambien puedes usar Scikit-learn sklearn.externals.joblib

    logging.info(f"Modelo cargado exitosamente desde {MODEL_PATH}")
except Exception as e:
    logging.error(f"Error al cargar el modelo desde {MODEL_PATH}: {e}", exc_info=True)
    # Manejar el error apropiadamente, quizás la API no debería iniciar.
    exit()

# Manejar constantes para el preprocesamiento:

# CONSTANTE_VAR ....

def preproccess_predict(*args):
    """
    funcion para preprocesar la predicción
    """
    try:
        """
            TODO codigo para el procesamiento y la predicción
        """

        return prediccion

    except Exception as e:
        logging.error(f"Error durante el preprocesamiento de la imagen: {e}", exc_info=True)
        raise # Relanzar la excepción para que sea manejada en la ruta

