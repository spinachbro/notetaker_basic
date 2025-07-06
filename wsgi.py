from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app import app as flask_app
from flask import Response

def default_app(environ, start_response):
    response = Response('Not Found', status=404)
    return response(environ, start_response)

application = DispatcherMiddleware(default_app, {
    '/app2': flask_app
})
