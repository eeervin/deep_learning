"""
Script for downloading imagenet synsets based on category name.

"""

import urllib.request
import numpy as np
import pandas as pd
import os
import socket
from multiprocessing.dummy import Pool as ThreadPool


def name2wordid(namelist,vocab):
    #Find WordNet ID from a list of names
    iddict={}
    for name in namelist:
        iddict[name]=vocab.loc[vocab[1] == name][0].to_numpy()
    return iddict

def urlgen(iddict):
    '''
    Generate URLs from IDs.
    Requires separate tabulated txt files in urlpath, with file names refering to the WordNet ID.
    The text file should have a column of file name, and url in this order.
    '''
    global urlpath
    urldict={}
    for name, wids in iddict.items():
        urls=[]
        filenames=[]
        for wid in wids:
            path=urlpath+wid+".txt"
            if os.path.exists(path):
                with open(path,"r", encoding='utf-8') as f:
                    lines=f.readlines()
                    for line in lines:
                        urls.append(line.split('\t')[1])
                        filenames.append(line.split('\t')[0])

        urldict[name]={'url':urls,'fname':filenames}
    return urldict

def downloadone(url,fname,folderpath):
    '''
    Download file from url and save it as folderpath/filename.
    '''
    try:
        urllib.request.urlretrieve(url,folderpath + '/' + fname + '.' + url.split('.')[-1][:-1])
        return 1
    except:
        #On failure remove junk data.
        if os.path.exists(folderpath + '/' + fname + '.' + url.split('.')[-1][:-1]):
            os.remove(folderpath + '/' + fname + '.' + url.split('.')[-1][:-1])
        return 0


def downloadset(urldict,pool):
    '''
    Get data from a dict of URLs using multiple workers in pool (ThreadPool).
    '''
    global imdatapath
    for name, data in urldict.items():
        #Remove commas from category names when naming folders.
        folderpath=imdatapath+name.replace(",","")
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        results = pool.starmap(downloadone, zip(data['url'], data['fname'],[folderpath for i in range(len(data['url']))]))
        success=np.sum(np.array(results))
        all=len(results)
        print("{0} images downloaded. {1} / {2} succeeded.".format(name,success,all))


#Setting global path variables
global urlpath
urlpath='./imnet/urls/'

global imdatapath
imdatapath='./imnet/'

global wordnetpath
wordnetpath='./imnet/words.txt'

if __name__=='__main__':
    #ThreadPools should be created under main guards to avoid freezing errors on my system config (Win10, Python 3.7)

    socket.setdefaulttimeout(20)

    #List of WordNet categories to download
    namelist=['songbird, songster']

    pool = ThreadPool(8)
    #Reading WordNet ID data
    vocab=pd.read_csv(wordnetpath, sep='\t', engine='python', header=None)
    #Extracting WordNet IDs
    iddict=name2wordid(namelist,vocab)
    del vocab
    #Generating URL dicts
    urldict=urlgen(iddict)
    #Downloading data
    downloadset(urldict,pool)
