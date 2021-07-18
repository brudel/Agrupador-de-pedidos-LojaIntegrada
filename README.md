# Agrupador de pedidos LojaIntegrada

Esse programa agrupa os pedidos de um mesmo produto com campos com valores iguais para facilitar pedidos para o fornecedor. Foi desenvolvido para facilitar os pedidos de moletons da [lojinha da SACIM](https://lojinha-da-sacim.lojaintegrada.com.br/).

## Como usar

Ajuste as variáveis definidas no começo do arquivo [pedidos.py](https://github.com/brudel/Agrupador-de-pedidos-LojaIntegrada/blob/main/pedidos.py) conforme descrito nos comentários e execute o programa com Python 3.

Execute o script [pedidos.sql](https://github.com/brudel/Agrupador-de-pedidos-LojaIntegrada/blob/main/pedidos.sql) em um banco de dados [PostgreSQL](https://www.postgresql.org/) (ex. `psql mybase < pedidos.sql`).

O arquivo gerado contém os pedidos agrupados em csv e pode ser copiado e colado diretamente em uma planilha.

Para examinar o html da página de pedido da mesma forma como o programa vê, use a função comentada no final do arquvio [pedidos.py](https://github.com/brudel/Agrupador-de-pedidos-LojaIntegrada/blob/7d6c21953afc0d52eb18206945d87de88d32add3/pedidos.py#L78).

## Licença

Licença MIT (MIT). Por favor, veja o [arquivo da licença](https://github.com/brudel/Agrupador-de-pedidos-LojaIntegrada/blob/main/LICENSE) para mais detalhes.
