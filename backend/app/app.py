from flask import Flask
from .db import db
from flask_migrate import Migrate
from .models import User, TextCreated, BookData, LineFetched, LineStamped

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://federa:unfilteredTOBACCO.369@localhost:3306/gPTA' # This is the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # This is just here to suppress a warning from SQLAlchemy as it will soon be removed


db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)