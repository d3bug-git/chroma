#!/bin/bash
sudo -i -u root python3.7 /home/pi/Desktop/chroma/main.py

pause(){
 read -n1 -rsp $'[Datalogger]:Press any key to close the terminal...\n'
}

pause