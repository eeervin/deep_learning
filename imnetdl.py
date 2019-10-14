import urllib.request
import numpy as np
import pandas as pd
import os
import socket
from multiprocessing.dummy import Pool as ThreadPool


def name2wordid(namelist,vocab):
    iddict={}
    for name in namelist:
        iddict[name]=vocab.loc[vocab[1] == name][0].to_numpy()
    return iddict

def urlgen(iddict):
    urldict={}
    for name, wids in iddict.items():
        urls=[]
        filenames=[]
        for wid in wids:
            path='./imnet/urls/'+wid+".txt"
            if os.path.exists(path):
                with open(path,"r", encoding='utf-8') as f:
                    lines=f.readlines()
                    for line in lines:
                        urls.append(line.split('\t')[1])
                        filenames.append(line.split('\t')[0])

        urldict[name]={'url':urls,'fname':filenames}
    return urldict

def downloadone(url,fname,folderpath):
    try:
        urllib.request.urlretrieve(url,folderpath + '/' + fname + '.' + url.split('.')[-1][:-1])
        return 1
    except:
        print(fname + ' failed.')
        return 0


def downloadset(urldict,pool):
    for name, data in urldict.items():
        folderpath='./imnet/imagenet_images/'+name
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
        results = pool.starmap(downloadone, zip(data['url'], data['fname'],[folderpath for i in range(len(data['url']))]))
    return results
if __name__=='__main__':
    socket.setdefaulttimeout(1)

    namelist=['window']
    pool = ThreadPool(300)
    vocab=pd.read_csv('./imnet/words.txt', sep='\t', engine='python', header=None)
    print(vocab.head())
    iddict=name2wordid(namelist,vocab)
    print(iddict)
    del vocab
    urldict=urlgen(iddict)
    results=downloadset(urldict,pool)
    print(results)
