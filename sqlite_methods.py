#DB without server
import sqlite3
#error management
from sqlite3 import Error
import datetime
#DB File
DB = "securities master.sqlite3"
def create_connection(db_file=DB):
    """
    Create sqlite db connection
    """
    con = None
    try:
        con = sqlite3.connect(db_file,detect_types=sqlite3.PARSE_DECLTYPES)
        return con
    except:
        print("Connection was not created")

def create_table(con,create_table_sql):
    """
    create table con=connection obj, table_sql=script to make table
    """
    try:
        c = con.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def execute_query(con,query):
    """
    execute query and fetch all records the cursor points to
    """
    try:
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        fetchall = cur.fetchall()
        cur.close()
        return fetchall
    except Error as e:
        print(e)

def insert_rows_query(con,table,table_vars,values_list):
    """
    Insert values as row into table
    """
    _list = list()
    for values in values_list:
        values_str =  ", ".join(str(x) for x in values)
        _list.append("("+values_str+")")
    try:
        values_str = ",".join(str(x) for x in _list) 
        table_vars_str = ",".join(str(x) for x in table_vars)
        final_str = " INSERT INTO "+table+" ("+table_vars_str+") VALUES "+values_str
        execute_query(con,final_str)
    except Error as e:
        print(e)
def select_all_from(con,table):
    """
    Query all rows in table
    """
    try:
        final_str = "SELECT * FROM " + table
        return execute_query(con,final_str)
    except Error as e:
        print(e)

def clean_strs_for_DB_query(_list):
    """
    Modify list by modifying strings. remove all ','
    from inside of strings and put quotes around each string
    """
    for i,s in enumerate(_list):
        try:
            if type(s)==str:
                _list[i] = "'"+s+"'"
            if ',' in s and type(s)==str:
                _list[i]=_list[i].split(',')
                _list[i] = " ".join(_list[i])

                _list[i]=_list[i].split('.')
                _list[i] = " ".join(_list[i])
        except:
            pass

def datetime_to_timestamp(date):
    return date.timestamp()
def timestamp_to_datetime(time):
    return datetime.datetime.fromtimestamp(time)
