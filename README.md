# Log analysis
A reporting tool to export the log data

## Getting Started
Clone the repo to your pre-installed and appropriate vagrant location carefully.

```sh
git clone https://github.com/chakradhar-s/log_analysis.git
```
## Prerequisites needed technologies to run scripts
Python with any version 2.x and 3.x.

Data was loaded by runing psql -d news -f newsdata.sql on a postgre server.

- Change the directory to the path of the cloned repository on your terminal/command prompt by cd "the path of the cloned repository" 

Run the script to create a report file
```sh
python report_tool.py
```
After the script was run successfully an acknowledgement, which tells a location of the output file, is displayed.
