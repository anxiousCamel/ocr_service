# 🧠 Microserviço OCR Local (Universal HTTP OCR)

Um microserviço simples, rápido e reutilizável que transforma imagens em texto usando Tesseract OCR — via uma API HTTP que qualquer linguagem pode consumir.

📸 → POST imagem → 🎯 texto extraído (serial, etiqueta, patrimônio, etc)

---

## 💡 Por que usar?

- ✅ **Universal**: acessível por qualquer linguagem (Python, JS, C#, Java, Flutter, Shell, etc.)
- ✅ **Offline/local**: sem dependência de nuvem, ideal para ambientes internos ou restritos
- ✅ **Pronto pra produção**: com cache em memória, tratamento de erros, validações e logs
- ✅ **Portável**: roda em Docker, VM, bare metal ou direto na sua máquina

---

## ⚙️ Como funciona

1. Envie uma imagem via POST para o endpoint:
```

POST [http://localhost:5000/ocr](http://localhost:5000/ocr)
Content-Type: multipart/form-data
Campo: file

````

2. Receba o texto extraído (serial) em resposta `text/plain`

---

## 🚀 Instalação rápida

### 1. Pré-requisitos

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

Instalação no Ubuntu/Debian/Mint:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
````

---

### 2. Clonar e instalar

```bash
git clone <repo-url>
cd ocr_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Rodar localmente

```bash
python -m app.main
```

> O serviço estará acessível em: `http://localhost:5000/ocr`

---

### 4. Rodar com Docker

```bash
docker build -t ocr_service .
docker run -p 5000:5000 ocr_service
```

---

## 🛠️ Exemplos de Consumo

### ✅ **cURL**

```bash
curl -F "file=@imagem.jpg" http://localhost:5000/ocr
```

---

### 🐍 **Python (requests)**

```python
import requests
with open("imagem.jpg", "rb") as f:
    resp = requests.post("http://localhost:5000/ocr", files={"file": f})
print(resp.text)
```

---

### 💻 **C++ (libcurl)**

```cpp
#include <curl/curl.h>

int main() {
    CURL *curl = curl_easy_init();
    curl_mime *form = curl_mime_init(curl);
    curl_mimepart *field = curl_mime_addpart(form);
    curl_mime_name(field, "file");
    curl_mime_filedata(field, "imagem.jpg");

    curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/ocr");
    curl_easy_setopt(curl, CURLOPT_MIMEPOST, form);
    curl_easy_perform(curl);
    curl_mime_free(form);
    curl_easy_cleanup(curl);
    return 0;
}
```

---

### 📟 **C (libcurl)**

```c
#include <curl/curl.h>

int main() {
    CURL *curl = curl_easy_init();
    struct curl_httppost *form = NULL;
    curl_formadd(&form, &form, CURLFORM_COPYNAME, "file", CURLFORM_FILE, "imagem.jpg", CURLFORM_END);
    curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/ocr");
    curl_easy_setopt(curl, CURLOPT_HTTPPOST, form);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    curl_formfree(form);
    return 0;
}
```

---

### ☕ **Java (OkHttp)**

```java
import okhttp3.*;

import java.io.File;
import java.io.IOException;

public class OcrOkHttpClient {
    public static void main(String[] args) throws IOException {
        OkHttpClient client = new OkHttpClient();
        RequestBody formBody = new MultipartBody.Builder()
            .setType(MultipartBody.FORM)
            .addFormDataPart("file", "imagem.jpg",
                RequestBody.create(new File("imagem.jpg"), MediaType.parse("image/jpeg")))
            .build();

        Request request = new Request.Builder()
            .url("http://localhost:5000/ocr")
            .post(formBody)
            .build();

        try (Response response = client.newCall(request).execute()) {
            System.out.println(response.body().string());
        }
    }
}

```

---

### 🎯 **C#**

```csharp
using System.Net.Http;

var client = new HttpClient();
var form = new MultipartFormDataContent();
form.Add(new ByteArrayContent(System.IO.File.ReadAllBytes("imagem.jpg")), "file", "imagem.jpg");
var response = await client.PostAsync("http://localhost:5000/ocr", form);
string result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);
```

---

### 🚀 **JavaScript (fetch)**

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://localhost:5000/ocr', {
  method: 'POST',
  body: formData
}).then(res => res.text()).then(console.log);
```

---

### 🐹 **Go**

```go
// Go com net/http
import (
    "net/http"
    "bytes"
    "mime/multipart"
    "os"
)

