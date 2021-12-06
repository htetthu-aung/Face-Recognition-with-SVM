import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import random




pick_in =  open("C:\\Users\\Htet\\Desktop\\Face Recognition with SVM\\data.pickle", "rb")
data = pickle.load(pick_in)
pick_in.close()

random.shuffle(data)

features = []
labels = []

for feature, label in data:
	features.append(feature)
	labels.append(label)

# print(labels)
# print(features)
# print("len of labels: ", len(labels))
# print("len of features: ", len(features))

features = np.array(features, dtype = np.uint8)
labels = np.array(labels, dtype = np.uint8)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25)

print(X_train.shape)
print(y_train.shape)


pick = open("model.sav",'rb')
svm  = pickle.load(pick)
pick.close()


categories = ["AdrienBrody","Htet Thu Aung", "Jisoo","Ronaldo"]


print("accuracy: ", svm.score(X_test, y_test))

prediction = svm.predict(X_test)
print("prediction is: ", categories[prediction[0]])


who = X_test[0].reshape(200,200)
plt.imshow(who, cmap='gray')
plt.show()

