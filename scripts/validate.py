import re
from pathlib import Path

class ValidationError(Exception):
    pass

def validate_id(value):
    """校验ID规则:
    1. 必须是1-99999之间的整数
    2. 不能跳号(需要检查已存在文件)
    """
    try:
        id_num = int(value)
        if not (1 <= id_num <= 99999):
            raise ValidationError("ID必须在1-99999之间")
        
        # 检查是否跳号
        data_dir = Path(__file__).parent.parent / 'data'
        existing_ids = [int(f.stem) for f in data_dir.glob('*.md')]
        if existing_ids:
            max_id = max(existing_ids)
            if id_num > max_id + 1:
                raise ValidationError(f"ID不能跳号: {max_id + 1} -> {id_num}")
    except ValueError:
        raise ValidationError("ID必须是整数")

def validate_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 基础必填字段校验
        base_required = ['id', 'registrationType', 'genericName', 'formulation', 
                        'specification', 'approvalDate', 'category']
        for field in base_required:
            if f'{field}:' not in content:
                raise ValidationError(f"缺少基础必填字段: {field}")

        # 注册类型相关校验
        reg_type_match = re.search(r'registrationType:\s*(.*)', content)
        reg_type = reg_type_match.group(1) if reg_type_match else None
        
        if reg_type == '境内生产药品':
            # 境内必填字段
            domestic_required = [
                'approvalNumber', 'productName', 'mahName', 
                'manufacturerName', 'manufacturerAddress'
            ]
            for field in domestic_required:
                if f'{field}:' not in content:
                    raise ValidationError(f"境内药品缺少必填字段: {field}")
                    
        elif reg_type == '境外生产药品':
            # 境外必填字段
            imported_required = [
                'registrationNumber', 'mahName', 'mahAddress',
                'manufacturerName', 'manufacturerAddress', 'manufacturerCountry'
            ]
            for field in imported_required:
                if f'{field}:' not in content:
                    raise ValidationError(f"境外药品缺少必填字段: {field}")

            # 境外药品的中英文要求
            if not (re.search(r'productName:\s*', content) or re.search(r'productNameEn:\s*', content)):
                raise ValidationError("境外药品必须至少有一种语言的产品名称")

        # 格式校验
        if approval_number_match := re.search(r'approvalNumber:\s*(.*)', content):
            approval_number = approval_number_match.group(1)
            if not re.match(r'^国药准字[HZSJTB]\d{8}$', approval_number):
                raise ValidationError("批准文号格式不正确")

        if reg_number_match := re.search(r'registrationNumber:\s*(.*)', content):
            reg_number = reg_number_match.group(1)
            if not re.match(r'^国药准字H[J]\d{8}$', reg_number):
                raise ValidationError("注册证号格式不正确")

        if approval_date_match := re.search(r'approvalDate:\s*(.*)', content):
            approval_date = approval_date_match.group(1)
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', approval_date):
                raise ValidationError("日期格式必须为YYYY-MM-DD")

        return True
    except Exception as e:
        raise ValidationError(f"文件校验失败: {str(e)}")

if __name__ == "__main__":
    import sys
    try:
        validate_file(sys.argv[1])
        print("校验通过")
    except ValidationError as e:
        print(f"错误: {str(e)}")
        exit(1) 