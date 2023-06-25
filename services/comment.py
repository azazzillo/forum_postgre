from services.database.database import DB, Comment

def to_comment(data: dict):
    c= Comment(
        text=data.get("text"),
        post_id=data.get("post_id"),
        user_id=data.get("user_id")
    )
    db: DB = DB()

    result_of_comment = db.make_comment(c)

    if result_of_comment == 3:
        return 3
    
    if result_of_comment == 1:
        return 1
    
    if result_of_comment == 0:
        return 0
