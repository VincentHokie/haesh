import os
import random

RANGE_MIN = 1
RANGE_MAX = 1000


class HaeshKeyGenerator(object):

    def __init__(self, file_path, text):
        self._file_path = file_path
        self._text = text

    def get_text_signature_key(self):
        file_size = self._get_file_size_int_signature()
        mod_time = self._get_file_modification_time_int_signature()
        file_header = self._get_file_header_int_signature() 
        key = f'{file_size}{mod_time}{file_header}'
        return key.encode(encoding = 'UTF-8')

    def get_file_signature_key(self):
        file_size = self._get_file_size_int_signature()
        mod_time = self._get_file_modification_time_int_signature()
        file_header = self._get_file_header_int_signature() 
        key = f'{file_size}{mod_time}{file_header}'
        return key.encode(encoding = 'UTF-8')

    def _get_file_size_int_signature(self):
        size = os.path.getsize(self._file_path)
        random.seed(size)
        random_int = random.randint(RANGE_MIN, RANGE_MAX)
        return f'{random_int:04}'

    def _get_file_modification_time_int_signature(self):
        time = os.path.getmtime(self._file_path)
        random.seed(time)
        random_int = random.randint(RANGE_MIN, RANGE_MAX)
        return f'{random_int:04}'
    
    def _get_file_header_int_signature(self):
        time = os.path.getmtime(self._file_path)
        random.seed(time)
        random_int = random.randint(RANGE_MIN, RANGE_MAX)
        return f'{0:08}'
