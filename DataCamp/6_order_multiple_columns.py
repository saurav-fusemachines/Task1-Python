'''We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or
 descending order for each individual column. Each column in the .order_by() method is fully sorted from left to right. This means 
 that the first column is completely sorted, and then within each matching group of values in the first column, it's 
 sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.'''

# Import and_
from sqlalchemy import MetaData, Table, select
from importlib.metadata import metadata
from multiprocessing import connection
from select import select
from sqlalchemy import create_engine,desc

engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
connection = engine.connect()

census = Table('census',metadata,autoload =True,autoload_with = engine)
# Build a query for the census table: stmt
stmt = select([census])

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])


