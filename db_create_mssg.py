from crud import db,app
from crud.models import Messages
import datetime


try:
    q = Messages.query.filter_by(nickname='Napoleon').one()
    pass

except:

    m = Messages(nickname='Napoleon')
    m.date_message= datetime.datetime.utcnow()
    m.message= 'If you build an army of 100 lions and their leader is a dog, in any fight, the lions will die like a dog. But if you build an army of 100 dogs and their leader is a lion, all dogs will fight as a lion'
    db.session.add(m)
    db.session.commit()


    m1 = Messages(nickname='Anonymous')
    m1.date_message= datetime.datetime.utcnow()
    m1.message= 'qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem'
    db.session.add(m1)
    db.session.commit()



    m2 = Messages(nickname='Random Guy')
    m2.date_message= datetime.datetime.utcnow()
    m2.message= 'qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem'
    db.session.add(m2)
    db.session.commit()
