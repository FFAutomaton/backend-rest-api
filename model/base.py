from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from constants import postgre_pass


temp = "postgresql://postgres:" + postgre_pass + "@localhost:5432/anlat"
engine = create_engine(temp)
Session = sessionmaker(bind=engine)

Base = declarative_base()
