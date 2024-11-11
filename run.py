from app.config import create_config
from app.startup import add_to_startup
from app.sync import sync_files
from app.encryption import generate_key

if __name__ == "__main__":
    # generate_key()
    create_config()
    add_to_startup()
    sync_files()
