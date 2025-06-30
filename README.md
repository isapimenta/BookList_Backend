# Acervo de Livros
Um aplicativo que funciona como um acervo de livros virtual. Permitindo fácil adição de livros novos, e busca dos mesmos.
Mantendo o tracking de leitura sempre em dia, e ajudando leitores a manter um controle de suas leituras.
# Back-end (Python/Flask)
- 4 rotas principais:
    - POST /adicionar_livro (cadastro);
    - GET /listar_livros (consulta geral);
    - GET /buscar_livro/<id> (busca por ID);
    - DELETE /remover_livro/<id> (exclusão)
- Banco de dados SQLite com tabela Livro
- Documentação Swagger integrada (/apidocs)
# Front-end (HTML/CSS/JS)
- SPA (Single Page Application) sem frameworks
- Interface responsiva com cards e formulários
- Funcionalidades:
    - Listagem dinâmica
    - Busca por Título
    - Adição/remoção de livros
    - Comunicação total com a API via Fetch
  # Instalação do Back-end (API Flask)
  Pré-requisitos
  - Python 3.8+ instalado
  - Pip (geralmente vem com o Python)
  - Git (opcional, para clonar o repositório)
  ### Passo a Passo
  1. Clone o repositório
  2. Crie e ative um ambiente virtua: python -m venv venv
  3. Instale as dependências: pip install -r requirements.txt
  4. Inicie a API: http://localhost:5000 // http://localhost:5000/apidocs
  # Instalação do Front-end
  ### Passo a Passo
  1. Clone o repositório
  2. Abra o projeto
