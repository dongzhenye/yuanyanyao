import pytest
from pathlib import Path
from export import markdown_to_yaml

def test_yaml_extraction():
    data = markdown_to_yaml('data/1.md')
    assert data['id'] == 1
    assert data['genericName'] == '奥司他韦'
    assert data['registrationNumber'] == '国药准字HJ20140344'

def test_date_parsing():
    data = markdown_to_yaml('data/1.md')
    assert 'approvalDate' in data
    assert str(data['approvalDate']) == '2024-01-15'

def test_nested_yaml():
    data = markdown_to_yaml('data/1.md')
    assert 'originatorSource' in data
    assert len(data['originatorSource']) == 2
    assert data['originatorSource'][0]['type'] == 'FDA橙皮书' 