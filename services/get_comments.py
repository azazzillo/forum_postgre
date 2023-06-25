from services.database.database import DB

def main_comments(data: int):
    db: DB = DB()

    comments = db.main_comments(data)

    return comments