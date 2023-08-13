# Laboratory Information Management System - Faluire

## 1. ISSUE SUMMARY
* Duration: 2023/08/09, 14:00 - 2023/08/10, 14:05
* Impact: Slowdown in result transfer and calculations on **LIMS** (Laboratory Information Management System), **LABWARE7**
    * Users namely lab analysts could not access or view their test results on LIMS
    * All users of the sytem were afected
* Root Cause: The server hosting the LIMS was overloaded due to lack of resources allocated during initial configuration. The server is a virtual machine on VMWARE.

## 2. TIMELINE
* 2023/08/09, 14:30 - Issue detected by Laboratory during verification of transfer and calculations
* 2023/08/09, 14:35 - Issue reported to Server Administrator by LIMS Administrator
* 2023/08/09, 14:45 - Server Administrator scheduled a server reboot and cache clearance for 15:00
* 2023/08/09, 15:00 - All users logged off and Server rebooted
* 2023/08/09, 15:10 - Laboratory reported that the problem still ongoing
* 2023/08/09, 15:30 - Server administrator checked physical resources available for the server
* 2023/08/09, 15:45 - Adequate amount of physical resources available and not utilised
* 2023/08/09, 16:00 - Comminication sent to Systems Administrator to trouble shoot why resources are not being utilised by the server
* 2023/08/09, 16:15 - Sever reported to being configured as a virtual machine with adequate physical resources. However not all resources were made available to the virtual machine.
* 2023/08/09, 17:00 - Server administrator configured virtual machine to make use of all physical resources
* 2023/08/09, 17:10 - Laboratory personell will perform tests on next shift the next day. Server was rebooted
* 2023/08/10, 07:30 - Laboratory personell reported no issues with the system.
* 2023/08/10, 14:00 - Laboratory personell reported no issues in result transfers and calculations
* 2023/08/10, 14:05 - Matter resolved and issue closed

## 3. ROOT CAUSE
In-adequate resources allocated to virtual machine machine running the LIMS server. Virtual machine was configured during install and not updated over the years.

Once the drive space allocated to the virtual machine was full, the server couldnt perform any additional tasks which required hard drive disc space

## 4. RESOLUTION AND RECOVERY
* Hard drive disc space increased on virtual machine
* Server and virtual machine where then both rebooted

## 5. CORRECTIVE AND PREVENTATIVE MEASURES
* Annual mantenance tasks updated to included the monitoring of resources on LIMS virtual machine
* VMWARE configuration and maintenance training must be conducted by all IT personell.
* All resources on all virtual machines present to be updated to reflect current usage and loads for the systems.
