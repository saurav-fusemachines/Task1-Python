# Import delete, select
from sqlalchemy import delete, select,create_engine,metadata,Table
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
connection = engine.connect()

census = Table('census',metadata,autoload =True,autoload_with = engine)

# Build a statement to empty the census table: stmt
delete_stmt = delete(census)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table : select_stmt
select_stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(select_stmt).fetchall())
