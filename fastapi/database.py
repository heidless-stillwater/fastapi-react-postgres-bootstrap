from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base  

URL_DATABASE="sqlite:///./finance.db"
engine = create_engine(URL_DATABASE, connect_args={"check_same_thread":False})

#URL_DATABASE = 'postgresql://bootstrap-user-0:GJaUUsg_%RYnXVCB@//cloudsql/cloud-run-install:europe-west2:bootstrap-instance-0/bootstrap-db-0'
#engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush="False", bind=engine)

Base = declarative_base()


