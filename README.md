```markdown
# Microserviço OCR Local

Microserviço universal de OCR: recebe uma imagem, retorna o texto do serial.  
Consuma via HTTP usando qualquer linguagem (Python, JS, C#, Java, Shell etc).
---

## ⚡ Como funciona

- **POST** sua imagem para `http://localhost:5000/ocr`
- Recebe o serial/texto como resposta (text/plain)
- Pode rodar local/offline

---

## 🚀 Instalação rápida

### 1. Pré-requisitos

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado

No Ubuntu/Debian/Mint:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

---

### 2. Instalação do serviço

```bash
git clone <repo-url>
cd ocr_service
pip install -r requirements.txt
```

---

### 3. Rodando localmente

```bash
python -m app.main
```
O serviço sobe na porta 5000.

---

### 4. Usando com Docker

```bash
docker build -t ocr_service .
docker run -p 5000:5000 ocr_service
```

---

## 🛠️ Como consumir (Exemplo cURL)

```bash
curl -F "file=@/caminho/para/imagem.jpg" http://localhost:5000/ocr
```

---

## 📁 Estrutura de Pastas

```
ocr_service/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ocr_engine.py
│   ├── cache.py
│   ├── utils.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   └── test_ocr.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Testes

Para rodar os testes automatizados:

```bash
pytest tests/test_ocr.py
```

---

## 📋 Notas

- Serviço **100% local**, não depende de cloud.
- **Qualquer linguagem** que consome HTTP pode usar.
- Se quiser cache **persistente**, troque a implementação do cache por Redis ou outro backend.
- **Não exponha para internet sem autenticação**. Use apenas para ambiente interno/local.

---

## 📢 Suporte

Dúvidas ou sugestões? Abra uma Issue ou Pull Request.
```