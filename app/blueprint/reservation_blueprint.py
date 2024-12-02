from flask_smorest import Blueprint
from flask import abort
from app.repository.reservation_repository import ReservationRepository
from app.schema.reservation_schema import ReservationSchema

reservation_blp = Blueprint('reservations', 'reservations', url_prefix='/reservations', description="Operations for reservations")

@reservation_blp.route("/", methods=['POST'])
@reservation_blp.arguments(ReservationSchema)
@reservation_blp.response(201, ReservationSchema)
def create_reservation(data):
    return ReservationRepository.create_reservation(data)

@reservation_blp.route("/<uuid:reservation_uuid>", methods=['GET'])
@reservation_blp.response(200, ReservationSchema)
def get_reservation_by_uuid(reservation_uuid):
    reservation = ReservationRepository.get_reservation_by_uuid(str(reservation_uuid))
    if not reservation:
        abort(404, description="Reservation not found")
    return reservation

@reservation_blp.route("/", methods=['GET'])
@reservation_blp.response(200, ReservationSchema(many=True))
def get_all_reservations():
    return ReservationRepository.get_all()

@reservation_blp.route("/<uuid:reservation_uuid>", methods=['PUT'])
@reservation_blp.arguments(ReservationSchema)
@reservation_blp.response(200, ReservationSchema)
def update_reservation(data, reservation_uuid):
    reservation = ReservationRepository.get_reservation_by_uuid(str(reservation_uuid))
    if not reservation:
        abort(404, description="Reservation not found")
    return ReservationRepository.update_reservation(reservation, data)

@reservation_blp.route("/<uuid:reservation_uuid>", methods=["DELETE"])
@reservation_blp.response(204)
def delete_reservation(reservation_uuid):
    reservation = ReservationRepository.get_reservation_by_uuid(str(reservation_uuid))
    if not reservation:
        abort(404, description="Reservation not found")
    ReservationRepository.delete_reservation(reservation)
    return ''
