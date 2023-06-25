from services.database.database import DB

def get_all_users():
    db: DB = DB()
    users = db.get_all_users()

    return users
