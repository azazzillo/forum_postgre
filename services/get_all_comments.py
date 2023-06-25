from services.database.database import DB

def get_all_comments():
    db: DB = DB()
    comments = db.all_comments
    print(comments)
    return comments
