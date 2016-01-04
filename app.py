#coding:utf-8
import os
from bottle import route, run, template, static_file, post, request

@route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root='static')

@route("/")
def index():
    return template("index")

if __name__ == '__main__':
    if os.getenv("HEROKU")==None:       
        # local
        #run(host="localhost", port=(os.environ.get("PORT",5100)), debug=True, reloader=True)
        # githubpages
        run(host="192.168.3.6", port=(os.environ.get("PORT",5100)), debug=True, reloader=True)
    else:
        run(host="0.0.0.0", port=(os.environ.get("PORT",5200)), debug=True, reloader=True)
