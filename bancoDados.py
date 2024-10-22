'''
Introdução a banco de dados:
Dado é a menor parte de um banco de dados, sendo o elemento bruto que é fornecido pelo user. O dado por si só não diz nada.
Base de dados = Conjunto de arquivos contendo dados relacionados de forma organizada.
Banco de dados = Arquivo que mantém tudo o que se deseja guardar.
SGDB (Sistema Gerenciador de Banco de Dados) = software que gerencia os dados do Banco de dados.

3 Fases do projeto de BD:
Modelo Conceitual = Pensar no conceito de como será preparada a estrutura do banco de dados. É necessário entender de negócio. (Analista de dados)
É necessário ter visão geral do negócio, tem que saber falar com o usuário e o desenvolvedor.
Só vão ter lista de regras e funcionalidades.

Modelo lógico = é necessário ter o modelo conceitual. Implementar como uma entidade associativa, transfoprmando algo conceitual em algo prático.
É necessário definir a chave primária, como um dado elegível (ou único), que identifica a informação.
Dicionário de dados: Adota a nomenclatura de dados da empresa, padronizando o nome das variáveis para cada tipo de dado. Entidades e atibutos são documentados.

Modelo físico = Define o sistema de gerenciamento de dados, com base nos critérios do projeto. (Não é função do programador, é do DBA)
DBA (Data Based Administrative) - Adm do banco de dados, especialista em um tipo de estrutura. A certificação é oferecido pelo fabricante do software, precisando fazer os testes que a empresa oferece.

Chave primária identifica a entidade.
Toda chave estrangeira é uma chave primária em sua própria entidade.

PASSOS PARA TRABALHAR COM BANCO DE DADOS
Determinar o objetivo. Será um sistema para um Restaurante? Para um Estacionamento?
Entidades são tabelas que guardam informações diferentes, como "Clientes", "Idade", etc.
Determinar os atributos para cada entidade. EX.: Entidade: Alunos, Atributos: Nome, idade, etc.
Determinar o Identificador da entidade, que vai definir a chave primária. Se não tiver algum atributo que pode ser a chave primária, deve ser criado.
EX.: No caso de alunos, seria CPF. Se não tiver CPF, pegar a matrícula. No caso de estacionamento, seria a placa.
Determinar os relacionamentos, identificando as associações entre as entidades.
Normalizar a estrutura de banco de dados, para que evite erros e haja padronização.

'''