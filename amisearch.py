#!/usr/bin/env python3

import sys
import argparse
import boto3

parser = argparse.ArgumentParser(
    description="cli tool to help you search through AMI Images on the AWS Marketplace",
    epilog="""Example: amisearch.py "*CloudGuard*BYOL*R80.40*" -f name -r ap-southeast-2 -v"""
)
parser.add_argument("value", help="enter a search term. Use wildcards and quotations e.g. \"*Fortinet*\"", nargs="?")
parser.add_argument("--field", "-f", default="name", help="enter the ami field you wish to search in. Default: name. To see other fields use -p")
parser.add_argument("--region", "-r", default="*", help="enter the region to search for amis in. default: all")
parser.add_argument("--printfields", "-p", action='store_true', help="Prints to console the available search fields")
parser.add_argument("--verbose", "-v", action='store_true', help="Returns all image fields instead of just the name, description and ami-id")

args = parser.parse_args()

if args.printfields:
    print('''architecture - The image architecture (i386 | x86_64 | arm64 ).
block-device-mapping.delete-on-termination  A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.
block-device-mapping.device-name            The device name specified in the block device mapping (for example, /dev/sdh or xvdh ).
block-device-mapping.snapshot-id            The ID of the snapshot used for the EBS volume.
block-device-mapping.volume-size            The volume size of the EBS volume, in GiB.
block-device-mapping.volume-type            The volume type of the EBS volume (gp2 | io1 | st1 | sc1 | standard ).
block-device-mapping.encrypted              A Boolean that indicates whether the EBS volume is encrypted.
description                                 The description of the image (provided during image creation).
ena-support                                 A Boolean that indicates whether enhanced networking with ENA is enabled.
hypervisor                                  The hypervisor type (ovm | xen ).
image-id                                    The ID of the image.
image-type                                  The image type (machine | kernel | ramdisk ).
is-public                                   A Boolean that indicates whether the image is public.
kernel-id                                   The kernel ID.
manifest-location                           The location of the image manifest.
name                                        The name of the AMI (provided during image creation).
owner-alias                                 String value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console.
owner-id                                    The AWS account ID of the image owner.
platform                                    The platform. To only list Windows-based AMIs, use windows .
product-code                                The product code.
product-code.type                           The type of the product code (devpay | marketplace ).
ramdisk-id                                  The RAM disk ID.
root-device-name                            The device name of the root device volume (for example, /dev/sda1 ).
root-device-type                            The type of the root device volume (ebs | instance-store ).
state                                       The state of the image (available | pending | failed ).
state-reason-code                           The reason code for the state change.
state-reason-message                        The message for the state change.
sriov-net-support                           A value of simple indicates that enhanced networking with the Intel 82599 VF interface is enabled.
tag                                         The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA , specify tag:Owner for the filter name and TeamA for the filter value.
tag-key                                     The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
virtualization-type                         The virtualization type (paravirtual | hvm ).
''')
elif args.region == "*" and args.value is not None:
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()
    for region in regions['Regions']:
        regec2 = boto3.client('ec2',region_name=region['RegionName'])
        images = regec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
        print('\n\n'+region['RegionName'])
        for image in images['Images']:
            if args.verbose:
                for k,v in zip(image.keys(),image.values()):
                    print(str(k)+': '+str(v))
            else:
                print('Name: '+image['Name'])
                try:
                    print('Description: '+image['Description'])
                except KeyError:
                    print('Description: ')
                print('id: '+image['ImageId'])
            print('-------------------------------------------------')
elif args.value is not None:
    regec2 = boto3.client('ec2',region_name=args.region)
    images = regec2.describe_images(Filters=[{'Name': args.field,'Values': [args.value,]}])
    for image in images['Images']:
        if args.verbose:
            for k,v in zip(image.keys(),image.values()):
                print(str(k)+': '+str(v))
        else:
            print('Name: '+image['Name'])
            try:
                print('Description: '+image['Description'])
            except KeyError:
                print('Description: ')
            print('id: '+image['ImageId'])
        print('-------------------------------------------------')
else:
    parser.print_help()
