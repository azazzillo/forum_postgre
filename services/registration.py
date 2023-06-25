from flask import session

from services.database.database import User, DB

def registrate_user(data: dict) -> int:
    
    
    user = User(
        name=data.get("name"),
        nickname=data.get("nickname"),
        is_author=data.get("is_author"),
        password=data.get("password")
    )

    if user.password != data.get("rpassword"):
        return 2
    
    db: DB = DB()
    result_of_regostration = db.registrate_user(data=user)
    all_users = db.get_all_users()

    if not isinstance(result_of_regostration, int):
        return 3

    if result_of_regostration == 3:
        return 3
    
    if result_of_regostration == 4:
        return 4
    for i in all_users:
        if i[2] == user.nickname:
            user_id = i[0]

    if result_of_regostration == 0:
        if result_of_regostration == 0:

            session['logged_in'] = True
            session['nickname'] = user.nickname
            session['is_author'] = user.is_author
            session['user_id'] = user_id

            return 0
        return 0
    
    return 1