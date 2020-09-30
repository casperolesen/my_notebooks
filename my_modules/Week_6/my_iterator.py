import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass

class MyIterator():
    def __init__(self, url_list):
        self.url_list = url_list
    
    def download(self, url, filename):
        r = requests.get(url)

        if r.status_code == 404:
            raise NotFoundException

        with open(r'downloads/temp/books/{}.txt'.format(filename), 'w') as file_object:
            file_object.write(r.text)
        
        return r.status_code

    def multi_download(self):
        self.filenames = ['file1', 'file2', 'file3']
        with ThreadPoolExecutor() as ex:
            res = ex.map(self.download, self.url_list, self.filenames)
            return list(res)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.filenames):
            res = self.filenames[self.index]
            self.index += 1
            return res

        raise StopIteration

    def urllist_generator(self):
        num = 0
        while num < len(self.url_list):
            yield self.url_list[num]
            num += 1

    def avg_vowels(self, text):
        words_count = 0
        vowels_count = 0
        for line in self._read_linewise(text): #filename - not path or text
            #count words
            words = line.split()
            words_count += len(words)
            
            #count vowels
            for word in words:
                for char in word:
                    if char.lower() in 'aeiou':
                        vowels_count += 1
            
        return words_count, vowels_count, vowels_count / words_count

    def hardest_read():
        pass

    def _read_linewise(self, filename):
        with open(r'downloads/temp/books/{}.txt'.format(filename)) as fp:
            for line in fp:
                yield line