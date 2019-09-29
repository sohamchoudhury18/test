from sqlalchemy.orm import Session
from sql_app import database as db
from sql_app import models as models
from sql_app import schemas as schemas


def get_info(sess,longitude: float , latitude: float):
    res = sess.query(models.Pincode.pin,
                     models.Pincode.state,
                     models.Pincode.place_name).filter(models.Pincode.latitude == longitude ,
                                               models.Pincode.longitude == latitude)
    temp_list = []
    for row in res:
        key_list = row.keys()
        value_list = row
        dict_value = dict(zip(key_list,value_list))
        temp_list.append(dict_value)
    return temp_list

def create_info(sess ,pinrow: schemas.PinRow):
    new_row = models.Pincode.table(pin = pinrow.pin,
                                   place_name = pinrow.place_name ,
                                   state = pinrow.state ,
                                   longitude = pinrow.longitude ,
                                   latitude = pinrow.latitude)
    sess.add(new_row)
    sess.commit()
    sess.refresh(new_row)
    return new_row


models.Pincode

# sess.refresh()

# temp = models.pincode_table(pin = "x" , place_name = "xx" , state = "xxxx" , longitude = 000 , latitude = 000)
# sess.add(temp)
# sess.commit()
# sess.refresh(temp)
# sess.close()
# x = sess.query(models.pin,models.state,models.place_name).filter(models.pincode_table.pin == "x")
# for i in x:
#     print(i)
