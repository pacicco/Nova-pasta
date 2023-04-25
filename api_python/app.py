from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'},
    {'id': 2, 'titulo': 'Harry Potter e a Câmara Secreta', 'autor': 'J.K. Rowling'},
    {'id': 3, 'titulo': 'Harry Potter e o Prisioneiro de Azkaban', 'autor': 'J.K. Rowling'},
    {'id': 4, 'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K. Rowling'},
    {'id': 5, 'titulo': 'Jurassic Park', 'autor': 'Michael Crichton'}
]

#função para retornar todos os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)


#função para consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'})

#função para editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    
#função para criar novo livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    livro_criado = request.get_json()
    livros.append(livro_criado)
    return jsonify(livro_criado)

#função para excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros.pop(indice)
            return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)

#return jsonify({'mensagem': 'Livro não encontrado'})