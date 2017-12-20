from report_psgcon import question1, question2, question3

def export_reports():
    # Export the results from the DB to a file
    output_file = open('reportingtool_output.txt', 'w')

    # Maintains questions and results format in a string
    rendered_content = '''1. What are the most popular three articles of all 
    time?\n'''
    rendered_content += "".join('''    %s -- %s views\n''' % ('"'+article+'"', 
                                                              totalviews)
                                for totalviews, article in question1())
        
    rendered_content += '''\n2. Who are the most popular article authors of all
    time?\n'''
    rendered_content += "".join('''    %s -- %s views\n''' % (name, totalviews)
                                for slug, totalviews, name in question2())
    question2()
    
    rendered_content += '''\n3. On which days did more than 1% of requests lead 
    to errors?\n'''
    rendered_content += "".join('''    %s -- %.2f %s errors\n''' % 
                                (time.strftime('%B %d, %Y'), errorpercent, "%")
                                for time, errorpercent, errorcodes in 
                                question3())
    
    # write the string content in a file
    output_file.write(rendered_content)
    output_file.close()

if __name__ == '__main__':
    export_reports()
