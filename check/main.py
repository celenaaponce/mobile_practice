# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:49:41 2018

@author: rcabg
"""

import sys
from spanish_word_freq import SpanishWordFreq
from word_chekcer import WordChecker

def main(word):

    filePath = "10000_frecuencias.txt"

    spanishWords = SpanishWordFreq(filePath)
    
    wordChecker = WordChecker(spanishWords.words, spanishWords.totalFreq)
    
    # print("Spanish Spelling Checker")
    # print("Please write 'q' or 'quitprogram' in order to exit")
    
    # while(1):
        # word = input("Write a Spanish word to be checked: ")

        
    list = wordChecker.getCorrection(word.lower())
    return list
if __name__ == "__main__":
    main(sys.argv[1:])