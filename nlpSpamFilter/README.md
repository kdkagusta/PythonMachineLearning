# Teknik Pemodelan Natural Language Processing(NLP) Deteksi Spam Email 
Teknik pemodelan menggunakan algoritma **Naive Bayes Classifier**

## Package Yang Di gunakan
```
command : pip install <package_name>
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- sklearn
```

## Execute Script
```py main.py```

## Urutan Script Coding
```
1. Import Library yang di gunakan
2. Ambil dataset dalam bentuk file .csv
dataset diambil dari website Kaggle (https://www.kaggle.com/datasets/ozlerhakan/spam-or-not-spam-dataset)
3. Check Data
4. Pengecekan Missing Value dan Duplikasi Data
5. Lihat kata-kata(data) yang biasanya tidak berguna dengan packgae stopwords
6. Splitting Data
7. Pemodelan Data dengan menggunakan Naive Bayes Classifier
8. Prediksi Model
```

## Hasil
```
PS E:\PythonMachineLearning\nlpSpamFilter> py main.py
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3016 entries, 0 to 3015
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   email   3016 non-null   object 
 1   label   3000 non-null   float64
dtypes: float64(1), object(1)
memory usage: 47.3+ KB
Ada duplikasi data sebanyak 128 data
Tidak ada duplikasi data
Jumlah data setelah menghilangkan duplikasi: (2872, 2)
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\pradn\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Confusion Matrix
 [[482   7]
 [  2  84]]
Classification Report:

              precision    recall  f1-score   support

         0.0       1.00      0.99      0.99       489
         1.0       0.92      0.98      0.95        86

    accuracy                           0.98       575
   macro avg       0.96      0.98      0.97       575
weighted avg       0.98      0.98      0.98       575

Accuracy: 98.43478260869564 %
```

## Refrensi 
[galihbahtera.medium.com](https://galihbahtera.medium.com/deteksi-spam-email-menggunakan-machine-learning-1838f0dcc41d)