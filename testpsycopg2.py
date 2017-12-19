# Database code for the DB Forum, full solution!

import psycopg2, bleach

DBNAME = "news"

def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select er.time,((er.error_requests::decimal/pas.totalrequests::decimal)*100) as errorpercent, er.errorcodes from (select lg.time::date,count(status) as error_requests,status as errorcodes from log lg group by lg.time::date,status having status not similar to '(2|3)%') as er,(select lg.time::date, count(status) as totalrequests from log lg group by lg.time::date) as pas where er.time=pas.time and (er.error_requests::decimal/pas.totalrequests::decimal)>0.01 order by er.time")
    posts = c.fetchall()
    db.close()
    return posts

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
    db.commit()
    db.close()
