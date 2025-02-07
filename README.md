# 原研药数据库

[![数据来源](https://img.shields.io/badge/数据来源-NMPA-blue)](https://www.nmpa.gov.cn/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![贡献指南](https://img.shields.io/badge/贡献-CONTRIBUTING-blue)](./CONTRIBUTING.md)

一个开源的原研药数据库，旨在为中国用户提供覆盖全面、更新及时、来源可靠的原研药数据。

## 项目特性

- **权威数据**：基于国家药监局(NMPA)等官方数据源
- **严格校验**：符合《药品注册管理办法》格式规范
- **结构清晰**：采用分层设计的YAML数据格式
- **变更追溯**：完整的Git历史记录和PR审核机制
- **社区共建**：支持通过GitHub进行协作维护

## 快速开始

```bash
git clone https://github.com/dongzhenye/yuanyanyao.git
cd yuanyanyao/data
```

查看示例数据：

```yaml
# data/1.yaml
id: 1
registrationNumber: 国药准字HJ20140344
registrationType: 境外生产药品
productName: 磷酸奥司他韦胶囊
productNameEn: Oseltamivir Phosphate Capsules
brandName: 达菲
category: 化学药品
specification: 75mg
mahName: Roche Pharma (Schweiz) AG
approvalDate: 2024-01-15
```

## 数据结构

核心字段定义（完整版见[schema.yaml](schema.yaml)）：

| 字段                | 类型     | 必填 | 示例值                  |
|---------------------|----------|------|-------------------------|
| id                 | string  | 是   | 1                      |
| registrationNumber | string  | 是   | 国药准字HJ20140344     |
| productName        | string  | 是   | 磷酸奥司他韦胶囊       |
| brandName          | string  | 是   | 达菲                   |
| specification      | string  | 是   | 75mg                   |

## 设计原则

1. **数据权威性**
   - 以NMPA官网数据为基准
   - 所有字段必须可官方核验
2. **更新及时性**
   - 自动化校验脚本
   - 社区驱动的更新机制
3. **适度设计**
   - 仅收录必要核心字段
   - 避免存储可推导数据

## 如何贡献

1. 阅读[贡献指南](CONTRIBUTING.md)
2. 创建新的药品数据文件
3. 提交Pull Request
4. 通过自动化校验流程

推荐贡献格式：
```bash
git commit -m '数据：新增磷酸奥司他韦胶囊(HJ20140344)'
```

## 开源协议

采用 [CC-BY-SA 4.0](LICENSE) 协议：

- 允许自由共享和演绎
- 需保留原始署名
- 衍生作品需采用相同协议

## 项目结构

```
yuanyanyao/
├── data/          # 核心数据库
├── docs/          # 设计文档
│   └── database.md # 数据库设计规范
├── scripts/       # 校验工具
└── schema.yaml    # 数据模式定义
```

## 致谢

感谢所有[贡献者](https://github.com/dongzhenye/yuanyanyao/graphs/contributors)的宝贵贡献！
