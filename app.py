from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SWAGGER'] = {
    'title': 'Catálogo de Livros API',
    'version': '1.0'
}
db = SQLAlchemy(app)
swagger = Swagger(app)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano_publicacao = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    """
    Adiciona um novo livro
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            autor:
              type: string
            ano_publicacao:
              type: integer
    responses:
      201:
        description: Livro adicionado
    """
    data = request.get_json()
    novo_livro = Livro(
        titulo=data['titulo'],
        autor=data['autor'],
        ano_publicacao=data.get('ano_publicacao')
    )
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro adicionado!"}), 201

@app.route('/listar_livros', methods=['GET'])
def listar_livros():
    """
    Lista todos os livros
    ---
    responses:
      200:
        description: Lista de livros
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              autor:
                type: string
              ano_publicacao:
                type: integer
    """
    livros = Livro.query.all()
    return jsonify([{
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano_publicacao": livro.ano_publicacao
    } for livro in livros]), 200

@app.route('/buscar_livro/<int:id>', methods=['GET'])
def buscar_livro(id):
    """
    Busca um livro por ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Dados do livro
      404:
        description: Livro não encontrado
    """
    livro = Livro.query.get(id)
    if livro:
        return jsonify({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao
        }), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

@app.route('/remover_livro/<int:id>', methods=['DELETE'])
def remover_livro(id):
    """
    Remove um livro
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Livro removido
      404:
        description: Livro não encontrado
    """
    livro = Livro.query.get(id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
        return jsonify({"mensagem": "Livro removido!"}), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)