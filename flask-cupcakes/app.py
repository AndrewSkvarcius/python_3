"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from flask_cors import CORS



app = Flask(__name__)
app.app_context().push()
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/api/cupcakes", methods=["GET"])
def list_cupcakes():

    all_cakes = Cupcake.query.all()
    cupcakes = [cupcake.serialize_cakes() for cupcake in all_cakes]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake, and return data about new cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    # POST requests should return HTTP status of 201 CREATED
    return (jsonify(cupcake=cupcake.serialize_cakes()), 201)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cakes(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize_cakes())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def cupcake_update(cupcake_id):

    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize_cakes())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cakes(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Removed")

