# Import create_engine function
from sqlalchemy import create_engine,select,Table,metadata

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
connection = engine.connect()


# Use the .table_names() method on the engine to print the table names
print(engine.table_names())     
census = Table('census',metadata,autoload =True,autoload_with = engine)

# ********************************************************************************************

# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York : stmt_filtered
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000
for result in results:
    print(result.age, result.sex, result.pop2000)



# ************************************************************************************************
# Usingin_()

states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)



# stmt.where(
#  or_(census.columns.state == 'Calafornia',census.columns.state='New York')
# )
