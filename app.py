from flask import Flask, request, jsonify
import json
import numpy as np

from model.loadModel import loadModel as lm
from assets.constants import labels_to_remove

app = Flask(__name__)

predict

@app.before_first_request
def load_model():
	global predict
	predict = lm()

@app.route('/', methods=['POST'])
def recieve_data():
	global predict
	data = json.loads(request.data)

	x = np.array(data['data'])

	x = x.reshape((*x.shape, 1))

	labels = predict(np.array(x))

	artefact_idx = []
	for idx, label in enumerate(labels):
		if str(label) in labels_to_remove:
			artefact_idx.append(idx)

	return jsonify(artefact_idx)
