from flask import session
from services.database.database import User,DB
from services.get_all_users import get_all_users

def authorizate_user(data:dict):
    user = User(
        name="",
        nickname=data.get("nickname"),
        is_author="",
        password=data.get("password")
    )
    db: DB = DB()

    result_of_authorization = db.authorization(data=user)
    all_users = get_all_users()

    for i in all_users:
        if i[2] == user.nickname:
            is_author = i[3]
            print(i, is_author)

    if result_of_authorization == 3:
        return 3
    
    for i in all_users:
        if i[2] == user.nickname:
            user_id = i[0]

    if result_of_authorization == 0:
        session['logged_in'] = True
        session['nickname'] = user.nickname
        session['is_author'] = is_author
        session['user_id'] = user_id

        return 0
    
    return 1
