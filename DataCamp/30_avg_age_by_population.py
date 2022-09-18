# Import select and func
from importlib.metadata import metadata
from multiprocessing import connection
from select import select
from sqlalchemy import create_engine,func,MetaData, Table, select

engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
connection = engine.connect()

census = Table('census',metadata,autoload =True,autoload_with = engine)

from sqlalchemy import select, func

#select the average age weighted by pop2000
stmt = select([func.sum(census.columns.pop2000 * census.columns.age) / func.sum(census.columns.pop2000)])


# *************************************************************************************************************
# Import select and func
from sqlalchemy import select, func

#select the average age weighted by pop2000
# Modify the select statement to alias the new column with weighted average as 'average_age' using .label().
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) / func.sum(census.columns.pop2000)).label('average_age')])


# *************************************************************************************************************
# Import select and func
from sqlalchemy import select, func

# Add the sex column to the select statement
stmt = select([census.columns.sex,
                (func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age')          
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# *****************************************************************************************************************

# Import select and func
from sqlalchemy import select, func

# Select sex and average age weighted by 2000 population
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age'),
               census.columns.sex
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and fetch all the results
results = connection.execute(stmt).fetchall()

# print the sex and average age column for each result
for result in results :
    print (result.sex,result.average_age)
