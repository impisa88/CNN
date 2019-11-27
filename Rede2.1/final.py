
# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy 
 
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(128, 128))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 128, 128, 3)
	# center pixel data
	img = img.astype('float32')
	#img = img - [123.68, 116.779, 103.939]
	return img
 
# load an image and predict the class
def run_example():
	# load the image
	img = load_image('5.jpg')
	# load model
	model = load_model('final_model.h5')
	model2 = load_model('modelo.h5')
	# predict the class
	result = model.predict(img)
	print(result)

	if result <= 0:
		print('Prato de comida')

		resultado = model2.predict(img)
		print(resultado)

		plt.figure(figsize=(6,3))
		plt.subplot(1,2,1)
		plot_image(img, resultado, labels, imagens)
		plt.subplot(1,2,2)
		plot_value_array(img, resultado, labels)
		plt.show()
		plot_image

	else:
		print('Voce vai morrer')
 
# entry point, run the example
run_example()