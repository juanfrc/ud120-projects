#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn import svm
clf = svm.SVC(C=10000)
# clf = svm.SVC(kernel='linear')
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s"

t1 =time()
score = clf.score(features_test, labels_test)
print "prediction time:", round(time()-t1, 3), "s"
print score

# print pred[10]
# print pred[26]
# print pred[50]

print sum(pred)


# c=10, accuracy = 0.616040955631
# c=100, accuracy = 0.616040955631
# c=1000, accuracy = 0.821387940842
# c=10000, accuracy = 0.892491467577
