#We will first convert the sentence into lowercase and remove punctuation so that similar words are treated the same.
#Then we will split it into words and use a dictionary to count the occurrence of each word.

import pandas as pd 
import re
import collections

word = "Data engineering is fun, and data engineering builds strong data foundations!"
word1 = word.lower()
cleaned_str = re.sub(r'[^a-zA-Z0-9 ]', '', word1)
words = cleaned_str.split()
total_words = collections.Counter(words)
print(total_words)
