"""
@file ocr_engine.py
@brief Funções de OCR usando pytesseract.
@details
    - Recebe imagem PIL
    - Retorna TODO o texto extraído
    - Usa config centralizada
"""

from PIL import Image, ImageEnhance, ImageOps
import pytesseract
from .config import TESSERACT_CONFIG

def preprocess_image(image: Image.Image) -> Image.Image:
    """
    @brief Pré-processa uma imagem para OCR.
    @details
        - Converte a imagem para escala de cinza.
        - Aplica autocontraste para realce de detalhes.
        - Aumenta o contraste geral para melhorar a leitura do OCR.
    @param image Imagem PIL.Image original.
    @return Imagem PIL.Image pré-processada para OCR.
    """
    image = image.convert('L')
    image = ImageOps.autocontrast(image)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    return image

def extrai_serial(image: Image.Image) -> str:
    """
    @brief Executa OCR na imagem pré-processada e retorna o texto extraído.
    @details
        - Usa a configuração centralizada TESSERACT_CONFIG.
        - Remove espaços e quebras de linha no início/fim do texto.
    @param image Imagem PIL.Image a ser processada.
    @return String com TODO o texto extraído da imagem.
    """
    img_pre = preprocess_image(image)
    texto = pytesseract.image_to_string(img_pre, config=TESSERACT_CONFIG)
    return texto.strip()
