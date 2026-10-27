# Loon Sync Robin

**Loon 配置自动同步与维护项目**

基于 GitHub Actions 实现 Loon 配置文件的自动化同步与维护，集中管理配置文件、自动选节点配置及自定义插件，减少手动更新操作，让配置维护更加方便。

## ✨ 项目简介

本项目用于维护个人 Loon 配置，结合 GitHub 仓库与自动化工作流，实现配置文件的集中管理和自动更新。

项目包含自动选节点配置、自定义分流插件以及相关脚本，适合希望通过 GitHub Actions 自动维护 Loon 配置的用户。

## 🚀 主要功能

- **自动化同步**：通过 GitHub Actions 执行配置同步任务。
- **配置文件管理**：集中维护 Loon 配置及相关资源。
- **自动选节点**：提供基于网络延迟测试的策略组配置，自动选择合适的节点。
- **多地区策略组**：支持香港、台湾、日本、韩国、新加坡、美国等地区的节点筛选与策略管理。
- **自定义插件**：集成 RealIP 相关插件，为指定域名配置真实 IP 处理及直连规则。
- **手动触发**：支持在 GitHub Actions 页面手动执行已配置的工作流。

## 📂 项目结构

```text
loon-sync-robin/
├── .github/
│   └── workflows/                      # GitHub Actions 工作流
├── scripts/                            # 自动化处理脚本
├── Loon_Auto_Select_Config_By_iKeLee.lcf  # 自动选节点配置
├── RealIP-Bypass-Domain.plugin         # 自定义 RealIP 插件
├── loon.conf                           # Loon 配置文件
└── README.md                            # 项目说明
```

## 📄 文件说明

| 文件 | 说明 |
|---|---|
| `Loon_Auto_Select_Config_By_iKeLee.lcf` | 自动选节点配置，包含地区节点筛选、延迟优选、备用策略及规则、插件配置。 |
| `RealIP-Bypass-Domain.plugin` | 自定义 RealIP 插件，为指定域名配置 RealIP 处理及直连规则。 |
| `loon.conf` | Loon 主配置文件，用于维护相关配置内容。 |
| `.github/workflows/` | 存放 GitHub Actions 工作流定义。 |
| `scripts/` | 存放自动化同步和配置处理脚本。 |

## 📥 如何使用

### 方式一：直接导入 Loon 配置

