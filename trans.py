# -*- coding: utf-8 -*-

import os, fileinput

def transliterate(string):
    georgian_dictionary = {
        u'ა': u'ɑ',
        u'ბ': u'b',
        u'გ': u'g',
        u'დ': u'd',
        u'ე': u'ɛ',
        u'ვ': u'v',
        u'ზ': u'z',
        u'თ': u'tʰ',
        u'ი': u'ɪ',
        u'კ': u'k\'',
        u'ლ': u'l',
        u'მ': u'm',
        u'ნ': u'n',
        u'ო': u'ɔ',
        u'პ': u'p\'',
        u'ჟ': u'ʒ',
        u'რ': u'r',
        u'ს': u's',
        u'ტ': u't\'',
        u'ჳ': u'wi',
        u'უ': u'u',
        u'უ': u'u',
        u'ფ': u'pʰ',
        u'ქ': u'kʰ',
        u'ღ': u'ʁ',
        u'ყ': u'q\'',
        u'შ': u'ʃ',
        u'ჩ': u'tʃ',
        u'ც': u'ts',
        u'ძ': u'dz',
        u'წ': u'tsʼ',
        u'ჭ': u'tʃʼ',
        u'ხ': u'χ',
        u'ჴ': u'q',
        u'ჯ': u'dʒ',
        u'ჰ': u'h',}

    for i, j in georgian_dictionary.items():
        string = string.replace(i, j)
    return string

#### 

with fileinput.FileInput('georgia.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(transliterate(line), end='')
