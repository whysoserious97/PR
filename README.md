# PR

Welcome to my lab1 on Network Programing

Here I will implement all the requirements for this lab.

In order to be able to se the result:

Step 1:
download the image from docker and run it

Run the server on port 5000
"docker run -p 5000:5000 alexburlacu/pr-server:latest"

Step 2:
Run the 'MyServer.py' program
In the console you will be able to see what he is getting from the server.

After you see the list of files in console, this means that the script has downloaded the data from the server
and is in the 'server mode' where it will wait for clients requests.

Step 3:

Run 'AsClient.py'.

Insert the querry for the server

SelectColumn <column>  - this statement returns all the specific column records.

ex:
SelectColumn email

SelectFromColumn <column> <pattern> - this statement selects from the specific column the records that matches a regular expresion
ex:
SelectFromColumn first_name olf$
  ["Randolf"]
