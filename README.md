#CEGO Job Interview Assignment

Assignment can be found in Assignment.md

Given a query, the solution will select that data from the database, write it to a given filename and delete the entry from the database.

Data integrity is secured by searching the file for the entry before deletion.

The solution can be tested by running test.py.

The parameters (such as database connection, query and filename) for the solution can be changed in config.py

Security Concerns:
	
	Writing user and password in a file
	
	Adding user & password to VCS!

Next Steps:
	
	Better Exception handling (for functions).

	Better checking of data integrity (more reliable method).

	Improve handling of file creationg (possibly make choice for append, in case new data should be appended to old).