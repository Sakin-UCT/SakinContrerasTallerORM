from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///reservas.db",
    echo=False
    )

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False
)