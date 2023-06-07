from contextlib import contextmanager

@contextmanager
def connection(db_name):
    try: 
        conn_string = f"host=localhost dbname={db_name} user=postgres password=root"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        yield (conn, cur)
        
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        traceback.print_exc()
        print(e)
    
    finally :
        conn.commit()
        cur.close()
        conn.close()




def inserting_value(DF,db_name,table_name):
    try:
        # Basically we need list of tuples of records. We can not use DF.to_record function as it returned numpy objects
        # Which are not suitable here
        list_of_tuple = [tuple(row) for row in DF.itertuples(index=False)]
        
        # to get lenght of row
        length = len(list_of_tuple[0])

        # Just to get no. %s 
        string_format = (",").join(["%s"] * length)
        
        with connection(db_name) as (conn, cur):

        # get tuples in string format
            args = ','.join(cur.mogrify(f"({string_format})", i).decode('utf-8')
            for i in list_of_tuple)

        # real query
        #args = ','.join([f"({string_format})" % i for i in list_of_tuple]

            query = f"INSERT INTO {table_name} VALUES " + (args)
            cur.execute(query)
            
        return query
        
    except Exception as e:
        return e
        
        
def connection_v(db_name):
    conn = None
    cur = None
    return conn,cur
        
        

        

        
