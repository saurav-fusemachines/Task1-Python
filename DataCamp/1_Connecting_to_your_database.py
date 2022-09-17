# Import create_engine
from importlib.metadata import metadata
from multiprocessing import connection
from sqlalchemy import create_engine

from sqlalchemy import MetaData, Table
# Metadata object is a catalog that stores database

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('mysql:///census.sqlite')  #census.sqlite is database name

connection = engine.connect()

# Print table names
print(engine.table_names())  #returns the list of tables name


#Reflection
# Reflection reads database and builds SQLAlchemy table objects

metadata = MetaData() #to reflect the table,we initalize MetaData object.

census = Table('census',metadata,autoload =True,autoload_with = engine)

# Print the column names
print(census.columns.keys())

print(repr(census))  #function repr shows the details of our table we stored in census

#O/P: Table('census', MetaData(), Column('state', VARCHAR(length=30), table=<census>), 
#   Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)