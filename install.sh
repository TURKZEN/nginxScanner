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
echo ""
echo "installation complete!"

sleep 1 

nginxScanner

