from flask import Flask, request, jsonify, render_template
import json
import uuid


app = Flask(__name__)

users = {}
user_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global user_id_counter
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    age = request.form.get('age')
    gender = request.form.get('gender')

    users[user_id_counter] = {
        "id": str(uuid.uuid4())

        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender
    }
    user_id_counter += 1

    return jsonify({'status': 'success', 'message': 'User added successfully'})

@app.route('/user', methods=['GET'])
def get_users():
    print(json.dumps(users))
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
