# APP for storing user data

## Overview of this app

This app stores given user data to database

User gives data of:

* First Name
* Last Name
* Address (street, city, state and zip)

This app has two User types

1. Parent User
2. Child User

Parent User can have address but the Child User can not have any address of it's own and it belongs to a parent

* On the Home page all the parent list is given
* New Parent and New Child can be created from the home page
* Parent can be updated, deleted and view detail from the home page
* Deleting parent will automatically delete the belonging child
* To update or delete child we need to go to detail page

For this app data is stored in **mysql** database

Applications required to run this app:

* MySQL database and localserver (I used laragon)(<https://sourceforge.net/projects/laragon/files/releases/4.0/laragon-full.exe/download>)

* Python (<https://www.python.org/downloads/>)
  * Note: Check the `Add python 3.9 to PATH` box on the installation stage

## Run the project

* First create a database in your local host server
* Give database name `user` and set username `root` and password `root`
* `cd` to the project directory
* Execute the command `python create.py` to create the tables in the database
* Execute the command `pip install -r requirements.txt` to install all the dependencies
* Now run the project with `python application.py` command
