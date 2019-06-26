from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///./db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def reinit_db():
    import tracker.database.models
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import tracker.database.models
    Base.metadata.create_all(engine)
