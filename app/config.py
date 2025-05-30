"""
@file config.py
@brief Configurações do microserviço OCR.
@details
    - Parâmetros de OCR/Tesseract
    - Outras configs do app (porta, limites, etc)
"""

# Porta padrão para rodar o Flask
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000

# Configuração padrão do Tesseract para buscar seriais (apenas letras e números)
TESSERACT_CONFIG = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Limite de tamanho da imagem (bytes), ex: 5MB
MAX_IMAGE_SIZE = 5 * 1024 * 1024

# Formatos aceitos de imagem
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "tiff"}

# Outros parâmetros futuros podem ser adicionados aqui
