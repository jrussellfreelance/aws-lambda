import json
from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider

def handler(event, context):
    ipaddr = get_ip(GoogleDnsProvider)
    return {
        'statusCode': 200,
        'body': json.dumps(ipaddr)
    }
