from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "library_system")

client = None
db = None

if MONGODB_URI:
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        db = client[DATABASE_NAME]
    except Exception as e:
        logger.error("❌ Failed to initialize MongoDB client: %s", e)
else:
    logger.warning("⚠️  MONGODB_URI is not set in environment variables.")



async def init_db():
    if client is None:
        logger.error("❌ MongoDB client not initialized. Cannot connect to database.")
        return

    try:
        await client.server_info()
        logger.info("✅ MongoDB connected successfully.")
    except Exception as e:
        logger.error("❌ MongoDB connection failed: %s", e)
