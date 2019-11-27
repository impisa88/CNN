from os import listdir
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# define location of dataset
folder = '/home/joao/Imagens/Rede/dataset/'

photos, labels = list(), list()

classificacao[4]

# enumerate files in the directory
for file in listdir(folder):
	# determine class
	output = classificacao[0,0,0,1]
	if file.startswith('carboidrato'):
		output = classificacao[1,0,0,0]
	elif file.startswith('legumes'):
		output = classificacao[0,1,0,0]
	elif file.startswith('proteina'):
		output = classificacao[0,0,1,0]
	
	# load image
	photo = load_img(folder + file, target_size=(128, 128))
	# convert to numpy array
	photo = img_to_array(photo)
	# store
	photos.append(photo)
	labels.append(output)
# convert to a numpy arrays
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)

# save the reshaped photos
save('imagens.npy', photos)
save('nomes.npy', labels)