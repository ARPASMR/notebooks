#!/usr/bin/python
# Gter copyleft
# Author: Roberto Marzocchi


#import librerie
from rasdapy.db_connector import DBConnector
from rasdapy.query_executor import QueryExecutor

#define the connection to sinergico03 (IP: 10.10.0.19)
#on sinergico there is a docker container
print('definisco la connessione')
db_connector = DBConnector("10.10.0.19", 7001, "rasadmin", "rasadmin")

#Create the query executor
query_executor = QueryExecutor(db_connector)



#open the connection to rasdaman
print('Provo a connettermi a rasdaman')
db_connector.open()

print('Mi sono connesso a rasdaman')


result = query_executor.execute_read("select avg_cells(c) from fwi_20190618 as c")
print(result)


#close the connection to rasdaman
db_connector.close()
exit()
