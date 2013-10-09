from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat

access_key = ''
secret_key = ''
enpoint = ''
conn = S3Connection(access_key, secret_key, host=enpoint, calling_format=OrdinaryCallingFormat())
bucket = conn.create_bucket('mybucket')
k = Key(bucket)
k.key = 'foobar'
k.set_contents_from_string('This is a test of S3')

