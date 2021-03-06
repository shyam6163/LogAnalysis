# Udacity Log Analysis Project
By CH.Shyam Prasad
This is the project from udacity NanoDegree : [Fullstack Web Developer](https://classroom.udacity.com/nanodegrees/nd004/dashboard/overview)

#### Your task is to create a reporting tool that prints out reports (in plain text) 

based on the data in the database. This reporting tool is a
Python program using the psycopg2 module to connect to the database. 

### Here is your Tasks to Answer:-
1. **What are the most popular three articles of all time?** Which
  articles have been accessed the most? Present this information as a
  sorted list with the most popular article at the top.
2. **Who are the most popular article authors of all time?** That is,
   when you sum up all of the articles each author has written, which
   authors get the most page views? Present this as a sorted list with
   the most popular author at the top.
3. **On which days did more than 1% of requests lead to errors?** The
   log table includes a column status that indicates the HTTP status
   code that the news site sent to the user's browser. (Refer to this
   lesson for more information about the idea of HTTP status codes.) 
   
### Tools to Install for Project Setup:

1. **Vagrant** - [Vagrant 2.2.3](https://releases.hashicorp.com/vagrant/2.2.3/vagrant_2.2.3_x86_64.msi)
2. **VirtualBox** - [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. Download vagrant setup files from **[Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)**
This files contains all configuration (Python3, Postgresql,PIP8 etc) setup for our project
4. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
5. After downloading goto downnloads folder and extract the zip file name contans **LOGS_ANALYSIS**
6. Keep it there (or) you can move to your own project path
7. Download this project:(https://github.com/shyam6163/LogAnalysis

### Process of executing the project:
1. Goto Vagrant folder
2. Open command prompt (or) Git Bash 
3. Run **vagrant up** - It is used to start the commandline virtual machine for the first it may take very long time depending on your internet connection
4. Run **vagrant ssh** It is the command to enter into the virtual machine
5. use command 'psql -d news -f newsdata.sql' to load database
   -use '\c' to connect to database="news"
   -use '\dt' to see the tables in database
   -use '\dv' to see the views in database
   -use '\q' to quit the database
6. Then run the project **python LogAnalysis_Project.py**


Note: It takes some time to run queries.

### Outpt that you got from the execution:
The Results are as follows:


What are the most popular three articles of all time in the Data
 (1) "Candidate is jerk, alleges rival" = 338647 views
 (2) "Bears love berries, alleges bear" = 253801 views
 (3) "Bad things gone, say good people" = 170098 views


Who are the most popular article authors of all time in the Data?
 (1) Ursula La Multa = 507594 views
 (2) Rudolf von Treppenwitz = 423457 views
 (3) Anonymous Contributor = 170098 views


 On which days did more than 1% of requests lead to errors?
 July, 17, 2016 is 2.3% errors