# Dockerfile para microserviço OCR
FROM python:3.11-slim

# Instala Tesseract e dependências do Pillow
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtiff5 libjpeg62-turbo libopenjp2-7 libpng16-16 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia arquivos do projeto
WORKDIR /app
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta padrão
EXPOSE 5000

# Comando padrão: inicia o serviço Flask
CMD ["python", "-m", "app.main"]
