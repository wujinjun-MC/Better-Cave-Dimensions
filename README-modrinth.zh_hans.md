# Better Cave Worlds (更好的洞穴世界)

[EN](https://github.com/wujinjun-MC/Better-Cave-Dimensions/blob/Better-Cave-Worlds-updated/README-modrinth.md) | **简体中文**

## 这是一个分支

这是 [Better Cave Worlds](https://modrinth.com/datapack/better-cave-worlds) 数据包的一个分支 ([Github仓库](https://github.com/klinbee/Better-Cave-Worlds))。之所以创建此分支，是因为原作者不再积极维护，并且新的Minecraft版本引入了多个破坏性变更，导致此数据包无法使用。

此分支旨在延续该项目的生命力，具体措施:
- 适配Minecraft新版本
- 修复最新变更导致的世界生成问题
- 维护多版本兼容性
- 修复漏洞
- 接受Issues和Pull requests

开发者/贡献者请前往Github阅读README ([EN](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Worlds-updated) | [简体中文](https://github.com/wujinjun-MC/Better-Cave-Dimensions/blob/Better-Cave-Worlds-updated/README.zh_hans.md))

<details>
<summary>一段小故事</summary>

之前，我沉浸于我的衍生项目 "Better Cave Dimensions" (适用于 [26.2](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later) (可能稍后发布到Modrinth) 或 [1.21.4~1.21.8](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy)), 并且获得了非常愉快的体验，包括单人游戏以及与1A1S生存服务器的伙伴们一起游玩时。由于原作者停止了开发，包括我在内的许多喜爱该项目的玩家被迫停留在Minecraft旧版本。鉴于玩家社区中无人继续维护，我认为是时候将这个数据包更新到最新的Minecraft版本了。

更新 [20260815]: 适用于26.2及以上版本的 "Better Cave Dimensions" 已发布稳定版 (将本数据包的世界生成放入独立维度，从而不影响主世界)。目前仅在 [Github Releases](https://github.com/wujinjun-MC/Better-Cave-Dimensions/releases) 提供下载，稍后会发布到Modrinth。

更新 [20260816]: "1A1S生存服务器"已经复活，并安装了 "Better Cave Dimensions" ，欢迎在服务器内体验。
- 服务器地址: lightseeking.eu.org
- 如何进入此维度: `/mvtp world_better_cave_dimensions_cave` 或在传送门区域进行传送

</details>

---

## 原来的描述

这个数据包启用"洞穴世界"生成，包括(多种)生物群系，允许植被、含水层、大型矿脉生成。遗憾的是，数据包无法更改大多数结构的生成高度，因此它们大部分生成在基岩顶部。你仍然可以做很多事情，但是充满挑战！

This is Datapack enables Cave World generation with biomes and allows foliage, aquifers, and large ore veins to generate. Unfortunately, you cannot change the height at which most structures generate with a datapack, so most of them generate on the bedrock roof. You should still be able to do everything you normally could, but it will be a challenge to do so!

### 生成说明 Generation Notes

- 以下结构声称在顶部或附近 The following structures generate on/near the roof:
    - 埋藏的宝藏 Buried Treasure
    - 沙漠神殿 Desert Pyramids
    - 雪屋 Igloos
    - 丛林神庙 Jungle Pyramids
    - 林地府邸 Mansions
    - 海底神殿 Ocean Ruins
    - 沉船 Shipwrecks
    - 沼泽小屋 Witch Huts
- 被动型生物遵循 [原版生成规则](https://zh.minecraft.wiki/w/%E7%94%9F%E7%89%A9%E7%94%9F%E6%88%90) Passive Mobs obey [vanilla spawning rules](https://minecraft.wiki/w/Mob_spawning):
    - 它们需要高亮度才能生成，仅出现在世界生成时靠近光源的位置 (岩浆或发光浆果) They require high light-levels to spawn, meaning only near light sources (lava or glowberries) on worldgen
        - 也会出现在其他结构，包括地下村庄的动物围栏 Also, from structures like underground village animal pens
    - 它们也能自然生成，但是有10个生物的生成上线，所以已加载区块(模拟距离)内的生物数量必须很少(请注意出生点区块！并从wiki了解生物类别)，考虑光照等级，考虑其他特殊生成情况 (你需要研究)。They can also spawn naturally, but there is a creature mob cap of 10, which means that you need to have very few creatures loaded (keep spawn chunks in mind! and understand mob categories from the Wiki as well) and also light levels, and additional spawn mechanics you will need to research in rare cases
- 顶部雪层被硬编码生成于表面，所以无法在地下生成 Snow top layers are hardcoded to generate on the surface, so won't generate underground
