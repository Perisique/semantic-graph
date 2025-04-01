from sem_graph import load_data, clean_dataframe, normalize_text, extract_ngrams, filter_ngram, print_status, remove_stopwords

directory = 'C:/Users/perisique/Desktop/decabristov'
df = load_data(directory)
print_status('Файл загружен')

df = clean_dataframe(df, 'text')
print_status('Файл очищен')

df['clean_text'] = df['clean_text'].apply(remove_stopwords)
df = normalize_text(df, 'clean_text', 'norm')
print_status('Файл нормализован')

df.to_parquet('df_normalized.parquet')
ngram_df = extract_ngrams(df, 'norm', ['город', 'улица'])
df, ngram_df = filter_ngram(df)

df.to_parquet('df_with_ngrams.parquet')
ngram_df.to_parquet('ngrams.parquet')
