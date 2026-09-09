import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    r"mssql+pymssql://cloud:123Gaugau@roomhubshop.database.windows.net:1433/roomhubshop?charset=utf8"
)

engine = create_engine(DATABASE_URL)