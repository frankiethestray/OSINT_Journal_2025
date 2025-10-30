Python
  DATA SELECTION

  The "Fake News Detection Dataset" was downloaded from Kaggle.  
  The two most important columns are: 1. Text: the body of the article (avg. 200-300 words) and 2. The label- The data originally displayed True for correct and False for Disinformation.  
  Using excel, the values were changed to numbers with 0 = correct and 1 = disinformation
  The dataset was used as it is openly available and made for easy begginer usage.  It is based on a selection of 20000 news articles.

                                                                                                                                 
┌──(myenv)─(kali㉿kali)-[/media/sf_Downloads]
└─$ python
Python 3.13.7 (main, Aug 20 2025, 22:17:40) [GCC 14.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> df = pd.read_csv('fake_news_dataset.csv')
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    df = pd.read_csv('fake_news_dataset.csv')
         ^^
NameError: name 'pd' is not defined. Did you mean: 'id'?
>>> import pandas as pd
>>> df = pd.read_csv('fake_news_dataset.csv')
>>> df
                                       title                                               text  ...       category label
0                    Foreign Democrat final.  more tax development both store agreement lawy...  ...       Politics     0
1        To offer down resource great point.  probably guess western behind likely next inve...  ...       Politics     1
2               Himself church myself carry.  them identify forward present success risk sev...  ...       Business     1
3                       You unit its should.  phone which item yard Republican safe where po...  ...        Science     1
4       Billion believe employee summer how.  wonder myself fact difficult course forget exa...  ...     Technology     1
...                                      ...                                                ...  ...            ...   ...
19995                      House party born.  hit and television I change very our happy doo...  ...  Entertainment     1
19996  Though nation people maybe price box.  fear most meet rock even sea value design stan...  ...  Entertainment     0
19997        Yet exist with experience unit.  activity loss very provide eye west create wha...  ...  Entertainment     0
19998               School wide itself item.  term point general common training watch respo...  ...         Health     1
19999         Offer chair cover senior born.  remain pressure glass me six senior though nor...  ...         Health     1

  
[20000 rows x 7 columns]
>>> from sklearn.feature_extraction.text import TfidfVectorizer
>>> from sklearn.naive_bayes import MultinomialNB
>>> from sklearn.pipeline import make_pipeline
>>> model = make_pipeline(TfidfVectorizer(), MultinomialNB())
>>> model.fit(df['text'], df['label'])
Pipeline(steps=[('tfidfvectorizer', TfidfVectorizer()),
                ('multinomialnb', MultinomialNB())])
>>> 

  
  
  
  
  
  
  
  
  
  REFERENCES 
  https://www.kaggle.com/datasets/mahdimashayekhi/fake-news-detection-dataset?resource=download)
