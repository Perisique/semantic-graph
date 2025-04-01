import re
import pymorphy3
from nltk.corpus import stopwords

LINK_PATTERN = r'https?://\S+|www\.\S+|http?://\S+'
russian_stopwords = stopwords.words("russian")

def clean_text(text):
    """Очищает текст от ссылок и спецсимволов"""
    if not isinstance(text, str):
        return ''
    
    text = re.sub(LINK_PATTERN, ' ', text)
    text = re.sub(r'\[id\d+\|[^\]]*\]', ' ', text)
    text = re.sub(r'\[club\d+\|[^\]]*\]', ' ', text)
    text = re.sub(r'#[^\s]+', ' ', text)
    text = re.sub(r'[^а-яА-ЯёЁ0-9]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    
    return text

def remove_stopwords(text):
    """Удаляет стоп-слова из текста"""
    words = text.split()
    return " ".join(word for word in words if word not in russian_stopwords)

def clean_dataframe(df, text_column):
    """Очищает датафрейм, удаляя дубликаты и очищая текст"""
    df = df.drop_duplicates(subset=[text_column])
    df.loc[:, 'clean_text'] = df[text_column].apply(clean_text)
    return df

def normalize_text(df, text_column, norm_column):
    """Нормализует текст с помощью pymorphy3"""
    morph = pymorphy3.MorphAnalyzer()
    df[norm_column] = df[text_column].apply(
        lambda text: ' '.join(morph.parse(word)[0].normal_form for word in text.split())
    )
    df = df[df[norm_column].str.strip() != '']
    return df
