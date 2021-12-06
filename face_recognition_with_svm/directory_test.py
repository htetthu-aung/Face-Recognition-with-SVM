# import os


# directory = "C:\\Users\\Htet\\Desktop\\Face Recognition with SVM\\Face Images"


# categories = ["AdrienBrody", "Htet Thu Aung", "Jisoo", "Ronaldo"]


# for category in categories:
# 	path = os.path.join(directory, category)
# 	label = categories.index(category)
# 	print(path)
# 	print(label)


# 	for img in os.listdir(path):
# 		img_path = os.path.join(path, img)

# 		print(img_path)










# import os


# directory = "C:\\Users\\Htet\\Desktop\\Face recognition with svm\\Face Images"

# categories = ["AdrienBrody","Htet Thu Aung","Jisoo", "Ronaldo"]


# for category in categories:
# 	path = os.path.join(directory, category)

# 	for img in os.listdir(path):
# 		img_path = os.path.join(path, img)

# 		print(img_path)



import os
import cv2


base_dir = os.path.dirname(os.path.abspath(__file__))

img_dir = os.path.join(base_dir, "Face Images")

for root, dirs, files in os.walk(img_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			img = os.path.join(root, file)
			