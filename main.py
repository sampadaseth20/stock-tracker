from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("MY_NAME")

print(name)