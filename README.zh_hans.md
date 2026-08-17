# Better Cave Worlds Updated (更好的洞穴世界-更新版)

这是 [klinbee/Better-Cave-Worlds](https://github.com/klinbee/Better-Cave-Worlds) (非官方)分支，用于支持新版Minecraft，因为原作者 [klinbee](https://github.com/klinbee) 从2025.10.18起没有维护。 ([最后一次 commit](https://github.com/klinbee/Better-Cave-Worlds/commit/cd8e17e98e29c024fc554cecf6763d1b8783f1c3))

另外查看用于Modrinth的README ([EN](https://modrinth.com/datapack/better-cave-worlds-updated) | [简体中文](./README-modrinth.zh_hans.md))

## 安装

查看 [Modrinth](https://modrinth.com/datapack/better-cave-worlds-updated)

## 开发者

### AI政策

查看 [docs/AI_policy](docs/AI_policy.zh_hans.md)

### 使用的工具

- [Data Pack Generators - Versions Explorer](https://misode.github.io/versions/): 对比数据包结构，查找不同版本的破坏性变更
- [Minecraft Assets Explorer](https://mcasset.cloud/): 并排比较原版数据包两个版本之间的差异
    - 示例: [1.21.10与1.21.11 data/minecraft/dimension_type/overworld.json 的不同](https://mcasset.cloud/1.21.11...1.21.10/data/minecraft/dimension_type/overworld.json)
- [Minecraft wiki: 数据生成器](https://zh.minecraft.wiki/w/%E6%95%B0%E6%8D%AE%E7%94%9F%E6%88%90%E5%99%A8) (英文版: [Tutorial:Running the data generator](https://minecraft.wiki/w/Tutorial:Running_the_data_generator)):
    - 命令: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports`
    - 生成服务端数据包结构
        - `The contents of the vanilla data pack (except "pack.mcmeta") will be generated to "generated" directory in the run directory of the command line interface.`
    - 从硬编码的维度定义生成 `data/minecraft/dimension/overworld.json` (在数据包中的路径) (输出位于 `./generated/reports/biome_parameters/minecraft`)。 对于 [Better-Cave-Dimensions](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later) 更有帮助。
- [minecraft-server-jar-downloads.md](https://gist.github.com/cliffano/77a982a7503669c3e1acb0a0cf6127e9#file-minecraft-server-jar-downloads-md): server.jar 的下载直链
- [How to Upgrade Datapacks (Youtube播放列表)](https://www.youtube.com/playlist?list=PLgbPk8f9bw9rtYmnIpcd0__q9cjVqmx1l): 查看每个版本的破坏性变更以及解决方法
    - [1.21.11](https://www.youtube.com/watch?v=9QuRZOP3Gcw)
    - [26.1.x](https://www.youtube.com/watch?v=4FFFRFIyqIs)
    - [26.2](https://www.youtube.com/watch?v=k53YFmA8Oe0)
    - [Tutorial files](https://drive.google.com/drive/folders/17h79rkR0QulQbeR--SPpC5So3vAU_1ga)
- [Blockbench](https://blockbench.net/): 创建图标的 .bbmodel 模型文件
    - 使用的插件:
        - [Minecraft Title Generator](https://www.blockbench.net/plugins/minecraft_title_generator)

### 开发详情

关于我如何对新的Minecraft版本进行适配: 查看 [docs/Updating_to_modern_Minecraft_version](docs/Updating_to_modern_Minecraft_version.md) (只有英文)

---

想要一个独立的洞穴维度? 查看我的 `Better Cave Dimensions` (用于版本 [1.21.4~1.21.8](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy) 或 [26.2+](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later)).

---

↓ 原始 README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
