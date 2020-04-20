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
        cursor.execute(f'''SELECT film_id FROM actfilm WHERE act_id ={actID!r}''')
        a = cursor.fetchall()
        list =[]
        for elem in a:
            list.append(elem[0])
        if list.__contains__(filmID):
            return
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
    def add_actor_in_consist_film(actor, *films):
        WorkingBD.add_actor_during_adding_film(actor)
        for elem in films:
            WorkingBD.connect_film_and_actor(elem,actor)
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
        if WorkingBD.get_film_by_title(title).__len__()!=0:
            return
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
        a = WorkingBD.get_films_by_director(name1)
        all_rows.append(a)
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
        a = WorkingBD.get_films_by_composer(name1)
        all_rows.append(a)
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
        a = WorkingBD.get_films_by_scrennwriter(name1)
        all_rows.append(a)
        conn.commit()
        conn.close()
        return all_rows
    def get_actors_by_film(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM film WHERE title ={name1!r}''')
        idf = cursor.fetchone()[0]
        cursor.execute(f'''SELECT act_id FROM actfilm WHERE film_id={idf!r}''')
        actf = cursor.fetchall()
        list =[]
        result =[]
        for elem in actf:
            list.append(elem[0])
        for elem in list:
            cursor.execute(f'''SELECT name FROM actor WHERE id ={elem!r}''')
            result+=cursor.fetchone()
        return result
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
            list.append(elem[0])
        result = []
        for elem in list:
            s = WorkingBD.get_film_by_id(elem)
            result+=s
        list =[]
        for elem in result:
            a = elem[0]
            list.append(WorkingBD.get_film_by_title(a))
        conn.commit()
        conn.close()
        return list
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
        cursor.execute('''''')
        conn.commit()
        conn.close()
        if all_rows.__len__()!=0:
            all_rows.append(WorkingBD.get_actors_by_film(name))
        return all_rows
    def get_films_by_year(year1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title
                FROM film
                WHERE year = {year1!r}
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result =[]
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result
    def get_films_by_rating(rating1,what):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if what=='less':
            query = f'''
                           SELECT title
                           FROM film
                           WHERE rating <= {rating1!r}
    
                       '''
        if what == 'more':
            query = f'''
                           SELECT title
                           FROM film
                           WHERE rating >= {rating1!r}

                       '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result
    def get_films_by_box_office(box1,what):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if what == 'less':
            query = f'''
                           SELECT title
                           FROM film
                           WHERE box_office <= {box1!r}

                       '''
        if what == 'more':
            query = f'''
                           SELECT title
                           FROM film
                           WHERE box_office >= {box1!r}

                       '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result

    def get_films_by_budget(budg,what):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if what == 'less':
            query = f'''
                    SELECT title
                    FROM film
                    WHERE box_office<={budg!r}
    
                '''
        if what == 'more':
            query = f'''
                            SELECT title
                            FROM film
                            WHERE box_office>={budg!r}
    
                        '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result

    def get_films_by_scrennwriter(screenwriter_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title
                FROM film
                WHERE screenwriter_name = {screenwriter_name1!r}
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result


    def get_films_by_director(director_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title
                FROM film
                WHERE director_name = {director_name1!r}
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()

        return result


    def get_films_by_composer(composer_name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title
                FROM film
                WHERE composer_name = {composer_name1!r}
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()
        return result

    def remove_film_by_title(*name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name:
            query = f'''
                        DELETE FROM film WHERE title = "{elem!r}"
                    '''
            cursor.execute(query)
        for elem in name:
            cursor.execute(f'''SELECT id FROM film WHERE title = "{elem!r}"''')
        conn.commit()
        conn.close()
    def remove_connection_by_actor(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM actor WHERE name ="{name1}"''')
        act_id = cursor.fetchall()[0][0]
        cursor.execute(f'''DELETE FROM actfilm WHERE act_id ="{act_id!r}"''')
        conn.commit()
        conn.close()
    def remove_actor_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            WorkingBD.remove_connection_by_actor(elem)
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

    def update_film(name, box_office, rating,budget, director_name, screenwriter_name, composer_name, *actors):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
        UPDATE film
        SET title = ?, box_office = ?, rating = ? ,budget = ?,director_name = ?, screenwriter_name = ?, composer_name = ?
        WHERE title = '{name}'
        '''
        cursor.execute(query, (name, box_office, rating, budget, director_name, screenwriter_name, composer_name))
        for actor in actors:
            WorkingBD.connect_film_and_actor(name,actor)
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
WorkingBD.add_actor('Andrew Garfield','89157213979','garfield','male','1986')
WorkingBD.add_film('The Amazing Spider-Man 2',800000000,40,2014,200000000,'Marc Webb','Idiot','Hans Zimmer','Andrew Garfield', 'Emma Stone', 'Jamie Foxx', 'Dane Dehaan', 'Sally Field')
WorkingBD.add_film('Captain America: The Winter Soldier',800000000,70,2014,200000000,'Russo Brothers','Russo Brothers','Michael Jackino','Chris Evans', 'Sam Jackson', 'Scarlett Johanson', 'Robert Redfford', 'Sebastian Stan')
WorkingBD.add_film('The Amazing Spider-Man',800000000,60,2012,200000000,'Marc Webb','Alvin Sargent','James Horner','Andrew Garfield', 'Emma Stone', 'Rhys Ifans')
WorkingBD.add_film('Spider-Man',800000000,80,2002,200000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco')
WorkingBD.add_actor_in_consist_film('Emma Stone', 'The Amazing Spider-Man','The Amazing Spider-Man 2')

