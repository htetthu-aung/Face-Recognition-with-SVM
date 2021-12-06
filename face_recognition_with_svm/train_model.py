import cv2
import numpy as np
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt


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


print(type(X_train))
print(type(y_train))
svm = SVC(C = 1,kernel = 'poly', gamma='auto')

svm.fit(X_train, y_train)


prediction = svm.predict(X_test)

accuracy = svm.score(X_test, y_test)

categories = ["AdrienBrody","Htet Thu Aung", "Jisoo","Ronaldo"]


print("The accuracy socre is: ", accuracy)


print('The prediction is: ', categories[prediction[0]])

my_pet = X_test[0].reshape(200,200)

plt.imshow(my_pet, cmap='gray')
plt.show()



pick = open("model.sav", "wb")
pickle.dump(svm, pick)
pick.close()



