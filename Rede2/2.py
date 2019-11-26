
# load and confirm the shape
from numpy import load
photos = load('imagens.npy')
labels = load('nomes.npy')
print(photos.shape, labels.shape)