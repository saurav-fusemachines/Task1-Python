# Import select
from sqlalchemy import MetaData, Table, select
from importlib.metadata import metadata
from multiprocessing import connection
from select import select
from sqlalchemy import create_engine

engine = create_engine('mysql:///census.sqlite')
# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)