from services.database.database import DB, Post

def create(data: dict):
    post = Post(
        author_id=data.get('author_id'),
        title=data.get('title'),
        main_text=data.get('main_text'),
        raite=data.get('raite'),
        date=data.get('date'),
    )

    db: DB = DB()
    result_of_posting = db.create_post(post)

    if result_of_posting == 3:
        return 3
    
    if result_of_posting == 1:
        return 1
    
    if result_of_posting == 0:
        return 0
