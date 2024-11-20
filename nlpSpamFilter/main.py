#Import basic library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string

# Load Data csv
email = pd.read_csv('../DataSet/spam_or_not_spam.csv')

# Melihat data yang ada
email.head()
email.tail()
email.shape
email.info()

# Pengecekan Missing Value dan Duplikasi Data
email = email.dropna()
#Pengecekan missing value
email.isnull().sum()

# data yang terduplikasi atau tidak
def cek_duplikat(dataframe):
  if dataframe.duplicated().sum() > 0 :
    print ('Ada duplikasi data sebanyak {} data'.
    format(dataframe.duplicated().sum()))
  else:
    print('Tidak ada duplikasi data')
cek_duplikat(email)
email.drop_duplicates(inplace=True)
cek_duplikat(email)
print('Jumlah data setelah menghilangkan duplikasi:', email.shape)

# download the stopwords package
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
def process_text(text):
    #remove punctuation
    nopunc = [char for char in text if char not in
    string.punctuation]
    nopunc = ''.join(nopunc)
    
    #remove stop words
    clean_words = [word for word in nopunc.split() if word.lower()
    not in stopwords.words('english')]
    
    #Return a list of clean words
    return clean_words
# to show the tokenization
email['email'].head().apply(process_text)
from sklearn.feature_extraction.text import CountVectorizer
message = CountVectorizer(analyzer = process_text).fit_transform(email['email'])

# Splitting Data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(message, email['label'],test_size = 0.20, random_state = 42)

# Pemodelan Machine Learning
# create and train the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(x_train, y_train)

# Prediksi Model
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
#Predict
y_pred = classifier.predict(x_test)
#evaluasi model dengan confusion matrix
cnf_matrix=confusion_matrix(y_test,y_pred)
print('Confusion Matrix\n',cnf_matrix)
plt.figure()
heatmap = sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, annot_kws={'size': 14}, fmt='d', cmap='YlGnBu')
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
plt.title('Confusion Matrix\n', fontsize=18, color='darkblue')
plt.ylabel('True label', fontsize=14)
plt.xlabel('Predicted label', fontsize=14)
plt.show()
# Print classification report
print('Classification Report:\n')
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred) *100, "%")