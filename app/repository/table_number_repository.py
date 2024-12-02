from app.extension import db
from app.models.table_number_model import TableNumberModel

class TableNumberRepository:

    @staticmethod
    def create_table(data):
        table = TableNumberModel(**data)
        db.session.add(table)
        db.session.commit()
        return table

    @staticmethod
    def get_table_by_uuid(table_uuid):
        return TableNumberModel.query.filter_by(table_uuid=table_uuid, deleted_at=None).first()

    @staticmethod
    def get_all():
        return TableNumberModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_table(table, data):
        for key, value in data.items():
            setattr(table, key, value)
        db.session.commit()
        return table

    @staticmethod
    def delete_table(table):
        table.deleted_at = db.func.current_timestamp()
        db.session.commit()
