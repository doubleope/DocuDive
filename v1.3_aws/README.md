## EC2 Instance
- Create ec2 instance with at least 32 GB
```
Instance type
c4.4xlarge
```
- TODO: Add more instructions

## Add public IP to AWS EC2 instance

- https://documentation.stormshield.eu/SNS/v4/en/Content/EVA_-_Amazon_Web_Services/30-Create_elastic_IP.htm
```
To enable remote administration of the firewall, you must define a public IP address (Elastic IP) and assign it to the firewall:

In the Services menu, select EC2
In the Network & Security menu, select Elastic IPs.
Click on Allocate New Address
Select VPC for allocation and confirm (Allocate)
Select the newly created Elastic IP
Click on Action > Associate address
In the Instance field, select your EVA new instance
In the Private IP field, select the suggested IP address
Click on Associate.
You can now access the Stormshield Network Administration Console with your web browser using the link https://EC2 Elastic IP address>/admin.
The default login is admin, and the default password is your EC2 instance ID (available in the EC2 Instances console).
```

## Guide to install GIT in AWS Linux
- https://linux.how2shout.com/how-to-install-git-on-aws-ec2-amazon-linux-2/
  sudo yum update
  sudo yum install git

git clone https://github.com/LarryBattle/DocuDive

$ python3 --version
Python 3.9.16

## For connection testing using nodejs
> sudo yum install nodejs
> cd $PROJECT/v1.3_basic_node_app_for_aws
> npm install
> npm start
> curl http://PUBLIC_IP:3000

