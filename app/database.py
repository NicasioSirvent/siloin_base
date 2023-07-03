from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://usr:pwd@localhost:5432/siloin')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
  # import all modules here that might define models so that
  # they will be registered properly on the metadata.  Otherwise
  # you will have to import them first before calling init_db()
  from models import Base
  Base.metadata.create_all(bind=engine)
