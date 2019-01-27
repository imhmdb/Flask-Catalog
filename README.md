# Flask-Catalog-app
This Project is required for Udacity's FullStack Nanodegree Program.
the main goal of this project is to develop an application that provides a list of items within a variety of categories, The project uses google OAuth to register and login users and is built with python Flask.

Developed By:
> Mohamad Bahamdain

## To Run the Project
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- Download [FSND Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm).

 - Once installed, clone this project and extract the files into the vagrant folder  "/vagrant"
  and then input the following commands:
   ```
    cd vagrant
    vagrant up 
    vagrant ssh
    cd /vagrant
    python database_setup.py
    python database_seeder.py
    python catalog.py
   ```

   you can then access the project at this URL `http://localhost:5000`