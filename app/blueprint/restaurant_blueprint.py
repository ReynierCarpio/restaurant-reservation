from flask_smorest import Blueprint
from flask import abort
from app.repository.restaurant_repository import RestaurantRepository
from app.schema.restaurant_schema import RestaurantSchema

# Define the blueprint
restaurant_blp = Blueprint('restaurants', 'restaurants', url_prefix='/restaurants', description="Operations for restaurants")

@restaurant_blp.route("/", methods=['POST'])
@restaurant_blp.arguments(RestaurantSchema)
@restaurant_blp.response(201, RestaurantSchema)
def create_restaurant(data):
    return RestaurantRepository.create_restaurant(data)

@restaurant_blp.route("/<uuid:restaurant_uuid>", methods=['GET'])
@restaurant_blp.response(200, RestaurantSchema)
def get_restaurant_by_uuid(restaurant_uuid):
    restaurant = RestaurantRepository.get_restaurant_by_uuid(str(restaurant_uuid))
    if not restaurant:
        abort(404, description="Restaurant not found")
    return restaurant

@restaurant_blp.route("/", methods=['GET'])
@restaurant_blp.response(200, RestaurantSchema(many=True))
def get_all_restaurants():
    return RestaurantRepository.get_all()

@restaurant_blp.route("/<uuid:restaurant_uuid>", methods=['PUT'])
@restaurant_blp.arguments(RestaurantSchema)
@restaurant_blp.response(200, RestaurantSchema)
def update_restaurant(data, restaurant_uuid):
    restaurant = RestaurantRepository.get_restaurant_by_uuid(str(restaurant_uuid))
    if not restaurant:
        abort(404, description="Restaurant not found")
    return RestaurantRepository.update_restaurant(restaurant, data)

@restaurant_blp.route("/<uuid:restaurant_uuid>", methods=["DELETE"])
@restaurant_blp.response(204)
def delete_restaurant(restaurant_uuid):
    restaurant = RestaurantRepository.get_restaurant_by_uuid(str(restaurant_uuid))
    if not restaurant:
        abort(404, description="Restaurant not found")
    RestaurantRepository.delete_restaurant(restaurant)
    return ''
