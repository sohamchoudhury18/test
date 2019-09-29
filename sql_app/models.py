from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, String , Float
from sqlalchemy import MetaData
from sql_app import database as db
from pydantic import BaseModel ,BaseConfig


class Row(db.Base):
    __tablename__ = "pincode"

    pin = Column(String, primary_key=True, index=True)
    place_name = Column(String, unique=True, index=True)
    state = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)





#reflect an existing database into a new model.
AutoMapBase = automap_base()
# mapped classes are now created with names by default
# matching that of the table name.
AutoMapBase.prepare(db.engine,reflect=True)

class Pincode(AutoMapBase.classes.pincode):
    table = AutoMapBase.classes.pincode
