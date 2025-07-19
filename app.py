from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['Post'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Here you can add logic to save to database, send email, etc.

    return jsonify({
        'status': 'success',
        'name': name,
        'email': email,
        'message': message
    })

if __name__ == '__main__':
    app.run(debug=True)
