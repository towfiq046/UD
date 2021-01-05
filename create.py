"""Creates all the tables"""


from flask import Flask
from model import db
from env import PASSWORD, DATABASE



app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + PASSWORD + '@localhost/' + DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



def main():
    """Main func"""
    db.create_all()



if __name__ == "__main__":
    with app.app_context():
        main()
