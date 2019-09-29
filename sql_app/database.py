from sqlalchemy import create_engine
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


# from sql_app import models
#
# res = sess.query(models.Pincode.pin).filter(models.Pincode.pin == "IN/110044").first()
# res
#
# for r in res:
#     print(r.keys())
