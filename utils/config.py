from dotenv import load_dotenv
import os

load_dotenv()


def get_ip():
    ip = os.getenv("IP")
    return ip


def get_port():
    PORT = os.getenv("PORT")
    return PORT
