import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from tqdm import tqdm

class NotFoundException(Exception):
    pass

class MyIterator():
    def __init__(self, url_list):
        self.url_list = url_list
    
    def download(self, url, filename):
        r = requests.get(url)

        if r.status_code == 404:
            raise NotFoundException

        with open(r'downloads/temp/books/{}'.format(filename), 'w') as file_object:
            file_object.write(r.text)
        
        return r.status_code

    def multi_download(self):
        # get last part of path in url
        self.filenames = [urlparse(url).path.split('/')[-1] for url in self.url_list]
        #self.filenames = ['file1', 'file2', 'file3']
        with ThreadPoolExecutor() as ex:
            #res = ex.map(self.download, self.url_list, self.filenames)
            res = tqdm(ex.map(self.download, self.url_list, self.filenames), total=len(self.url_list))
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
            
        #return words_count, vowels_count, vowels_count / words_count
        return text, vowels_count / words_count

    def hardest_read(self, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            #res = ex.map(self.avg_vowels, self.filenames)
            res = tqdm(ex.map(self.avg_vowels, self.filenames), total=len(self.filenames))

        res = list(res) # results from multiprocessing
        names, vowels = zip(*res) # unzipping res of tuples into two lists
        hardest_value = max(vowels) # find highest value in vowels list
        answer = [item for item in res if hardest_value in item] # find the item in the list of tuple with hardest_value (returns a list)
        return answer

    def _read_linewise(self, filename):
        with open(r'downloads/temp/books/{}'.format(filename)) as fp:
            for line in fp:
                yield line