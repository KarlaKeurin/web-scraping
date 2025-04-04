# WEB SCRAPING

Este repositório contém um projeto de Web Scraping. Siga os passos abaixo para rodá-lo em sua máquina. 🚀

## ⚙️ Configurações do Backend

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

Acessando o terminal MySQL

```
mysql -u root -p --local-infile=1
```

Dentro do terminal MySQL, selecione o banco de dados

```
USE db_intuitive_care;
```

💾 Desafio 3 - Teste de Banco de Dados

```
SOURCE db.sql;
SOURCE queries.sql;
```

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
