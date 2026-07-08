# EasyMart - Sistema de Gerenciamento de Produtos

## Descrição
EasyMart é um sistema Django para gerenciar produtos e fornecedores. O foco atual é o cadastro de produtos, vínculo de fornecedores e solicitação de reposição por e-mail.

## Funcionalidades
- **Listagem de Produtos**: Página inicial com nome, preço, quantidade em estoque e fornecedor vinculado.
- **Fornecedores**: Gerenciamento de fornecedores via admin do Django.
- **Pedido ao Fornecedor**: Botão que abre formulário para enviar e-mail ao fornecedor do produto.
- **Admin Django**: Cadastro e edição de produtos e fornecedores pelo painel `/admin/`.

## Tecnologias
- **Framework**: Django
- **Banco de Dados**: SQLite
- **Front-end**: HTML, CSS e JavaScript estáticos

## Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- Git (opcional)

### Passo 1: Clonar ou Baixar o Repositório
```powershell
git clone <seu-repositorio>
cd EasyMart
```

### Passo 2: Criar e Ativar Ambiente Virtual
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Se receber erro de execução, ative a execução de scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Passo 3: Instalar Dependências
```powershell
pip install -r requirements.txt
```

### Passo 4: Executar Migrações do Banco de Dados
```powershell
.\venv\Scripts\python.exe manage.py migrate
```

### Passo 5: Iniciar o Servidor de Desenvolvimento
```powershell
.\venv\Scripts\python.exe manage.py runserver
```

Você verá uma mensagem como:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Passo 6: Acessar a Aplicação

Abra seu navegador e acesse:
- **Página principal**: `http://127.0.0.1:8000/` (lista de produtos)
- **Fornecedores**: `http://127.0.0.1:8000/fornecedores/`
- **Painel Admin**: `http://127.0.0.1:8000/admin/`

## Credenciais de Admin
O superusuário é criado automaticamente pela migração do projeto:

- **Usuário**: admin
- **Senha**: admin

Acesse `http://127.0.0.1:8000/admin/` para gerenciar produtos e fornecedores.

## Rodando Testes
```powershell
.\venv\Scripts\python.exe manage.py test
```

## Dicas Úteis

### Parar o Servidor
Pressione `CTRL + C` no terminal

### Reativar o Ambiente Virtual
Se você fechar o terminal e precisar reativar o ambiente virtual:
```powershell
.\venv\Scripts\Activate.ps1
```

### Limpar o Banco de Dados
Para resetar o banco de dados (apaga todos os dados):
```powershell
del db.sqlite3
.\venv\Scripts\python.exe manage.py migrate
```

### Criar um Novo Superusuário
```powershell
.\venv\Scripts\python.exe manage.py createsuperuser
```

## Estrutura do Projeto
- `easymart/`: Configurações do projeto Django
- `products/`: App de produtos e lógica de pedido ao fornecedor
- `fornecedores/`: App de fornecedores e vínculo com produtos
- `static/`: CSS e JavaScript estáticos
- `manage.py`: Script de gerenciamento do Django

## Observações Importantes

### Configuração de E-mail
- No ambiente de **desenvolvimento**, os e-mails são exibidos no console (terminal).
- Para **produção**, configure um servidor SMTP real editando as variáveis em `easymart/settings.py`:
  - `EMAIL_BACKEND`
  - `EMAIL_HOST`
  - `EMAIL_PORT`
  - `EMAIL_USE_TLS`
  - `EMAIL_HOST_USER`
  - `EMAIL_HOST_PASSWORD`

### Banco de Dados
- O projeto usa **SQLite** por padrão (`db.sqlite3`)
- Ideal para desenvolvimento e testes
- Para produção, considere usar PostgreSQL ou MySQL

### Dependências Instaladas
- **Django 6.0.5**: Framework web
- **reportlab >= 4.0.0**: Geração de PDFs
- **Pillow >= 9.0.0**: Processamento de imagens
- **sqlparse >= 0.5.0**: Parse de SQL
- **asgiref >= 3.11.1**: Interface ASGI

