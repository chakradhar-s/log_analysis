import os
from testpsycopg2 import question1, question2, question3

def open_movies_page():
    # Create or overwrite the output file
    output_file = open('reportingtool_output.txt', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = '''1. What are the most popular three articles of all time?\n'''
    rendered_content += "".join('''    %s -- %s views\n''' % ('"'+article+'"', totalviews)for totalviews, article in question1())
        
    rendered_content += '''\n2. Who are the most popular article authors of all time?\n'''
    rendered_content += "".join('''    %s -- %s views\n''' % (name, totalviews)for slug, totalviews, name in question2())
    question2()
    
    rendered_content += '''\n3. On which days did more than 1% of requests lead to errors?\n'''
    rendered_content += "".join('''    %s -- %s %s errors\n''' % (time.strftime('%B %d, %Y'), errorpercent, "%")for time, errorpercent, errorcodes in question3())
    
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)

if __name__ == '__main__':
    open_movies_page()
