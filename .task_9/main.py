from flask import Flask, request, jsonify, render_template
import json
import os
import psycopg2
import init_db

app=Flask(__name__)

env = os.environ.get("ENV", "staging")
author = os.environ.get("AUTHOR", "devops")
http_port = os.environ.get("HTTP_PORT", "80")
# db_host = os.environ.get("DB_HOST", "database")
# db_port = os.environ.get("DB_PORT", "5432")
# db_user = os.environ.get("DB_USER", "reader")
# db_password = os.environ.get("DB_PASSWORD", "reader123")
# db_name = os.environ.get("DB_NAME", "books")

@app.route('/', methods=['GET'])
def default():
    res = {
	    'string': 'Pod',
        'env': env,
        'http_port': http_port
	}
    return jsonify(res)

@app.route('/check-ingress', methods=['GET'])
def check_ingress():
    res = {
        'domain': request.headers['Host'],
        'endpoint': '/check-ingress',
        'full_path:': request.headers['Host'] + '/check-ingress'
    }
    return res

@app.route('/practice', methods=['GET'])
def practice():
    res = {
        'author': author,
        'message': "Well DONE!"
    }
    return res
    

# @app.route('/get-pod', methods=['GET'])
# def get_pod():
#     with open('/mnt/data.json', 'r') as outfile:
#         data = json.loads(outfile.read())
#     print(data)
#     return jsonify(data)

# def postgres():
#     conn = psycopg2.connect(
#         host=db_host,
#         database=db_name,
#         user=db_user,
#         password=db_password,
#         port=db_port)
#     init_db.init_db()
#     return conn

# @app.route('/get-book', methods=['GET'])
# def get_book():
#     con = postgres()
#     cur = con.cursor()
#     query = "SELECT * FROM books"
#     cur.execute(query=query)
#     books = cur.fetchall()
#     cur.close()
#     con.close()
#     print(books)
#     return render_template('index.html', books=books)

# @app.route('/select-book', methods=['GET'])
# def select_book():
#     id = request.args.get("id")
#     con = postgres()
#     cur = con.cursor()
#     query = "SELECT * FROM {book} WHERE id={id} ".format(id=id, book="book")
#     cur.execute(query=query)
#     books = cur.fetchall()
#     cur.close()
#     con.close()
#     return render_template('index.html', books=books)
    