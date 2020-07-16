import geopandas
import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "zxcvbnm",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "test")
    
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")
    
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")
    
    sql = "select * from pan_adm1"
    
    df = geopandas.GeoDataFrame.from_postgis(sql,connection,geom_col='geom')
    df.plot()
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            



