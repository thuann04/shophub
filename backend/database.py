import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    r"mssql+pymssql://shophub:gaugau%4012@shophub.database.windows.net:1433/hubroom?encrypt=yes"
)

engine = create_engine(DATABASE_URL)