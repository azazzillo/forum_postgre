import psycopg2
import datetime
from typing import NamedTuple

from services.settings.database_base import (
    TABLE_COMMENTS,
    TABLE_POSTS,
    TABLE_RAITINGS,
    TABLE_USERS
)

class User(NamedTuple):
    name: str
    nickname: str
    is_author: str
    password: str

class Post(NamedTuple):
    author_id: int
    title: str
    main_text: str
    raite: float
    date: datetime.datetime

class Comment(NamedTuple):
    text: str
    post_id: int
    user_id: int

class Raiting(NamedTuple):
    user_id: int
    post_id: int
    raiting: int

class DB:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            dbname='forum',
            user='postgres',
            password='admin',
            host='localhost'
        )
        self.cursor = self.connection.cursor()
        self.create_all_tables(
            TABLE_USERS, TABLE_COMMENTS,
            TABLE_POSTS, TABLE_RAITINGS
        )

    def execute(self, query: str, is_commit: int = 0):
        result = self.cursor.execute(query)
        if is_commit == 1:
            self.connection.commit()
        else:
            return self.cursor.fetchall()
    
    def create_all_tables(self, *tables: list[str]):
        for table in tables:
            self.execute(query=table, is_commit=1)

    def registrate_user(self, data: User):
        if (len(data.name) == 0) or \
        (len(data.nickname) == 0) or \
        (len(data.is_author) == 0) or \
        (len(data.password) == 0):
            return 3
        
        user_exists = self.execute(
            query=f'''
                SELECT id FROM users
                WHERE nickname='{data.nickname}'
                AND
                password='{data.password}'
            '''
        )
        if data.is_author.lower() != 'no'and \
        data.is_author.lower() != 'yes':
            return 4
         
        if len(user_exists) > 0:
            return 1
        
    
        result = self.execute(
            query=f'''
                INSERT INTO users (
                    name,
                    nickname,
                    is_author,
                    password
                ) VALUES (
                    '{data.name}',
                    '{data.nickname}',
                    '{data.is_author}',
                    '{data.password}'
                )
            ''',
                is_commit=1
        )
 
        return 0
    
    def authorization(self, data: User):

        if (len(str(data.nickname)) == 0) or \
        (len(str(data.password)) == 0):
            return 3 
        
        is_exist = self.execute(
            query=f'''
                SELECT id FROM users WHERE
                nickname='{data.nickname}'
                AND
                password='{data.password}'
            '''
        )

        if len(is_exist) > 0:
            return 0
        
        return 1
    
    def all_posts(self):
        posts = self.execute(
            query='''
                SELECT * FROM posts
                ORDER BY raite ASC;
            '''
        )
        print(posts)
        return posts
    
    def create_post(self, data: Post):
        is_exist = self.execute(
            query=f'''
                SELECT id FROM posts WHERE
                author_id={data.author_id}
                AND
                title='{data.title}'
                AND
                main_text='{data.main_text}'
                AND
                date='{data.date}'
            '''
        )
        if len(is_exist) > 0:
            return 1
        
        if (data.author_id == 0) or \
        (len(data.title) == 0) or \
        (len(data.main_text) == 0) or \
        (len(data.date) == 0):
            return 3
        
        post = self.execute(
            query=f'''
                INSERT INTO posts(
                    author_id,
                    title,
                    main_text,
                    raite,
                    date
                ) VALUES (
                    {data.author_id},
                    '{data.title}',
                    '{data.main_text}',
                    {data.raite},
                    '{data.date}'
                )
            ''',
            is_commit=1
        )
        return 0
    
    def get_all_users(self):
        users = self.execute(
            query='''
                SELECT * FROM users
            '''
        )
        return users
    
    def get_user_from_post(self,post_id: int):
        user_id = self.execute(
            query=f'''
                SELECT author_id FROM posts
                WHERE id = {int(post_id[0][0])}
            '''
        )
        user = self.execute(
            query=f'''
                SELECT * FROM users 
                WHERE id = {int(user_id[0][0])}
            '''
        )

        return user
    
    def get_post_from_post(self,post_id: int):
        post = self.execute(
            query=f'''
                SELECT * FROM posts
                WHERE id = {int(post_id[0][0])}
            '''
        )
        return post

    def get_posts_innerjoin(self):
        post = self.execute(
            query=f'''
                SELECT * FROM posts
                INNER JOIN users ON users.id = posts.author_id 
            '''
        )
        print(post)

        return post
    
    def make_comment(self, data: Comment):

        if len(data.text) == 0 or\
        data.post_id == None or \
        data.user_id == None:
            return 3
        
        is_exists = self.execute(
            f'''
                SELECT * FROM comments
                WHERE text = '{data.text}'
                AND
                post_id = {data.post_id}
                AND
                user_id = {data.user_id}
            '''
        )
        if len(is_exists) > 0:
            return 1
        
        comment = self.execute(
            f'''
                INSERT INTO comments
                (text,post_id,user_id) VALUES 
                ('{data.text}',{data.post_id},{data.user_id})
            ''',
            is_commit=1
        )

        return 0
    
    def all_comments(self):
        commets = self.execute(
            query='''
                SELECT * FROM comments
                INNER JOIN posts ON posts.id = comments.post_id
                INNER JOIN users ON users.id = comments.user_id
            '''
        )
        return commets
    
    def main_comments(self,post_id: int):
        comments = self.execute(
            query=f'''
                SELECT * FROM comments
                INNER JOIN posts ON posts.id = comments.post_id
                INNER JOIN users ON users.id = comments.user_id
                WHERE post_id = {post_id}
            '''
        )
        return comments

    
    def add_raite(self,data: Raiting):

        if len(str(data.raiting)) == 0:
            return 3
        
        is_exist = self.execute(
            query=f'''
                SELECT * FROM raitings
                WHERE user_id = {data.user_id}
                AND post_id = {data.post_id}
            '''
        )
        if len(is_exist) > 0:
            return 1
        
        raiting = self.execute(
            query=f'''
                INSERT INTO raitings(
                    user_id,
                    post_id,
                    raiting
                ) VALUES (
                    {data.user_id},
                    {data.post_id},
                    {data.raiting})
            ''',
            is_commit = 1
        )

        avg = self.execute(
            query=f'''
                SELECT AVG(raiting) FROM raitings
                WHERE post_id = {data.post_id}
            '''
        )
        
        update = self.execute(
            query=f'''
                UPDATE posts SET raite={round(avg[0][0],2)} 
                WHERE id = {data.post_id}
            ''',
            is_commit=1
        )

        return 0
