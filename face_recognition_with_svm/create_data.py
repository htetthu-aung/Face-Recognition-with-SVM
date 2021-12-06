import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle


directory = "C:\\Users\\Htet\\Desktop\\Face Recognition with SVM\\Face Images"


categories = ["AdrienBrody","Htet Thu Aung", "Jisoo","Ronaldo"]

data = []

for category in categories:
	path = os.path.join(directory, category)
	label = categories.index(category)

	# print(path)

	for img in os.listdir(path):
		img_path = os.path.join(path, img)
		#print(img_path)

		image = cv2.imread(img_path,0)
		image.resize(200,200)
		# cv2.imshow("img", image)

		image = np.array(image).flatten()


		data.append([image, label])


# print(len(data))

#print(data)

data = np.array(data,dtype=np.uint8)

pick_in = open("data.pickle",'wb')

pickle.dump(data, pick_in)

pick_in.close()