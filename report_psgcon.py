# Database code for the report tool

import psycopg2


DBNAME = "news"


# Query to answer the question 1
def question1():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(
            '''select count(path) totalviews, ar.title article from log lg,
            articles ar where status similar to '(2|3)%' and
            path like '%/article%' and
            substring(path from '([a-zA-z\-]+)$') = ar.slug group by path,
            ar.title order by totalviews desc limit 3''')
        posts = c.fetchall()
        db.close()
        return posts
    except Exception as e:
        print(e)
        raise


# Query to answer the question 2
def question2():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute('''select count(ar.slug), SUM(dt.total) as totalviews,au.name
        from authors au,
        articles ar,(select count(path) total, path,
        substring(path from '([a-zA-z\-]+)$') as sub from log
        where path like '%/article%' group by path order by total desc) dt
        where au.id=ar.author and dt.sub=ar.slug group by au.id''')
        posts = c.fetchall()
        db.close()
        return posts
    except Exception as e:
        print(e)
        raise


# Query to answer the question 3
def question3():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute('''select er.time,
        ((er.error_requests::decimal/pas.totalrequests::decimal)*100)
        as errorpercent from
        (select lg.time::date,count(status) as error_requests
        from log lg where status not similar to '(2|3)%'
        group by lg.time::date) as er,
        (select lg.time::date, count(status) as totalrequests from log lg
        group by lg.time::date) as pas where er.time=pas.time and
        (er.error_requests::decimal/pas.totalrequests::decimal)>0.01
        order by er.time''')
        posts = c.fetchall()
        db.close()
        return posts
    except Exception as e:
        print(e)
        raise
