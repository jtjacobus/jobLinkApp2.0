delete from assign_job;
delete from job;
delete from admin;
delete from technician;
delete from client;
delete from location;
delete from pay;
delete from user;




insert into user(User_ID, UserName, First_Name, Last_Name, Company)
values 
(000000000, "NancyO", "Nancy", "O'Reily", "Markraft"), 
(000000001, "SandraS", "Sandra", "Summers", "Markraft"),
(000000002, "ChloeD", "Chloe", "Davis", "Markraft"),
(000000003, "BCarson", "Bert", "Carson", "Markraft"),
(000000004, "VictorW", "Victor", "Winklevoss", "Markraft"),
(000000005, "JimmyBlauer", "Jim", "Blauer", "Markraft"),
(000000006, "David1977", "David", "Joseph", "Markraft"), 
(000000007, "Dave", "David", "Fulsom", "Markraft"),
(000000008, "mLypski", "Mark", "Lypski", "Markraft"),
(000000009, "MAlgernon", "Mark", "Algernon", "Markraft"), 
(000000010, "Myron", "Steve", "Myron", "Markraft"), 
(000000011, "redBottles1990", "Rhett", "Norman", "Markraft"),
(000000012, "JJA", "Jason", "Jarvis", "Markraft"),
(000000013, "Sarge", "Scott", "Summerling", "Markraft"),
(000000014, "DLogan", "Dee", "Logan", "Logan Construction"),
(000000015, "DougS", "Doug", "Stevens", "Stevens Fine Homes"), 
(000000016, "SHardison", "Steve", "Hardison", "Hardison Construction"),
(000000017, "DaveKent", "David", "Kent", "Kent Homes");

insert into pay (Pay_ID, Pay)
values
(000000000, 870.00), 
(000000001, 1348.00),
(000000002, 2320.00),
(000000003, 456.00),
(000000004, 434.00),
(000000005, 1229.00),
(000000006, 1395.00),
(000000007, 1001.00),
(000000008, 150.00),
(000000009, 298.00),
(000000010, 333.00),
(000000011, 870.00), 
(000000012, 1348.00),
(000000013, 2320.00),
(000000014, 456.00),
(000000015, 434.00),
(000000016, 1229.00),
(000000017, 1395.00),
(000000018, 1001.00),
(000000019, 150.00),
(000000020, 298.00),
(000000021, 333.00);

insert into location (Location_ID, GPS, Street, City, State, Zip)
values
(000000000, "34.03999334, -77.22332938", "2293 Waterford Way", "Leland", "NC", 28442),
(000000001, "34.23434223, -77.22000093", "45 Compass Point", "Leland", "NC", 28399),
(000000002, "34.22342323, -77.55554433", "Lot 122 Mallory Creek", "Leland", "NC", 24433),
(000000003, "34.23423423, -77.92293872", "Lot 19 Waterford", "Leland", "NC", 28401),
(000000004, "34.23423423, -77.92293872", "2443 Eastwind Rd", "Wilmington", "NC", 28401),
(000000005, "34.23423423, -77.92293872", "Lot 4 Alamosa Place", "Wilmington", "NC", 28401),
(000000006, "34.23428423, -77.92293872", "445 Cypress Pointe Dr.", "Wilmington", "NC", 28401),
(000000007, "34.23424422, -77.92293872", "Lot 144 Courtney Pines", "Wilmington", "NC", 28401),
(000000008, "34.23423423, -77.92253872", "161 S Front St.", "Wilmington", "NC", 28401),
(000000009, "34.23423474, -77.92293872", "233 Bradley Dr.", "Wilmington", "NC", 28401),
(000000010, "34.23423443, -77.92893872", "Lot 12 Brunswick Forest", "Leland", "NC", 28401),
(000000011, "34.23423403, -77.92293872", "Lot 99 Olde Pointe", "Hampstead", "NC", 28401),
(000000012, "34.23443423, -77.92293871", "Lot 12 St. James", "Bolivia", "NC", 28401),
(000000013, "34.23423423, -77.92293873", "Lot 43 St. James", "Bolivia", "NC", 28401),
(000000014, "34.23423423, -77.92293874", "1716 Watercrest Ln", "Sunset Beach", "NC", 28401),
(000000015, "34.27423427, -77.92294877", "112 Yaupon Dr.", "Carolina Beach", "NC", 28401),
(000000016, "34.23423421, -77.92283879", "Lot 81 Tyler's Cove", "Bellville", "NC", 28401),
(000000017, "34.23423403, -77.92293872", "Lot 18 River's Wind", "Rocky Point", "NC", 28401),
(000000018, "34.23427420, -77.92274872", "84 W. Salsbury Ct.", "Wilmington", "NC", 28401),
(000000019, "34.23743822, -77.92293872", "18 S. Lumina", "Wrightsville Beach", "NC", 28401),
(000000020, "34.23444728, -77.92293872", "Lot 19 Mott's Landing", "Wilmington", "NC", 28401),
(000000021, "34.27423427, -77.92297772", "Lot 6 Compass Point", "Leland", "NC", 28401);


