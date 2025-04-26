# Import necessary libraries
# from sklearn.datasets import load_breast_cancer:

# Loads the breast cancer dataset from scikit-learn, which is a dataset of features related to breast cancer and whether the tumor 
# is malignant or benign.
# from sklearn.model_selection import train_test_split:

# Splits your data into training and testing sets, typically used to ensure that you can evaluate your model's performance on unseen data.
# from sklearn.svm import SVC:

# Imports the Support Vector Classifier (SVC) algorithm, which will be used to train the model using an SVM with different kernel functions.
# from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay:

# accuracy_score helps evaluate the overall accuracy of the model.
# confusion_matrix provides a matrix showing the number of true positives, false positives, true negatives, and false negatives.
# ConfusionMatrixDisplay is used to visualize the confusion matrix.
# import matplotlib.pyplot as plt:

# Imports Matplotlib, a library for creating visualizations like plots, which will help in displaying results like decision boundaries 
# and confusion matrices.
# from sklearn.inspection import DecisionBoundaryDisplay:

# This is used to visualize the decision boundary of the SVM, which helps in understanding how well the classifier is separating 
# the different classes.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

# 1. Load the dataset
cancer = load_breast_cancer()
X = cancer.data[:, :2]  # Use the first two features for simplicity
# Here, cancer.data contains the feature data (shape of 569 samples x 30 features).
# By using [:, :2], you're selecting only the first two features from the dataset (e.g., radius and texture of the cell nuclei).
# X now becomes a matrix with 569 rows (samples) and 2 columns (features).
y = cancer.target
# Target Label Explanation:
# Malignant (0): The tumor is harmful and cancerous.
# Benign (1): The tumor is non-cancerous and typically not harmful.



# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# train_test_split(X, y, test_size=0.3, random_state=42):

# X: The feature matrix that will be split.
# y: The target vector that will be split.
# test_size=0.3: This specifies that 30% of the data will be used as the test set, and the remaining 70% will be used as the training set.
# You can adjust this ratio (e.g., 0.2 for 20% test data and 80% training data).
# random_state=42: This ensures reproducibility of the split. By fixing the random_state, you ensure 
# that every time you run the code, the data is split the same way. If you don't specify a random_state, the split would be '
# 'random each time you run it.

# 3. Train the SVM model with RBF kernel
svm = SVC(kernel="rbf", gamma=0.5, C=1.0)
svm.fit(X_train, y_train)
# kernel="rbf": This specifies the use of the Radial Basis Function (RBF) kernel. The RBF kernel is commonly used for classification tasks 
# because it can create complex decision boundaries.

# gamma=0.5: The gamma parameter controls the influence of individual data points on the decision boundary. A smaller gamma value makes
# the decision boundary smoother, while a larger value allows the boundary to be more flexible and fit the data more closely. 
# In this case, gamma=0.5 provides a moderate level of flexibility.

# C=1.0: The C parameter controls the regularization of the model. A smaller C allows more flexibility and a larger number of 
# misclassifications, leading to a smoother decision boundary. A larger C value gives the model less flexibility and tries 
# to classify all points correctly, which could lead to overfitting. Here, C=1.0 
# is a commonly used value and strikes a balance between bias and variance.

# 4. Make predictions on the test set
y_pred = svm.predict(X_test)

# 5. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# 6. Display confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=cancer.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.show()

# 7. Visualize the decision boundary
plt.figure(figsize=(8, 6))
DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.6,
    xlabel=cancer.feature_names[0],
    ylabel=cancer.feature_names[1],
)

# Scatter plot of the dataset
plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolors="k", cmap=plt.cm.RdYlBu)
plt.title("SVM Decision Boundary on Breast Cancer Dataset")
plt.show()
