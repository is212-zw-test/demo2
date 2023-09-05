from flask import jsonify, abort, request
from classes.CustomException import CustomException
from models.models import RoleListing, db
from config import app

@app.errorhandler(404)
def handle_resource_not_found(e):
    """Handles exception thrown when flask app is aborted using `abort` with HTTP status code 404."""
    app.logger.exception(e)
    data = CustomException(str(e)).json()
    return jsonify(data=data), 404


@app.errorhandler(400)
def handle_bad_request(e):
    """Handles exception thrown when flask app is aborted using `abort` with HTTP status code 400."""
    app.logger.exception(e)
    data = CustomException(str(e)).json()
    return jsonify(data=data), 400


@app.errorhandler(Exception)
def handle_unhandled_exception(e: Exception):
    app.logger.exception(e)
    data = CustomException(str(e)).json()
    return jsonify(data=data), 500

@app.route('/api/hi')
def heartbeat():
    return jsonify({'message': 'Hello World'})

@app.route("/api/listings")
def find_all_listings():
    listings = db.session.execute(db.select(RoleListing)).scalars().all()
    data = [l.json() for l in listings]
    return jsonify(data=data), 200


@app.route("/api/listings/<uuid:id>")
def find_listing_by_id(id):
    listing = (
        db.session.execute(db.select(RoleListing).where(RoleListing.id == id)).scalars().first()
    )

    if listing is None:
        abort(404, description=f"RoleListing {str(id)} not found.")

    data = listing.json()
    return jsonify(data=data), 200


@app.route("/api/listings", methods=["POST"])
def create_listing():
    body = request.get_json()
    app.logger.info(f"POST /api/listings request body: {body}")

    listing = RoleListing(**body)
    db.session.add(listing)
    db.session.commit()

    return jsonify(data=listing.json()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=5000)