1. 打开 [Loon Sync Robin 仓库](https://github.com/llc-robin/loon-sync-robin)。
2. 找到需要使用的配置文件。
3. 根据 Loon 支持的配置导入方式，将配置导入客户端。
4. 检查订阅、节点策略组、规则和插件是否正常加载。

自动选节点配置：

[查看 Loon_Auto_Select_Config_By_iKeLee.lcf](https://raw.githubusercontent.com/llc-robin/loon-sync-robin/main/Loon_Auto_Select_Config_By_iKeLee.lcf)

自定义 RealIP 插件：

[查看 RealIP-Bypass-Domain.plugin](https://raw.githubusercontent.com/llc-robin/loon-sync-robin/main/RealIP-Bypass-Domain.plugin)

> 使用前请检查配置中的订阅信息、策略组、规则和插件地址，并根据自己的实际环境进行调整。

### 方式二：启用 GitHub Actions 自动同步

1. Fork 本仓库，或在自己的 GitHub 仓库中维护相关文件。
2. 进入仓库的 **Actions** 页面。
3. 如果 GitHub 提示需要启用工作流，请先启用。
4. 选择对应的同步工作流。
5. 点击 **Run workflow**，手动执行一次任务。
6. 查看执行日志，确认同步、配置处理及提交步骤是否成功。
7. 后续按照工作流中定义的触发条件自动运行。

自动同步的实际频率、更新来源、文件覆盖范围及提交规则，以 `.github/workflows/` 中的工作流和 `scripts/` 中的脚本为准。

## ⚙️ 自动化机制

本项目通过 GitHub Actions 执行自动化任务。一般工作流程如下：

1. 检出 GitHub 仓库。
2. 获取或处理待同步的配置内容。
3. 执行配置修正或其他脚本操作。
4. 检查文件变化。
5. 将发生变化的文件提交并推送到仓库。

以上为项目自动化流程的概括，具体执行步骤及行为请以实际工作流代码为准。

## 🔧 自定义与维护

### 修改配置

可根据自己的使用需求调整以下内容：

- 地区节点名称匹配规则。
- 手动选择策略组与延迟优选策略组。
- 默认出口及备用策略。
- 远程分流规则与插件列表。
- RealIP 处理的域名范围。

修改前建议先备份原始文件，并确认配置语法符合 Loon 的要求。

### 检查自动同步结果

当 GitHub Actions 显示执行成功，但仓库文件没有更新时，可以依次检查：

1. 上游配置是否实际发生变化。
2. 同步脚本是否成功获取最新内容。
3. 后续处理步骤是否覆盖了同步结果。
4. 工作流是否包含文件变更检测。
5. Git 提交步骤是否正确执行。
6. GitHub Actions 是否具有相应的仓库写入权限。

**注意：** 工作流执行成功不一定意味着每次运行都会产生新的提交。如果目标文件内容没有变化，或者处理脚本没有将结果写入目标文件，仓库就可能不会出现新的提交记录。

## ❓ 常见问题

### 1. GitHub Actions 执行成功，但配置文件没有更新？

请检查同步来源、目标文件路径、脚本处理逻辑和 Git 提交日志，确认最新内容是否真正写入目标文件。

### 2. 自动选节点没有生效？

请检查节点名称是否符合地区匹配规则、节点订阅是否正常，以及策略组是否包含有效节点。

### 3. 插件无法加载？

请检查插件 URL 是否可以访问、插件语法是否正确，以及 Loon 中的插件启用状态。

### 4. 修改后如何确认生效？

先检查 GitHub 仓库中的最新文件，再在 Loon 中重新加载对应配置或更新远程资源，最后验证策略组、规则和插件运行情况。

## ⚠️ 使用说明

- 本项目主要用于个人配置管理与自动化维护。
- 配置文件中的远程订阅、规则和插件依赖外部服务，实际可用性取决于相关服务状态。
- 请勿在公开仓库中提交订阅密钥、访问令牌、密码或其他敏感信息。
- 使用前请自行检查配置内容，并遵守相关软件及服务的使用条款。
- 本项目与 Loon 及第三方插件作者的官方项目之间的关系，请以各自的官方说明为准。

## 🔗 相关链接

- 项目仓库：[llc-robin/loon-sync-robin](https://github.com/llc-robin/loon-sync-robin)
- GitHub Actions：[查看自动化任务](https://github.com/llc-robin/loon-sync-robin/actions)
- 自动选节点配置：[Loon_Auto_Select_Config_By_iKeLee.lcf](https://raw.githubusercontent.com/llc-robin/loon-sync-robin/main/Loon_Auto_Select_Config_By_iKeLee.lcf)
- 自定义插件：[RealIP-Bypass-Domain.plugin](https://raw.githubusercontent.com/llc-robin/loon-sync-robin/main/RealIP-Bypass-Domain.plugin)

---
## 🙏 致谢

特别感谢 [iKeLee](https://github.com/iKeLee) 及相关上游项目作者的开源分享与持续维护。

本项目使用并参考了上游提供的 Loon 自动选节点配置及相关规则。感谢原作者在配置编写、节点筛选、延迟测试和自动化策略等方面所做的工作，为本项目提供了良好的基础。

本项目在上游配置的基础上，结合个人使用需求进行同步、整理及自动化维护，旨在降低配置维护成本，方便持续更新。

**开源不易，感谢每一位开源作者的付出与分享！** 使用上游项目时，请尊重原作者的劳动成果，并遵循其项目的许可证及相关使用说明。

如需了解上游项目的完整内容、更新记录及使用方式，请优先访问原始项目。



如果本项目对你有所帮助，欢迎 Star ⭐ 支持。
