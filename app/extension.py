from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize database and migration objects
db = SQLAlchemy()
migrate = Migrate()
