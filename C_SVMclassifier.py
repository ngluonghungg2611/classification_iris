from B_SVM import *
from A_dataset import *
import numpy as np
Svc_classifier = svm.SVC(kernel='linear', 
                         C=C, 
                         decision_function_shape='ovr').fit(X, y)
Z = Svc_classifier.predict(X_plot)
Z = Z.reshape(xx.shape)
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.contour(xx, yy, Z, cmap = plt.cm.tab10, alpha = 0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Sepal length')
plt.ylabel('Sepel width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()