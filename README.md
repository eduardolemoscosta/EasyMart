# EasyMart - Sistema de Supermercado

## Descrição
EasyMart é um sistema simples de gerenciamento de supermercado desenvolvido em Django. Esta é a versão 1.0, focada nas funcionalidades básicas: listagem de produtos, venda de unidades e cadastro via painel admin.

## Funcionalidades
- **Listagem de Produtos**: Página inicial mostrando uma tabela com nome, preço e quantidade em estoque de cada produto.
- **Venda Simples**: Botão "Vender 1 unidade" para cada produto, que diminui o estoque em 1 e recarrega a página.
- **Cadastro**: Adição de novos produtos via painel de administração do Django (/admin).

## Tecnologias
- **Framework**: Django (Python)
- **Banco de Dados**: SQLite (padrão do Django)
- **Interface**: HTML simples, sem estilos avançados

## Instalação e Execução
1. Certifique-se de ter Python instalado.
2. Instale as dependências: `pip install django`
3. Execute as migrações: `python manage.py migrate`
4. Crie um superusuário: `python manage.py createsuperuser`
5. Inicie o servidor: `python manage.py runserver`
6. Acesse `http://127.0.0.1:8000/` para a listagem e `/admin/` para cadastro.

## Estrutura do Projeto
- `easymart/`: Configurações do projeto Django
- `products/`: App responsável pelos produtos (modelos, views, templates)
- `manage.py`: Script de gerenciamento do Django

## Próximos Passos
- Adicionar validações e tratamento de erros
- Implementar estilos CSS para melhor aparência
- Expandir funcionalidades (carrinho de compras, categorias, etc.)
- Refatorar para views baseadas em classe (CBV)

