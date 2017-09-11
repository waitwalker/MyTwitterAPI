from models import engine
from models.users import Base

def run():
    Base.metadata.create_all(engine)