# MyProject - Sistema de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Django com API REST.

## 🚀 Tecnologias Utilizadas

- **Django 4.x** - Framework web Python
- **Django REST Framework** - Framework para construção de APIs REST
- **Django CORS Headers** - Middleware para CORS
- **SQLite** - Banco de dados
- **Docker** - Containerização da aplicação

## 📋 Pré-requisitos

- Python 3.9+
- Docker e Docker Compose (opcional)

## 🛠️ Instalação e Configuração

### Opção 1: Instalação Local

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd myproject
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

### Opção 2: Usando Docker

1. Execute o projeto com Docker Compose:
```bash
docker-compose up --build
```

## 🏗️ Estrutura do Projeto

```
myproject/
├── library/                 # Aplicação principal
│   ├── models.py           # Modelos de dados (Author, Book)
│   ├── views.py            # ViewSets da API
│   ├── serializers.py      # Serializers para JSON
│   ├── urls.py             # Configuração de URLs
│   └── settings.py         # Configurações do Django
├── manage.py               # Script de gerenciamento Django
├── requirements.txt         # Dependências Python
├── docker-compose.yml      # Configuração Docker
└── Dockerfile              # Imagem Docker
```

## 📚 Padrões de Projeto

- **ViewSets** - Organização de views relacionadas em classes
- **Model Serializers** - Serialização automática de modelos Django
- **REST API** - Arquitetura RESTful com endpoints padronizados
- **MVC/MTV** - Padrão Django (Model-Template-View)

## 🔌 Endpoints da API

### Autores
- `GET /authors/` - Lista todos os autores
- `GET /authors/{id}/` - Obtém autor específico
- `POST /authors/` - Cria novo autor
- `GET /authors/top/` - Lista top 5 autores por número de livros

### Livros
- `GET /books/` - Lista todos os livros
- `GET /books/{id}/` - Obtém livro específico
- `POST /books/` - Cria novo livro
- `PATCH /books/{id}/` - Atualiza livro parcialmente

## 🗄️ Modelos de Dados

- **Author**: Nome do autor
- **Book**: Título, data de publicação e autor (relacionamento FK)

## ⚙️ Configurações Importantes

- **CORS**: Habilitado para todas as origens (desenvolvimento)
- **Database**: SQLite por padrão, configurável via variável de ambiente
- **Porta**: 8000 (configurável no Docker)

## 🚀 Executando o Projeto

Após a instalação, acesse:
- **API**: http://localhost:8000/
- **Admin Django**: http://localhost:8000/admin/

## 📝 Notas

- Projeto configurado para desenvolvimento
- CORS habilitado para todas as origens
- Banco SQLite incluído no repositório
- Configuração Docker pronta para uso
