import json
from app import update_status

dummy_event = {
    'account': 'admin',
    'detail': {},
    'detail-type': 'Scheduled Event',
    'id': 'dummy',
    'region': 'ap-northeast-1',
    'resources': [],
    'source': 'aws.events',
    'time': '2019-06-24T01:23:45Z',
    'version': '1.0'
}

# ローカル実行用
if __name__ == '__main__':
    print(json.dumps(update_status(), ensure_ascii=False, indent=2))
