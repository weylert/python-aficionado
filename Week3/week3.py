#1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations.

#From these VLAN_ID and VLAN_NAME combinations, construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:
#[('1', 'default'),
# ('400', 'blue400'),
# ('401', 'blue401'),
# ('402', 'blue402'),
# ('403', 'blue403')]


from pprint import pprint

spacer = "-----"
vlan_list= []

with open("showvlan.txt", "r") as openvlan:
    vlans = openvlan.read()

    for line in vlans.splitlines():
        if "VLAN" in line or "-----" in line or line.startswith("  "):
            continue
        fields = line.split()
        vlan_id = fields[0]
        vlan_name = fields[1]
        vlan_list.append((vlan_id,vlan_name))

pprint(vlan_list)


print("\n",spacer * 80, "\n ### END OF EXERCISE 1 ### \n", spacer * 80,"\n")  

#----------------------------------------------------------------  EXERCICIO 2  ----------------------------------------------------------------------------------------------------

#2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

#Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

#Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

#Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.


with open("arp.txt", "r") as openarp:
    arp_opened = openarp.read()


value1 = False
value2 = False

for a in arp_opened.splitlines():

    if "protocol" in a.lower():
        continue
    b = a.split()
    e2_ip_addr = b[1]
    e2_mac_addr = b[3]
    
    if e2_ip_addr == "10.220.88.1":
        print("Default gateway IP/MAC is {} : {}".format(e2_ip_addr,e2_mac_addr))  
        value1 = True 
    if e2_ip_addr == "10.220.88.30":
        print("\nArista3 IP/Mac is {} : {}".format(e2_ip_addr,e2_mac_addr))
        value2 = True
    if value1 and value2 == True:
        break
    

print("\n",spacer * 80, "\n ### END OF EXERCISE 2 ### \n", spacer * 80,"\n")  


#----------------------------------------------------------------  EXERCICIO 3  ----------------------------------------------------------------------------------------------------
#3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote
#"Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines 
#(i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.

with open("show_lldp.txt") as lldp:
    lldp_opened = lldp.read()

verifier, verifier2 = (False,False)

for info in lldp_opened.splitlines():

    if "system name" in info.lower():
        sysname_list = info.split()
        verifier = True

    if "port id" in info.lower():
        portid_list = info.split()
        verifier2 = True

    if verifier and verifier2 == True:
        break

print("The port ID is {} and the system ID is {}".format(portid_list[2],sysname_list[2]))


print("\n",spacer * 80, "\n ### END OF EXERCISE 3 PEGASUS ### \n", spacer * 80,"\n")  


#----------------------------------------------------------------  EXERCICIO 4  ----------------------------------------------------------------------------------------------------

#4. You have the following data structure:
arp_table = [
 ('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')
] 

#Loop over this data structure and extract all of the MAC addresses. Process all of the MAC addresses to get them into a standard format.
#  Print the standardized MAC addresses to the screen. The standardized format should be as follows:

#00:62:EC:29:70:FE

#The hex digits should be capitalized. Additionally, there should be a colon between each octet in the MAC address.


for information in arp_table:
    sorted_arp = information[1].upper().split(".")

    new_mac = []
    sorted_arp = "".join(sorted_arp)
    #print(sorted_arp)
    
    while len(sorted_arp) > 0:
        entry = sorted_arp[:2]
        sorted_arp = sorted_arp[2:]
        new_mac.append(entry)
    
    new_mac = ":".join(new_mac)
    print(new_mac)




print("\n",spacer * 80, "\n ### END OF EXERCISE 4 PEGASUS ### \n", spacer * 80,"\n")  


#----------------------------------------------------------------  EXERCICIO 5  ----------------------------------------------------------------------------------------------------    
    
#*** Note, to actually test this in your environment, change the test IP addresses to something in your environment that you can ping successfully. ***

#Construct a list of 254 IP addresses. The base IP address should be equal to '192.168.0.0' or '192.168.0.'.

#You should use the 'range' builtin to accomplish this.

#Your list should have all of the IP addresses from 192.168.0.1 to 192.168.0.254

#Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should look similar to the following: 
#0 ---> 192.168.0.1
#1 ---> 192.168.0.2
#2 ---> 192.168.0.3
#3 ---> 192.168.0.4
#4 ---> 192.168.0.5
#...

#Use a list slice to create a new list that goes from 192.168.0.3 to 192.168.0.6

#Using a loop and os.system("ping -c 3 192.168.0.3") try pinging all of the IP addresses in this short list. For Windows the command will probably be os.system("ping -n 3 192.168.0.3").

#Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following:
#WINDOWS = False

#base_cmd_linux = 'ping -c 2'
#base_cmd_windows = 'ping -n 2'
# Ternary operator
#base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

import os

ip_list = []
numerics = []
new_list = []
numerics.extend(range(1,255))
x=0
enumerated_list = []

for e5_ips in numerics:
    
    ip_list = ["192.168.0.{}".format(numerics[x])]
    new_list.append(ip_list[0])
    x +=  1


for count, count2 in enumerate(new_list):
   # print(count,"-->", count2)
    pass

specific_list = new_list[0:1]

for count3 in specific_list:
    os.system("ping -n 1 {}".format(count3))
    





    