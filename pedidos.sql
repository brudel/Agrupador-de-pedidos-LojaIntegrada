# Cria tabela para os pedidos se ela já não existir.
CREATE TABLE IF NOT EXISTS pedidos
(
    produto text,
    tipo text,
    quantidade integer
);

# Garante que a tabela está vazia.
TRUNCATE pedidos;

# Copia os pedidos para o banco de dados.
\copy pedidos FROM pedidos.csv

# Exporta os pedidos em CSV agrupados por produto e tipo.
\copy (SELECT produto, tipo, sum(quantidade) FROM pedidos GROUP BY produto, tipo ORDER BY produto, tipo) TO final.csv