# Face-Recognition-with-SVM

This is the face recognition system with Support Vector Machine(SVM)


## Project Set up and Installation
This project is used opencv, numpy and matplotlib library.


## Dataset 
I use my created own dataset with four different people in different folders. The images
contain (200x200) pixels and  convert them into numpy arrays dump these arrays into
`data.pickle` with pickle module.


## Script Files Used

`create_data` file is for creating `data.pickle` file for training the model
in `train_model.py`.

After the tarining, `model.sav` will get and `detection.py` is used for the
face detection testing with matplotlib.


# Results

Face recognition with SVM gets a good result. Support Vector Machine
is a good model for two-class or multi-class classification among the Machine Learning models.
