from collections import Counter
from nltk import ngrams
from tqdm import tqdm
import pandas as pd

def extract_ngrams(df, text_column, target_words, min_frequency=3, max_ngram_length=6):
    """Извлекает n-граммы из текста"""
    target_words_set = set(target_words)
    ngram_freq = Counter()
    
    for text in tqdm(df[text_column], desc="Извлечение n-грамм"):
        tokens = text.split()
        for n in range(2, max_ngram_length + 1):
            for ngram in ngrams(tokens, n):
                ngram_str = ' '.join(ngram)
                if set(ngram).intersection(target_words_set):
                    ngram_freq[ngram_str] += 1
    
    filtered_ngrams = {ngram: freq for ngram, freq in ngram_freq.items() if freq >= min_frequency}
    return pd.DataFrame(filtered_ngrams.items(), columns=['Ngram', 'Frequency'])

def filter_ngram(df):
    """Фильтрует повторяющиеся n-граммы"""
    df['ngram'] = df['ngram'].apply(lambda x: sorted(set(x), key=len, reverse=True))
    all_ngrams = sum(df['ngram'].tolist(), [])
    counter = Counter(all_ngrams)
    return pd.DataFrame(counter.items(), columns=['Ngram', 'Frequency'])
