TABLE_USERS='''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(80) NOT NULL,
        nickname VARCHAR(80) UNIQUE NOT NULL,
        is_author VARCHAR(10) DEFAULT('no') NOT NULL,
        password VARCHAR(255) NOT NULL
    );
'''

TABLE_POSTS='''
    CREATE TABLE IF NOT EXISTS posts(
        id SERIAL PRIMARY KEY,
        author_id INTEGER REFERENCES users(id) NOT NULL,
        title VARCHAR(80) UNIQUE NOT NULL,
        main_text VARCHAR(5000) NOT NULL,
        raite FLOAT DEFAULT(0),
        date DATE DEFAULT(NOW()) NOT NULL
    );

'''

TABLE_COMMENTS='''
    CREATE TABLE IF NOT EXISTS comments(
        id SERIAL PRIMARY KEY,
        text VARCHAR(1500) NOT NULL,
        post_id INTEGER REFERENCES posts(id) NOT NULL,
        user_id INTEGER REFERENCES users(id) NOT NULL
    );

'''

TABLE_RAITINGS='''
    CREATE TABLE IF NOT EXISTS raitings(
        user_id INTEGER REFERENCES users(id) NOT NULL,
        post_id INTEGER REFERENCES posts(id) NOT NULL,
        raiting INTEGER CHECK( 0 <= raiting AND raiting <= 5) NOT NULL
    );

'''
