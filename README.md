# 📚 Gestão de Tarefas e Rotina de Estudos

Aplicação web Full-Stack desenvolvida para facilitar o gerenciamento de tarefas e a organização da rotina de estudos. O sistema permite cadastrar, visualizar e excluir tarefas, oferecendo uma interface simples e intuitiva para o acompanhamento das atividades.

O projeto conta com uma API REST desenvolvida em Python com Flask, persistência de dados utilizando SQLite e uma interface responsiva construída com HTML5, CSS3 e JavaScript.

## 🛠️ Tecnologias Utilizadas

**Back-end**

- Python 3
- Flask
- Flask-CORS

**Banco de Dados**

- SQLite3

**Front-end**

- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API

**Versionamento**

- Git
- GitHub

## 📌 Funcionalidades

- [ ] **Listar tarefas:** Consulta dinâmica das tarefas cadastradas e armazenadas no banco de dados.
- [ ] **Adicionar tarefas:** Cadastro de novas tarefas por meio de requisições HTTP POST.
- [ ] **Remover tarefas:** Exclusão individual de tarefas utilizando seus respectivos IDs por meio de requisições HTTP DELETE.
- [ ] **Limpar todas as tarefas:** Remoção completa dos registros cadastrados no banco de dados.

## 🔗 Endpoints da API REST

A aplicação possui os seguintes endpoints para comunicação entre o front-end e o back-end:

| Método HTTP | Rota                | Descrição                             |
| ----------- | ------------------- | ------------------------------------- |
| `GET`       | `/api/tarefas`      | Retorna todas as tarefas cadastradas. |
| `POST`      | `/api/tarefas`      | Cadastra uma nova tarefa.             |
| `DELETE`    | `/api/tarefas/<id>` | Remove uma tarefa específica pelo ID. |
| `DELETE`    | `/api/tarefas`      | Remove todas as tarefas cadastradas.  |

**Exemplo de requisição POST:**

```json
{
    "titulo": "Estudar programação"
}
```

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.x
- Git
- Navegador web de sua preferência

### 1. Clonar o Repositório

```bash
git clone https://github.com/WSantiago2003/gestao-de-tarefas.git
```

Acesse a pasta do projeto:

```bash
cd gestao-de-tarefas
```

### 2. Criar o Ambiente Virtual

```bash
python -m venv venv
```

**Ativação no Windows (CMD):**

```bash
venv\Scripts\activate
```

**Ativação no Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Ativação no Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, execute:

```bash
pip install flask flask-cors
```

### 4. Executar o Back-end

Inicie o servidor Flask com o comando:

```bash
python app.py
```

### 5. Executar o Front-end

Abra o arquivo `index.html` diretamente no navegador de sua preferência.

Com o servidor Flask em execução, a interface poderá realizar as requisições à API para cadastrar, consultar e excluir tarefas.

## 👨‍💻 Autor

Projeto desenvolvido como prática de desenvolvimento Full-Stack, aplicando conceitos de desenvolvimento web, criação de APIs RESTful, integração entre front-end e back-end e persistência de dados em banco relacional.
