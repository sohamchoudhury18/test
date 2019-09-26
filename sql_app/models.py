from sqlalchemy.ext.automap import automap_base
from sql_app import database as db

#reflect an existing database into a new model.
Base = automap_base()

# mapped classes are now created with names by default
# matching that of the table name.
Base.prepare(db.engine, reflect=True)

pincode_table = Base.classes.pincode
pin = pincode_table.pin
place_name = pincode_table.place_name
state = pincode_table.state
longitude = pincode_table.longitude
latitude = pincode_table.latitude
