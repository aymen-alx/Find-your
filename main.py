from models import db
from flask import Flask
from flask_login import LoginManager, current_user
from models.user import User
from models.interest import Interest
from models.message import Message
from models.match import Match
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey__@4342'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
socketio = SocketIO(app)

app.app_context().push()
db.create_all()
login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)



# =================Routs=======================
@app.route('/home')
def home():
    return 'Home'



@app.route('/messages')
def messages():
    messages = Message.query.filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id)).order_by(Message.timestamp.desc()).all()

    return render_template('messages.html', messages=messages)









if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
