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
1. Certifique-se de ter Python 3 instalado.
2. Crie e ative um ambiente virtual (Windows PowerShell):
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Execute as migrações:
   ```powershell
   .\venv\Scripts\python.exe manage.py migrate
   ```
5. Inicie o servidor:
   ```powershell
   .\venv\Scripts\python.exe manage.py runserver
   ```
6. Acesse a aplicação:
   - `http://127.0.0.1:8000/` para lista de produtos
   - `http://127.0.0.1:8000/fornecedores/` para fornecedores
   - `http://127.0.0.1:8000/admin/` para painel admin

## Admin Padrão
- **Usuário**: admin
- **Senha**: admin

> O superusuário `admin` é criado automaticamente pela migração do projeto.

## Rodando Testes
```powershell
.\venv\Scripts\python.exe manage.py test
```

## Estrutura do Projeto
- `easymart/`: Configurações do projeto Django
- `products/`: App de produtos e lógica de pedido ao fornecedor
- `fornecedores/`: App de fornecedores e vínculo com produtos
- `static/`: CSS e JavaScript estáticos
- `manage.py`: Script de gerenciamento do Django

## Observações
- O envio de e-mail no ambiente de desenvolvimento usa o backend de console do Django.
- Para produção, configure um servidor SMTP real em `easymart/settings.py`.

