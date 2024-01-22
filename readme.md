# Alura Space - Projeto Django

Este é o repositório de estudos do projeto Alura Space, desenvolvido como parte do curso de Django da Alura. O Alura Space é uma aplicação simples para aprendizado do framework Django.

## Como executar o projeto em outro computador

Siga os passos abaixo para configurar e executar o projeto em um ambiente local.

### 1. Clonar o repositório

```bash
git clone https://github.com/Rafael-Ribeiro-de-Lima/django-alura.git
cd django-alura
```

### 2. Criar e ativar o ambiente virtual

```bash
# No diretório do projeto, crie um ambiente virtual chamado "venv"
python -m venv venv

# Ative o ambiente virtual
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
# Certifique-se de estar no diretório raiz do projeto
# Instale as dependências do projeto a partir do arquivo requirements.txt
pip install -r requirements.txt
```

### 4. Executar o servidor de desenvolvimento

```bash
# No diretório raiz do projeto, execute o servidor Django
python manage.py runserver
```

Após executar esses passos, a aplicação estará disponível em http://127.0.0.1:8000/ no navegador.

### 5. Sobre o curso

#### 5.1. Boas Práticas

Durante o curso, foram enfatizadas boas práticas de desenvolvimento Django, incluindo a estruturação adequada de projetos, o uso eficiente de templates e a organização de código Python seguindo as convenções do framework.

#### 5.2. Persistência de Dados

A seção de persistência de dados abrange os conceitos fundamentais de modelagem de banco de dados com Django, mostrando como criar modelos, realizar migrações e interagir com o banco de dados para garantir uma manipulação eficiente e segura dos dados.

#### 5.3. Autenticação de Formulários

A autenticação de formulários é uma parte crucial do desenvolvimento web. O curso explora como criar formulários seguros e eficientes, garantindo que as informações submetidas sejam validadas corretamente e protegidas contra ataques comuns.

#### 5.4. Cloud

O tópico de integração com serviços de nuvem concentra-se em aspectos práticos, como a implementação de recursos na nuvem para a aplicação Django. Isso inclui o uso de serviços como armazenamento em nuvem para gerenciar arquivos estáticos e de mídia.



