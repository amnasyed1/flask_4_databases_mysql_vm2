# flask_4_databases_mysql_vm
Manually setting up and running a database on a cloud VM. Hands-on experience setting up a MySQL instance on a VM

## Virtual Machine Setup on Azure 
1. Log into your Azure Account.
2. Locate the hamburger icon on the left-hand side of the screen, click it, then locate `Virtual Machine` on the menu list, and click it.
3. Once on the `Virtual Machine` page, click `+ Create`, which is located towards the top of the page, and then click the first option on the drop down, `Azure virtual machine`.
4. The page will automatically navigate to the proper page, and land you under the `Basics` tab. Under the Basics tab, ensure your subscription is `Azure for Students`, and create and name a new resouce group. I named my resource group `504-wk4b`.
5. Under `Instance details`, give your VM a name. I named mine `AmnaMySQL`. Next, change the `Security type` it `Standard`.
6. Next to `Size`, select `See all sizes ` and then under `VM sizes`, scroll to find `B-series`, click the drop down, and then click on `B1ms`, ensure the row gets highlighted and then click select. The selection should look like the screenshot below:
   ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/d3c64bc5-88bf-4961-8ac5-228d7ad529fd)
7. Under `Administrator account` for the `Authentication type` select `Password`. Now configure a `Username` and `Password`.
8. For the port, under `Inbound port rules`, go to `select inbound ports`, click the drop-down, and select `HTTP (80)` and `HTTPS (443)`.
9. Next, navigate to the `Networking` tab, located in same row as the Basics tab.
10. Click the box next to `Delete public IP and NIC whne VM is deleted` so the box is check marked.
11. Click `Review + Create`, review all the information presented to ensure it is correct, the price should look like the screenshot below:
 ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/d3054fc1-1853-4fc6-a2e2-533d141fe001)


14. If all looks well, click `Create`.
## Virtual Machine Setup on GCP
1. Log into your Google Cloud account, ensure you are in `console.cloud.google.com`, and navigate to the hamburger icon on the left-hand side, and click on `Compute Engine` from the menu.
2. Click `Create Instance`, and name your instance. I named mine `amna-504-sql`.
3. Under `Machine Type` select this:
 ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/0ee3d302-f590-4700-88ad-48c6829e312a)

4. Under `Firewall`, select  `Allow HTTP traffic` and `Allow HTTPS traffic`.
5. Keep everything else under the default settings and click `Create`.

## MySQL Setup for Azure VM on Cloud Shell & Connecting Cloud Shell to MySQL Workbench Username
1. Go to shell.cloud.google.com, and in the terminal type `ssh` followed by your username the '@' symbol and the public IP address that Azure provided, and then hit enter. For example, I typed `ssh amna@IPaddress`. 
2. After that, it will ask for a password. The password you type in is the password you had chosen in the Azure VM setup above.
3. Next, in the terminal type `sudo apt-get update` and hit enter. Then type `sudo apt install mysql-client mysql-server` and hit enter. This will install MySQL Client and MySQL Server. Tp check if the programs were installed, you can type `mysql` and hit enter. If it states access was denied, it means MySQL was successfully installed.
4. Type `sudo mysql`, and it should show `mysql>` in the terminal after hitting enter. It is important to remember after every command add a ';' and then hit enter. For instance to view databases you can type `show databases;` and it will display the databases.
5. To create a user: in the terminal next to mysql>, type `create user 'yourchosenusername'@'%' identified by 'choseapasswordhere';` and hit enter. For example, you can write `create user 'dba'@'%' identified by 'dba2023';` 'dba' stands for database administrator.
6. The next command is `grant all  privileges on *.* to 'theusernameyouchose'@'%' with grant option;`
7. To ensure connection, go back to Azure and under Virtual Machines, on the left-hand side from the menu click on `Networking Settings`, once you have clicked that on the right-hand side of the page there is blue button that says `Create port rule` click the drop down and select `Inbound port rule`.
8. Leave everything as default except under Service select `MySQL` from the drop-down, and it will automatically populate port `3306` under `Destination port ranges`, click `add`.
9. To log out or disconnect from the VM in the terminal hit `control 'd'` or `/quit` and it'll close the connection, detach your terminal from that session. 

