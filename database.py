from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = "username"
password = quote_plus("password")
database = "FastAPI"

db_url = f"mysql+pymysql://{username}:{password}@localhost:3306/{database}"

engine = create_engine(db_url)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)