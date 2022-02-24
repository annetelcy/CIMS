from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)


class Product(db.Model):

    __tablename__ = 'products'
    product_id      = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_id

class Location(db.Model):
    __tablename__   = 'locations'
    location_id     = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Location %r>' % self.location_id

class ProductMovement(db.Model):

    __tablename__   = 'productmovements'
    movement_id     = db.Column(db.Integer, primary_key=True)
    product_id      = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    qty             = db.Column(db.Integer)
    from_location   = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    to_location     = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    movement_time   = db.Column(db.DateTime, default=datetime.utcnow)

    product         = db.relationship('Product', foreign_keys=product_id)
    fromLoc         = db.relationship('Location', foreign_keys=from_location)
    toLoc           = db.relationship('Location', foreign_keys=to_location)
    
    def __repr__(self):
        return '<ProductMovement %r>' % self.movement_id

@app.route('/', methods=["POST", "GET"])
def index():
        
    if (request.method == "POST") and ('product_name' in request.form):
        product_name    = request.form["product_name"]
        new_product     = Product(product_id=product_name)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/")
        
        except:
            return "There Was an issue while add a new Product"
    
    if (request.method == "POST") and ('location_name' in request.form):
        location_name    = request.form["location_name"]
        new_location     = Location(location_id=location_name)

        try:
            db.session.add(new_location)
            db.session.commit()
            return redirect("/")
        
        except:
            return "There Was an issue while add a new Location"
    else:
        products    = Product.query.order_by(Product.date_created).all()
        locations   = Location.query.order_by(Location.date_created).all()
        return render_template("index.html", products = products, locations = locations)

@app.route('/locations/', methods=["POST", "GET"])
def viewLocation():
    if (request.method == "POST") and ('location_name' in request.form):
        location_name = request.form["location_name"]
        new_location = Location(location_id=location_name)

        try:
            db.session.add(new_location)
            db.session.commit()
            return redirect("/locations/")

        except:
            locations = Location.query.order_by(Location.date_created).all()
            return "There Was an issue while add a new Location"
    else:
        locations = Location.query.order_by(Location.date_created).all()
        return render_template("locations.html", locations=locations)

