
# test about xmlrpc

import xmlrpc.client

connection = xmlrpc.client.Server("http://www.pythonchallenge.com/pc/phonebook.php")
print(connection.system.listMethods())
print(connection.phone("Bert"))

