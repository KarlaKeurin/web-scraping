# WEB SCRAPING
Este repositório contém um projeto de Web Scraping. Siga os passos abaixo para rodá-lo em sua máquina. 🚀

## ⚙️ Configurações do Backend
Todos os passos da configuração do backend precisam ser rodados dentro do terminal integrado da pasta backend.

### 1. Criando e ativando o ambiente virtual
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalando as dependências
```
pip install -r requirements.txt
```

### 3. Iniciando o servidor FastAPI
Após instalar as dependências, inicie o servidor executando:
```
uvicorn main:app --reload
```

❗ Abra outro terminal integrado da pasta backend e faça os passos anteriores novamente.

### 4. Executando os desafios
🔍 Desafio 1 - Teste de Web Scraping
```
python scraper.py
```

🔍 Desafio 2 - Teste de Transformação de Dados
```
python data_transformer.py
```

### 5. Configurando o Banco de Dados
<details>
  <summary>💡 Talvez seja necessário setar o local_infile globalmente, siga as instruções caso necessário:</summary><br/>

  * No terminal, conecte-se ao MySQL como root:
  ```
  mysql -u root -p
  ```
  * Depois, rode este comando para ativar a opção no servidor:
  ```
  SET GLOBAL local_infile = 1;
  ```
  * Verifique se está ativado:
  ```
  SHOW VARIABLES LIKE 'local_infile';
  ```
  * Se retornar ON, então está ativado.
</details><br/>


Acessando o terminal MySQL
```
mysql -u root -p --local-infile=1
```

💾 Desafio 3 - Teste de Banco de Dados
```
SOURCE db.sql;
SOURCE queries.sql;
```

### 5. Acessar a coleção do Postman
Abra os links para acessar a coleção do Postman: <br/>
* [Para acessar a busca com o nome "medicina"](http://127.0.0.1:8000/buscar?nome=medicina)
* [Para acessar a busca com o nome "beneficios"](http://127.0.0.1:8000/buscar?nome=beneficios)

## 💻 Configuração do Frontend
Abra o terminal integrado da pasta frontend e execute os seguintes comandos:

### 1. Instalando as dependências
```
npm install
```

### 2. Iniciando o servidor
🔍 Desafio 4 - Teste de API

Inicie o frontend na porta 5173 e faça sua busca:
```
npm run dev
```
