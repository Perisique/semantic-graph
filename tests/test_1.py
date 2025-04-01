import pytest
from semantic_graph.text_processing import clean_text

def test_clean_text():
    assert clean_text("Пример #текста с [ссылкой] и спецсимволами!") == "пример текста с ссылкой и спецсимволами"