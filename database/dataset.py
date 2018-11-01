import os
import numpy as np

class get_file(object):
	"""docstring for get_file"""
	def __init__(self, file_dir):
		super(get_file, self).__init__()
		self.file_dir = file_dir

	def func(self):
		image_rule = ['png', 'jpg']
		labels = []
		images = []
		temp = []
		for root, sub_folders, files in os.walk(self.file_dir):
			for name in files:
				if name.split('.')[-1] in image_rule:
					images.append(os.path.join(root, name))
			for name in sub_folders:
				temp.append(os.path.join(root, name))
		i = 0
		for one_folder in temp:
			label = one_folder.split('/')[-1]
			labels = np.append(labels, label)
			i += 1
		temp = np.array([images, labels])
		image_list = list(temp[0])
		label_list = list(temp[1])

		return image_list, label_list

if __name__ == '__main__':
	path = './face_recognition_database'
	test = get_file(path)
	print(test.func()[1])