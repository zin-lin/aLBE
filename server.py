#Author: Zin Lin Htun

import bcrypt
from flask import *
from flask_cors import *
from flask_bcrypt import *
from models import *

app = Flask(__name__)

#configuration
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' #allows CORS
app.config['SECRETE_KEY'] = 'annex-logistics' #set up Database with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

#inits
bcrypt = Bcrypt(app)
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route("/home")
@cross_origin()
def home():
    return "Hello World"

@app.route("/morgan")
@cross_origin()
def morgan():
    return str("Morgan")

@app.route("/freeman")
@cross_origin()
def freeman():
    return "Freeman"

@app.route("/new")
@cross_origin()
def new():
    return "Hello new user welcome"

@app.route("/free/<int:id>", methods = ['GET'])
@cross_origin()
def free(id):
    return str(id)

@app.route('/register', methods= ['GET','POST'])
@cross_origin()
def register():
    # email = request.json['email']
    # password = request.json['password']
    email = "dfff_00@gmail.com"
    password = "xcmkxcmkxmckm"
    user_exists=False
    try:
        user_exists = User.query.filter_by(email=email).first()
    except:
        print("table hasn't been created, creating table")


    hashed = bcrypt.generate_password_hash(password)
    new_user = User(email = email, password= hashed)

    if user_exists:
        return jsonify({"error":"Ready as I'll ever be"}), 409

    db.session.add(new_user)
    db.session.commit()

    return "Hello"

if __name__ == '__main__':
    app.run()