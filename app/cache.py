"""
@file cache.py
@brief Implementação simples de cache em memória para resultados de OCR.
@details
    - Usa um dicionário para mapear hash da imagem para o texto extraído.
    - Evita reprocessar imagens idênticas.
    - Não persistente (reset ao reiniciar o serviço).
"""

import hashlib

class OcrCache:
    def __init__(self):
        """Inicializa o cache como um dicionário."""
        self._cache = {}

    def _hash_image(self, image_bytes):
        """
        Calcula o hash SHA256 dos bytes da imagem.
        @param image_bytes: bytes
        @return: str (hash)
        """
        return hashlib.sha256(image_bytes).hexdigest()

    def get(self, image_bytes):
        """
        Tenta recuperar o resultado do cache.
        @param image_bytes: bytes
        @return: str | None
        """
        key = self._hash_image(image_bytes)
        return self._cache.get(key)

    def set(self, image_bytes, text):
        """
        Salva o resultado do OCR no cache.
        @param image_bytes: bytes
        @param text: str
        """
        key = self._hash_image(image_bytes)
        self._cache[key] = text

# Instância global para ser usada no app
ocr_cache = OcrCache()
