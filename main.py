import json
import os
import sys
from app import lambda_handler

# ローカル実行用
if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__name__), 'event.json'), 'r', encoding='utf-8') as f:
        print(json.dumps(lambda_handler(json.loads(f.read()), context={}), ensure_ascii=False, indent=2))
