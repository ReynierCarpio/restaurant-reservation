from app.extension import db
from app.models.reservation_model import ReservationModel

class ReservationRepository:

    @staticmethod
    def create_reservation(data):
        reservation = ReservationModel(**data)
        db.session.add(reservation)
        db.session.commit()
        return reservation

    @staticmethod
    def get_reservation_by_uuid(reservation_uuid):
        return ReservationModel.query.filter_by(reservation_uuid=reservation_uuid, deleted_at=None).first()

    @staticmethod
    def get_all():
        return ReservationModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_reservation(reservation, data):
        for key, value in data.items():
            setattr(reservation, key, value)
        db.session.commit()
        return reservation

    @staticmethod
    def delete_reservation(reservation):
        reservation.deleted_at = db.func.current_timestamp()
        db.session.commit()