func main() {
    buf := new(bytes.Buffer)
    writer := multipart.NewWriter(buf)
    file, _ := os.Open("imagem.jpg")
    part, _ := writer.CreateFormFile("file", "imagem.jpg")
    io.Copy(part, file)
    writer.Close()

    resp, _ := http.Post("http://localhost:5000/ocr", writer.FormDataContentType(), buf)
    body, _ := io.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

---

### 📎 **Visual Basic (VBA Excel)**

```vba
Sub EnviarOCR()
    Set objHTTP = CreateObject("MSXML2.XMLHTTP")
    objHTTP.Open "POST", "http://localhost:5000/ocr", False
    objHTTP.send "file=@C:\imagem.jpg"
    MsgBox objHTTP.responseText
End Sub
```

---

### 🏛️ **Delphi/Object Pascal**

```pascal
uses IdHTTP, IdMultipartFormData;

var
  HTTP: TIdHTTP; Form: TIdMultipartFormDataStream;
begin
  HTTP := TIdHTTP.Create(nil); Form := TIdMultipartFormDataStream.Create;
  Form.AddFile('file', 'imagem.jpg');
  ShowMessage(HTTP.Post('http://localhost:5000/ocr', Form));
  Form.Free; HTTP.Free;
end;
```

---

### 💽 **SQL (MySQL com comando curl)**

```sql
SELECT sys_exec("curl -F 'file=@imagem.jpg' http://localhost:5000/ocr");
```

---

### 🧑‍🔬 **Fortran**

```fortran
call system('curl -F "file=@imagem.jpg" http://localhost:5000/ocr')
```

---

### 📊 **R**

```R
library(httr)
res <- POST("http://localhost:5000/ocr", body=list(file=upload_file("imagem.jpg")))
content(res, "text")
```

---

### 🛡️ **Ada**

```ada
-- Chamada via curl externo:
Ada.Command_Line.Execute("curl -F 'file=@imagem.jpg' http://localhost:5000/ocr");
```

---

### 🐘 **PHP**

```php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://localhost:5000/ocr");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, ["file" => new CURLFile("imagem.jpg")]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
echo curl_exec($ch);
curl_close ($ch);
```

---

### 🐪 **Perl**

```perl
use LWP::UserAgent;
my $ua = LWP::UserAgent->new();
my $response = $ua->post("http://localhost:5000/ocr", Content_Type => 'form-data', Content => [ file => ["imagem.jpg"] ]);
print $response->decoded_content;
```

---

### 📐 **MATLAB**

```matlab
url = 'http://localhost:5000/ocr';
response = webwrite(url, 'file', fopen('imagem.jpg','rb'));
disp(response);
```

### 🦀 **Rust (reqwest)**

```rust
use reqwest::blocking::multipart;
fn main() {
    let form = multipart::Form::new()
        .file("file", "imagem.jpg").unwrap();
    let resp = reqwest::blocking::Client::new()
        .post("http://localhost:5000/ocr")
        .multipart(form).send().unwrap().text().unwrap();
    println!("{}", resp);
}
```
---

### 📼 **COBOL**

```cobol
CALL 'SYSTEM' USING 'curl -F "file=@imagem.jpg" http://localhost:5000/ocr'.
```

---

### 🔧 Parâmetros disponíveis:

O arquivo `config.py` centraliza todos os parâmetros ajustáveis do microserviço.
Aqui você pode alterar a porta de escuta do servidor, as opções do Tesseract, extensões aceitas e tamanho máximo da imagem.

| Parâmetro            | Descrição                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `SERVER_HOST`        | IP onde o Flask escuta. Padrão: `"0.0.0.0"` (todas interfaces). Use `"127.0.0.1"` para acesso apenas local.        |
| `SERVER_PORT`        | Porta HTTP do serviço. Padrão: `5000`. Pode ser alterada para evitar conflitos.                                    |
| `TESSERACT_CONFIG`   | Configuração do Tesseract (modo, whitelist, etc). Padrão: apenas letras maiúsculas e números (ideal para seriais). |
| `MAX_IMAGE_SIZE`     | Tamanho máximo da imagem (em bytes). Padrão: `5 * 1024 * 1024` (5 MB). Retorna erro 413 se exceder.                |
| `ALLOWED_EXTENSIONS` | Formatos de imagem aceitos. Padrão: `{"png", "jpg", "jpeg", "bmp", "tiff"}`. Pode ser expandido ou reduzido.       |

---

### ✍️ Exemplos de personalização:

#### ✅ Permitir letras minúsculas e símbolos:

```python
TESSERACT_CONFIG = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.'
```

#### 📷 Aumentar o limite para 10 MB:

```python
MAX_IMAGE_SIZE = 10 * 1024 * 1024
```

#### 🖼️ Restringir para aceitar apenas PNG:

```python
ALLOWED_EXTENSIONS = {"png"}
```

---

### 🧠 Dica

> **Não é necessário reconstruir o serviço para aplicar mudanças.**
> Basta editar o `config.py` e reiniciar o microserviço com:
>
> ```bash
> python -m app.main
> ```
>
> ou
>
> ```bash
> docker restart <container-id>
> ```

---

## 📁 Estrutura do Projeto

```
ocr_service/
├── app/
│   ├── __init__.py        # Define pacote
│   ├── main.py            # Entrypoint Flask + endpoints
│   ├── ocr_engine.py      # Função de OCR com Tesseract
│   ├── cache.py           # Cache em memória (por hash)
│   ├── utils.py           # Validações e helpers
│   └── config.py          # Parâmetros globais do app
├── tests/
│   ├── __init__.py
│   └── test_ocr.py        # Testes básicos
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

## 📌 Notas

* Ideal para automação de inventário, preventivas, manutenção e cadastro rápido por imagem.
* Pode ser consumido por qualquer tecnologia com suporte a HTTP.
* Não recomendado expor publicamente sem autenticação — use em rede interna/local.
* Cache interno pode ser substituído por Redis se desejar persistência distribuída.

---

## 📢 Contribuição

Pull Requests e sugestões são bem-vindos!

Para bugs ou melhorias, abra uma [Issue](https://github.com/anxiousCamel/ocr_service/issues).

---

## 📬 Contato

Se quiser usar esse microserviço em algo maior, integrar com sistemas legados ou precisa de ajuda para adaptar, me chama no [LinkedIn](https://www.linkedin.com/in/luizbelmontedev/) ou abra uma issue.

---

🛠️ Criado por \[Luiz Vinicius Ventura Belmonte] • 2025

