from flask_mongoengine import MongoEngine


db = None

def init_app(app):
    global db
    
    db = MongoEngine(app)
