from services.database.database import DB

def posts_innerjoin():
    db: DB = DB()
    post = db.get_posts_innerjoin()

    return post
