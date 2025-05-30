"""
@file main.py
@brief Microserviço HTTP para OCR usando Flask.
@details
    - Expõe endpoint POST /ocr: recebe imagem, retorna serial extraído (texto puro)
    - Usa cache em memória para acelerar requisições repetidas
    - Parâmetros principais são definidos em config.py
    - Pronto para integração com qualquer linguagem moderna via HTTP

    ## Exemplos de Consumo

    ### cURL (Linux/Terminal)
    curl -F "file=@/caminho/para/imagem.jpg" http://localhost:5000/ocr

    ### Python (requests)
    import requests
    with open("imagem.jpg", "rb") as f:
        resp = requests.post("http://localhost:5000/ocr", files={"file": f})
    print(resp.text)
"""

from flask import Flask, request, Response
from PIL import Image
import io
import logging
import time

from .ocr_engine import extrai_serial
from .cache import ocr_cache
from .config import SERVER_HOST, SERVER_PORT
from .utils import extensao_permitida, tamanho_permitido

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def erro(msg: str, status: int = 400) -> Response:
    """
    @brief Retorna uma resposta de erro padronizada.
    @param msg: Mensagem de erro a ser retornada.
    @param status: Código HTTP do erro.
    @return: Response HTTP Flask.
    """
    return Response(msg, status=status, mimetype="text/plain; charset=utf-8")

@app.route("/ocr", methods=["POST"])
def ocr():
    """
    @brief Endpoint principal para OCR.
    @details
        - Recebe imagem via campo 'file' (multipart/form-data)
        - Valida extensão e tamanho da imagem
        - Usa cache para acelerar resultados repetidos
        - Retorna texto extraído (serial) em text/plain

    @returns 200 text/plain: Serial/texto extraído da imagem enviada
    @returns 400 text/plain: Se arquivo não enviado
    @returns 413 text/plain: Se arquivo for muito grande
    @returns 422 text/plain: Se extensão não for permitida
    @returns 500 text/plain: Em caso de erro interno no processamento

    ## Exemplo de request:
        POST /ocr
        Content-Type: multipart/form-data
        campo: file (imagem)
    """
    inicio = time.time()

    file = request.files.get("file")
    if file is None:
        return erro("Arquivo não enviado", status=400)

    if not file.filename or not extensao_permitida(file.filename):
        return erro("Formato de arquivo não permitido", status=422)

    image_bytes = file.read()
    if not tamanho_permitido(len(image_bytes)):
        return erro("Arquivo muito grande", status=413)

    serial = ocr_cache.get(image_bytes)
    if serial is not None:
        logging.info(f"Cache hit para {file.filename} em {round((time.time() - inicio)*1000)} ms")
        return Response(serial, mimetype="text/plain; charset=utf-8")

    try:
        with Image.open(io.BytesIO(image_bytes)) as image:
            serial = extrai_serial(image)
        ocr_cache.set(image_bytes, serial)
        logging.info(f"OCR executado para {file.filename} em {round((time.time() - inicio)*1000)} ms")
        return Response(serial, mimetype="text/plain; charset=utf-8")
    except Exception:
        logging.exception("Erro ao processar imagem")
        return erro("Erro ao processar imagem", status=500)

@app.route("/health", methods=["GET"])
def health():
    """
    @brief Endpoint simples para healthcheck.
    @details
        - Retorna "OK" caso o serviço esteja ativo.

    @returns 200 text/plain: "OK"
    """
    return Response("OK", mimetype="text/plain; charset=utf-8")

if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT)