insert into client (Client_ID, User_ID)
values
(000000000, 000000014),
(000000001, 000000015),
(000000002, 000000016),
(000000003, 000000017);

insert into technician (Tech_ID, User_ID)
values
(000000000, 000000003),
(000000001, 000000004),
(000000002, 000000006),
(000000003, 000000007),
(000000004, 000000008),
(000000005, 000000009),
(000000006, 000000010),
(000000007, 000000011),
(000000008, 000000012);

insert into admin (Admin_ID, User_ID)
values
(000000000, 000000000),
(000000001, 000000001),
(000000002, 000000002),
(000000003, 000000005),
(000000004, 000000013);

insert into job (Job_ID, Job_Status, Location_ID, Job_Type, Pay_ID, Req_Start_Date, Act_Start_Date, End_Date)
values
(000000000, "Complete", 000000000, "New Residential", 000000000, "2017-11-14", "2017-11-21", "2017-11-24"),
(000000001, "Complete", 000000001, "Residential Remodel", 000000001, "2017-11-14", "2017-11-20", "2017-11-24"),
(000000002, "Complete", 000000002, "New Residential", 000000002, "2017-11-15", "2017-11-15", "2017-11-16"),
(000000003, "Complete", 000000003, "New Residential", 000000003, "2017-11-15", "2017-11-17", "2017-11-20"),
(000000004, "On Hold", 000000004, "Commercial Remodel", 000000004, NULL, NULL, NULL),
(000000005, "Complete", 000000005, "New Residential", 000000005, "2017-11-16", "2017-11-21", "2017-11-24"),
(000000006, "In Progress", 000000006, "New Residential", 000000006, "2017-11-17", "2017-11-17", NULL),
(000000007, "In Progress", 000000007, "New Residential", 000000007, "2017-11-17", "2017-11-18", NULL),
(000000008, "In Progress", 000000008, "New Residential", 000000008, "2017-11-17", "2017-11-17", NULL),
(000000009, "On Hold", 000000009, "Residential Remodel", 000000009, NULL, NULL, NULL),
(000000010, "In Progress", 000000010, "New Residential", 000000010, "2017-11-19", "2017-11-19", NULL),
(000000011, "In Progress", 000000011, "New Residential", 000000011, "2017-11-20", "2017-11-20", NULL),
(000000012, "Scheduled", 000000012, "New Residential", 000000012, "2017-11-20", NULL, NULL),
(000000013, "In Progress", 000000013, "Residential Remodel", 000000013, "2017-11-23", "2017-11-23", NULL),
(000000014, "Scheduled", 000000014, "New Residential", 000000014, "2017-11-23", NULL, NULL),
(000000015, "In Progress", 000000015, "New Residential", 000000015, "2017-11-23", "2017-11-23", NULL),
(000000016, "In Progress", 000000016, "New Residential", 000000016, "2017-11-24", "2017-11-24", NULL),
(000000017, "Scheduled", 000000017, "New Residential", 000000017, "2017-11-25", NULL, NULL),
(000000018, "Scheduled", 000000018, "New Residential", 000000018, "2017-12-01", NULL, NULL),
(000000019, "Scheduled", 000000019, "Residential Remodel", 000000019, "2017-12-01", NULL, NULL),
(000000020, NULL, 000000020, "New Residential", 000000020, "2017-12-02", NULL, NULL),
(000000021, NULL, 000000021, "New Residential", 000000021, "2017-12-02", NULL, NULL);

insert into assign_job (Job_ID, Client_ID, Admin_ID, Tech_ID)
values
(0, 0, 0, 0),
(1, 0, 0, 1),
(2, 0, 0, 2),
(3, 1, 0, 3), 
(4, 1, 1, 4), 
(5, 2, 2, 5),
(6, 2, 0, 6), 
(7, 3, 0, 7),
(8, 1, 1, 8), 
(9, 0, 2, 0),
(10, 0, 3, 1), 
(11, 2, 4, 0), 
(12, 1, 2, 1),
(13, 1, 2, 0),
(14, 3, 2, 1), 
(15, 3, 0, 0),
(16, 0, 0, 1), 
(17, 1, 0, 0),
(18, 2, 1, 1), 
(19, 2, 2, 0);