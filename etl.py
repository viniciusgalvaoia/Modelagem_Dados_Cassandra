import os
import glob
import cassandra
import csv
from cassandra.cluster import Cluster
from sql_queries import *


def process_event_file(session, file):
    
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(session_activity_table_insert, (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
            session.execute(user_activity_table_insert, (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))
            session.execute(song_event_table_insert, (line[9], line[1], line[4]))

            
def process_csv_files(datapath):

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + datapath

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
    
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
    
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    
    # for every filepath in the file path list 
    for f in file_path_list:

        # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
        
            # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line)
                
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


def main():
    
    try: 
        cluster = Cluster() 
    
        # create a session to establish a connection and for executing queries on
        session = cluster.connect()
    except Exception as e:
        print(e)
        
        # Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('sparkfydb')
    except Exception as e:
        print(e)
    
    process_csv_files(datapath = '/event_data')
    process_event_file(session, file = 'event_datafile_new.csv')

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()