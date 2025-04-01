"""
Python package for extracting data from Social Media and creating a semantic graph.
"""
import importlib.metadata

__version__ = importlib.metadata.version("sem_graph")
__author__ = "Igor K"
__email__ = "igor773012@gmail.com"
__credits__ = []
__license__ = "BSD-3"

from .data_loader import load_data
from .text_processing import clean_text, clean_dataframe, normalize_text, remove_stopwords
from .ngram_extractor import extract_ngrams, filter_ngram
from .utils import print_status
__all__ = [
    'load_data', 'clean_text', 'clean_dataframe', 'normalize_text', 
    'remove_stopwords', 'extract_ngrams', 'filter_ngram'
]
