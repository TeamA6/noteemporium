THE NOTE EMPORIUM

To run Note Emporium locally one must:

1. Clone this repository into a directory on the local machine.
2. Ensure they have the requirements needed for the project listed in requirements.txt (they can also be installed
    from that file by running pip install <file>
3. Navigate to the repository via command line and synchronise the database by running:
        $ python manage.py syncdb
    Then run the server:
        $ python manage.py runserver
4. The server should now launch and were you to visit the ip address shown in terminal appended with /note you should
    see the site
5. The default port is 8000 so the homepage will (by default) be viewable at 127.0.0.1:8000/note although this can be changed
    when you run the server by appending with a different port (e.g. 8001)

Thank you for visiting.

This application was made by:
Alex Smith, Lorenzo Betto, Yiting Shen and William Kavanagh