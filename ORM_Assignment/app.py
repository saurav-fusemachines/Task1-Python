from cgitb import text
from importlib.metadata import metadata
from itertools import count
from select import select
from urllib import request
from flask import Flask,jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey,MetaData



engine = create_engine('mysql+mysqldb://root:mounteverest8848@localhost:3306/orm_test')

connection = engine.connect()

Session = sessionmaker(bind = engine)

session = Session()

metadata = MetaData()

Base = declarative_base()

app = Flask(__name__)

#MODEL
#USER
class UserDetails(Base):
    __tablename__ = 'userdetails'

    sn = Column(Integer,primary_key = True)
    user_name = Column(String(60))
    burrowed_book_id = Column(Integer)

    def __repr__(self) -> str:
        return super().__repr__()

#BOOK
class Book(Base):
    __tablename__ = 'book'

    book_id = Column(Integer,primary_key=True)
    category = Column(String(60),nullable =False)
    description = Column(String(255),nullable = False)
    book_name = Column(String(60), nullable =False)
    author_name = Column(String(60),nullable = False)

    def __repr__(self) -> str:
         return super().__repr__()

#CREATE TABLE
@app.route('/api/create_table',methods=['GET'])
def create_table():
       Base.metadata.create_all(engine)
       print(engine.table_names())
       return jsonify({'message':'Tables Successfully created.',
       'tables':engine.table_names()})


#INSERT USER DATA
@app.route('/api/insert_user',methods = ['GET'])
def insert_user():
      query = session.query(UserDetails).filter_by(user_name='Joey Tribiani')
      c = query.count()
     
      user = UserDetails(sn=8,user_name='Joey Tribiani',burrowed_book_id=80)
      if c<=2:
          session.add(user)
          session.commit()
          return jsonify({"message":"User added successfully"})
      else:
        return({'message':'User have already accessed 3 books'})    


#INSERT BOOK DATA
@app.route('/api/insert_books/<int:b_id>',methods=['GET'])
def insert_books(b_id):
    try:
        books = Book(book_id=30,category='Drama',description='Descp of the book.',book_name='Hello World',author_name='Olie Watkins')
        session.add(books)
        session.commit()
        return jsonify({'message':'New Book added to library',
                    'book_id':books.book_id,
                    'book_name':books.book_name,
                    'author':books.author_name,
                    'description':books.description
    })
    except:
        return jsonify({'message':'book is already in the list'})


#RETURNED BOOK
@app.route('/api/returned/<int:book_id>',methods=['GET'])
def return_books(book_id):
    try:
      sql = '''
       DELETE  FROM userdetails
       WHERE burrowed_book_id = {0};
    '''.format(book_id)
      with engine.connect() as conn:
        query = conn.execute(sql)    
        session.commit()     
      df = pd.DataFrame(query.fetchall())
    
      return jsonify({'msg':'Book returned'})
   
    except:
        return jsonify({'message':'Book returned'})
        
   
#BOOK LIST
@app.route('/api/book_list',methods = ['GET'])
def book_list():
        sql = '''
        SELECT book_name, count(book_name) AS  Number_of_books
        FROM book
        GROUP BY  book_name;
    '''
        with engine.connect() as conn:
         query = conn.execute(sql)         
        df = pd.DataFrame(query.fetchall())
        session.commit()
        print(df)
    
        return jsonify({'msg':'success'})



#Show Books According to Catgories   
@app.route('/api/book_categories',methods = ['GET'])
def book_cat():
        sql = '''
       SELECT u.user_name, count(burrowed_book_id) AS Burrowed_books
       FROM userdetails u
       LEFT JOIN book b
       ON u.burrowed_book_id = b.book_id AND b.category IN ('Fantasy and Adventure','Drama')
       GROUP BY user_name
    '''
        with engine.connect() as conn:
         query = conn.execute(sql)         
        df = pd.DataFrame(query.fetchall())
        session.commit()
        print(df)
    
        return jsonify({'msg':'success'})



#Books which is famous among users[top 5] 
@app.route('/api/top_5',methods = ['GET'])
def top_5_famous():
        sql = '''
      SELECT u.user_name, count(burrowed_book_id) AS Burrowed_books, b.category
      FROM userdetails u
      LEFT JOIN book b
      ON u.burrowed_book_id = b.book_id
      GROUP BY user_name
      ORDER BY Burrowed_books DESC ;
    '''
        with engine.connect() as conn:
         query = conn.execute(sql)         
        df = pd.DataFrame(query.fetchall())
        session.commit()
        print(df)
    
        return jsonify({'msg':'success'})




#UPDATE BOOK 
@app.route('/api/update',methods = ['GET'])
def update_booklist():
    update_query = session.query(Book).filter_by(book_id=1).update(dict(book_name="Nepali"))
    session.commit()
    

    return jsonify({'msg':'success'})
     

if __name__ == '__main__':
    app.run(debug=True)

