# Better Cave Dimensions

Make "Better Cave Worlds" a standalone dimension that does not affect overworld. Based on my [updated port](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Worlds-updated).

**Version Support:** This branch strictly targets the latest Minecraft version (Currently **26.2**).

**Development Transparency:** AI/LLMs are **not** used in datapack logic development to ensure maximum precision and accuracy. AI tools may occasionally be used to generate README, assets, icons, or documentation.

---

## Install

Simply go to [releases](https://github.com/wujinjun-MC/Better-Cave-Dimensions/releases) page and download datapack named `Better Cave Dimensions - *`:

| Minecraft Version | Datapack Version | Branch |
| :--- | :--- | :--- |
| **1.21.4 – 1.21.8** | `v1.0.0` – `v1.4.1` | [`Better-Cave-Dimensions-legacy`](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy) |
| **26.2+** | `v2.x.x` | [`Better-Cave-Dimensions-26.2_or_later`](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later) |

---

## Goals & Roadmap

> [!NOTE]
> Most content in this section is adapted from the legacy branch. Some goals may be adjusted over time. (especially `Support third-party structure datapacks`)

### Structure Generation Fixes

- [ ] Pillager Outposts
- Villages
    - [ ] Desert
    - [ ] Plains
    - [ ] Savanna
    - [ ] Snowy
    - [ ] Taiga

### Vanilla Structure Support
> [!WARNING]
> Do **not** run `/locate structure` for Ocean Monuments, as it will crash your game/server.

- [ ] Ancient City
- [ ] Bastion Remnant [^1]
- [ ] Buried Treasure [^2]
- [ ] Desert Pyramid [^2]
- [ ] End City [^1]
- [ ] Igloo [^2]
- [ ] Jungle Pyramid [^2]
- [ ] Mineshaft
- [ ] Nether Fortress [^1]
- [ ] Nether Fossil [^1]
- [ ] Ocean Monument (Rare or nonexistent)
- [ ] Ocean Ruins [^2]
- [ ] Shipwreck [^2]
- [ ] Stronghold
- [ ] Swamp Hut [^2]
- [ ] Trial Chambers
- [ ] Woodland Mansion [^2]

### Third-Party Datapack Compatibility
*Note: Compatibility addons are not in this datapack and will be hosted in separate repositories.*

- [ ] [Dungeons and Taverns(DnT)](https://modrinth.com/user/NovaWostra)
    - Addon required: [Dungeons and Taverns compat](#addon_dnt_compat)
    - Full support:
        - [ ] [Main](https://modrinth.com/datapack/dungeons-and-taverns)
        - [ ] [Ancient City Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-ancient-city-overhaul)
        - [ ] [Desert Temple Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-desert-temple-overhaul)
        - [ ] [End Castle Standalone](https://modrinth.com/datapack/dungeons-and-taverns-end-castle-standalone)
        - [ ] [Nether Fortress Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-nether-fortress-overhaul)
        - [ ] [Pillager Outpost Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-pillager-outpost-overhaul)
        - [ ] [Stronghold Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-stronghold-overhaul)
- [ ] [Explorify](https://modrinth.com/datapack/explorify)
    - Addon required: [Explorify compat](#addon_compat_explorify)
- [ ] [Structory](https://modrinth.com/datapack/structory)
    - Addon required: [Structory compat](#addon_compat_structory)
- [ ] [Hopo Better Mineshaft](https://modrinth.com/datapack/hopo-better-mineshaft)
    - Addon required: [Hopo Better Mineshaft compat](#addon_compat_hopobettermineshaft)
- [ ] [Copper Golem Statue](https://modrinth.com/datapack/copper-golem-statue)
    - Addon required: [Copper Golem Statue compat](#addon_compat_coppergolemstatue)
- [ ] [EnderCat](https://modrinth.com/datapack/ender-cat)
    - Addon required: [EnderCat compat](#addon_compat_endercat)
- [ ] [Happy Ghast Houses](https://modrinth.com/datapack/happy-ghast-houses)
    - Addon required: [Happy Ghast Houses compat](#addon_compat_happyghasthouses)
- [ ] [Tidal Towns](https://modrinth.com/datapack/tidal-towns)
    - Addon required: [Tidal Towns compat](#addon_compat_tidaltowns)

### Other features

- [ ] Extend-able height (e.g. -128~512)
- [ ] Guidelines / Presets to create more custom cave dimensions

[^1]: Absolutely not exist due to missing biomes. Use addon `Unlimited vanilla structures` to fix.
[^2]: May break bedrock roof
[^3]: Rare or completely missing due to missing biomes. Use addon `overlay_addon_compat_`*`_larger` to fix.

---

## Bug Fix

- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))

---
---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
