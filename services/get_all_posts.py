from services.database.database import DB, Post

def get_all_posts():
    db: DB = DB()
    result = db.all_posts()
    
    return result
