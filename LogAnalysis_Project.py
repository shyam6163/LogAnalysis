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
    query1 = """select articles.title, count(*) as views
    from articles inner join log on log.path
    like concat('%', articles.slug, '%')
    where log.status like '%200%' group by
    articles.title, log.path order by views desc limit 3
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
        Select authors.name, COUNT(*) AS total
        from authors inner
        join articles
        on authors.id = articles.author
        join log
        on log.path like concat('/article/%', articles.slug)
        group by authors.name
        order by total desc
        limit 3;
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
        select total.day,
          round(((errors.error_requests*1.0) / total.requests), 3) as Percent
        from (
          select date_trunc('day', time) "day", count(*) as Error_Requests
          from log
          where status like '404%'
          group by day
        ) as errors inner
        join (
          select date_trunc('day', time) "day", count(*) as Requests
          from log
          group by day
          ) as total
        on total.day = errors.day
        where (round(((errors.Error_Requests*1.0) / total.Requests), 3) > 0.01)
        order by Percent desc
    """

    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n")
    print('On which days did more than 1% of requests lead to errors?')

    for i in results:
        date = i[0].strftime('%B, %d, %Y')
        per = str(round(i[1]*100, 1))
        print(date + " is " + per + "%" + " errors")

print('\nThe Results are as follows:')
top_articles()
top_authors()
percentage_errors()
