from services.interface import *

# python
from flask import(
    Flask,
    request,
    redirect,
    render_template,
    url_for,
    session,
    g
)
from decouple import config
import datetime

app: Flask = Flask(__name__)
app.secret_key = "dslakfjlskfjasfs5f5644d4"


@app.route('/',methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        user: dict = {
            "name" : request.form.get('name'),
            "nickname" : request.form.get('nickname'),
            "is_author" : request.form.get('is_author'),
            "password" : request.form.get('password'),
            "rpassword" : request.form.get('rpassword'),
        }
        result = registrate_user(data=user)

        if result == 1:
            error: str = "пользователь с таким ником уже существует"
            return render_template(
                template_name_or_list="registration.html",
                error=error
            )

        if result == 2:
            error: str = "пароли не совпадают"
            return render_template(
                template_name_or_list="registration.html",
                error=error
            )
        if result == 3:
            error: str = "заполните все поля"
            return render_template(
                template_name_or_list="registration.html",
                error=error
            )
        
        if result == 4:
            error: str = "пишите только yes / no"
            return render_template(
                template_name_or_list="registration.html",
                error=error
            )
        

        if not session.get("nickname") == None:

            if str(session.get('is_author')).lower() == 'yes':
                if result == 0:
                    return redirect(url_for("posts"))

            if str(session.get('is_author')).lower() == 'no':
                if result == 0:
                    return redirect(url_for("posts2"))
           

    return render_template(
        template_name_or_list="registration.html"
    )

@app.route("/authorization", methods=['GET','POST'])
def authorization():
    if request.method == 'POST':
        user: dict = {
            "nickname" : request.form.get('nickname'),
            "password" : request.form.get('password')
        }
        result = authorizate_user(user)

        if result == 3:
            error: str = "заполните все поля"
            return render_template(
                template_name_or_list='authorization.html',
                error=error
            )
        
        if result == 1:
            error: str = "никнэйм или пароль введены неправильно"
            return render_template(
                template_name_or_list='authorization.html',
                error=error
            )        
        
        if not session.get("nickname") == None:

            if str(session.get('is_author')).lower() == 'yes':
                if result == 0:
                    return redirect(url_for("posts"))

            if str(session.get('is_author')).lower() == 'no':
                if result == 0:
                    return redirect(url_for("posts2"))
    
    return render_template(
        template_name_or_list='authorization.html'
    )


@app.route("/posts", methods=['GET','POST'])
def posts():
    if g.nickname:
        nickname=session.get('nickname')
        all_posts = posts_innerjoin()
        all_posts = luchsh(all_posts)
        return render_template(
            template_name_or_list="posts.html",
            posts=all_posts,
            nickname=nickname
        )
    return redirect(url_for("authorization"))

@app.route("/makepost/<user_nick>",methods=['GET','POST'])
def make_post(user_nick):

    user_nick = session.get("nickname")

    if request.method == 'POST':
        
        post: dict = {
            'author_id': session.get('user_id'),
            'title': request.form.get('title'),
            'main_text': request.form.get('main_text'),
            'raite': 0,
            'date' : f'{datetime.datetime.now()}'
        }
        result = create(post)
        
        if result == 3:
            error: str = "заполните все поля!"
            return render_template(
                template_name_or_list='make_post.html',
                nickname=user_nick,
                error=error
            )
        
        if result == 1:
            error: str = "такой пост уже существут :Э"
            return render_template(
                template_name_or_list='make_post.html',
                nickname=user_nick,
                error=error
            )            

        if result == 0:
            error: str = "пост успешно доваблен!"
            return render_template(
                template_name_or_list='make_post.html',
                nickname=user_nick,
                error=error
            ) 
        
    return render_template(
        template_name_or_list='make_post.html',
        nickname=user_nick
    )

@app.route("/posts2", methods=['GET','POST'])
def posts2():
    if g.nickname:
        nickname=session.get('nickname')
        all_posts = posts_innerjoin()
        all_posts = luchsh(all_posts)
        return render_template(
            template_name_or_list="posts2.html",
            posts=all_posts,
            nickname=nickname
        )
    return redirect(url_for("authorization"))


@app.route("/post/<post_id>/raiting", methods=['GET','POST'])
def raitete(post_id):

    all_comments = main_comments(post_id)
    post = get_post_post(post_id)
    user = get_user_post(post_id)

    if str(session.get('is_author')).lower() == 'yes':
        ssylka = 'posts' 

    if str(session.get('is_author')).lower() == 'no':
        ssylka = 'posts2'

    if request.method == 'POST':
        raiting: dict = {
            'user_id' : session.get("user_id"),
            'post_id' : post_id,
            'raiting' : request.form.get('raite')
        }
        print(post_id)            
        print(session.get("user_id"))            
        print(request.form.get("raite"))            
        result_r = raite_add(raiting)

        if result_r == 3:
            error_r = "поле пустое >:("
            return render_template(
                template_name_or_list="post.html",
                error_r=error_r,
                post_id=post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka
            )           

        if result_r == 1:
            error_r = "голосовать можно только одина раз"
            return render_template(
                template_name_or_list="post.html",
                error_r=error_r,
                post_id=post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka
            )
        if result_r == 0:
            return redirect(
                url_for(
                "post",
                post_id = post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka               
                )
            )      
    return render_template(
        template_name_or_list = "post.html",
        post_id = post_id,
        post = post,
        author = user[0][2],
        all_comments=all_comments,
        ssylka=ssylka
    )      

        
@app.route("/post/<post_id>", methods=['GET','POST'])
def post(post_id):

    all_comments = main_comments(post_id)
    post = get_post_post(post_id)
    user = get_user_post(post_id)
    
    print(post)
    if str(session.get('is_author')).lower() == 'yes':
        ssylka = 'posts' 

    if str(session.get('is_author')).lower() == 'no':
        ssylka = 'posts2'

    if request.method == 'POST':
        comment: dict = {
            'text' : request.form.get('text'),
            'post_id' : post_id,
            'user_id' : session.get("user_id")
        }

        result = to_comment(comment)


        if result == 3:
            error = "напишите что-нибудб"
            return render_template(
                template_name_or_list="post.html",
                error=error,
                post_id=post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka
            )
        
        if result == 1:
            error = "вы уже писали такой комментарий под этим постом!"
            return render_template(
                template_name_or_list="post.html",
                error=error,
                post_id=post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka
            )

        if result == 0:
            print(main_comments(1))
            return redirect(
                url_for(
                "post",
                post_id = post_id,
                post = post,
                author = user[0][2],
                all_comments=all_comments,
                ssylka=ssylka               
                )
            )
            
    return render_template(
        template_name_or_list = "post.html",
        post_id = post_id,
        post = post,
        author = user[0][2],
        all_comments=all_comments,
        ssylka=ssylka
    )


@app.before_request
def before_request():
    g.nickname = None

    if 'nickname' in session:
        g.nickname = session['nickname']

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )
