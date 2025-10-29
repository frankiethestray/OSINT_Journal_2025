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
>>> 
