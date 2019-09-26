from sqlalchemy.orm import Session
from sql_app import database as db
from sql_app import models as models

sess = Session(db.engine)
#
# result = sess.query(pin,state,place_name).filter(pincode_table.latitude == 28.7556 , pincode_table.longitude == 77.1667)
#
# sam_list = []
# for row in result:
#     sam_list.append(row)
# s = json.dumps(sam_list)
# s
# type(s)

# res = sess.query(pin,state,place_name).filter(pincode_table.latitude == 28.7556 , pincode_table.longitude == 77.1667).first()
# type(res)
# key_list = res.keys()
# value_list = res
# key_list
# value_list
# d = dict(zip(key_list,value_list))
# e = json.dumps(d)
# e
#
# len(res.keys())
# for r in res:
#     print(r.asdict())

def get_info(longitude: float , latitude: float):
    res = sess.query(models.pin,models.state,models.place_name).filter(models.pincode_table.latitude == longitude , models.pincode_table.longitude == latitude)
    temp_list = []
    for row in res:
        key_list = row.keys()
        value_list = row
        dict_value = dict(zip(key_list,value_list))
        temp_list.append(dict_value)
    return temp_list


# get_info(latitude=77.1667,longitude=28.7556)
