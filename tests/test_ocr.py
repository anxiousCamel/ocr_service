"""
@file test_ocr.py
@brief Testes automatizados para o OCR engine e utilitários.
"""

import pytest
from PIL import Image
import io
from app.ocr_engine import extrai_serial
from app.utils import extensao_permitida, tamanho_permitido
from app.config import MAX_IMAGE_SIZE

def test_extensao_permitida():
    assert extensao_permitida("teste.png") is True
    assert extensao_permitida("foto.jpg") is True
    assert extensao_permitida("arquivo.bmp") is True
    assert extensao_permitida("documento.pdf") is False
    assert extensao_permitida("semextensao") is False

def test_tamanho_permitido():
    assert tamanho_permitido(100) is True
    assert tamanho_permitido(MAX_IMAGE_SIZE) is True
    assert tamanho_permitido(MAX_IMAGE_SIZE + 1) is False

def test_extrai_serial_simples():
    # Cria uma imagem branca simples (OCR não vai achar nada, mas testa funcionamento)
    img = Image.new('RGB', (100, 40), color = (255,255,255))
    texto = extrai_serial(img)
    assert isinstance(texto, str)  # Deve sempre retornar string
    # Pode não retornar texto, pois a imagem é branca (esperado)

# Para rodar:
# pytest tests/test_ocr.py
