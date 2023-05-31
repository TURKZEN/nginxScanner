# /bin/bash

sudo mkdir /opt/nginxScanner

sudo cp  nginxScanner.py /opt/nginxScanner/

sudo touch /usr/bin/nginxScanner

sudo chmod 777 /usr/bin/nginxScanner

echo """
# /bin/bash

python3 /opt/nginxScanner/nginxScanner.py \$1

""" > /usr/bin/nginxScanner

pip3 install -r requirements.txt

clear

echo ""
echo "Installation Complete!"

sleep 1 

clear

nginxScanner

