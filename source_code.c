/* 
Copyright 2023 Nadim Khan
Copyright 2023 Amit
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
*/

/*
There will be udf_database(user defined database) of modules and sdf_database(self detected database) of modules which will play an 
important role in autoassign_nodeid operation
*/

Case : init // module will enter this state on every power on.
// If module sdf_database exists then jump to case sdf_init_check mode
// If no module mapping exists then jump to case sdf_init_map mode


Case : sdf_init_check // In this state module will check the sdf_database with all actual modules connected by asking their data one by one.

/*
In this mode coupler will execute autoassign_nodeid logic but the data base will be a temporary instance of previous sdf_database 
named temp_sdf_database

autoassign_nodeid : Below operation is called autoassign_nodeid this will be used many times in this operation
Module will transmit a code to the next station via 'config bus' and next station upon acceptance of the code, will transmit self identification 
data via 'main bus' to coupler for temp_sdf_database mapping. when coupler acknowleges the acceptance via main bus then this station will transmit 
subsequent code to next station for check and self data registration to coupler and so on untill all stations provide self identification 
data to coupler.
If the last station will transmit code via config bus but there will be no next station to take action and give self identification data so 
coupler will wait self identification data via 'main bus' untill config timeout time and assume that station as last station in line 
It will also end the temp_sdf_database updation.
*/

/* If the temp_sdf_database is same as sdf_database is correct then coupler will copy temp_sdf_database to sdf_database and jump 
to case udf_init_comp mode
If database is incorrect then coupler will copy temp_sdf_database to sdf_database and jump to case sdf_init_map mode
*/

Case : sdf_init_map // In this state module will assign node id to each module and save all the data of module in its temp_sdf_database. 
/*
Data to be saved is like type of module, serial number, etc
See autoassign_nodeid description
During mapping state module will wait for timeout of last module and mapping state will end and coupler will copy temp_sdf_database to sdf_database
jump to case recheck_sdf_init_map mode
*/
Case : recheck_sdf_init_map // In this state the coupler will once again talk to each module and reconfirm the sdf_database data
//It will also check the presence of last module and finish the sdf_database
// If this state is complete then coupler will jump to case udf_init_comp mode


Case : udf_init_comp // In this state coupler will compare the data of udf_database with sdf_database.
//If both databases are matching then jump to case normal_op mode
//If both databases are not matching then jump to case error_op mode and generate error code


Case : normal_op // In this state the Coupler will start taking and giving data to and from modules in normal mode at the highest speed
//Details normal op protocol specs are under development
//If during normal operation any module heartbeat fails then coupler will jump to case error_op mode and generate error code


Case : error_op // In this state coupler will start blinking led and all modules will blink LEd and indicate that there is 
//some error in normal operation of modules also generate error code
 
