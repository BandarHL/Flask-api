from werkzeug.security import *
from flask import *
import json
from flask_jwt_extended import *
from user import User
from db import db
import os

app = Flask(__name__)
app.secret_key = "rdh%i$tzq)u^c2u5bjwrz(q^%w(lc(os5zb)7ry1o65*z-h^$z"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bandar:0B21v00ceXbLjdogDrIT@localhost/users' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}


def dump_content(content):
    with open('/var/www/webApp/webApp/templates/movies.json', mode='w', encoding='utf-8') as feedsjson:
        json.dump(content, feedsjson, ensure_ascii=False, indent=4)
    return jsonify({'msg': 'done'})


def load_movies():
    with open('/var/www/webApp/webApp/templates/movies.json', mode='r', encoding='utf-8') as lis:
        data = json.load(lis)
    return data


@app.route('/movies', methods=['GET', 'POST'])
@jwt_required
def movies():
    if request.method == 'GET':
        return jsonify(load_movies()), 200
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 404


@app.route('/movie/<int:_id>', methods=['GET', 'POST'])
@jwt_required
def movie(_id):
    if request.method == 'GET':
        return jsonify(load_movies()[_id]), 200
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 402


@app.route('/addMovie', methods=['GET', 'POST'])
@jwt_required
def addMovie():
    claims = get_jwt_claims()
    if not claims['is_admin']:
        return jsonify({'msg': 'Your not admin, so get fuck off from here'}), 401
    if request.method == 'POST':
        movies_list = load_movies()
        req = request.form
        json_of_new_movie = {
            'id': len(movies_list),
            'name': req.get('name'),
            'eps': []
        }
        movies_list.append(json_of_new_movie)
        dump_content(movies_list)
        return jsonify(json_of_new_movie), 201
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 404


@app.route('/addEpisode', methods=['GET', 'POST'])
@jwt_required
def addEpisode():
    if request.method == 'POST':
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return jsonify({'msg': 'Your not admin, so get fuck off from here'}), 401
        movies_list = load_movies()
        req = request.form
        for index, value in enumerate(movies_list):
            if str(value['id']) in req.get('id'):
                number_of_episode = len(value['eps'])
                json_of_new_episode = {
                    'id': number_of_episode,
                    'title': req.get('title'),
                    'video_url': req.get('url'),
                    'video_preview': req.get('preview_url')
                }
                value['eps'].append(json_of_new_episode)
                dump_content(movies_list)
                return jsonify(json_of_new_episode), 201
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 404


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        req = request.form
        username = req.get('username')
        password = req.get('password')
        if User.find_by_username(username):
            return jsonify({'msg': 'this username already exists'}), 400
        user = User(username, password)
        user.create_new_user()
        return jsonify({'msg': 'user successfully register', 'username': username, 'password': password}), 201
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.form
        user = User.find_by_username(req.get('username'))
        if user and safe_str_cmp(user.password, req.get('password')):
            token = create_access_token(identity=user.id, fresh=True)
            refresh = create_refresh_token(user.id)
            return jsonify({'access_token': token, 'refresh_token': refresh}), 200
        return jsonify({'msg': 'user not found'}), 404
    else:
        return jsonify({'msg': 'The method is not allowed for the requested URL.'}), 404


@app.route('/')
def root():
    return ''


if __name__ == '__main__':
    app.run()
