import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21661450")

API_HASH = os.environ.get("API_HASH", "79612bc71908f95372808520a7eeee74")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6705941368:AAFmsbnucvohSVQpPfFgVpJKlvh85eogSdg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002169744829") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://MadhanBlastz:N0password@cluster0.4usvnqj.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/3edfa4f6b18c72d85e4d7.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2021408974').split()]

