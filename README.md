# EasyMart - Sistema de Gerenciamento de Produtos

## Descrição
EasyMart é um sistema Django para gerenciar produtos e fornecedores. O foco atual é o cadastro de produtos, vínculo de fornecedores e solicitação de reposto por e-mail.

## Funcionalidades
- **Listagem de Produtos**: Página inicial com nome, preço, quantidade em estoque e fornecedor vinculado.
- **Fornecedores**: Cadastro e gerenciamento de fornecedores via admin do Django.
- **Pedido ao Fornecedor**: Botão que abre formulário para enviar e-mail ao fornecedor do produto.
- **Admin Django**: Cadastro e edição de produtos e fornecedores pelo painel `/admin/`.

## Tecnologias
- **Framework**: Django
- **Banco de Dados**: SQLite
- **Front-end**: HTML com CSS separado em arquivos estáticos

## Instalação e Execução
1. Certifique-se de ter Python instalado.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Crie um superusuário (opcional, caso queira outro usuário):
   ```bash
   python manage.py createsuperuser
   ```
5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
6. Acesse:
   - `http://127.0.0.1:8000/` para lista de produtos
   - `http://127.0.0.1:8000/fornecedores/` para fornecedores
   - `http://127.0.0.1:8000/admin/` para painel admin

## Credenciais de Admin Padrão
- **Usuário**: admin
- **Senha**: admin

## Estrutura do Projeto
- `easymart/`: Configurações do projeto Django
- `products/`: App de produtos e formulário de pedido ao fornecedor
- `fornecedores/`: App de fornecedores e vínculo com produtos
- `static/`: CSS e arquivos estáticos
- `manage.py`: Script de gerenciamento do Django

## Observações
- O envio de e-mail no ambiente de desenvolvimento usa o backend de console do Django.
- Para produção, configure um servidor SMTP real no `easymart/settings.py`.

