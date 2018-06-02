# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:21:29 2018

@author: Mallikarjun
"""

from keras.preprocessing.text import one_hot
from keras.preprocessing.text import text_to_word_sequence
import numpy
import pandas
import csv

# =============================================================================
# dataframe1 = pandas.read_csv(r"C:\Users\DST_AI\Desktop\Test_Data/test_and_diagnosis_output.csv", delimiter=",")
# datasetIn = dataframe1.values
# print(datasetIn)
# 
# =============================================================================


infile1=r"C:\Users\DST_AI\Desktop\Test_Data/CNInput.csv"
outfile1=open(r"C:\Users\DST_AI\Desktop\Test_Data/CNInputEncoded.csv",'w')
with open(infile1) as fo:
    for text in fo:
        words = set(text_to_word_sequence(text))
        vocab_size = len(words)
        result = one_hot(text, round(vocab_size*0.8))
        writer = csv.writer(outfile1, lineterminator='\n')
        writer.writerow(result)
        
        

outfile1.close()
