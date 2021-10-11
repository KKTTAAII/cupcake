"""Flask app for Cupcakes"""

from types import resolve_bases
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake, DEFAULT_PIC

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "EvieTheCutiePie"

connect_db(app)

@app.route("/api/cupcakes")
def get_cupcakes():
    """Get all the cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Show a cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a new cupcake and returns JSON of that cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"],
    size=request.json["size"], rating=request.json["rating"], image=request.json.get("image", DEFAULT_PIC))
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Updates a particular cupcake and responds w/ JSON of that updated cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size",  cupcake.size)
    cupcake.rating = request.json.get("rating",  cupcake.rating)
    cupcake.image = request.json.get("image",  cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes a particular todo"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
