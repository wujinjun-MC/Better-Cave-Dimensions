# AI政策

## 正文

AI / LLM 被禁止用于:
- 为此数据包生成代码、资源(例如图标、.nbt模型)、文本(例如README)
    - 原因:
        - 如果包含这几种AI生成的内容，我必须在"编辑项目"的"Content disclosures"部分打开"Contains AI-generated content"(并选择用AI生成了哪种内容)。如果其他玩家在"Advanced exclusions"过滤了AI生成内容，他们无法看到本项目
        - 根据 `Modrinth content rules` 6.2: "No images uploaded to a gallery, icon, description, or any other part of a project page may be created or derived from generative AI output. Any such images may be removed." (上传到图库、图标、描述或项目页面任何其他部分的图片不能用生成式AI创建或衍生于生成式AI。此类图像可能被移除)
- 提交Issues或Pull requests
    - 原因: 任何修复或请求必须由真人经过谨慎思考后提出，不应该由AI生成
- 国际化(i18n)/翻译
    - 包括"传统"机翻(例如 translate.google.com)和LLM

AI/LLM*可以*被用于:
- 代码审查、错误修复、质量改进建议
    - 然而，任何修改不能直接生成
        - 例如

参阅:
- [Modrinth content rules](https://modrinth.com/legal/rules) 2026.08.13起 (第6部分)

## 贡献者

