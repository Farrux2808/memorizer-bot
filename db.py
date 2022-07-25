from sqlalchemy import create_engine

url = 'mysql://root:Pass_123@localhost/memorizer'

def connect():
    global engine
    engine = create_engine(url, echo=True)
    return engine


# # user = Session(User)

# user = UserModelClass()
# user.user_id= 124124
# user.phone = '+234234'
# user.chat_id = 23423
# user.menu_url = 'sdf/sdfs'
# user.full_name = "farrux"

# session.add(user)
# our_user = session.query(User).filter_by(full_name='farrux').first() 
# session.commit()