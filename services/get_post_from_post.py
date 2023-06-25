from services.database.database import DB

def get_post_post(post_id: int):
    db: DB = DB()
    post = db.get_post_from_post(post_id)

    return(post)
