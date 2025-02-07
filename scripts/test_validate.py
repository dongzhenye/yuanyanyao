import pytest
from validate import validate_file, ValidationError
from pathlib import Path
import tempfile

@pytest.fixture
def valid_file():
    return Path("data/1.md")

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as td:
        yield Path(td)

def test_valid_file(valid_file):
    assert validate_file(str(valid_file))

def test_missing_id(valid_file, temp_dir):
    content = valid_file.read_text(encoding='utf-8').replace("id: 1", "")
    test_file = temp_dir / "missing_id.md"
    test_file.write_text(content, encoding='utf-8')
    with pytest.raises(ValidationError) as excinfo:
        validate_file(str(test_file))
    assert "缺少基础必填字段: id" in str(excinfo.value)

def test_invalid_approval_number(valid_file, temp_dir):
    content = valid_file.read_text(encoding='utf-8').replace(
        "国药准字HJ20140344", "国药准字X12345678"
    )
    test_file = temp_dir / "invalid_approval.md"
    test_file.write_text(content, encoding='utf-8')
    with pytest.raises(ValidationError) as excinfo:
        validate_file(str(test_file))
    assert "注册证号格式不正确" in str(excinfo.value)

if __name__ == "__main__":
    pytest.main() 