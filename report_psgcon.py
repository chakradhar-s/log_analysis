# Database code for the report tool

import psycopg2
import bleach


DBNAME = "news"


# Query to answer the question 1
def question1():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute('''select count(path) totalviews, 
        substring(path from '([a-zA-z\-]+)$') article from log
        where status similar to '(2|3)%' group by path 
        having path like '%/article%' order by totalviews 
        desc limit 3''')
        posts = c.fetchall()
        db.close()
        return posts
    except:
        print "Failed to read on postgre"
        raise    


# Query to answer the question 2
def question2():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute('''select ar.slug, dt.total totalviews,au.name from authors au, 
        articles ar,(select count(path) total, path,
        substring(path from '([a-zA-z\-]+)$') as sub from log group by path 
        having path like '%/article%' order by total desc) dt  
        where au.id=ar.author and dt.sub=ar.slug''')
        posts = c.fetchall()
        db.close()
        return posts
    except:
        print "Failed to read on postgre"
        raise        


# Query to answer the question 3
def question3():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute('''select er.time,
        ((er.error_requests::decimal/pas.totalrequests::decimal)*100) 
        as errorpercent, er.errorcodes from 
        (select lg.time::date,count(status) as error_requests,
        status as errorcodes from log lg group by lg.time::date,status 
        having status not similar to '(2|3)%') as er,
        (select lg.time::date, count(status) as totalrequests from log lg 
        group by lg.time::date) as pas where er.time=pas.time and 
        (er.error_requests::decimal/pas.totalrequests::decimal)>0.01 
        order by er.time''')
        posts = c.fetchall()
        db.close()
        return posts
    except:
        print "Failed to read on postgre"
        raise    
