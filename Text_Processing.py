Python
                                                                                                                                                                                           
                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ NLTK --version
NLTK: command not found
                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ nltk --version
nltk, version 3.9.1
                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ # nltk already installed
                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ # switching to Python interpreter
                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ python
Python 3.13.7 (main, Aug 20 2025, 22:17:40) [GCC 14.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> #importing nltk libraries
>>> import nltk
>>> # download 'punkt' algorithm for tokenization
>>> # nltk.download (
>>> nltk.download ('punkt')
[nltk_data] Downloading package punkt to /home/kali/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
True
>>> # 'punkt' downloaded
>>> text = ('Canada must condemn US aggression against Venezuela. Deploying warships & threatening violence under the false pretext of a "war on drugs" is a disgrace. We cannot be compli\
cit in this imperialism. #cdnpoli #Venezuela') # assigning text data to a variable 'text'
>>> tokens = nltk.word_tokenize(text) # using method word_tokenize to activate tokenization and sending to variable 'tokens'
>>> print (tokens) #printing output
['Canada', 'must', 'condemn', 'US', 'aggression', 'against', 'Venezuela', '.', 'Deploying', 'warships', '&', 'threatening', 'violence', 'under', 'the', 'false', 'pretext', 'of', 'a', '``', 'war', 'on', 'drugs', "''", 'is', 'a', 'disgrace', '.', 'We', 'can', 'not', 'be', 'complicit', 'in', 'this', 'imperialism', '.', '#', 'cdnpoli', '#', 'Venezuela']
>>> 
KeyboardInterrupt
>>> lower_text = text.lower()
>>> print lower_text # will make all letters of the list lower case
  File "<python-input-10>", line 1
    print lower_text # will make all letters of the list lower case
    ^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(lower_text) # will make all letters of the list lower case
canada must condemn us aggression against venezuela. deploying warships & threatening violence under the false pretext of a "war on drugs" is a disgrace. we cannot be complicit in this imperialism. #cdnpoli #venezuela
>>> from nltk.corpus import stopwords # will import stopwards from nltk to delete stopwords
>>> nltk.download('stopwords')
[nltk_data] Downloading package stopwords to /home/kali/nltk_data...
[nltk_data]   Unzipping corpora/stopwords.zip.
True
>>> stop_words = set(stopwords.words('english'))
>>> filtered_tokens_stop = [word for word in tokens if word not in stop_word]
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    filtered_tokens_stop = [word for word in tokens if word not in stop_word]
                                                                   ^^^^^^^^^
NameError: name 'stop_word' is not defined. Did you mean: 'stop_words'?
>>> filtered_tokens_stop = [word for word in tokens if word not in stop_words] # will filter using stopwords
>>> print (filtered_tokens_stop)
['Canada', 'must', 'condemn', 'US', 'aggression', 'Venezuela', '.', 'Deploying', 'warships', '&', 'threatening', 'violence', 'false', 'pretext', '``', 'war', 'drugs', "''", 'disgrace', '.', 'We', 'complicit', 'imperialism', '.', '#', 'cdnpoli', '#', 'Venezuela']
>>> import string
>>> # removing punctuation
>>> filtered_tokens_stop = [token for token in tokens if token not in string.punctuation]
>>> print('filtered_tokens_stop')
filtered_tokens_stop
>>> print(filtered_tokens_stop)
['Canada', 'must', 'condemn', 'US', 'aggression', 'against', 'Venezuela', 'Deploying', 'warships', 'threatening', 'violence', 'under', 'the', 'false', 'pretext', 'of', 'a', '``', 'war', 'on', 'drugs', "''", 'is', 'a', 'disgrace', 'We', 'can', 'not', 'be', 'complicit', 'in', 'this', 'imperialism', 'cdnpoli', 'Venezuela']
>>> #lemmatization to reduce to root form
>>> nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /home/kali/nltk_data...
True
>>> from nltk.stem import WordNetLemmatizer
>>> lemmatizer = WordNetLemmatizer()
>>> lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens_stop]
>>> print(lemmatized_tokens)
['Canada', 'must', 'condemn', 'US', 'aggression', 'against', 'Venezuela', 'Deploying', 'warship', 'threatening', 'violence', 'under', 'the', 'false', 'pretext', 'of', 'a', '``', 'war', 'on', 'drug', "''", 'is', 'a', 'disgrace', 'We', 'can', 'not', 'be', 'complicit', 'in', 'this', 'imperialism', 'cdnpoli', 'Venezuela']
>>> # remove white space
>>> clean_text = ' '.join(lemmatized_tokens())
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    clean_text = ' '.join(lemmatized_tokens())
                          ~~~~~~~~~~~~~~~~~^^
TypeError: 'list' object is not callable
>>> clean_text = ' '.join(lemmatized_tokens.split())
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    clean_text = ' '.join(lemmatized_tokens.split())
                          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'split'
>>> # object 'lemmatized_tokens' is already a list with no whitespace
>>> clean_text = ' '.join(lemmatized_tokens.split())
Traceback (most recent call last):
  File "<python-input-33>", line 1, in <module>
    clean_text = ' '.join(lemmatized_tokens.split())
                          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'split'
>>> print(lemmatized_tokens)
['Canada', 'must', 'condemn', 'US', 'aggression', 'against', 'Venezuela', 'Deploying', 'warship', 'threatening', 'violence', 'under', 'the', 'false', 'pretext', 'of', 'a', '``', 'war', 'on', 'drug', "''", 'is', 'a', 'disgrace', 'We', 'can', 'not', 'be', 'complicit', 'in', 'this', 'imperialism', 'cdnpoli', 'Venezuela']
>>> #Results above
>>> 