## Connecting to MySQL Workbench 
1. Open MySQL Workbench, create a new instance.
2. Choose a connection name, I named mine `azure_vm_amna`, change the host name to the `IP Address` given from your Azure VM, change the username to the username you chose above, and for the password click on `store in keychain` and type your password you had chosen above and hit enter. For exmaple, using the dba example --> for username you would put `dba` and for the password `dba2023`.
3. We need to update the configuration file so connections are not refused. To do this go back into Cloud Shell and ensure you are no longer seeing `mysql>` in the terminal. If you are hit the control button and 'd' simultaneously to exit out of that. Then type `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf` in the terminal to nativate to the special configuration file named `mysql.cnf`.
4. After that, move down to `bind-address` and change the given numbers to `0.0.0.0`, and do the same for the `mysqlx-bind-address` then press the control button and 'o' to save the changes then hit enter, lastly to exit the view hit control 'x'.
5. Back in the terminal type `/etc/init.d/mysql restart` for the changes to occur, we need to restart MySQL from this command. It will then ask for a password, this pasword is the original passowrd you had chosen in Azure when initially setting up your VM. 
6. Go back to MySQL Workbench, and the connection should work after these steps are completed.

## Rational Behind My Database Schema
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/ec205851-c745-4b5b-a7be-ce14f84b00cb)

I created 2 tables, a `providers` table and a `patients` table. In my `providers` table the primary key (PK) is `provider_id`. In the `patients` table, the PK is `patient_id`. I made the PKs the patient and provider ids, due to each individual having their own unique ID numbers, which would allow for easy identification. There is a foreign key (FK) relationship between the two tables; under the `patients` table, the foreign key was the `provider_id`. I chose this rational due to the norm in a healthcare setting where each patient is under the care of a provider, whether it be a physician, nurse practitioner, physician assistant, occupational therapist, physical therapist, respiratory therapist etc. 

## Errors and Challenges
I ran into a few hiccups along the process. The first major hiccup was earlier today, I had to delete my original repo I had been working on for the past few days, to make this new one due to a small mistake in my .env file, which could have lead to a security leak. Once I created this new repo, I was still coming accross errors. I went back into MySQL Workbench, because I had thought there may had been a connectivity issue in connecting the database, username, or password. When I went back to look at my database in Workbench, it would not show up and the program froze and unexpectedly shut off. A few moments later, I received a message on the screen there were reportedly issues with the program, so I right-clicked ontop of the application and clicked 'quit' and then restarted it again. In addition, when I would run the flask app, the values of the columns in the tables I had created were not being displayed. This lead me to believe there were connectivity issues between MySQL Workbench and Google Cloud Shell. When I was working on the assignment previously, I did not encounter these errors, therefore, I ruled out the possiblity of making a mistake in the set-up process or even missing a step in the connecting process. I created a brand new instance, created my tables from the code I had used before because it had worked previously and populated the tables, manually. In the first repo, I had utilized the code Professor Williams had previously provided us, such as utilizing the package faker to populate the tables. However, when all the additional errors started occuring, it was like a snowball effect, so to make things simpler I utilized the `INSERT INTO` sql commands instead of using pandas and faker. Everything was running smoothly, or so I thought. All the tables were able to be created and populated, as seen in the screenshots below showing the `providers` and `patients` tables. However, when I went back into Cloud Shell, and ran the flask app, only the column labels were able to be displayed, none of the values within the table, as seen in the `screenshots` folder above. 
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/c1518f59-5efb-4a4b-81ba-89ae23a0e60e)
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/6414c9af-6db4-42d7-83cc-06e97a8c20ab)
I then decided to try to populate the tables manually in the Cloud Shell Terminal under MySQL hoping the flask app would then display the table values. I was able to create the tables in Cloud Shell, with the desired values, however they still were not able to be displayed on the flask app. 
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/f80606b6-687c-48e7-9ac3-1e94a555e388)
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/103f2ce7-49ba-406a-b609-e86583065beb)

Other errors I also came across are shown below:
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/da76eae7-f2e0-4995-b88f-f2e3be66dac3)
I tried troubleshooting, but ultimately I could not find fix the errors. 
Fortunately, in I was successfully able to push the .env and .gitignore files after creating the new instance. Some connectivity issues were able to be resolved, but unfortunatley I was not able to resolve all errors. 
Lastly, I forgot to screenshot or document additonal errors I encountered, or how I was able to resolve them. For instance, I forgot to pip install a few packages, when I realized why the error was occuring, and installed the packages the codes ran smoothly. 
