from keras.models import load_model

from model.clusteringLayer import ClusteringLayer

def loadModel():
	model = load_model(
		'./data/dcec_model_.h5',
		custom_objects={
			'ClusteringLayer': ClusteringLayer
		}
	)

	model._make_predict_function()

	def predict(x):
		q, _ = model.predict(x, verbose=0)
		return q.argmax(1)
	
	return predict
