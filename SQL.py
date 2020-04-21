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
    age   INT,
    average_salary INT,
    birth_year     INT
            )
        '''
        queryDirector = '''
                CREATE TABLE IF NOT EXISTS director(
                    id    INTEGER CONSTRAINT director_pk PRIMARY KEY AUTOINCREMENT,
        name  TEXT    ,
        phone TEXT   ,
        email TEXT,    
        average_salary INT,
                )
            '''
        queryComposer = '''
                    CREATE TABLE IF NOT EXISTS composer(
    id    INTEGER CONSTRAINT composer_pk PRIMARY KEY AUTOINCREMENT,
    name  TEXT,
    phone TEXT,
    average_salary INT,
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
        average_salary INT,
        num_of_salaries INT,
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
        queryActSal ='''CREATE TABLE IF NOT EXISTS actsal (
        act_id  INTEGER,
        film_id INT,
        salary INT
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
        cursor.execute(queryActor)
        cursor.execute(queryDirector)
        cursor.execute(queryFilm)
        cursor.execute(queryWinners)
        cursor.execute(queryNews)
        cursor.execute(queryScreenwriter)
        cursor.execute(queryAwards)
        cursor.execute(queryActorFilm)
        cursor.execute(queryComposer)
        cursor.execute(queryScrSal)
        cursor.execute(queryDirSal)
        cursor.execute(queryActSal)
        cursor.execute(queryCompSal)

        conn.commit()
        conn.close()
    def update_salary(who,id):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='actor':
            list = []
            cursor.execute(f'''SELECT salary FROM actsal WHERE act_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums+=elem
            if length!=0:
                aver_salery = sums/length
            else:
                aver_salery = 0
            query = f'''UPDATE actor SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who=='director':
            list = []
            cursor.execute(f'''SELECT salary FROM dirsal WHERE dir_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums+=elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE director SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who=='screenwriter':
            list = []
            cursor.execute(f'''SELECT salary FROM scrsal WHERE scr_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums+=elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE screenwriter SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        if who=='composer':
            list = []
            cursor.execute(f'''SELECT salary FROM compsal WHERE comp_id={id!r}''')
            a = cursor.fetchall()
            for elem in a:
                list.append(elem[0])
            length = len(list)
            sums = 0
            for elem in list:
                sums+=elem
            if length != 0:
                aver_salery = sums / length
            else:
                aver_salery = 0
            query = f'''UPDATE composer SET average_salary=? WHERE id={id!r}'''
            cursor.execute(query, (aver_salery,))
        conn.commit()
        conn.close()
    def connect_salary_and_person(film,who,name,salary):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='actor':
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
            if(list.__contains__(filmID)):
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
            WorkingBD.update_salary('actor',actID)
        if who=='director':
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
            if names!=name:
                return
            query = '''
                    INSERT INTO dirsal(dir_id, film_id,salary)
                                    VALUES (?,?,?)'''
            cursor.execute(query, (actID, filmID, salary))
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director',actID)
        if who=='screenwriter':
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
        if who=='composer':
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

    def add_actor(name, phone, email, sex, birth_year):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if(WorkingBD.get_actor_by_name(name).__len__()!=0):
            return
        age = 2020 - int(birth_year)
        query = '''
                   INSERT INTO actor(name, phone, email, sex, birth_year,age)
                                VALUES (?,?,?,?,?, ?)
                '''
        cursor.execute(query, (name, phone, email, sex, birth_year,age))
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

    def get_actor_by_age(age1,which):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if which=='more':
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
        if all_rows.__len__()==0:
            return all_rows
        a = WorkingBD.get_films_by_director(name1)
        all_rows.append(a)
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
        if all_rows.__len__()==0:
            return all_rows
        a = WorkingBD.get_films_by_composer(name1)
        all_rows.append(a)
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
        if all_rows.__len__()==0:
            return all_rows
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
    def get_personID_by_name(name, who):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name = {name!r}''')
        if who=='director':
            cursor.execute(f'''SELECT id FROM director WHERE name = {name!r}''')
        if who=='screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name = {name!r}''')
        if who=='composer':
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

    def get_salary_by_person(who,name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='actor':
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
                a = WorkingBD.get_film_by_id(elem)
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])
            return result
        if who=='director':
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
                a = WorkingBD.get_film_by_id(elem)
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])
            return result
        if who=='screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name ={name!r}''')
            id = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT salary FROM scrtsal WHERE scr_id={id!r}''')
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
                a = WorkingBD.get_film_by_id(elem)
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])
            return result
        if who=='composer':
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
                a = WorkingBD.get_film_by_id(elem)
                result.append(a)
            for i in range(len(sallist)):
                result[i].append(sallist[i])
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
    def remove_salary_by_person(film,who, name):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who == 'composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute( f'''DELETE FROM compsal WHERE comp_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('composer', actID)
        if who == 'director':
            cursor.execute(f'''SELECT id FROM director WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute( f'''DELETE FROM dirsal WHERE dir_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director', actID)
        if who == 'actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute( f'''DELETE FROM actsal WHERE act_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('actor', actID)
        if who == 'screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute( f'''DELETE FROM scrsal WHERE scr_id={actID!r} AND film_id={filmID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('screenwriter', actID)
    def update_salary_when_created(film,who,name,salary):
        conn = sqlite3.connect('Movies.db')
        cursor = conn.cursor()
        if who=='composer':
            cursor.execute(f'''SELECT id FROM composer WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE compsal SET salary = {salary!r} WHERE film_id={filmID!r} AND comp_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('composer', actID)
        if who=='director':
            cursor.execute(f'''SELECT id FROM director WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE dirsal SET salary = {salary!r} WHERE film_id={filmID!r} AND dir_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('director', actID)
        if who=='actor':
            cursor.execute(f'''SELECT id FROM actor WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE actsal SET salary = {salary!r} WHERE film_id={filmID!r} AND comp_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('actor', actID)
        if who=='screenwriter':
            cursor.execute(f'''SELECT id FROM screenwriter WHERE name={name!r}''')
            actID = cursor.fetchall()[0][0]
            cursor.execute(f'''SELECT id FROM film WHERE title={film!r}''')
            filmID = cursor.fetchall()[0][0]
            cursor.execute(f'''UPDATE scrsal SET salary = {salary!r} WHERE film_id={filmID!r} AND comp_id ={actID!r}''')
            conn.commit()
            conn.close()
            WorkingBD.update_salary('screenwriter', actID)
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
#WorkingBD.create_table()
WorkingBD.add_actor('Andrew Garfield','89157213979','garfield','male','1986')
#WorkingBD.remove_film_by_title('The Amazing Spider-Man 2')
WorkingBD.add_film('The Amazing Spider-Man 2',800000000,40,2014,200000000,'Marc Webb','Idiot','Hans Zimmer','Andrew Garfield', 'Emma Stone', 'Jamie Foxx', 'Dane Dehaan', 'Sally Field')
WorkingBD.add_film('Captain America: The Winter Soldier',800000000,70,2014,200000000,'Russo Brothers','Russo Brothers','Michael Jackino','Chris Evans', 'Sam Jackson', 'Scarlett Johanson', 'Robert Redfford', 'Sebastian Stan')
WorkingBD.add_film('The Amazing Spider-Man',800000000,60,2012,200000000,'Marc Webb','Alvin Sargent','James Horner','Andrew Garfield', 'Emma Stone', 'Rhys Ifans')
WorkingBD.add_film('Spider-Man',800000000,80,2002,200000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco')
WorkingBD.add_film('Spider-Man 3',800000000,90,2004,200000000,'Sam Raimi','David Koepp','Danny Elfman','Tobey Maguire', 'Kirsten Dunst', 'Willem Dafoe', 'James Franco', 'Alfred Molina')
WorkingBD.connect_salary_and_person('The Amazing Spider-Man','actor','Tobey Maguire',135000)
WorkingBD.connect_salary_and_person('The Amazing Spider-Man 2','actor','Emma Stone',5221220)
WorkingBD.update_salary_when_created('The Amazing Spider-Man 2','director','Marc Webb',20)
#WorkingBD.remove_salary_by_person('The Amazing Spider-Man 2', 'director','Marc Webb')
print(WorkingBD.get_salary_by_person('actor','Emma Stone'))
