#!/bin/bash
#title           :solar
#description     :Read current from sdm120 and sends it to Domoticz.
#author		 :JM
#date            :20160605
#version         :0.1
#usage		 :./solar
#notes           :
#bash_version    :
#==============================================================================
SERVER="http://192.168.10.181:8888"   #server location
IDX=98	  #id of your device

#SDM120C
SDM120="/usr/local/bin/sdm120c" #location sdm120c script
TTY="/dev/ttyUSB0"		  #USB port sdm120c

#CURRENT=$($SDM120 $TTY -P N -p -q -z 10 | awk '{print $1}') #get current from sdm120c

# echo "$SERVER/json.htm?type=command&param=udevice&idx=$IDX&nvalue=$CURRENT&svalue=POWER;ENERGY"

x=0 
for gelezenWaardE in $($SDM120 $TTY -P N -z 10  -ip|awk -F ":" '!/OK/ {print $2} '|sed 's/[ a-zA-Z]//g') ; do 

if [ ! $x -eq 1 ]; then
	watt=$gelezenWaardE
	x=1
	else
	kilowattuur=$(($gelezenWaardE))
fi 

done

curl -s {"$SERVER/json.htm?type=command&param=udevice&idx=$IDX&nvalue=0&svalue=${watt};${kilowattuur}"}  #send current to domoticz
curl -s {"$SERVER/json.htm?type=command&param=addlogmessage&message=SDM120Update"}  #send current to domoticz#!/bin/bash
