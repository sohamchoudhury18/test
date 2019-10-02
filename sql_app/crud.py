from sqlalchemy.orm import Session
from sqlalchemy import func
from sql_app import database as db
from sql_app import models as models
from sql_app import schemas as schemas


def getby_longlang(sess,longitude: float , latitude: float):
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
    sess.close()
    return temp_list

def getby_pin(sess,pin: str):
    res = sess.query(models.Pincode.pin).filter(models.Pincode.pin == pin ).first()
    sess.close()
    return res

def precision_check(sess,longitude: float , latitude: float):
    ress = sess.query(models.Pincode.pin).filter(func.trunc(models.Pincode.longitude,1) == func.trunc(longitude,1),
                                                 func.trunc(models.Pincode.latitude,1)==func.trunc(latitude,1)).first()
    sess.close()
    return ress

def create_info(sess ,pinrow: schemas.PinRow):
    new_row = models.Pincode.table(pin = pinrow.pin,
                                   place_name = pinrow.place_name ,
                                   state = pinrow.state ,
                                   longitude = pinrow.longitude ,
                                   latitude = pinrow.latitude)
    sess.add(new_row)
    sess.commit()
    sess.refresh(new_row)
    sess.close()
    return new_row
