import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgresUser:password@172.17.0.2:5432/ticket_table"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

app = create_app()

db = SQLAlchemy(app)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Integer)

db.create_all()

test_ticket1 = Ticket(name='Mt. Joy', price = 100)
test_ticket2 = Ticket(name="odesza", price = 50)


db.session.add(test_ticket1)
db.session.add(test_ticket2)
db.session.commit()

h = Ticket.query.all()

@app.route("/home")
def home():
    dic = {"name": [], "price": []}
    for tick in h:
        dic["name"].append(tick.name)
        dic["price"].append(tick.price)


    return str(dic)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
