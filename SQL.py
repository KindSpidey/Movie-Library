import sqlite3
import subprocess as sp


def create_table():
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    queryyActorNews = '''
            CREATE TABLE IF NOT EXISTS actnews(
                act_id  INT REFERENCES actor (id),
                news_id INT REFERENCES news (id) 
    )'''
    queryyActorFilm = '''
        CREATE TABLE IF NOT EXISTS actfilm(
            act_id  INT REFERENCES actor (id),
            film_id INT REFERENCES film (id) 
)
    '''
    queryActor = '''
        CREATE TABLE IF NOT EXISTS actor(
        	id    INTEGER CONSTRAINT actor_pk PRIMARY KEY,
            name  TEXT,
            phone TEXT,
            email TEXT,
            sex   TEXT,
            age  INT
        )
    '''
    queryDirector = '''
            CREATE TABLE IF NOT EXISTS director(
            id    INTEGER CONSTRAINT director_pk PRIMARY KEY,
            name  TEXT,
            phone TEXT,
            email TEXT
            )
        '''
    queryFilm = '''
            CREATE TABLE IF NOT EXISTS film(
            id              INTEGER CONSTRAINT film_pk PRIMARY KEY,
            title           TEXT,
            box_office      INT,
            rating          INT,
            year            INT,
            id_director     INT     REFERENCES director (id),
            id_screenwriter INT     REFERENCES screenwriter (name) 
            )
        '''
    queryAwards = '''
            CREATE TABLE IF NOT EXISTS awards(
            id   INTEGER CONSTRAINT awards_pk PRIMARY KEY AUTOINCREMENT,
            name TEXT)
        '''
    queryNews = '''
            CREATE TABLE IF NOT EXISTS news(
            id          INTEGER CONSTRAINT news_pk PRIMARY KEY AUTOINCREMENT,
            title       TEXT,
            description TEXT,
            link        TEXT,
            meaning     TEXT,
            year        INT
            )
        '''
    queryScreenwriter = '''CREATE TABLE IF NOT EXISTS screenwriter(
            	id INTEGER PRIMARY KEY, 
            	name TEXT,
                phone TEXT,
                email TEXT)'''
    queryWinners = '''
            CREATE TABLE IF NOT EXISTS winners(
            	id INTEGER PRIMARY KEY, 
                year INTEGER,
                id_award INTEGER,
                id_actor INTEGER,
                id_director INTEGER,
                id_screenwriter INTEGER
            )
        '''
    cursor.execute(queryActor)
    cursor.execute(queryDirector)
    cursor.execute(queryFilm)
    cursor.execute(queryWinners)
    cursor.execute(queryNews)
    cursor.execute(queryScreenwriter)
    cursor.execute(queryAwards)
    cursor.execute(queryyActorFilm)

    conn.commit()
    conn.close()
