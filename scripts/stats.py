from pathlib import Path
from datetime import datetime
import os
import json

def get_stats():
    data_dir = Path('data')
    count = len(list(data_dir.glob('*.md')))
    
    # 获取最后更新时间
    latest = max(os.path.getmtime(f) for f in data_dir.glob('*.md'))
    days_ago = int((datetime.now().timestamp() - latest) / 86400)
    
    return {
        'count': count,
        'days_ago': days_ago
    }

def update_badges():
    stats = get_stats()
    
    # 生成徽章URLs
    badges = {
        'count': f'https://img.shields.io/badge/数据量-{stats["count"]}条-blue',
        'update': f'https://img.shields.io/badge/更新-{stats["days_ago"]}天前-orange'
    }
    
    # 保存为JSON供CI使用
    Path('stats').mkdir(exist_ok=True)
    with open('stats/badges.json', 'w', encoding='utf-8') as f:
        json.dump(badges, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    update_badges() 