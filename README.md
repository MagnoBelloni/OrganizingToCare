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
- A aplicação deverá listar todos os medicamentos na página "Medicamentos";
- A aplicação deverá permitir que todos os usuário criem/editem medicamentos;
- A aplicação deverá listar todos os usuários apenas a usuários com perfil "admnistrador" na página "Usuários";
- A aplicação deverá permitir apenas a usuários com perfil "admnistrador" crie/edite novos usuários;
- A aplicação deverá permitir apenas a usuários com perfil "admnistrador" resete a senha dos usuários;
- A aplicação deverá consultar a API ViaCEP, para realizar uma consulta do logradouro pelo CEP do usuário;

### Caso de Uso:
![Preview](https://github.com/MagnoBelloni/AC5-OrganizingToCare/blob/main/documentacao/CasoDeUso.jpg)


### Banco de dados:

![Preview](https://github.com/MagnoBelloni/AC5-OrganizingToCare/blob/main/documentacao/DiagramaBanco.jpg)

[Conexão com o Banco de dados]

- Para realizar a conexão ao Banco de Dados é necessário fazer o download de um arquivo .json contendo as 
  credenciais do Banco de Dados em uma pasta do Google Drive
- O nome da pasta é AppConfig, e o link é https://drive.google.com/drive/u/1/folders/1odwcZLYWGuf0w47j8ytTvCVnmu6vZEXV
- O nome do arquivo necessário é AppConfig.json
- Para ser feita a configuração das credenciais é só realizar a troca do arquivo AppConfig.json na pasta credentials
  pelo arquivo de mesmo nome com origem na pasta do Drive




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
- organizingtocare/credentials, pasta onde deve ser colocado o arquivo json com as crendenciais do DataBase.

## Para contribuir com o projeto

### Crie uma branch a partir da main

- NUNCA faça um commit direto para a main.
- git pull, para se certificar que a branch main está atualizada.
- git checkout -b "feature/nome-da-branch".
- git push --set-upstream origin feature/nome-da-branch
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

### Rodar a aplicação

- Rodar a aplicação:
  python run.py

## Construído com:

- [Python](https://www.python.org/) - Python is a programming language that lets you work quickly.
  and integrate systems more effectively.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web development one drop at a time.
- [SqlAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [PostgreSQL](https://www.postgresql.org/about/) - PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.
- [Figma](https://figma.com/) - Online prototyping tool.
- [ViaCEP](https://viacep.com.br/) - Consulte CEPs de todo o Brasil.
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - The world’s most popular framework for building responsive, mobile-first sites.
- [Material Dashboard](https://demos.creative-tim.com/material-dashboard/docs/2.1/getting-started/introduction.html) - Material Dashboard is a Bootstrap 4 Admin Template.

## Integrantes do Projeto:

- Leonardo Andrade de Souza - [Linkedin](https://www.linkedin.com/in/leoadsouza/) - [Github](https://github.com/Leoads99)
- Magno Belloni - [Linkedin](https://www.linkedin.com/in/magnobelloni/) - [Github](https://github.com/MagnoBelloni)
- Thaina Souza - [Linkedin](https://www.linkedin.com/in/thaina-souza-270585185/) - [Github](https://github.com/thainabsouza)

## Acknowledgments

- Este projeto foi construído como trabalho de conclusão do curso de Análise e Desenvolvimento de Sistemas durante o 4ºSemestre de Análise e Desenvolvimento de Sistemas da [Faculdade Impacta de Tecnologia](https://www.impacta.edu.br/), sob a orientação do Professor Fernando Sequeira.
