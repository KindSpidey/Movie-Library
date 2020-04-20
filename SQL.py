import sqlite3
import subprocess as sp

class WorkingBD():
    def create_table():
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        queryyActorNews = '''
                CREATE TABLE IF NOT EXISTS actnews(
                    act_id  INT REFERENCES actor (id),
                    news_id INT REFERENCES news (id) 
        )'''
        queryActorFilm = '''
            CREATE TABLE IF NOT EXISTS actfilm(
                act_id  INT REFERENCES actor (id),
                film_id INT REFERENCES film (id) 
    )
        '''
        queryActor = '''
            CREATE TABLE IF NOT EXISTS actor(
                    id    INTEGER CONSTRAINT actor_pk PRIMARY KEY AUTOINCREMENT,
    name  TEXT,
    phone TEXT,
    email TEXT,
    sex   TEXT,
    age   INT
            )
        '''
        queryDirector = '''
                CREATE TABLE IF NOT EXISTS director(
                    id    INTEGER CONSTRAINT director_pk PRIMARY KEY AUTOINCREMENT,
        name  TEXT    ,
        phone TEXT   ,
        email TEXT    
                )
            '''
        queryComposer = '''
                    CREATE TABLE IF NOT EXISTS composer(
   id    INTEGER CONSTRAINT composer_pk PRIMARY KEY AUTOINCREMENT,
    name  TEXT,
    phone TEXT,
    email TEXT
                    )
                '''
        queryFilm = '''
                CREATE TABLE IF NOT EXISTS film(
                    id                INTEGER CONSTRAINT film_pk PRIMARY KEY AUTOINCREMENT,
        title             TEXT    NOT NULL,
        box_office        INT     NOT NULL,
        budget            INT     NOT NULL,
        rating            INT     NOT NULL,
        year              INT     NOT NULL,
        director_name     TEXT    REFERENCES director (name) 
                                  NOT NULL,
        screenwriter_name TEXT    REFERENCES screenwriter (name) 
                                  NOT NULL,
        composer_name     TEXT    NOT NULL
                                  REFERENCES composer (name) 
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
                        id    INTEGER CONSTRAINT screenwriter_pk PRIMARY KEY AUTOINCREMENT,
        name  TEXT    ,
        phone TEXT    ,
        email TEXT   )'''
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
        cursor.execute(queryActorFilm)
        cursor.execute(queryComposer)

        conn.commit()
        conn.close()
    def connect_film_and_actor(film_title, actor_name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if(WorkingBD.get_actor_by_name(actor_name).__len__()==0):
            WorkingBD.add_actor_during_adding_film(actor_name)
        cursor.execute(f'''SELECT id FROM actor WHERE name = {actor_name!r}''')
        actID = cursor.fetchall()
        cursor.execute(f'''SELECT id FROM film WHERE title ={film_title!r} ''')
        filmID = cursor.fetchall()
        result = actID[0]+filmID[0]
        actID, filmID = result[0], result[1]
        query ='''
        INSERT INTO actfilm(act_id, film_id)
                        VALUES (?,?)'''
        cursor.execute(query, (actID,filmID))
        conn.commit()
        conn.close()
    def add_actor_during_adding_film(name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if (WorkingBD.get_actor_by_name(name).__len__() != 0):
            return
        query = '''
                                INSERT INTO actor(name)
                                            VALUES (?) 
                            '''
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()
    def add_person_during_adding_film(name,who):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if (who=='actor'):
            if (WorkingBD.get_actor_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO actor(name)
                                                VALUES (?) 
                                '''
        if (who=='director'):
            if (WorkingBD.get_director_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO director(name)
                                                VALUES (?) 
                                '''
        if (who=='composer'):
            if (WorkingBD.get_composer_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO composer(name)
                                                VALUES (?) 
                                '''
        if (who=='screenwriter'):
            if (WorkingBD.get_screenwriter_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO screenwriter(name)
                                                VALUES (?) 
                                '''
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()

    def add_actor(name, phone, email, sex, age):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if(WorkingBD.get_actor_by_name(name).__len__()!=0):
            return
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
    def add_film(title, box_office, rating, year, budget,  director_name, screenwriter_name, composer_name, *actors_names):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = '''
                    INSERT INTO film(title, box_office,rating, year,budget, director_name, screenwriter_name,composer_name)
                                VALUES (?,?,?,?,?,?,?,?)
                '''
        cursor.execute(query, (title, box_office, rating, year, budget, director_name, screenwriter_name,composer_name))
        conn.commit()
        for elem in actors_names:
            WorkingBD.connect_film_and_actor(title,elem)
        WorkingBD.add_person_during_adding_film(director_name, 'director')
        WorkingBD.add_person_during_adding_film(screenwriter_name, 'screenwriter')
        WorkingBD.add_person_during_adding_film(composer_name, 'composer')
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

    def get_composer_by_name(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT name, phone, email
                FROM composer
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
        for elem in id_films[0]:
            list.append(elem)
        result = []
        for elem in list:
            s = WorkingBD.get_film_by_id(elem)
            result+=s
        conn.commit()
        conn.close()
        return result
    def get_film_by_id(ids):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                    SELECT title, box_office, rating, year, budget,director_name, screenwriter_name, composer_name
                    FROM film
                    WHERE id = {ids!r}
    
                '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows
    def get_film_by_title(name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
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
                SELECT title, box_office, rating, year, budget, director_name, screenwriter_name, composer_name
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
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
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
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
                FROM film
                WHERE box_office>={box1!r}
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows

    def get_films_by_budget(budg):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
                FROM film
                WHERE box_office>={budg!r}

            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows
    def get_films_by_scrennwriter(screenwriter_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
                FROM film
                WHERE screenwriter_name = {screenwriter_name1!r}
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows
    def get_films_by_director(director_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
                FROM film
                WHERE director_name = {director_name1!r}
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows
    def get_films_by_composer(composer_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, box_office, rating, year,budget, director_name, screenwriter_name, composer_name
                FROM film
                WHERE composer_name = {composer_name1!r}
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return all_rows

    def remove_film_by_title(*name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name:
            query = f'''
                        DELETE FROM film WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()
    def remove_actor_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM actor WHERE name = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()
    def remove_director_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM director WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()
    def remove_screenwriter_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM screenwriter WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()
    def remove_composer_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM composer WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def update_film(name, box_office, rating,budget, director_name, screenwriter_name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
        UPDATE film
        SET title = ?, box_office = ?, rating = ? ,budget = ?,director_name = ?, screenwriter_name = ?
        WHERE title = '{name}'
        '''
        cursor.execute(query, (name, box_office, rating, budget, director_name, screenwriter_name))
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
        SET phone = ?,email = ?
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
        SET phone = ?,email = ?
        WHERE name = '{name1}'
        '''
        cursor.execute(query, (name1, phone, email))
        conn.commit()
        conn.close()
WorkingBD.create_table()
WorkingBD.remove_film_by_title('Spider-Man')
WorkingBD.remove_actor_by_name('Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe','James Franco', 'J.K. Simmons', 'Joe Manganiello')
WorkingBD.add_film('Spider-Man',821708551,90,2002,139000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe','James Franco', 'J.K. Simmons', 'Joe Manganiello')

