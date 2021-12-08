import os

API_KEY = "UVvm0w9bs9oi33bHeBbD03MgQx9B5QpeuXrZijXk0qZOFSw4ubzqqmel8tfevyZT"
API_SECRET = "OeBqxnd4YdmNKaVannukTYPacqRHbwqUUk8igSZ8GggyyGmocKiWaemddaZMOCGU"
SECRET_KEY = '#$%^&*'

PSG_PASSWORD = os.environ.get("PSG_PASSWORD", "password")
PSG_USER = os.environ.get("PSG_USER", "user")
PSG_HOST = os.environ.get("PSG_HOST", "localhost")
SQLALCHEMY_DATABASE_URI = f"postgresql://{PSG_USER}:{PSG_PASSWORD}@{PSG_HOST}:5432/turk_force"
SQLALCHEMY_TRACK_MODIFICATIONS = False

