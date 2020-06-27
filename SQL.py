import sqlite3
import subprocess as sp
import json

class WorkingBD():
    def create_table(self):
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
    name           TEXT,
    email          TEXT,
    phone          TEXT,
    sex            TEXT,
    birth_year     INT,
    age            INT,
    average_salary INT
            )
        '''
        queryDirector = '''
                CREATE TABLE IF NOT EXISTS director(
                    id    INTEGER CONSTRAINT director_pk PRIMARY KEY AUTOINCREMENT,
    name           TEXT,
    email          TEXT,
    phone          TEXT,
    average_salary INT
                )
            '''
        queryComposer = '''
                    CREATE TABLE IF NOT EXISTS composer(
    id    INTEGER CONSTRAINT composer_pk PRIMARY KEY AUTOINCREMENT,
    name           TEXT,
    email          TEXT,
    phone          TEXT,
    average_salary INT
                    )
                '''
        queryFilm = '''
                CREATE TABLE IF NOT EXISTS film(
                    id                INTEGER CONSTRAINT film_pk PRIMARY KEY AUTOINCREMENT,
    id                INTEGER CONSTRAINT film_pk PRIMARY KEY AUTOINCREMENT,
    title             TEXT,
    box_office        INT,
    budget            INT,
    rating            INT,
    year              INT,
    director_name     TEXT    REFERENCES director (name),
    screenwriter_name TEXT    REFERENCES screenwriter (name),
    composer_name     TEXT    REFERENCES composer (name) 
    )
            '''
        queryScreenwriter = '''CREATE TABLE IF NOT EXISTS screenwriter(
    id             INTEGER CONSTRAINT screenwriter_pk PRIMARY KEY AUTOINCREMENT,
    name           TEXT,
    email          TEXT,
    phone          TEXT,
    average_salary INT  )'''
        queryActSal = '''CREATE TABLE IF NOT EXISTS actsal (
        act_id  INTEGER,
        film_id INT,
        salary INT
        );
        '''
        queryLogPass = '''CREATE TABLE IF NOT EXISTS loginpassword (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL,
    login    STRING  UNIQUE
                     NOT NULL,
    password STRING  NOT NULL
);
'''
        queryDirSal = '''CREATE TABLE IF NOT EXISTS dirsal (
            dir_id  INTEGER,
            film_id INT,
            salary INT
        );
        '''
        queryScrSal = '''CREATE TABLE IF NOT EXISTS scrsal (
            scr_id  INTEGER,
            film_id INT,
            salary INT
        );
        '''
        queryCompSal = '''CREATE TABLE IF NOT EXISTS compsal (
            comp_id  INTEGER,
            film_id INT,
            salary INT
        );
        '''
        queryFilmInPlan = '''CREATE TABLE IF NOT EXISTS filminplan (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           STRING,
    description     STRING,
    theme           STRING,
    idea            STRING,
    planning_budget INTEGER
);
'''
        queryFilmInProgress = '''CREATE TABLE IF NOT EXISTS filminprogress (
    id           INTEGER NOT NULL
    title           STRING,
    description     STRING,
    theme           STRING,
    idea            STRING,
    planning_budget INTEGER
);

);
'''
        queryActFilmInProgress = '''CREATE TABLE IF NOT EXISTS actfilminprogress (
    act_id              INT,
    film_in_progress_id INT
);'''
        cursor.execute(queryActFilmInProgress)
        cursor.execute(queryActor)
        cursor.execute(queryDirector)
        cursor.execute(queryFilm)
        cursor.execute(queryScreenwriter)
        cursor.execute(queryActorFilm)
        cursor.execute(queryComposer)
        cursor.execute(queryScrSal)
        cursor.execute(queryDirSal)
        cursor.execute(queryActSal)
        cursor.execute(queryCompSal)
        cursor.execute(queryFilmInProgress)
        cursor.execute(queryFilmInPlan)
        cursor.execute(queryLogPass)
        conn.commit()
        conn.close()

    def update_salary(who, id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'actor':
            list = []
            cursor.execute(f'''SELECT salary FROM actsal WHERE act_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums += elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE actor SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who == 'director':
            list = []
            cursor.execute(f'''SELECT salary FROM dirsal WHERE dir_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums += elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE director SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who == 'screenwriter':
            list = []
            cursor.execute(f'''SELECT salary FROM scrsal WHERE scr_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums += elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE screenwriter SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who == 'composer':
            list = []
            cursor.execute(f'''SELECT salary FROM compsal WHERE comp_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums += elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE composer SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        conn.commit()
        conn.close()

    def connect_salary_and_person(film, who, name, salary):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name = {name!r}''')
            actID = cursor.fetchall()
            cursor.execute(f'''SELECT id FROM film WHERE title ={film!r} ''')
            filmID = cursor.fetchall()
            result = actID[0] + filmID[0]
            actID, filmID = result[0], result[1]
            cursor.execute(f'''SELECT film_id FROM actsal WHERE act_id ={actID!r} ''')
            aid = cursor.fetchall()
            list = []
            for elem in aid:
                list.append(elem[0])
            cursor.execute(f'''SELECT name FROM actor WHERE id={actID!r}''')
            if (list.__contains__(filmID)):
                return
            cursor.execute(f'''SELECT film_id FROM actfilm WHERE act_id={actID!r}''')
            lFilms = cursor.fetchall()
            lf = []
            for elem in lFilms:
                lf.append(elem[0])
            if not (lf.__contains__(filmID)):
                return
            query = '''
                    INSERT INTO actsal(act_id, film_id,salary)
                                    VALUES (?,?,?)'''
            cursor.execute(query, (actID, filmID, salary))
            conn.commit()
            WorkingBD.update_salary('actor', actID)
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name = {name!r}''')
            actID = cursor.fetchall()
            cursor.execute(f'''SELECT id FROM film WHERE title ={film!r} ''')
            filmID = cursor.fetchall()
            result = actID[0] + filmID[0]
            actID, filmID = result[0], result[1]
            cursor.execute(f'''SELECT film_id FROM dirsal WHERE dir_id ={actID!r} ''')
            aid = cursor.fetchall()
            list = []
            for elem in aid:
                list.append(elem[0])
            if (list.__contains__(filmID)):
                return
            cursor.execute(f'''SELECT director_name FROM film WHERE title ={film!r}''')
            names = cursor.fetchall()[0][0]
            if names != name:
                return
            query = '''
                    INSERT INTO dirsal(dir_id, film_id,salary)
                                    VALUES (?,?,?)'''
            cursor.execute(query, (actID, filmID, salary))
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director', actID)
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name = {name!r}''')
            actID = cursor.fetchall()
            cursor.execute(f'''SELECT id FROM film WHERE title ={film!r} ''')
            filmID = cursor.fetchall()
            result = actID[0] + filmID[0]
            actID, filmID = result[0], result[1]
            cursor.execute(f'''SELECT film_id FROM scrsal WHERE scr_id ={actID!r} ''')
            aid = cursor.fetchall()
            list = []
            for elem in aid:
                list.append(elem[0])
            if (list.__contains__(filmID)):
                return
            cursor.execute(f'''SELECT screenwriter_name FROM film WHERE title ={film!r}''')
            names = cursor.fetchall()[0]
            if names != name:
                return
            query = '''
                    INSERT INTO scrsal(scr_id, film_id,salary)
                                    VALUES (?,?,?)'''
            cursor.execute(query, (actID, filmID, salary))
            conn.commit()
            WorkingBD.update_salary('screenwriter', actID)
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name = {name!r}''')
            actID = cursor.fetchall()
            cursor.execute(f'''SELECT id FROM film WHERE title ={film!r} ''')
            filmID = cursor.fetchall()
            result = actID[0] + filmID[0]
            actID, filmID = result[0], result[1]
            cursor.execute(f'''SELECT film_id FROM compsal WHERE comp_id ={actID!r} ''')
            aid = cursor.fetchall()
            list = []
            for elem in aid:
                list.append(elem[0])
            if (list.__contains__(filmID)):
                return
            cursor.execute(f'''SELECT composer_name FROM film WHERE title ={film!r}''')
            names = cursor.fetchall()[0][0]
            if names != name:
                return
            query = '''
                    INSERT INTO compsal(comp_id, film_id,salary)
                                    VALUES (?,?,?)'''
            cursor.execute(query, (actID, filmID, salary))
            conn.commit()
            WorkingBD.update_salary('composer', actID)

    def connect_film_and_actor(film_title, actor_name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if (WorkingBD.get_actor_by_name(actor_name).__len__() == 0):
            WorkingBD.add_actor_during_adding_film(actor_name)
        cursor.execute(f'''SELECT id FROM actor WHERE name = {actor_name!r}''')
        actID = cursor.fetchall()
        cursor.execute(f'''SELECT id FROM film WHERE title ={film_title!r} ''')
        filmID = cursor.fetchall()
        result = actID[0] + filmID[0]
        actID, filmID = result[0], result[1]
        cursor.execute(f'''SELECT film_id FROM actfilm WHERE act_id ={actID!r}''')
        a = cursor.fetchall()
        list = []
        for elem in a:
            list.append(elem[0])
        if list.__contains__(filmID):
            return
        query = '''
        INSERT INTO actfilm(act_id, film_id)
                        VALUES (?,?)'''
        cursor.execute(query, (actID, filmID))
        conn.commit()
        conn.close()

    def connect_film_and_actor_in_progress(film_title, actor_name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if (WorkingBD.get_actor_by_name(actor_name).__len__() == 0):
            WorkingBD.add_actor_during_adding_film(actor_name)
        cursor.execute(f'''SELECT id FROM actor WHERE name = {actor_name!r}''')
        actID = cursor.fetchall()
        cursor.execute(f'''SELECT id FROM filminprogress WHERE title ={film_title!r} ''')
        filmID = cursor.fetchall()
        result = actID[0] + filmID[0]
        actID, filmID = result[0], result[1]
        cursor.execute(f'''SELECT film_in_progress_id FROM actfilminprogress WHERE act_id ={actID!r}''')
        a = cursor.fetchall()
        list = []
        for elem in a:
            list.append(elem[0])
        if list.__contains__(filmID):
            return
        query = '''
        INSERT INTO actfilminprogress(act_id, film_in_progress_id)
                        VALUES (?,?)'''
        cursor.execute(query, (actID, filmID))
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

    def add_actor_in_consist_film(actor, films):
        WorkingBD.add_actor_during_adding_film(actor)
        for elem in films:
            WorkingBD.connect_film_and_actor(elem, actor)

    def add_actor_in_consist_film_in_progress(actor, films):
        WorkingBD.add_person_during_adding_film(actor, 'actor')
        for elem in films:
            WorkingBD.connect_film_and_actor_in_progress(elem, actor)

    def add_person_during_adding_film(name, who):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if (who == 'actor'):
            if (WorkingBD.get_actor_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO actor(name)
                                                VALUES (?) 
                                '''
        if (who == 'director'):
            if (WorkingBD.get_director_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO director(name)
                                                VALUES (?) 
                                '''
        if (who == 'composer'):
            if (WorkingBD.get_composer_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO composer(name)
                                                VALUES (?) 
                                '''
        if (who == 'screenwriter'):
            if (WorkingBD.get_screenwriter_by_name(name).__len__() != 0):
                return
            query = '''
                                    INSERT INTO screenwriter(name)
                                                VALUES (?) 
                                '''
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()

    def add_actor(name, phone, email, sex, birth_year):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        age = 0
        if (WorkingBD.get_actor_by_name(name).__len__() != 0):
            return
        if birth_year!='':
            age = 2020 - int(birth_year)
        else:
            age = None
        query = '''
                   INSERT INTO actor(name, phone, email, sex, birth_year,age)
                                VALUES (?,?,?,?,?, ?)
                '''
        cursor.execute(query, (name, phone, email, sex, birth_year, age))
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

    def add_composer(name, phone, email):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = '''
                INSERT INTO composer(name, phone, email)
                            VALUES (?,?,?)
            '''
        cursor.execute(query, (name, phone, email))

        conn.commit()
        conn.close()

    def add_film(title, box_office, rating, year, budget, director_name, screenwriter_name, composer_name,
                 actors_names):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if WorkingBD.get_film_by_title(title).__len__() != 0:
            return
        query = '''
                    INSERT INTO film(title, box_office,rating, year,budget, director_name, screenwriter_name,composer_name)
                                VALUES (?,?,?,?,?,?,?,?)
                '''
        cursor.execute(query,
                       (title, box_office, rating, year, budget, director_name, screenwriter_name, composer_name))
        conn.commit()
        if actors_names!=None:
            for elem in actors_names:
                WorkingBD.connect_film_and_actor(title, elem)
        WorkingBD.add_person_during_adding_film(director_name, 'director')
        WorkingBD.add_person_during_adding_film(screenwriter_name, 'screenwriter')
        WorkingBD.add_person_during_adding_film(composer_name, 'composer')
        conn.close()

    def add_filminplan(title, description, theme, idea, budget):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if len(WorkingBD.get_film_in_plan(title))!=0:
            return
        query = '''
                INSERT INTO filminplan(title, description, theme, idea, planning_budget)
                            VALUES (?,?,?,?,?)
            '''
        cursor.execute(query, (title, description, theme, idea, budget))
        conn.commit()
        conn.close()

    def add_filmInProgress(title, budget, director_name, screenwriter_name, composer_name, actors_names):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if WorkingBD.get_film_in_progress_by_title(title).__len__() != 0:
            return
        query = '''
                        INSERT INTO filmInProgress(title, budget, director_name, screenwriter_name,composer_name)
                                    VALUES (?,?,?,?,?)
                    '''
        cursor.execute(query, (title, budget, director_name, screenwriter_name, composer_name))
        conn.commit()
        for elem in actors_names:
            WorkingBD.add_person_during_adding_film(elem, 'actor')
            WorkingBD.connect_film_and_actor_in_progress(title, elem)
        WorkingBD.add_person_during_adding_film(director_name, 'director')
        WorkingBD.add_person_during_adding_film(screenwriter_name, 'screenwriter')
        WorkingBD.add_person_during_adding_film(composer_name, 'composer')
        conn.close()

    def get_actor_by_age(age1, which):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if which == 'more':
            query = f'''
                    SELECT name, phone, email, sex, age
                    FROM actor
                    WHERE age >= {age1!r} 
        
                '''
        if which == 'less':
            query = f'''
                    SELECT name, phone, email, sex, age
                    FROM actor
                    WHERE age <= {age1!r} 

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
    def get_film_in_progress_title_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                        SELECT title
                        FROM filminprogress
                        WHERE id = {id!r} 

                    '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.close()
        return all_rows
    def get_film_title_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                        SELECT title
                        FROM film
                        WHERE id = {id!r} 

                    '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        conn.close()
        return all_rows
    def get_actor_by_name_for_profile(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT name, average_salary, phone, email, sex, age
                FROM actor
                WHERE name = {name1!r} 

            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        if all_rows.__len__() == 0:
            return all_rows
        a = WorkingBD.get_salary_by_person('actor', name1)
        all_rows.append(a)
        a = WorkingBD.get_films_title_by_actor(name1)
        b = WorkingBD.get_films_in_progress_by_actor(name1)
        other_films = []
        for elem in b:
            other_films.append(elem)
        if len(all_rows[1]) == 0:
            for elem in a:
                other_films.append(elem)
        for i in range(0, len(a)):
            not_inside = 0
            for elem in all_rows[1]:
                if not elem.__contains__(a[i]):
                    not_inside += 1
                if not_inside == len(all_rows[1]):
                    other_films.append(a[i])
        if len(other_films) != 0 or len(all_rows[1]) != 0:
            all_rows.append(other_films)
        if len(all_rows)==2:
            all_rows.append([])
        conn.commit()
        conn.close()
        return all_rows
    def get_actor_by_name(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT name, average_salary, phone, email, sex, age
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
                SELECT name, average_salary, phone, email
                FROM director
                WHERE name = {name1!r} 
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        if all_rows.__len__() == 0:
            return all_rows
        a = WorkingBD.get_salary_by_person('director', name1)
        all_rows.append(a)
        a = WorkingBD.get_films_title_by_person('director', name1)
        other_films = []
        if len(all_rows[1]) == 0:
            for elem in a:
                other_films.append(elem)
            all_rows.append(other_films)
        for i in range(0, len(a)):
            not_inside = 0
            for elem in all_rows[1]:
                if not elem.__contains__(a[i]):
                    not_inside += 1
                if not_inside == len(all_rows[1]):
                    other_films.append(a[i])
        if len(other_films) != 0 or len(all_rows[1]) != 0:
            all_rows.append(other_films)
        conn.commit()
        conn.close()
        return all_rows

    def get_composer_by_name(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT name, average_salary, phone, email
                FROM composer
                WHERE name = {name1!r} 

            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        if all_rows.__len__() == 0:
            return all_rows
        a = WorkingBD.get_salary_by_person('composer', name1)
        all_rows.append(a)
        a = WorkingBD.get_films_title_by_person('composer', name1)
        other_films = []
        if len(all_rows[1])==0:
            for elem in a:
                other_films.append(elem)
            all_rows.append(other_films)
        for i in range(0, len(a)):
            not_inside = 0
            for elem in all_rows[1]:
                if not elem.__contains__(a[i]):
                    not_inside += 1
                if not_inside == len(all_rows[1]):
                    other_films.append(a[i])
        if len(other_films) != 0 or len(all_rows[1])!=0:
            all_rows.append(other_films)
        conn.commit()
        conn.close()
        return all_rows

    def get_screenwriter_by_name(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT name, average_salary, phone, email
                FROM screenwriter
                WHERE name = {name1!r} 
    
            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        if all_rows.__len__() == 0:
            return all_rows
        a = WorkingBD.get_salary_by_person('screenwriter', name1)
        all_rows.append(a)
        a = WorkingBD.get_films_title_by_person('screenwriter', name1)
        other_films = []
        if len(all_rows[1]) == 0:
            for elem in a:
                other_films.append(elem)
            all_rows.append(other_films)
        for i in range(0, len(a)):
            not_inside = 0
            for elem in all_rows[1]:
                if not elem.__contains__(a[i]):
                    not_inside += 1
                if not_inside == len(all_rows[1]):
                    other_films.append(a[i])
        if len(other_films) != 0 or len(all_rows[1]) != 0:
            all_rows.append(other_films)
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
        list = []
        result = []
        for elem in actf:
            list.append(elem[0])
        for elem in list:
            cursor.execute(f'''SELECT name FROM actor WHERE id ={elem!r}''')
            result += cursor.fetchone()
        return result

    def get_actors_by_filminprogress(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM filminprogress WHERE title ={name1!r}''')
        idf = cursor.fetchone()[0]
        cursor.execute(f'''SELECT act_id FROM actfilminprogress WHERE film_in_progress_id={idf!r}''')
        actf = cursor.fetchall()
        list = []
        result = []
        for elem in actf:
            list.append(elem[0])
        for elem in list:
            cursor.execute(f'''SELECT name FROM actor WHERE id ={elem!r}''')
            result += cursor.fetchone()
        return result
    def get_films_in_progress_by_actor(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''SELECT id
                        FROM actor
                        WHERE name = {name1!r}
                    '''
        idact = cursor.execute(query).fetchall()[0][0]
        query = f'''SELECT film_in_progress_id
                            FROM actfilminprogress
                            WHERE act_id = {idact!r}'''
        id_films = cursor.execute(query).fetchall()
        list = []
        for elem in id_films:
            list.append(elem[0])
        result = []
        for elem in list:
            s = WorkingBD.get_film_in_progress_title_by_id(elem)[0]
            result += s
        conn.commit()
        conn.close()
        return result
    def get_films_in_progress_title_by_actor(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''SELECT id
                FROM actor
                WHERE name = {name1!r}
            '''
        idact = cursor.execute(query).fetchall()[0][0]
        query = f'''SELECT film_in_progress_id
                    FROM actfilminprogress
                    WHERE act_id = {idact!r}'''
        id_films = cursor.execute(query).fetchall()
        list = []
        for elem in id_films:
            list.append(elem[0])
        result = []
        for elem in list:
            s = WorkingBD.get_film_in_progress_title_by_id(elem)[0]
            result += s
        conn.commit()
        conn.close()
        return result
    def get_films_in_progress_title_by_actor(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''SELECT id
                FROM actor
                WHERE name = {name1!r}
            '''
        idact = cursor.execute(query).fetchall()[0][0]
        query = f'''SELECT film_in_progress_id
                    FROM actfilminprogress
                    WHERE act_id = {idact!r}'''
        id_films = cursor.execute(query).fetchall()
        list = []
        for elem in id_films:
            list.append(elem[0])
        result = []
        for elem in list:
            s = WorkingBD.get_film_in_progress_title_by_id(elem)[0]
            result += s
        conn.commit()
        conn.close()
        return result
    def get_films_title_by_actor(name1):
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
            s = WorkingBD.get_film_title_by_id(elem)[0]
            result += s
        conn.commit()
        conn.close()
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
            result += s
        list = []
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

    def get_personID_by_name(name, who):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name = {name!r}''')
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name = {name!r}''')
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name = {name!r}''')
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name = {name!r}''')
        return cursor.fetchall()[0][0]

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
        cursor.execute(query)
        conn.commit()
        conn.close()
        if all_rows.__len__() != 0:
            all_rows.append(WorkingBD.get_actors_by_film(name))
        return all_rows

    def add_user(login, password):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''INSERT INTO loginpassword(login, password) VALUES (?,?)'''
        cursor.execute(query, (login, password))
        conn.commit()
        conn.close()

    def get_password(login):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                        SELECT password
                        FROM loginpassword
                        WHERE login = {login!r} 

                    '''
        cursor.execute(query)
        a = cursor.fetchall()
        if len(a)==0:
            return 'incorrect password!'
        else:
            a = a[0][0]
        conn.commit()
        conn.close()
        return a

    def get_film_in_plan(name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, theme, idea, planning_budget, description
                FROM filminplan
                WHERE title = {name!r} 

            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(elem) for elem in all_rows]
        cursor.execute(query)
        conn.commit()
        conn.close()
        return all_rows

    def get_film_in_progress_by_title(name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
                SELECT title, budget, director_name, screenwriter_name, composer_name
                FROM filminprogress
                WHERE title = {name!r} 

            '''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        cursor.execute(query)
        conn.commit()
        conn.close()
        if all_rows.__len__() != 0:
            all_rows.append(WorkingBD.get_actors_by_filminprogress(name))
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
        result = []
        for elem in all_rows:
            list.append(elem[0])
        for elem in list:
            a = WorkingBD.get_film_by_title(elem)
            result.append(a)
        conn.commit()
        conn.close()
        return result

    def get_films_by_rating(rating1, what):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if what == 'less':
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

    def get_films_by_box_office(box1, what):
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

    def get_films_by_budget(budg, what):
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

    def get_salary_by_person(who, name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name ={name!r}''')
            id = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT salary FROM actsal WHERE act_id={id!r}''')
            sal = cursor.fetchall()
            cursor.execute(f'''SELECT film_id FROM actsal WHERE act_id = {id!r}''')
            a = cursor.fetchall()
            sallist = []
            for elem in sal:
                sallist.append(elem[0])
            list = []
            for elem in a:
                list.append(elem[0])
            result = []
            for elem in list:
                a = [WorkingBD.get_film_title_by_id(elem)[0][0]]
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])

            return result
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name ={name!r}''')
            id = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT salary FROM dirsal WHERE dir_id={id!r}''')
            sal = cursor.fetchall()
            cursor.execute(f'''SELECT film_id FROM dirsal WHERE dir_id = {id!r}''')
            a = cursor.fetchall()
            sallist = []
            for elem in sal:
                sallist.append(elem[0])
            list = []
            for elem in a:
                list.append(elem[0])
            result = []
            for elem in list:
                a = [WorkingBD.get_film_title_by_id(elem)[0][0]]
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])

            return result
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name ={name!r}''')
            id = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT salary FROM scrsal WHERE scr_id={id!r}''')
            sal = cursor.fetchall()
            cursor.execute(f'''SELECT film_id FROM scrsal WHERE scr_id = {id!r}''')
            a = cursor.fetchall()
            sallist = []
            for elem in sal:
                sallist.append(elem[0])
            list = []
            for elem in a:
                list.append(elem[0])
            result = []
            for elem in list:
                a = [WorkingBD.get_film_title_by_id(elem)[0][0]]
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])

            return result
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name ={name!r}''')
            id = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT salary FROM compsal WHERE comp_id={id!r}''')
            sal = cursor.fetchall()
            cursor.execute(f'''SELECT film_id FROM compsal WHERE comp_id = {id!r}''')
            a = cursor.fetchall()
            sallist = []
            for elem in sal:
                sallist.append(elem[0])
            list = []
            for elem in a:
                list.append(elem[0])
            result = []
            for elem in list:
                a = [WorkingBD.get_film_title_by_id(elem)[0][0]]
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])

            return result
    def get_actors_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT name FROM actor WHERE id ={id!r}''')
        all_rows = cursor.fetchall()[0][0]
        return all_rows
    def get_director_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT name FROM director WHERE id ={id!r}''')
        all_rows = cursor.fetchall()[0][0]
        return all_rows
    def get_screenwriter_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT name FROM screenwriter WHERE id ={id!r}''')
        all_rows = cursor.fetchall()[0][0]
        return all_rows
    def get_composer_by_id(id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT name FROM composer WHERE id ={id!r}''')
        all_rows = cursor.fetchall()[0][0]
        return all_rows
    def get_salary_by_film(title):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        result = []
        query = f'''SELECT id FROM film WHERE title = {title!r}'''
        id = cursor.execute(query).fetchone()[0]
        try:
            query = f'''SELECT salary FROM dirsal WHERE film_id = {id!r}'''
            director_salary = cursor.execute(query).fetchall()[0][0]
            query = f'''SELECT dir_id FROM dirsal WHERE film_id = {id!r}'''
            dir_id = cursor.execute(query).fetchall()[0][0]
            dir_name = WorkingBD.get_director_by_id(dir_id)
            abc = [dir_name, 'Режиссер', director_salary]
            result.append(abc)
        except:
            pass
        try:
            query = f'''SELECT salary FROM scrsal WHERE film_id = {id!r}'''
            scr_salary = cursor.execute(query).fetchall()[0][0]
            query = f'''SELECT scr_id FROM scrsal WHERE film_id = {id!r}'''
            scr_id = cursor.execute(query).fetchall()[0][0]
            scr_name = WorkingBD.get_screenwriter_by_id(scr_id)
            abc = [scr_name, 'Сценарист', scr_salary]
            result.append(abc)
        except:
            pass
        try:
            query = f'''SELECT salary FROM compsal WHERE film_id = {id!r}'''
            composer_salary = cursor.execute(query).fetchall()[0][0]
            query = f'''SELECT comp_id FROM compsal WHERE film_id = {id!r}'''
            comp_id = cursor.execute(query).fetchall()[0][0]
            comp_name = WorkingBD.get_composer_by_id(comp_id)
            abc = [comp_name, 'Композитор', composer_salary]
            result.append(abc)
        except:
            pass
        try:
            query = f'''SELECT salary FROM actsal WHERE film_id = {id!r}'''
            actors_salary = cursor.execute(query).fetchall()
            actors_salary = [list(elem) for elem in actors_salary]
            query = f'''SELECT act_id FROM actsal WHERE film_id = {id!r}'''
            actors_id = cursor.execute(query).fetchall()
            actors_id = [list(i) for i in actors_id]
            actors_names = []
            for elem in actors_id:
                actors_names.append(WorkingBD.get_actors_by_id(elem[0]))
            for i in range (0, len(actors_names)):
                abc = [actors_names[i], 'Актёр', actors_salary[i][0]]
                result.append(abc)
        except:
            pass
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
            WorkingBD.remove_connection_by_film(elem)
        for elem in name:
            query = f'''
                        DELETE FROM film WHERE title = "{elem}"
                    '''
            cursor.execute(query)

        conn.commit()
        conn.close()

    def remove_connection_by_film(title):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM film WHERE title ="{title}"''')
        act_id = cursor.fetchall()[0][0]
        cursor.execute(f'''DELETE FROM actfilm WHERE film_id ="{act_id!r}"''')
        conn.commit()
        conn.close()

    def remove_connection_by_film_in_progress(title):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM filminprogress WHERE title ="{title}"''')
        act_id = cursor.fetchall()[0][0]
        cursor.execute(f'''DELETE FROM actfilminprogress WHERE film_in_progress_id ="{act_id!r}"''')
        conn.commit()
        conn.close()

    def remove_connection_by_actor(name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT id FROM actor WHERE name ="{name1}"''')
        act_id = cursor.fetchall()[0][0]
        cursor.execute(f'''DELETE FROM actfilm WHERE act_id ="{act_id!r}"''')
        cursor.execute(f'''DELETE FROM actfilminprogress WHERE act_id ="{act_id!r}"''')
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
                        DELETE FROM director WHERE name = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def remove_screenwriter_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM screenwriter WHERE name = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def remove_composer_by_name(*name1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in name1:
            query = f'''
                        DELETE FROM composer WHERE name = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def remove_filminplan(*title1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in title1:
            query = f'''
                        DELETE FROM filminplan WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def remove_filminprogress(*title1):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        for elem in title1:
            WorkingBD.remove_connection_by_film_in_progress(elem)
            query = f'''
                        DELETE FROM filminprogress WHERE title = "{elem}"
                    '''
            cursor.execute(query)
        conn.commit()
        conn.close()

    def remove_salary_by_person(film, who, name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''DELETE FROM compsal WHERE comp_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('composer', actID)
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''DELETE FROM dirsal WHERE dir_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director', actID)
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''DELETE FROM actsal WHERE act_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('actor', actID)
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''DELETE FROM scrsal WHERE scr_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('screenwriter', actID)

    def update_salary_when_created(film, who, name, salary):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(
                f'''UPDATE compsal SET salary = {salary!r} WHERE film_id={filmID!r} AND comp_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('composer', actID)
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE dirsal SET salary = {salary!r} WHERE film_id={filmID!r} AND dir_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director', actID)
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE actsal SET salary = {salary!r} WHERE film_id={filmID!r} AND act_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('actor', actID)
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE scrsal SET salary = {salary!r} WHERE film_id={filmID!r} AND scr_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('screenwriter', actID)

    def update_film(name, box_office, rating, budget, year, director_name, screenwriter_name, composer_name, actors):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
        UPDATE film
        SET title = ?, box_office = ?, rating = ? ,budget = ?, year = ? ,director_name = ?, screenwriter_name = ?, composer_name = ?
        WHERE title = '{name}'
        '''
        cursor.execute(query, (name, box_office, rating, budget, year, director_name, screenwriter_name, composer_name))
        for actor in actors:
            WorkingBD.connect_film_and_actor(name, actor)
        conn.commit()
        conn.close()

    def update_actor(name1, phone, email, sex, year):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        age = 0
        if year!='':
            age = 2020 - int(year)
        else:
            age = None
        query = f'''
        UPDATE actor
        SET name = ?, phone = ?,email = ?, sex =?, birth_year = ?, age =?
        WHERE name = '{name1}'
        '''
        cursor.execute(query, (name1, phone, email, sex, year, age))
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

    @staticmethod
    def get_all_films(self):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM film'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        list_actors = []
        for elem in all_rows:
            list_actors.append(WorkingBD.get_actors_by_film(elem[1]))
        for i in range(0, len(all_rows)):
            all_rows[i].append(list_actors[i])
        conn.close()
        return all_rows

    @staticmethod
    def get_all_films_in_plan(self):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM filminplan'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        conn.close()
        return all_rows

    @staticmethod
    def get_all_films_in_progress(self):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM filminprogress'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        list_actors = []
        for elem in all_rows:
            list_actors.append(WorkingBD.get_actors_by_filminprogress(elem[1]))
        for i in range(0, len(all_rows)):
            all_rows[i].append(list_actors[i])
        conn.close()
        return all_rows

    @staticmethod
    def get_all_actors(self):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        real =[]
        in_progress =[]
        query = '''SELECT * FROM actor'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        for elem in all_rows:
            elem.remove(elem[5])
        list_actors = []
        for elem in all_rows:
            try:
                real = WorkingBD.get_films_title_by_actor(elem[1])
            except:
                pass
            try:
                in_progress = WorkingBD.get_films_in_progress_title_by_actor(elem[1])
            except:
                pass
            if len(real)==0 and len(in_progress)==0:
                list_actors.append([])
            elif len(real)!=0 and len(in_progress)==0:
                list_actors.append(real)
            else:
                list_actors.append(in_progress)
        for i in range(0, len(all_rows)):
            all_rows[i].append(list_actors[i])
        conn.close()
        return all_rows

    @staticmethod
    def get_all_person(self, who):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''SELECT * FROM {who!r}'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_rows = [list(i) for i in all_rows]
        list_actors = []
        for elem in all_rows:
            list_actors.append(WorkingBD.get_films_title_by_person(who,elem[1]))
        for i in range(0, len(all_rows)):
            all_rows[i].append(list_actors[i])
        conn.close()
        return all_rows

    @staticmethod
    def get_films_title_by_person(who, name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='director':
            query = f'''SELECT title FROM film where director_name={name!r} UNION SELECT title FROM filminprogress where director_name={name!r}'''
        if who=='screenwriter':
            query = f'''SELECT title FROM film where screenwriter_name={name!r} UNION SELECT title from filminprogress where screenwriter_name={name!r}'''
        if who=='composer':
            query = f'''SELECT title FROM film where composer_name={name!r} UNION SELECT title from filminprogress where composer_name={name!r}'''
        cursor.execute(query)
        all_rows = cursor.fetchall()
        list = []
        for elem in all_rows:
            list.append(elem[0])
        return list

    def update_filminplan(title, description, theme, idea, budget):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''UPDATE filminplan
        SET title = ?,description = ?, theme = ?, idea = ?, planning_budget = ?
        WHERE title = '{title}'
        '''
        cursor.execute(query, (title, description, theme, idea, budget))
        conn.commit()
        conn.close()

    def update_filminprogress(title, budget, director_name, screenwriter_name, composer_name, actors_names):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
        UPDATE filminprogress
        SET title = ? ,budget = ?,director_name = ?, screenwriter_name = ?, composer_name = ?
        WHERE title = '{title}'
        '''
        cursor.execute(query, (title, budget, director_name, screenwriter_name, composer_name))
        for actor in actors_names:
            WorkingBD.connect_film_and_actor_in_progress(title, actor)
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

    def update_composer(name1, phone, email):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        query = f'''
        UPDATE composer
        SET name = ?, phone = ?,email = ?
        WHERE name = '{name1}'
        '''
        cursor.execute(query, (name1, phone, email))
        conn.commit()
        conn.close()


# WorkingBD.create_table()
# WorkingBD.add_actor('Andrew Garfield','89157213979','garfield','male','1986')
# WorkingBD.remove_film_by_title('The Amazing Spider-Man 2')
# WorkingBD.add_film('The Amazing Spider-Man 2',800000000,40,2014,200000000,'Marc Webb','Idiot','Hans Zimmer','Andrew Garfield', 'Emma Stone', 'Jamie Foxx', 'Dane Dehaan', 'Sally Field')
# WorkingBD.add_film('Captain America: The Winter Soldier',800000000,70,2014,200000000,'Russo Brothers','Russo Brothers','Michael Jackino','Chris Evans', 'Sam Jackson', 'Scarlett Johanson', 'Robert Redfford', 'Sebastian Stan')
# WorkingBD.add_film('The Amazing Spider-Man',800000000,60,2012,200000000,'Marc Webb','Alvin Sargent','James Horner','Andrew Garfield', 'Emma Stone', 'Rhys Ifans')
# WorkingBD.add_film('Spider-Man',800000000,80,2002,200000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco')
# WorkingBD.add_film('Spider-Man 3',800000000,90,2004,200000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco', 'Alfred Molina')
# WorkingBD.connect_salary_and_person('The Amazing Spider-Man','actor','Tobey Maguire',135000)
# WorkingBD.connect_salary_and_person('The Amazing Spider-Man 2','actor','Emma Stone',5221220)
# WorkingBD.update_salary_when_created('The Amazing Spider-Man 2','director','Marc Webb',20)
# WorkingBD.remove_salary_by_person('The Amazing Spider-Man 2', 'director','Marc Webb')
# WorkingBD.add_user('Daniil Pugavko', 'd123123123')
# print(WorkingBD.get_salary_by_person('actor','Emma Stone'))
#WorkingBD.add_director('as','32','3232')
#WorkingBD.add_filmInProgress('ds',32,'dsdsds','sddsds','dsdssd','dasdsadsada')
#WorkingBD.add_filminplan('Atlas Shrugged', 'How talent people fight agaisnt shit','Capitalism, happiness, objectivism','Strike of Atlases', 1000000)
#WorkingBD.remove_actor_by_name('')
#WorkingBD.remove_film_by_title('')
#WorkingBD.remove_director_by_name('')
#WorkingBD.remove_screenwriter_by_name('')
#WorkingBD.remove_composer_by_name('')
#print(WorkingBD.get_director_by_name('Marc Webb'))
#WorkingBD.add_film('500 Days of Summer',12131313,80,2009,10000000,'Marc Webb','I dont know', 'Good guys', 'Joseph Gordon Levitt')
#print(WorkingBD.get_composer_by_name('Hans Zimmer'))
#WorkingBD.remove_film_by_title('500 Days of Summer')
#print(WorkingBD.get_films_title_by_actor('Andrew Garfield'))
#WorkingBD.connect_salary_and_person('Star Wars 1', 'actor', 'Andrew Garfield', 10000000)
#print(WorkingBD.add_film('Example',None,None,None,None,None,None,None, 'Danila'))
#a = ['Andrew Garfield','89157213979','garfield','male','1986']
#a = '"]Andrew Garfield','89157213979','garfield','male','1986']WorkingBD.add_actor]\r\n\r\n"'\
#WorkingBD.get_all_person(WorkingBD, 'director')
#letter = json.dumps(['elem', None, None,None, None,None, None,None,['self.nameEdit.text()']]+ ']WorkingBD.add_film')
#a = letter + ']WorkingBD.add_film'
#print((letter))
#print(WorkingBD.get_salary_by_film('The Amazing Spider-Man 2'))
