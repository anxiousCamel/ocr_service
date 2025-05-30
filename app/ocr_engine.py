"""
@file ocr_engine.py
@brief Funções de OCR usando pytesseract.
@details
    - Recebe imagem PIL
    - Retorna texto extraído (serial)
    - Usa config centralizada
"""

import pytesseract
from PIL import Image
from .config import TESSERACT_CONFIG

def extrai_serial(image: Image.Image) -> str:
    """
    Executa OCR na imagem e retorna o texto extraído.
    @param image: Objeto PIL.Image.Image
    @return: String do serial extraído
    """
    return pytesseract.image_to_string(image, config=TESSERACT_CONFIG).strip()
