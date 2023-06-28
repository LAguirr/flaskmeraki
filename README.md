# flaskmeraki

Looking for a simple app for simple search in the meraki network throughout some projects in CodeExchange and find nothing similar, finding just heavy but useful projects, I decided build the simplest app just for check the fewest things of organizations, networks and devices, the app it's not complete yet, But I think that if you read a few the main.py file and understand what I've done in the other files you can adapt it to your own project and reduce hours of develop

The is all front end, the backend is the reponses from api meraki, don't save nothing of information

For use it you can view it and run it in https://replit.com/@LeonelHernande4/flaskmeraki

The only information of authentication that use is the apikey. For access to the API, first enable the API for your organization under Organization > Settings > Dashboard API access,and then go to your profile (Click your email at the top right of any Dashboard page and click "My Profile") to generate a key. You can follow the steps in the following link, but remember don't share the apikey, and change it frequently for more security
https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API


The app only use 
python-versions = ">=3.6"
Flask version = "2.2.2"
request version = '2.28.1'


THE APP IS NOT COMPLETE, BUT IT'S USEFUL IF YOU USE IT AND MODIFY IT FOR YOUR OWN PROJECT, I hope beeing adding funcionalities for modify routers, switchs and AP's configuration
