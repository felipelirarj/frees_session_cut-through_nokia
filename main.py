from pysnmp.hlapi import *
from pysnmp import hlapi
from snmp_cmds import Session
import os


print('''

.__   __.   ______    __  ___  __       ___      
|  \ |  |  /  __  \  |  |/  / |  |     /   \     
|   \|  | |  |  |  | |  '  /  |  |    /  ^  \    
|  . `  | |  |  |  | |    <   |  |   /  /_\  \   
|  |\   | |  `--'  | |  .  \  |  |  /  _____  \  
|__| \__|  \______/  |__|\__\ |__| /__/     \__\ 
                                                 

=================================================
Author: Felipe Lira
Data: 05/03/2024
=================================================

Function: Unloock Session locked the Cut Trough ONT

If allocked IP address diferent of 0.0.0.0, execute
command snmpset for liberate the connection.

''')


ip_olt = input("Enter IPv4 OLT: ")


print("\n\nPlease waiting... Consulting information on OLT...\n\n")


for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public', mpModel=0),
                          UdpTransportTarget((f'{ip_olt}', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('1.3.6.1.4.1.637.61.1.35.10.1.1.52'))):

    if errorIndication or errorStatus:
        print(errorIndication or errorStatus)
        break

    else:
        for varBind in varBinds:

            return_info = str(varBind)        
            return_info = return_info.split('=')
            ip_bind = return_info[1]
            ip_bind = ip_bind.strip()
            ifIndex = return_info[0]
            ifIndex = ifIndex.split('.')
            ifIndex = ifIndex[-1]

            if '0.0.0.0' in ip_bind:
                pass

            elif len(ip_bind) == 1:
                pause_app = input("Frees All Sessions...")
                exit(0)
            
            else:
                print(ifIndex)
                print(ip_bind)

                print(f"Frees the session on ONT Index {ifIndex}...")
                os.system(f'snmpset -v 1 -c public -On {ip_olt} .1.3.6.1.4.1.637.61.1.35.10.1.1.52.{ifIndex} a 0.0.0.0' )
                
                

   
