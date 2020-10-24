__version__ = '0.1.0'
import boto3

if __name__ == '__main__':
    s3 = boto3.client('s3')
    r = s3.list_buckets()
    for b in r['Buckets']:
        print(f'{b["Name"]}')

    print('Magpi')
