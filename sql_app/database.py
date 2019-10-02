from sqlalchemy import create_engine , cast , CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker




#database url for postgres
db_url = "postgres://nhnkasrvutflfm:c9a474ad38b5aa3b2dbfd08d8c15eba100965502e7fc2eaccfdd7610a2a9c0d3@ec2-184-73-169-163.compute-1.amazonaws.com:5432/d2ifiv8t7kftei"
Base = declarative_base()
engine = create_engine(db_url)
conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sess = Session(engine)

#
# from sql_app import models
# from sqlalchemy import func
#
# ress = sess.query(models.Pincode.pin).filter(func.trunc(models.Pincode.longitude,1) == func.trunc(77.2,1),
#                                              func.trunc(models.Pincode.latitude,1)==func.trunc(28.6,1)).first()
#
#
# r = crud.precision_check(sess,77.2,28.6)
# type(r)
