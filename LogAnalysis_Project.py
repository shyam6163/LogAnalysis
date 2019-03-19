#!/usr/bin/env python3

import psycopg2

db_name = "news"
def run_query(query1):
    """Database Connection Setup for Query Executions"""
    db = psycopg2.connect('dbname=' + db_name)
    c = db.cursor()
    c.execute(query1)
    rows = c.fetchall()
    db.close()
    return rows


def top_articles():
    """TOP THREE MOST ARTICLES"""

    # Build Query String
    query1 = """
        SELECT articles.title, COUNT(*) AS total
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY total DESC
        LIMIT 3;
    """
    # Run Query
    results = run_query(query1)
    # Print Results
    print("\n######################################")
    print(' VIEWS THE TOP MOST THREE ARTICLES  :')
    print("######################################")
    count = 1
    for i in results:
        print('(' + str(count) + ') "' + i[0] + '" :: ' + str(i[1]) + " views")
        count += 1
def top_authors():
    """TOP THREE MOST AUTHORS"""

    # Build Query String
    query1 = """
        SELECT authors.name, COUNT(*) AS total
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY total DESC
        LIMIT 3;
    """
    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n######################################")
    print('TOP THREE MOST AUTHORS:')
    print("######################################")
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' :: ' + str(i[1]) + " views")
        count += 1


def percentage_errors():
    """Percentage of Days Error  which leads more than 1% of requests"""

    # Build Query String
    query1 = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS Percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS Error_Requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS Requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.Error_Requests*1.0) / total.Requests), 3) > 0.01)
        ORDER BY Percent DESC;
    """

    # Run Query
    results = run_query(query1)

    # Print Results
    print("\n######################################")
    print('PERCENTAGE OF DAYS WITH MORE THAN 1% ERRORS:')
    print("######################################")

    for i in results:
        date = i[0].strftime('%B, %d, %Y')
        per = str(round(i[1]*100, 1))
        print(date + " -- " + per + "%" + " errors")

print('\nThe Results are:')
top_articles()
top_authors()
percentage_errors()
