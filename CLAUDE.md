# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

### Data Validation and Testing

```bash
# Validate a single data file
python scripts/validate.py data/1.md

# Run all tests
pytest scripts/test_*.py -v

# Export data to different formats
python scripts/export.py

# Generate statistics and update badges
python scripts/stats.py
```

### Git Workflow

```bash
# Standard commit messages for this project
# For new drug data
git commit -m "数据：添加[药品名]（[数量]种）"

# For fixes
git commit -m "修复：[描述问题]"

# For other changes
git commit -m "其他：[描述]"
```

## Architecture Overview

### Project Structure

This is the Original Drug Database (原研药数据库) - an open-source database of original/innovator drugs aimed at providing comprehensive, reliable drug data for Chinese users.

### Core Components

1. **Data Layer** (`/data/`)
   - Individual drug entries in Markdown format with YAML frontmatter
   - Each file numbered sequentially (1.md, 2.md, etc.)
   - Strict validation against schema.yaml

2. **Schema Definition** (`schema.yaml`)
   - Comprehensive field definitions with validation rules
   - Supports both domestic and imported drugs
   - Original drug identification logic embedded

3. **Validation Pipeline** (`/scripts/`)
   - `validate.py`: Ensures data compliance with schema
   - `export.py`: Converts data to JSON/CSV formats
   - `stats.py`: Generates statistics and updates badges
   - Test coverage with pytest

4. **CI/CD** (`.github/workflows/`)
   - Automated validation on every PR
   - Auto-updates statistics and badges
   - Enforces data quality standards

### Key Design Principles

1. **Data Authority**: All data must be verifiable through official sources (NMPA)
2. **Strict Validation**: Approval numbers must match exact regulatory format
3. **Change Tracking**: Complete Git history with PR review mechanism
4. **Community-driven**: Open for contributions with clear guidelines

### Data Model Highlights

- **Registration Types**: 境内生产药品 (domestic) / 境外生产药品 (imported)
- **Original Drug Logic**:
  - Imported: Originator matches MAH/Manufacturer/Packager
  - Domestic: Originator matches MAH/Manufacturer
- **Required Fields**: ID, registration type, generic name, formulation, specification, approval date, category
- **Conditional Fields**: Different requirements for domestic vs imported drugs

### Development Guidelines

1. **Adding New Drug Data**:
   - Create new file in `/data/` with next sequential ID
   - Include all required fields per schema.yaml
   - Provide at least one official source reference
   - Run validation before committing

2. **Data Sources Priority**:
   - A级: NMPA official documents
   - B级: Company official statements
   - C级: Industry consensus
   - D级: Market research data

3. **Validation Rules**:
   - ID format: 1-99999 (no gaps allowed)
   - Approval number: 国药准字[HZSJTB]八位数字
   - Registration number: 国药准字H[J]八位数字
   - Date format: YYYY-MM-DD

### Important Notes

- This is a Chinese-language database focusing on drugs available in mainland China
- All drug names and regulatory information follow Chinese NMPA standards
- The project uses CC-BY-SA 4.0 license for data sharing
- Contributions must follow the guidelines in CONTRIBUTING.md
