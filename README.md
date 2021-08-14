# Organizing To Care

![Preview](https://github.com/MagnoBelloni/AC5-OrganizingToCare/blob/main/documentacao/Sistema.jpg)

## Pré-requisitos:

Você precisa do Python instalado em sua máquina.

Você precisa do virtualenv instalado em sua máquina. Ex:

```
pip install virtualenv
```

## Documentação:

### Projeto proposto:

Uma aplicação para gerenciar medicamentos.

### Requisitos:

- O usuário deverá realizar o login para utilizar a aplicação;
- O usuário deverá realizar a troca de senha no primeiro Login;
- A aplicação deverá listar os medicamentos com vencimento de no minímo 15 dias na página "Home";
- A aplicação deverá mostrar em vermelho os medicamentos vencidos na página "Home";
- A aplicação deverá listar todos os medicamentos na página "Medicamentos";
- A aplicação deverá permitir que todos os usuário criem/editem medicamentos;
- A aplicação deverá listar todos os usuários apenas a usuários com perfil "admnistrador" na página "Usuários";
- A aplicação deverá permitir apenas a usuários com perfil "admnistrador" crie/edite novos usuários;
- A aplicação deverá permitir apenas a usuários com perfil "admnistrador" resete a senha dos usuários;
- A aplicação deverá consultar a API ViaCEP, para realizar uma consulta do logradouro pelo CEP do usuário;

### Banco de dados:

![Preview](https://github.com/MagnoBelloni/AC5-OrganizingToCare/blob/main/documentacao/DiagramaBanco.jpg)

## Layout:

Criamos o layout utilizando o Figma. Você pode encontrar o arquivo [aqui](https://www.figma.com/file/P3XmjCFWHuon7Yrnf1urkA/AC5-Aplica%C3%A7%C3%B5es-Distribuidas?node-id=14%3A507).

### Camadas:

- controllers, aonde todas as rotas se encontram separadas por contexto.
- helpers, funções úteis a toda aplicação. Ex: Gerar senha aleatória.
- models, modelos de tabela do banco de dados.
- static, arquivos staticos. Ex: css, js, imagens.
- templates, arquivos html com o template jinja.
- apis, acesso a APIs externas.

### Estrutura:

- app, diretorio aonde se encontra todas as camadas.
- run.py, arquivo utilizado para rodar a aplicação.
- app/**init**.py, inicia toda a aplicação.
- app/controllers/default, arquivo de unificação de todos os controllers.

## Para contribuir com o projeto

### Crie uma branch a partir da main

- git checkout -b "feature/nome-da-branch"
- git push
- Vá até o [Github](https://github.com/MagnoBelloni/AC5-OrganizingToCare).
- Crie uma PR para a main.
- Aguarde a aprovação da PR.
- Se a PR estiver correta será aprovada e ira ser feito o merge com a main.
- Rode o comando "git checkout main" para voltar para a branch main
- Rode o comando "git pull", para atualizar sua branch main

## Para rodar a aplicação

### Criar o ambiente virtual

- cd organizingtocare
- python -m virtualenv venv

### Ativar o ambiente virtual

- source venv/Scripts/activate

### Instalar dependencias

- pip install -r requirements.txt

### [Opcional!!!] Rodar o flask em ambiente de dev(ativar o fast reload)

- export FLASK_ENV=development

### Rodar a aplicação

- Rodar a aplicação:
  python run.py

## Construído com:

- [Python](https://www.python.org/) - Python is a programming language that lets you work quickly
  and integrate systems more effectively.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web development one drop at a time.
- [SqlAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [SQLite](https://www.sqlite.org/) - SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- [Figma](https://figma.com/) - Online prototyping tool.
- [ViaCEP](https://viacep.com.br/) - Consulte CEPs de todo o Brasil

## Integrantes do Projeto:

- Leonardo Andrade de Souza - [Linkedin](https://www.linkedin.com/in/leoadsouza/) - [Github](https://github.com/Leoads99)
- Magno Belloni - [Linkedin](https://www.linkedin.com/in/magnobelloni/) - [Github](https://github.com/MagnoBelloni)
- Thaina Souza - [Linkedin](https://www.linkedin.com/in/thaina-souza-270585185/) - [Github](https://github.com/thainabsouza)

## Acknowledgments

- Este projeto foi construído para a matéria Desenvolvimento de Aplicações Distribuídas, com a orientação do Professor Jadir Custódio Mendonça Junior,
  durante o 3ºSemestre de Análise e Desenvolvimento de Sistemas da [Faculdade Impacta de Tecnologia](https://www.impacta.edu.br/).
