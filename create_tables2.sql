drop view if exists assigned_jobs;
drop table if exists assign_job;
drop table if exists task;
drop table if exists job;
drop table if exists admin;
drop table if exists technician;
drop table if exists client;
drop table if exists location;
drop table if exists pay;
drop table if exists user;
drop function if exists jobStatus;
drop procedure if exists countCity;
drop procedure if exists create_technician;
drop procedure if exists job_is_assigned;
drop trigger if exists unassigned_job;


create table user 
	(User_ID int(9) not null, 
    UserName varchar(30) not null, 
    First_Name varchar(30) not null, 
    Last_Name varchar(30) not null, 
    Company varchar(30) not null,
    primary key (User_ID)
    ) ENGINE = INNODB;
    
create table pay
	(Pay_ID int(9) not null, 
    Pay numeric(10,2) not null, 
    primary key (Pay_ID)) ENGINE = INNODB;
    
    
create table location
	(Location_ID int(9) not null, 
    GPS varchar(30), 
    Street varchar(30) not null, 
    City varchar(30) not null,
    State varchar(30) not null,
    Zip int(5) not null, 
    primary key (Location_ID)
    ) ENGINE = INNODB;
    
create table client
	(Client_ID int(9) not null, 
    User_ID int(9) not null, 
    primary key (Client_ID), 
    foreign key (User_ID) references user (User_ID) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE = INNODB;
    
create table technician
	(Tech_ID int(9) not null, 
    User_ID int(9) not null, 
    primary key (Tech_ID),
    foreign key (User_ID) references user (User_ID) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE = INNODB;
    
create table admin
	(Admin_ID int(9) not null,
    User_ID int(9) not null, 
    primary key (Admin_ID), 
    foreign key (User_ID) references user (User_ID) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE = INNODB; 
    
create table job
	(Job_ID int(9) not null, 
	Job_Status varchar(30),
    Location_ID int(9) not null,
    Job_Type varchar(30) not null, 
    Pay_ID int(9) not null, 
    Req_Start_Date date,
    Act_Start_Date date,
    End_Date date, 
    primary key (Job_ID),
    foreign key (Location_ID) references location (Location_ID) ON UPDATE CASCADE, 
    foreign key (Pay_ID) references pay (Pay_ID) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE = INNODB; 
    

create table assign_job
	(Job_ID int(9) not null,
    Client_ID int(9),
    Admin_ID int(9),
    Tech_ID int(9),
    primary key (Job_ID),
    foreign key (Client_ID) references client (Client_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key (Admin_ID) references admin (Admin_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key (Tech_ID) references technician (Tech_ID) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=INNODB;
	
	
    

create view assigned_jobs as (select job.Job_ID, job.Job_Status, c.Company, l.Street, job.Job_Type, job.Req_Start_Date, pay.Pay, c.Client_ID, a.Admin_ID, t.Tech_ID, tech.UserName 
from job natural join (select * 
	from assign_job) as t natural join (select Client_ID, Company 
		from user natural join client) as c natural join pay natural join (select Location_ID, Street 
			from location) as l natural join (select Admin_ID 
				from user natural join admin) as a natural join (select Tech_ID, UserName 
					from user natural join technician) as tech);
					


DELIMITER $$
	
	create function jobStatus(day date) returns varchar(12)	
		BEGIN
			declare status varchar(12);
			IF day < DATE(NOW()) THEN
				set status = 'In Progress';
			ELSE
				set status = 'Completed';
			END IF;
		return(status);
		END $$

	create procedure countCity(in city varchar(30), out user_count integer)
		BEGIN
		SELECT count(*) into user_count from location where location.city = city;
		END $$

	create trigger unassigned_job before insert on job
		for each row
		BEGIN	
			IF NEW.job_status IS NULL THEN
				set NEW.job_status = 'Unassigned';
			END IF;
		END $$
	
	create procedure create_technician(
		IN User_ID int(9), 
    		IN UserName varchar(30), 
    		IN First_Name varchar(30), 
    		IN Last_Name varchar(30),
    		IN Company varchar(30),
		IN Tech_ID int(9)
		)

		BEGIN
			DECLARE errno INT;
			DECLARE EXIT HANDLER FOR SQLEXCEPTION
			BEGIN
				GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
				SELECT errno AS MYSQL_ERROR;
				ROLLBACK;
			END;
		
		START TRANSACTION;
			INSERT INTO user values(User_ID, UserName, First_Name, Last_Name, Company);
			
			INSERT INTO technician values(Tech_ID, User_ID);
		COMMIT WORK;
		END $$

	CREATE PROCEDURE job_is_assigned(
    		IN Job_ID INT(9),
    		IN Client_ID INT(9),
    		IN Admin_ID INT(9),
    		IN Tech_ID INT(9)
  		)

		BEGIN
		START TRANSACTION;
    			INSERT INTO assign_job VALUES(Job_ID, Client_ID, Admin_ID, Tech_ID);
    			UPDATE job SET Job_Status="Assigned" WHERE job.Job_ID=Job_ID;
		COMMIT;
		END $$
		

DELIMITER ;


															