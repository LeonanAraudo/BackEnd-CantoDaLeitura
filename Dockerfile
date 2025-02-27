# Usar uma imagem oficial do Python
FROM python:3.9

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . /app/

# Instalar dependências
RUN pip install -r requirements.txt

# Expor a porta 8000
EXPOSE 8000

# Rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
