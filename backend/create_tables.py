# this is just a one-off script to create tables
from database import engine, Base
from models import Incident

Base.metadata.create_all(bind=engine)