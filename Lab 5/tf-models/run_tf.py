import time
import logging
#from mobilenet_v2 import MobileNetV2Base
import os
import sys
import numpy as np
from PIL import Image, ImageOps
import tensorflow.keras

CONFIDENCE_THRESHOLD = 0.5
PERSISTANCE_THRESHOLD = 0.25

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

#model = MobileNetV2Base()
model_path = '/home/pi/TensorflowonThePi/TeachableMachinesExample/keras_model.h5'
model = tensorflow.keras.models.load_model(model_path)

last_seen = [None] * 5

def detect(img):
	prediction = model.predict(img)
	for p in prediction:
		label,name,conf = p
		if conf > CONFIDENCE_THRESHOLD:
			print("Detected", name)
		else:
			print("NOT Detected.")

if __name__ == "__main__":
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
	image = Image.open('/home/pi/Interactive-Lab-Hub/Lab 5/example.jpg')
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	img_array = np.asarray(image)
	img_n = (img_array.astype(np.float32) / 127.0) - 1
	data[0] = img_n
	detect(data)
