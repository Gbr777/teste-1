from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Caminho do arquivo JSON para armazenar usuários
USER_DATA_FILE = 'data/users.json'

# Função para carregar dados dos usuários
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return []
    with open(USER_DATA_FILE, 'r') as f:
        return json.load(f)

# Função para salvar dados dos usuários
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        users = load_user_data()
        users.append({'name': name, 'email': email, 'password': password})
        save_user_data(users)
        
        return redirect(url_for('contests'))
    return render_template('register.html')

@app.route('/contests')
def contests():
    contests_list = [
        'Concurso 1: Prefeitura de São Paulo',
        'Concurso 2: Polícia Federal',
        'Concurso 3: Banco do Brasil'
    ]
    return render_template('contests.html', contests=contests_list)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = load_user_data()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
