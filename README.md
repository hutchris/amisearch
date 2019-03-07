# amisearch
Searches across all AWS AMI Images in all regions


usage:
```
python3 amisearch.py *FortiAnalyzer*(6.0.4)* -r us-east-1
Name: FortiAnalyzer VM64-AWSOnDemand build0292 (6.0.4) GA-137ae5b3-1f45-4ebd-81bf-93687e21d93e-ami-0901ac5a302e36a2a.4
Description: FortiAnalyzer VM64-AWSOnDemand build0292 (6.0.4) GA
id: ami-09d522e6fa223221b 
```

Command line options:
--field -f changes the field that is searched. defaults to description
--region -r changes the region that is searched. defaults to all

Requirements:
python3
boto3
aws cli credentials configured with read access to ec2
