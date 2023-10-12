# flask_4_databases_mysql_vm
Manually setting up and running a database on a cloud VM. Hands-on experience setting up a MySQL instance on a VM

## Virtual Machine Setup on Azure 
1. Log into your Azure Account.
2. Locate the hamburger icon on the left-hand side of the screen, click it, then locate `Virtual Machine` on the menu list, and click it.
3. Once on the `Virtual Machine` page, click `+ Create`, which is located towards the top of the page, and then click the first option on the drop down, `Azure virtual machine`.
4. The page will automatically navigate to the proper page, and land you under the `Basics` tab. Under the Basics tab, ensure your subscription is `Azure for Students`, and create and name a new resouce group. I named my resource group `504-wk4b`.
5. Under `Instance details`, give your VM a name. I named mine `AmnaMySQL`. Next, change the `Security type` it `Standard`.
6. Next to `Size`, select `See all sizes ` and then under `VM sizes`, scroll to find `B-series`, click the drop down, and then click on `B1ms`, ensure the row gets highlighted and then click select. The selection should look like the screenshot below: ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/d3c64bc5-88bf-4961-8ac5-228d7ad529fd)
7. Under `Administrator account` for the `Authentication type` select `Password`. Now configure a `Username` and `Password`.
8. For the port, under `Inbound port rules`, go to `select inbound ports`, click the drop-down, and select `HTTP (80)` and `HTTPS (443)`.
9. Next, navigate to the `Networking` tab, located in same row as the Basics tab.
10. Click the box next to `Delete public IP and NIC whne VM is deleted` so the box is check marked.
11. Click `Review + Create`, review all the information presented to ensure it is correct, the price should look like the screenshot below: ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/d3054fc1-1853-4fc6-a2e2-533d141fe001)


12. If all looks well, click `Create`.
## Virtual Machine Setup on GCP
1. Log into your Google Cloud account, ensure you are in `console.cloud.google.com`, and navigate to the hamburger icon on the left-hand side, and click on `Compute Engine` from the menu.
2. Click `Create Instance`, and name your instance. I named mine `amna-504-sql`.
3. Under `Machine Type` select this: ![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/0ee3d302-f590-4700-88ad-48c6829e312a)

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
![image](https://github.com/amnasyed1/flask_4_databases_mysql_vm2/assets/123895397/86e5d353-c26e-4c98-b3d3-0c534bcbab7b)

I created 2 tables, a `providers` table and a `patients` table. In my `providers` table the primary key (PK) is `provider_id`. In the `patients` table, the PK is `patient_id`. I made the PKs the patient and provider ids, due to each individual having their own unique ID numbers, which would allow for easy identification. There is a foreign key (FK) relationship between the two tables; under the `patients` table, the foreign key was the `provider_id`. I chose this rational due to the norm in a healthcare setting where each patient is under the care of a provider, whether it be a physician, nurse practitioner, physician assistant, occupational therapist, physical therapist, respiratory therapist etc. 
