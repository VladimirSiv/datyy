import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "dburi": os.getenv("DBURI"),
    "log_folder": os.getenv("LOG_FOLDER"),
}
