from datetime import date


from model.base import Session, engine, Base
from model.users import Users


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

temp = Users('anil', 'anan@hotmail.com', '3131', str(date), True)

session.add(temp)
session.commit()
session.close()