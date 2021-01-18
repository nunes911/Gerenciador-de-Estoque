# Gerenciador de Estoque
 Desafio de criar um projeto de front, back e banco de dados de um Gerenciador de Estoque.

[ ] Colocar projeto no github
[ ] Aplicar Modal ao botão excluir e faze-lo funcionar
[ ] Botão ao clicar no botão movimento terá um auto select do produto
[ ] Auto incremento do No de registro
[ ] Validação no Back-end
[ ] DB que armezene o histórico de movimentação
[ ] botão DETALHES para mostrar a descrição e o histórico


# CRIAÇÃO DA TABELA NO MYSQL

Em seu Banco de Dados no MYSQL, executar o seguinte comando para criar a tabela:

CREATE TABLE `produto` (
  `cod_registro` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `fabricante` varchar(255) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `data_atualizacao` date DEFAULT NULL,
  `local` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cod_registro`)
);

# CONFIGURAÇÃO CONEXÃO DO BANCO DE DADOS

No arquivo app.py, preencher a configuração a seguir com os dados de seu bannco de dados:

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database'

# INICIANDO O SERVIDOR

No prompt de comando, localize a pasta do projeto e digite o seguinte comando:

python app.py

Use o link que foi descrito no terminal.
