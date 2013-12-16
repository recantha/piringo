piringo
=======
The PiRingo is an add-on board created by 4tronix.
Documentation and build instructions for the board can be found at:
http://4tronix.co.uk/piringo


The scripts here are to create an internet-of-things interface to control the PiRingo.

Put both files in the same folder
Then run:
sudo python server.py

This runs a web server on port 8080 (you can change that in server.py).

Then, call http://server:8080/circuit.py
