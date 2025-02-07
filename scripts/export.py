import csv
import json
from pathlib import Path
import yaml

def markdown_to_yaml(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        try:
            content = f.read().replace('\ufeff', '')
            content = content.replace('\r\n', '\n').replace('\r', '\n')
            
            # 提取第一个YAML块
            yaml_block = ''
            in_yaml = False
            for line in content.split('\n'):
                if line.strip() == '---':
                    if not in_yaml:
                        in_yaml = True
                        continue
                    else:
                        break
                if in_yaml:
                    yaml_block += line + '\n'
            
            # 打印调试信息
            print("提取的YAML块:\n", yaml_block)
            
            # 直接用YAML解析器
            data = yaml.safe_load(yaml_block)
            
            # 验证必要字段
            required_fields = ['id', 'genericName', 'registrationNumber']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"缺少必要字段: {field}")
            
            return data
        except Exception as e:
            print(f"解析错误：{md_file}")
            print(f"错误详情: {str(e)}")
            return {}

def export(format):
    data_dir = Path('data')
    exports = []
    
    for md_file in data_dir.glob('*.md'):
        data = markdown_to_yaml(md_file)
        if data:
            # 将date对象转换为字符串
            if 'approvalDate' in data:
                data['approvalDate'] = data['approvalDate'].isoformat()
            exports.append(data)
    
    Path('exports').mkdir(exist_ok=True)
    
    if format == 'json':
        with open('exports/drugs.json', 'w', encoding='utf-8') as f:
            json.dump(exports, f, ensure_ascii=False, indent=2)
        print(f"已生成JSON文件，包含{len(exports)}条记录")
            
    elif format == 'csv':
        with open('exports/drugs.csv', 'w', newline='', encoding='utf-8') as f:
            if exports:
                writer = csv.DictWriter(f, fieldnames=exports[0].keys())
                writer.writeheader()
                writer.writerows(exports)
                print(f"已生成CSV文件，包含{len(exports)}条记录")
            else:
                print("无有效数据可导出")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=['json', 'csv'], required=True)
    args = parser.parse_args()
    export(args.format) 