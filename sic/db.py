#!/usr/bin/python3.6

try :
    import psycopg2, os, crypt, binascii
except ImportError as e :
    print("[!] Missing module : ",e)


x = '44523057353534505f433146'
y =  binascii.unhexlify(x)
z = str(y,'ascii')
pwd = crypt.crypt(z[::-1],"0x")

def create_table(table_name): 
    try :
        conn = psycopg2.connect(database="sic_db", user="sic_user", password=pwd, host="127.0.0.1", port="5432")
    except Exception as e :
        print("[!] ",e)
    else :
        c = conn.cursor()
        c.execute('''CREATE TABLE '''+table_name+
        ''' (file_path TEXT PRIMARY KEY NOT NULL, 
        file_hash TEXT, 
        check_some TEXT,
        file_inode TEXT NOT NULL, 
        file_permission TEXT NOT NULL,
        file_uid TEXT NOT NULL,
        file_gid TEXT NOT NULL, 
        file_reference TEXT NOT NULL, 
        file_table TEXT NOT NULL);''')
        conn.commit()
    finally :
        conn.close()

def drop_table(table_name):
    try :
        conn = psycopg2.connect(database='sic_db', user="sic_user" , password=pwd, host="127.0.0.1", port="5432")
    except Exception as e :
        print("[!] ,",e)
    else : 
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS "+table_name)
        conn.commit()
    finally :
        conn.close()


def insert_table(table_name,row,verbose):
    try :
        conn = psycopg2.connect(database="sic_db", user="sic_user", password=pwd, host="127.0.0.1", port="5432")
    except Exception as e :
        print("[!] ",e)
    else : 
        c = conn.cursor()
        if verbose :
              print(str(row))
        c.execute("INSERT INTO "+table_name+" (file_path , file_hash , check_some , file_inode , file_permission , file_uid , file_gid , file_reference , file_table) VALUES "+str(row))
        conn.commit()
    finally :
        conn.close()

def retrieve_row(table_name,file_path):
    try :
        conn = psycopg2.connect(database="sic_db", user="sic_user", password=pwd, host="127.0.0.1", port="5432")
    except Exception as e :
        print("[!] ",e)
    else :
        c = conn.cursor()
        c.execute('SELECT * from '+table_name+' WHERE file_path = \''+file_path+'\'')
        row = c.fetchone()
        return row

    finally :
        conn.close()

