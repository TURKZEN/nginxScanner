# /bin/bash

sudo cp -r ../nginxScanner /opt/

sudo touch /usr/bin/nginxScanner

sudo chmod 777 /usr/bin/nginxScanner

echo """
# /bin/bash

python3 /opt/nginxScanner/nginxScanner.py

""" > /usr/bin/nginxScanner

echo "installation complete!"

nginxScanner

