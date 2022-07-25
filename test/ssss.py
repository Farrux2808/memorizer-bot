
from sqlalchemy.orm import sessionmaker

import database
import domain
from db import connect



engine = connect()
user = domain.User()
# user.buildChatId(10).buildFullName('farrux').buildMenuUrl('sdf/sdf').buildPhone('sdf').buildUserId(15)
# a = domain.UserRepository(engine)
# a.creat(user)


# Session = sessionmaker(bind=engine)
# session = Session()

u = domain.UserRepository.sncById(12)
print(u)
