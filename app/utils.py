"""
@file utils.py
@brief Funções utilitárias para validação e manipulação de imagens.
@details
    - Validação de extensão
    - Validação de tamanho
"""

from .config import ALLOWED_EXTENSIONS, MAX_IMAGE_SIZE

def extensao_permitida(nome_arquivo: str) -> bool:
    """
    @brief Verifica se a extensão do arquivo é permitida.
    @param nome_arquivo: Nome do arquivo (str)
    @return: True se permitido, False caso contrário
    """
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def tamanho_permitido(tamanho_bytes: int) -> bool:
    """
    @brief Verifica se o tamanho do arquivo está dentro do limite.
    @param tamanho_bytes: Tamanho em bytes (int)
    @return: True se permitido, False caso contrário
    """
    return tamanho_bytes <= MAX_IMAGE_SIZE
