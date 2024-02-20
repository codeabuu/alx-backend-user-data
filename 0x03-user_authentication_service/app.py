#!/usr/bin/env python3
'''set up a basic Flask app'''


from flask import jsonify, request, Flask, abort, redirect
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main() -> str:
    '''flask app to return'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    '''method to def users'''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    '''create a new session for the user'''
    email = request.form.get('email')
    password = request.form.get('password')

    if not(AUTH.valid_login(email, password)):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    '''the user exists destroy the session'''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
