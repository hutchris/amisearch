# amisearch
Searches across all AWS AMI Images in all regions.


Example brief results:
```
amisearch.py "*FortiGate*6.2.3*" -f name -r ap-southeast-2
Name: FortiGate-VM64-AWS build1066 (6.2.3) GA-e5936f4a-0d69-479f-919c-d5e158bd4d12-ami-00364bb191729739b.4
Description: FortiGate-VM64-AWS build1066 (6.2.3) GA
id: ami-003c22d372f903dc6
-------------------------------------------------
Name: FortiGate-VM64-AWSONDEMAND build8270 (6.2.3) SB-3124a694-441c-4ff1-8bf7-4d153be424a6-ami-0e2c276bcf8d36c0e.4
Description: FortiGate-VM64-AWSONDEMAND build8270 (6.2.3) SB
id: ami-05708d1e433accc2a
-------------------------------------------------
Name: FortiGate-VM64-AWSONDEMAND build1066 (6.2.3) GA-3124a694-441c-4ff1-8bf7-4d153be424a6-ami-07d8d9716be7d7aa1.4
Description: FortiGate-VM64-AWSONDEMAND build1066 (6.2.3) GA
id: ami-0a980e6dca63b0eb6
-------------------------------------------------
```  
Example verbose results:
```
amisearch.py "ami-003c22d372f903dc6" -f image-id -r ap-southeast-2 -v
Architecture: x86_64
CreationDate: 2019-12-20T19:02:46.000Z
ImageId: ami-003c22d372f903dc6
ImageLocation: aws-marketplace/FortiGate-VM64-AWS build1066 (6.2.3) GA-e5936f4a-0d69-479f-919c-d5e158bd4d12-ami-00364bb191729739b.4
ImageType: machine
Public: True
OwnerId: 679593333241
ProductCodes: [{'ProductCodeId': 'dlaioq277sglm5mw1y1dmeuqa', 'ProductCodeType': 'marketplace'}]
State: available
BlockDeviceMappings: [{'DeviceName': '/dev/sda1', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-01a91c514535c0496', 'VolumeSize': 2, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'Ebs': {'DeleteOnTermination': True, 'VolumeSize': 30, 'VolumeType': 'gp2', 'Encrypted': False}}]
Description: FortiGate-VM64-AWS build1066 (6.2.3) GA
EnaSupport: True
Hypervisor: xen
ImageOwnerAlias: aws-marketplace
Name: FortiGate-VM64-AWS build1066 (6.2.3) GA-e5936f4a-0d69-479f-919c-d5e158bd4d12-ami-00364bb191729739b.4
RootDeviceName: /dev/sda1
RootDeviceType: ebs
SriovNetSupport: simple
VirtualizationType: hvm
-------------------------------------------------
```
Command line options:  
--field -f changes the field that is searched. defaults to name.  
--region -r changes the region that is searched. defaults to all  
--printfields -p prints all available search fields
--verbose -v returns all fields instead of just name, description and image-id

Requirements:  
python3  
boto3  
aws cli credentials configured with read access to ec2  
