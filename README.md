# Log analysis
A reporting tool to export the log data

## Getting Started
Clone the repo to your pre-installed and appropriate vagrant location carefully.

```sh
git clone https://github.com/chakradhar-s/log_analysis.git
```
## Prerequisites needed technologies to run scripts
Python with any version 2.x and 3.x.

[Instructions to setup vagrant environment and run vagrant are on](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

[Download the newsdata.sql from](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

- Extract the files in the zip and Put those files into the vagrant directory, which is shared with your virtual machine.
- Data was loaded by runing psql -d news -f newsdata.sql on a postgre server.

- Change the directory to the path of the cloned repository on your terminal/command prompt by cd "the path of the cloned repository" 

Run the script to create a report file
```sh
python report_tool.py
```
After the script was run successfully an acknowledgement, which tells a location of the output file, is displayed.
