from .base_loader import BaseLoader
from numpy import loadtxt, np
from numpy import numarray


class CsvLoader(BaseLoader):

    def __init__(self, file):
        super().__init__(file)
        self.file = file

