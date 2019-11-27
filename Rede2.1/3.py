
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random

# create directories
dataset_home = 'dataset/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['carboidrato/', 'proteina/', 'legumes/', 'outros/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)

seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories
src_directory = 'dataset/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('carboidrato'):
		dst = dataset_home + dst_dir + 'carboidrato/'  + file
		copyfile(src, dst)
	elif file.startswith('proteina'):
		dst = dataset_home + dst_dir + 'proteina/'  + file
		copyfile(src, dst)
	elif file.startswith('legumes'):
		dst = dataset_home + dst_dir + 'legumes/'  + file
		copyfile(src, dst)
	elif file.startswith('outros'):
		dst = dataset_home + dst_dir + 'outros/'  + file
		copyfile(src, dst)