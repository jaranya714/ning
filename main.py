import streamlit as st
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = sns.load_dataset('iris')
df

x = df.iloc[:, :-1]
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

st.sidebar.title('Classifiers')
classifier = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'Decision Tree', 'random forest', 'Neural Network'))
if classifier == 'KNN':
  knn = KNeighborsClassifier(n_neighbors=3)
  knn.fit(x_train, y_train)
  y_pred = knn.predict(x_test)
  acc = accuracy_score(y_test, y_pred)
  st.write(acc)
if classifier == 'SVM':
  svm = SVC()
  svm.fit(x_train, y_train)
  y_pred = svm.predict(x_test)
  acc = accuracy_score(y_test, y_pred)
  st.write(acc)
if classifier == 'Decision Tree':
  dt = DecisionTreeClassifier()
  dt.fit(x_train, y_train)
  y_pred = dt.predict(x_test)
  acc = accuracy_score(y_test, y_pred)
  st.write(acc)
if classifier == 'random forest':
  rf = DecisionTreeClassifier()
  rf.fit(x_train, y_train)
  y_pred = rf.predict(x_test)
  acc = accuracy_score(y_test, y_pred)
  st.write(acc)
 if classifier == 'Neural Network':
  nn = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
  nn.fit(x_train, y_train)
  y_pred = nn.predict(x_test)
  acc = accuracy_score(y_test, y_pred)
  st.write(acc) 

