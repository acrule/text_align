# Text Alignment
April 2, 2019
Adam Rule

This folder contains functions to align two strings of text and calculate the redundancy, or overlap, between them. There a many methods to align sequences of text, but this library uses the modified Levenshtein distance algorithm proposed by [Wrenn et al.](https://www.ncbi.nlm.nih.gov/pubmed/20064801) to do so. More information on how Levenshtein distance is calculated can be found on [Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance). Other methods for calculating local or global string alignment follow a very similar method, though with different weights for the scoring and traceback algorithms.

## NLTK Dependency
Currently this library depends on the Natural Language ToolKit (nltk) to tokenize the input strings, that is, to split them into words. You will need to download the nltk Python library to run this code. The first time you use nltk, it may ask you to download the nltk dataset which supports other natural language processes such as stemming words, removing stop words, and classifying part of speech. The code can be modified to tokenize words without requiring nltk (e.g. using str.split('')) but this method may be less robust than using nltk.

## Running the files
In Python, one of the easiest ways to run this code is to install the library from a local directory using pip. You will want to direct pip to the folder containing setup.py:
```
pip install /path/to/text_align

import text_align

a = "Here is some text to align"
b = "Here is other text to align as well"
redundancy = seq_align.calculate_redundancy(a, b)
```
