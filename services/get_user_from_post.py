from services.database.database import DB

def get_user_post(post_id: int):
    db: DB = DB()
    user = db.get_user_from_post(post_id)

    return user

