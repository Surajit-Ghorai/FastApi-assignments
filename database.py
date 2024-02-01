from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

#engine = create_engine("postgresql://postgres:pgadmin1234@localhost/Quiz", echo= True)
#Base = declarative_base()
#Session_local = sessionmaker(bind=engine)

###
Base = declarative_base()
db_url = "postgresql+psycopg2://127.0.0.1:5432/Quiz?user=postgres&password=pgadmin1234"
engine = create_engine(db_url, connect_args={}, future= True)
Session_local = sessionmaker(autocommit= False, autoflush= False, bind= engine, future= True)