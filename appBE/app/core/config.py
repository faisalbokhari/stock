
# app/core/config.py

SECRET_KEY = "your-secret-key"  # Replace with a secure key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5000
DATABASE_URL = "postgresql://psqdbuser:password@localhost:5432/stockdb"
