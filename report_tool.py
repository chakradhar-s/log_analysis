#!/usr/bin/env python2

import os
from report_psgcon import question1, question2, question3


# Export the results from the DB to a file
def export_reports():
    output_file = open('reportingtool_output.txt', 'w')

    solution1 = question1()
    solution2 = question2()
    solution3 = question3()

# Maintains questions and results format in a string
    rendered_content = '''1. What are the most popular three articles of all
    time?\n'''
    if(len(solution1) > 0):
        rendered_content += "".join('''    %s -- %s views\n'''
                                    % ('"' + article + '"', totalviews)
                                    for totalviews, article in solution1)
    else:
        rendered_content += "No data was found.\n"

    rendered_content += '''\n2. Who are the most popular article authors of all
    time?\n'''
    if(len(solution2) > 0):
        rendered_content += "".join('''    %s -- %s views\n'''
                                    % (name, totalviews)
                                    for count, totalviews, name in solution2)
    else:
        rendered_content += "No data was found.\n"

    rendered_content += '''\n3. On which days did more than 1% of requests lead
    to errors?\n'''
    if(len(solution3) > 0):
        rendered_content += "".join('''    %s -- %.2f %s errors\n'''
                                    % (time.strftime('%B %d, %Y'),
                                       errorpercent,
                                       "%")
                                    for time, errorpercent
                                    in solution3)
    else:
        rendered_content += "No data was found.\n"

# write the string content in a file
    output_file.write(rendered_content)
    output_file.close()

# Acknowledgment
    outputPath = os.path.abspath(output_file.name)
    print(' Successfully! generated reports to the %s\n' % (outputPath))

if __name__ == '__main__':
    export_reports()
