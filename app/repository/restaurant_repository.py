from app.extension import db
from app.models.restaurant_model import RestaurantModel

class RestaurantRepository:

    @staticmethod
    def create_restaurant(data):
        restaurant = RestaurantModel(**data)
        db.session.add(restaurant)
        db.session.commit()
        return restaurant

    @staticmethod
    def get_restaurant_by_uuid(restaurant_uuid):
        return RestaurantModel.query.filter_by(restaurant_uuid=restaurant_uuid, deleted_at=None).first()

    @staticmethod
    def get_all():
        return RestaurantModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_restaurant(restaurant, data):
        for key, value in data.items():
            setattr(restaurant, key, value)
        db.session.commit()
        return restaurant

    @staticmethod
    def delete_restaurant(restaurant):
        restaurant.deleted_at = db.func.current_timestamp()
        db.session.commit()
