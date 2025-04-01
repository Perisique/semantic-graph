import os
import pandas as pd

def load_data(path):
    """Загружает данные из файла или директории"""
    data_frames = []
    
    if os.path.isfile(path):
        if path.endswith('.csv'):
            df = pd.read_csv(path, usecols=['text', 'date', 'type'])
            df['public_id'] = os.path.basename(path)
            data_frames.append(df.dropna())
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith('.csv'):
                file_path = os.path.join(path, filename)
                df = pd.read_csv(file_path, usecols=['text', 'date', 'type'])
                df['public_id'] = filename
                data_frames.append(df.dropna())
    else:
        raise ValueError(f"{path} не является файлом или директорией.")
    
    return pd.concat(data_frames, ignore_index=True) if data_frames else pd.DataFrame()