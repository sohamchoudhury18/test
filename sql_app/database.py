from sqlalchemy import create_engine



#database url for postgres
db_url = "postgres://nhnkasrvutflfm:c9a474ad38b5aa3b2dbfd08d8c15eba100965502e7fc2eaccfdd7610a2a9c0d3@ec2-184-73-169-163.compute-1.amazonaws.com:5432/d2ifiv8t7kftei"

engine = create_engine(db_url)
conn = engine.connect()
