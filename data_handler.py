import os
import subprocess
import gzip
import numpy as np
import struct

class data_handler(object):
    """
    downloads mnist data into pandas dataframe or numpy array
    """
    
    def __init__(self):
        self.url = 'http://yann.lecun.com/exdb/mnist/'
        self.files = [
            'train-images-idx3-ubyte.gz',
            'train-labels-idx1-ubyte.gz',
            't10k-images-idx3-ubyte.gz',
            't10k-labels-idx1-ubyte.gz'
        ]
        self.data = {}
    
    
    def download(self, folder_name = 'data'):
        '''
            downloads mnist data
        '''
        if not os.path.exists(self.dir): os.mkdir(self.dir)
        self.opaths = []
        for file in self.files:
            file_link = f'{self.url}{file}'
            opath = os.path.join(self.dir,file)
            opaths.append(opath)
            if not os.path.exists(opath):
                cmd = ['curl',file_link,'-o',opath]
                print(f'Downloading file: {file}')
                subprocess.check_call(cmd)
    
    def download_to_np(self, folder_name = 'data'):
        '''
            downloads dataset and returns a numpy array
            returns:
                dictionary with key as 'X_train', 'y_train', 'X_test', 'y_test' 
                and their values as the images and labels
        '''
        if not os.path.exists(folder_name): self.download(folder_name)
        self.file_links = [ folder_name + '/' + x for x in self.files ]
        
        for file in self.file_links:
            print(f'Converting: {file}')
            key = self.__get_key(file)
            with gzip.open(file, 'rb') as gz:
                magic, size = struct.unpack('>II', gz.read(8))
                if 'X' in key:
                    n_rows, n_cols = struct.unpack('>II', gz.read(8))
                    buf = gz.read(28 * 28 * size) # image size = 28 * 28 * 1 [BW]
                else:
                    buf = gz.read(size)
                data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
                data = self.__reshape_and_return(data, key, size)
                
            self.data[key] = data
        
        return self.data
    
    def __get_key(self, file):
        if '10k' in file:
            if 'images' in file:
                key = 'X_test'
            if 'labels' in file:
                key = 'y_test' 
        elif 'train' in file:
            if 'images' in file:
                key = 'X_train'
            if 'labels' in file:
                key = 'y_train' 
        
        return key
    
    def __reshape_and_return(self, data, key, size):
        if 'X' in key:
            return data.reshape(size, 28, 28, 1)
        else:
            return data.reshape(size)
                