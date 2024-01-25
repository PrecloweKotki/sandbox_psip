import sqlalchemy.orm
from geoalchemy2 import Geometry
import os
from dotenv import load_dotenv







engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

Base = sqlalchemy.orm.declarative.base()

class User(Base):
    __tablename__ = 'table'

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location = Column('geom',Geometry(geometry_type = 'POINT', srid=4326),nullabe=True)

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


userlist: list = []
for item in range(10_000):
userlist.append(
    User(
        name=fake.name()

    )
)
session.add_all(object_to_add)