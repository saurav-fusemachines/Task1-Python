# Import insert
from sqlalchemy import insert

# Build an insert statement : stmt
stmt = insert(census)

# Use values_list to insert data: results   
results = connection.execute(stmt,values_list)

# Print rowcount
print(results.rowcount)