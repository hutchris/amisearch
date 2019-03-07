import sys
import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("value", help="enter a search term. See AWS ")
parser.add_argument("--field", "-f", default="description", help="enter the ami field you wish to search in. Default: description. Good alternative: name")
parser.add_argument("--region", "-r", default="*", help="enter the region to search for amis in. default: all")

args = parser.parse_args()

ec2 = boto3.client('ec2')

if args.region == "*":
    regions = ec2.describe_regions()
    for region in regions['Regions']:
        tempec2 = boto3.client('ec2',region_name=region['RegionName'])
        images = tempec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
        print('\n\n'+region['RegionName'])
        for image in images['Images']:
            print('Name: '+image['Name'])
            print('Description: '+image['Description'])
            print('id: '+image['ImageId'])
else:
    tempec2 = boto3.client('ec2',region_name=args.region)
    images = tempec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
    for image in images['Images']:
        print('Name: '+image['Name'])
        print('Description: '+image['Description'])
        print('id: '+image['ImageId'])
