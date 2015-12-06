'''
Created on Dec 1, 2015

@author: jingweigu
'''
from shanbay.api import API
import json
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET 
from time import sleep

token = '''
{
    "token_type": "Bearer", 
    "state": "PwoXRkUFNdcbeKeWSNVddLjN4beoUy", 
    "access_token": "rsrLV1WaBpzzMYsrTZAjfRJmq8oKVz", 
    "scope": [
        "read", 
        "write"
    ], 
    "expires_in": "2592000", 
    "expires_at": 1451613656.925714
}
'''

DICT_FOLDER = '/Users/jingweigu/Google Drive/sync/'


api = API('091e43d72fe4466a0433', token=json.loads(token))

def forgetAll(learning_id):
    print(api.forget(learning_id))

def loadDictFile():
    dictFiles = [ f for f in listdir(DICT_FOLDER) if isfile(join(DICT_FOLDER, f)) and f.endswith('xml') ]
    
    wordList = []
    for f in dictFiles:
        tree = ET.parse(join(DICT_FOLDER, f))
        root = tree.getroot()
        for item in root.findall('item'):
            word = item.find('word').text
            progress = int(item.find('progress').text)
            if progress < 5:
                wordList.append(word)
    return wordList

def main():
    
    # TBD:
    # support youdao words import 
    #  read from txt/excel file. do not add duplicate words 
    #  adding the word to shanbay, before that check, check if this word is already in shanbay 
    #  
    
    wordList = loadDictFile()
    
    # getting the word id 
    for word in wordList:
        result = api.word(word)
                
        if not result['msg'] == 'SUCCESS':
            continue
                
        if 'learning_id' in result['data']:
            print('already learned ', result['data']['learning_id'])
            continue
        
        
        sleep(2)
        
        wid = result['data']['id']
        result = api.add_word(wid)
        
        print(result)
        
    
        if result['msg'] == 'SUCCESS':
            print("add",  word)
        else:
            print('error in adding ', word)
        
        return
    
    # adding words by id 
    
    
    


if __name__ == '__main__':
    main()