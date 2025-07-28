from flask import Flask, request, jsonify, render_template
import json
import uuid

app = Flask(__name__)

users = {}
user_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

# Create or Add New User
@app.route('/submit', methods=['POST'])
def submit():
    global user_id_counter
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    age = request.form.get('age')
    gender = request.form.get('gender')

    users[user_id_counter] = {
        "id": str(uuid.uuid4()),
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender
    }
    user_id_counter += 1

    return jsonify({'status': 'success', 'message': 'User added successfully'})

# Edit / Update Existing User
@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    if id in users:
        users[id]['first_name'] = request.form.get('firstName')
        users[id]['last_name'] = request.form.get('lastName')
        users[id]['age'] = request.form.get('age')
        users[id]['gender'] = request.form.get('gender')

        return jsonify({'status': 'success', 'message': 'User updated successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

# Get all users
@app.route('/user', methods=['GET'])
def get_users():
    print(jsonify(users))
    return jsonify(users)

# Delete user
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({'status': 'success', 'message': 'User deleted successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
