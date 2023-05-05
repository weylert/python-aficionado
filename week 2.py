#with open("version.txt", "a") as version:
    #host_write = version.write("ROUTER CISCO\n,TESTFILE\n")

#with open("version.txt", "r") as version2:
    #host_root = version2.read()   
#print(host_root)

#print(type(host_root))

##############################################################################################

#IP_LIST = ["192.168.0.110","10.10.10.10"]
#my_list = []

#my_list.append("192.186.0.1")
#print(my_list)

#my_list.extend(IP_LIST)
#print(my_list)

#my_list.pop(0)
#print(my_list)

#my_list[0] = "2.2.2.2"
#print(my_list)


################################################################################################

#with open("arp.txt","r") as openarp:
#    arpvar = openarp.readlines()
#    print(arpvar)
#print("#####################################################")

#new_slice = arpvar[0:2]

#arpvar.sort()
#from pprint import pprint
#pprint(arpvar)
#print("SEPARATING ##########################################################")
#new_listslice = arpvar[0:3]
#pprint(new_listslice)

#new_listslice = "\n".join(new_listslice)
#print(new_listslice)

#with open("savearp.txt", "w") as arpsave:
 #   arpsave.write(new_listslice)


#Use the list .sort() method to sort the list based on IP addresses.

#Create a new list slice that is only the first three ARP entries.

#Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

#Write this string containing the three ARP entries out to a file named "arp_entries.txt".


####################################################################################################################

#4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

#with open("show ip int brief.txt", "r") as ipbrief:
#    ipvar = ipbrief.readlines()

#fa4 = ipvar[5].split()
#fields = fa4
#fields = fa4[0:2]

#interface = fields[0]
#ip = fields[1]
#print(interface,ip)

#Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered 
# for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding
#  interface associated with the IP.

#Create a two element tuple from the result (intf_name, ip_address).

#Print that tuple to the screen.

#Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.

##################################################################################################################################################

#5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

#From the first line use the string .split() method to obtain the local AS number.

#From the last line use the string .split() method to obtain the BGP peer IP address.

#Print both local AS number and the BGP peer IP address to the screen.

with open("showbgp.txt", "r") as bgpfile:
    bgp = bgpfile.read()

bgp = bgp.splitlines()
bgplines = bgp[0].split()
bgplines2 = bgp[3].split()

localas=(bgplines[7])
bgppeer=(bgplines2[0])

print("the local AS number is",localas, "and the bgp peer is", bgppeer)