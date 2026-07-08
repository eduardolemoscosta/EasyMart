-- Consulta SQL: Inner Join entre Produtos e Fornecedores
-- Seleciona: Nome do Produto, Nome do Fornecedor e Preço do Produto

SELECT 
    products_produto.nome AS produto_nome,
    fornecedores_fornecedor.nome AS fornecedor_nome,
    products_produto.preco AS produto_preco
FROM 
    products_produto
INNER JOIN 
    fornecedores_fornecedor ON products_produto.fornecedor_id = fornecedores_fornecedor.id
ORDER BY 
    products_produto.nome ASC;
