from services.database.database import DB,Raiting

def raite_add(data: dict):
    raiting: Raiting = Raiting(
        user_id=data.get("user_id"),
        post_id=data.get("post_id"),
        raiting=data.get("raiting")
    )
    db: DB = DB()

    result_of_raite = db.add_raite(raiting)

    if result_of_raite == 3:
        return 3

    if result_of_raite == 1:
        return 1
    
    if result_of_raite == 0:
        return 0
