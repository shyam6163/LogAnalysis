import psycopg2

db_name = "news"


def run_query(query1):
    """Database Connection Setup for Query Executions In Log Analysis"""
    db = psycopg2.connect('dbname=' + db_name)
    c = db.cursor()
    c.execute(query1)
    rows = c.fetchall()
    db.close()
    return rows


def top_articles():
    """Top Three Most Articles of all Time"""

    # Build Query String
    query1 = """WITH top_three_articles as (select b.title,a.cnt from
     (select path,count(*) cnt from log  where status
     like '%200%' group by path) a
     inner join articles b on a.path like concat('%', b.slug, '%'))
     select top_three_articles.title,top_three_articles.cnt
     from top_three_articles order by top_three_articles.cnt desc limit 3
    """

    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n")
    print('What are the most popular three articles of all time in the Data?')
    count = 1
    for i in results:
        print('(' + str(count) + ') "' + i[0] + '" = ' + str(i[1]) + " views")
        count += 1


def top_authors():
    """Top Three Most Article Authors of all Time"""

    # Build Query String
    query1 = """
       WITH top_three_views as (select c.name,sum(a.cnt) "views"
        from (select path,count(*) cnt from log  where status
        like '%200%' group by path) a
        inner join articles b on a.path like concat('/article/%', b.slug)
        inner join authors c on
        (b.author=c.id) group by c.name)
        select * from top_three_views order by "views" desc limit 3
    """

    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n")
    print('Who are the most popular article authors of all time in the Data?')

    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' = ' + str(i[1]) + " views")
        count += 1


def percentage_errors():
    """Percentage of Days Error  which leads more than 1% of requests"""

    # Build Query String
    query1 = """
          WITH errors as (select a.day,b.Error_Requests,a.Requests,
          (((Error_Requests*1.0)/Requests)*100) as
          error_percentage from (select time::date "day",
          count(*) as Requests from log group by time::date) a
          inner join
 (select time::date "day", count(*) as Error_Requests
 from log where status like '%NOT FOUND'
 group by time::date) b on (a.day=b.day))
 select errors.day,errors.error_percentage
 from errors where errors.error_percentage > 1;
    """

    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n")
    print('On which days did more than 1% of requests lead to errors?')

    for i in results:
        date = i[0].strftime('%B, %d, %Y')
        per = str(round(i[1], 1))
        print(date + " is " + per + "%" + " errors")

print('\nThe Results are as follows:')
top_articles()
top_authors()
percentage_errors()
