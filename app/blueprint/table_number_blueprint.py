from flask_smorest import Blueprint
from flask import abort
from app.repository.table_number_repository import TableNumberRepository
from app.schema.table_number_schema import TableNumberSchema

table_blp = Blueprint('tables', 'tables', url_prefix='/tables', description="Operations for table numbers")

@table_blp.route("/", methods=['POST'])
@table_blp.arguments(TableNumberSchema)
@table_blp.response(201, TableNumberSchema)
def create_table(data):
    return TableNumberRepository.create_table(data)

@table_blp.route("/<uuid:table_uuid>", methods=['GET'])
@table_blp.response(200, TableNumberSchema)
def get_table_by_uuid(table_uuid):
    table = TableNumberRepository.get_table_by_uuid(str(table_uuid))
    if not table:
        abort(404, description="Table not found")
    return table

@table_blp.route("/", methods=['GET'])
@table_blp.response(200, TableNumberSchema(many=True))
def get_all_tables():
    return TableNumberRepository.get_all()

@table_blp.route("/<uuid:table_uuid>", methods=['PUT'])
@table_blp.arguments(TableNumberSchema)
@table_blp.response(200, TableNumberSchema)
def update_table(data, table_uuid):
    table = TableNumberRepository.get_table_by_uuid(str(table_uuid))
    if not table:
        abort(404, description="Table not found")
    return TableNumberRepository.update_table(table, data)

@table_blp.route("/<uuid:table_uuid>", methods=["DELETE"])
@table_blp.response(204)
def delete_table(table_uuid):
    table = TableNumberRepository.get_table_by_uuid(str(table_uuid))
    if not table:
        abort(404, description="Table not found")
    TableNumberRepository.delete_table(table)
    return ''
