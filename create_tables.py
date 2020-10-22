import cassandra
from cassandra.cluster import Cluster
from sql_queries import create_table_queries, drop_table_queries


def create_keyspace():
    """
    - Creates and set keyspace to the sparkifydb
    - Returns the session to sparkifydb
    """
    
    # create a session to establish a connection and for executing queries on
    try: 
        cluster = Cluster() 
        session = cluster.connect()
    except Exception as e:
        print(e)
    
    # Create keyspace
    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkfydb 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")

    except Exception as e:
        print(e)
    
    # Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('sparkfydb')
    except Exception as e:
        print(e)
        
    return cluster, session


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        session.execute(query)


def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        session.execute(query)


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cluster, session = create_keyspace()
    
    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()