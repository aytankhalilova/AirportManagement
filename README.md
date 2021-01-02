# AirportManagement

<i>This is a client-server based console app that is developed by utilizing Flask Restful API, Flask SQLAlchemy and OOP approach.</i>

# Scenario 
* <b>Admin</b> – user that has access to get, post, update and delete flight data
* <b>User</b> – user that has access to get the data

# Installation
 To download console app, you need to type following command:<br/>
 ```
  git clone https://github.com/aytankhalilova/AirportManagement.git
  ```
  
 Then install requirements to have all packets needed for this project:<br/>
 ```
 pip install requirements.txt
 ```
 
 # Usage
 # Server-side: <br/>
Above all, a terminal for the server side is opened. This terminal must operate the ```main.py``` file, so the software can be utilized by administrator and users. When the database isn't generated, with the ```db.create all()``` function which was included at the end of code, must be used in the ```main.py``` file. Server terminal will be stopped manually with entering Ctrl+c in this terminal. <br/>
```
python3 main.py
```
 # Client side: <br/>
 * Admin: <br/>
  After that, the ```insert_admin.py``` file must be executed , due to the admin's username and password should be applied to the database and admin can manage the application. Then client can run the ```admin.py``` file on another terminal if he/she choose to utilize the application as an admin. At the begining of the sesssion admin will need to enter login details (username and password). If authentication and authorization are accurate, then one of the these criteria can be entered as an input: add, update, delete, get, get, all or end. If you select end, the session will be stopped. Instead that, in order to perform the add, get, delete and update functions, admin will be required to select some relevant information.The administrator has to end the session after having the required data.<br/>
  ```
  python3 admin.py
  ```
 * User: <br/>
  Next, the client can run ```user.py``` on another terminal if the client selects a user. In this, two criteria must be entered - departure city and destination city. Then, the collection of one-way flights between these two cities will be displayed. The user session will be ended automatically after obtaining the required information.<br/>
  ```
  python3 user.py
  ```
 
