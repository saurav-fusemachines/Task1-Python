from importlib.metadata import metadata
from multiprocessing import connection
from select import select
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table



# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('mysql:///census.sqlite')  #census.sqlite is database name

connection = engine.connect()

stmt = 'SELECT * FROM People'

result_proxy = connection.execute(stmt)   #result_proxy is a ResultProxy

result = result_proxy.fetchall()  #Fetch all data from the result_proxy  Result is a ResultSet.

#Handling ResultSets
first_row = result[0]   #returns 1st rows data

print(first_row.keys())  #returns the columns of first_row

print(first_row.column_ko_name)  # returns 1st element from the specific column name



#SQLALCHEMY QUERYING
# Import,metadata,census same huncha
census = Table('census',metadata,autoload =True,autoload_with = engine)
stmt = select([census])
# result = connection.execute(stmt).fetchall
print(stmt) 