def connect_film_and_actor(film_title, actor_name):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
        SELECT id
        FROM film
        WHERE title ={film_title!r} 
        UNION 
        SELECT id
        FROM actor
        WHERE name ={actor_name!r}'''
    b = cursor.execute(query)

    all_rows2 = cursor.fetchall()
    wtf = all_rows2[0]+all_rows2[1]
    actID, filmID = wtf[0], wtf[1]
    query ='''
    INSERT INTO actfilm(act_id, film_id)
                    VALUES (?,?)'''
    cursor.execute(query, (actID,filmID))
    conn.commit()
    conn.close()

def add_actor(name, phone, email, sex, age):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = '''
    	    INSERT INTO actor(name, phone, email, sex, age)
    	    	        VALUES (?,?,?,?, ?)
    	'''
    cursor.execute(query, (name, phone, email, sex, age))

    conn.commit()
    conn.close()
def add_director(name, phone, email):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = '''
    	    INSERT INTO director(name, phone, email)
    	    	        VALUES (?,?,?)
    	'''
    cursor.execute(query, (name, phone, email))

    conn.commit()
    conn.close()
def add_screenwriter(name, phone, email):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = '''
    	    INSERT INTO screenwriter(name, phone, email)
    	    	        VALUES (?,?,?)
    	'''
    cursor.execute(query, (name, phone, email))

    conn.commit()
    conn.close()
def add_film(title, box_office, rating, year, id_director, id_screenwriter):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = '''
        	    INSERT INTO film(title, box_office,rating,year,id_director, id_screenwriter)
        	    	        VALUES (?,?,?,?,?,?)
        	'''
    cursor.execute(query, (title, box_office, rating, year, id_director,id_screenwriter))

    conn.commit()
    conn.close()

def get_actor_by_age(age1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
       	    SELECT name, phone, email, sex, age
       	    FROM actor
       	    WHERE age = {age1!r} 

       	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_actor_by_sex(sex1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
       	    SELECT name, phone, email, sex, age
       	    FROM actor
       	    WHERE sex = {sex1!r} 

       	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_actor_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
       	    SELECT name, phone, email, sex, age
       	    FROM actor
       	    WHERE name = {name1!r} 

       	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def get_director_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
       	    SELECT name, phone, email
       	    FROM director
       	    WHERE name = {name1!r} 

       	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_screenwriter_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
       	    SELECT name, phone, email
       	    FROM screenwriter
       	    WHERE name = {name1!r} 

       	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def get_films_by_actor(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''SELECT id
    FROM actor
    WHERE name = {name1!r}
'''
    idact = cursor.execute(query).fetchall()[0][0]
    query = f'''SELECT film_id
        FROM actfilm
        WHERE act_id = {idact!r}'''
    id_films = cursor.execute(query).fetchall()
    list = []
    for elem in id_films:
        list.append(elem)
    query = f'''SELECT title, box_office, rating, year
        FROM film
        WHERE id in {list!r}'''
    cursor.execute(query)
    a = cursor.fetchall()
    conn.commit()
    conn.close()
    return a
def get_film_by_title(name):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year, id_director,id_screenwriter
    	    FROM film
    	    WHERE title = {name!r} 

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_films_by_year(year1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year
    	    FROM film
    	    WHERE year = {year1!r}

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_films_by_rating(rating1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year
    	    FROM film
    	    WHERE rating>={rating1!r}

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_films_by_box_office(box1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year
    	    FROM film
    	    WHERE box_office>={box1!r}

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_films_by_scrennwriter(scr_id):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year
    	    FROM film
    	    WHERE id_screenwriter = {scr_id!r}

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows
def get_films_by_director(director_id):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    	    SELECT title, box_office, rating, year
    	    FROM film
    	    WHERE id_director = {director_id!r}

    	'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def remove_film_by_title(name):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
           	    DELETE FROM film WHERE title = "{name}"
           	'''
    cursor.execute(query)
    conn.commit()
    conn.close()
def remove_actor_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
           	    DELETE FROM actor WHERE title = "{name1}"
           	'''
    cursor.execute(query)
    conn.commit()
    conn.close()
def remove_director_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
           	    DELETE FROM director WHERE title = "{name1}"
           	'''
    cursor.execute(query)
    conn.commit()
    conn.close()
def remove_screenwriter_by_name(name1):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
           	    DELETE FROM screenwriter WHERE title = "{name1}"
           	'''
    cursor.execute(query)
    conn.commit()
    conn.close()

def update_film(name, box_office, rating, id_director, id_screenwriter):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    UPDATE director
    SET title = ?, box_office = ?, rating = ? ,id_director = ?, id_screenwriter = ?
    WHERE title = '{name}'
    '''
    cursor.execute(query, (name, box_office, rating, id_director, id_screenwriter))
    conn.commit()
    conn.close()
def update_actor(name1, phone, email):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    UPDATE actor
    SET name = ?, phone = ?,email = ?
    WHERE name = '{name1}'
    '''
    cursor.execute(query, (name1, phone, email))
    conn.commit()
    conn.close()
def update_screenwriter(name1, phone, email):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    UPDATE screenwriter
    SET name = ?, phone = ?,email = ?
    WHERE name = '{name1}'
    '''
    cursor.execute(query, (name1, phone, email))
    conn.commit()
    conn.close()
def update_director(name1, phone, email):
    conn = sqlite3.connect('Movies.db')
    cursor = conn.cursor()
    query = f'''
    UPDATE director
    SET name = ?, phone = ?,email = ?
    WHERE name = '{name1}'
    '''
    cursor.execute(query, (name1, phone, email))
    conn.commit()
    conn.close()

print(get_films_by_actor('Tobey Maguire'))
