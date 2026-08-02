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

## Dev Details

<details>
<summary>Stage 1: Make it a seperate dimension</summary>

Following the path in [Better-Cave-Dimensions-legacy](https://github.com/wujinjun-MC/Better-Cave-Dimensions/commits/Better-Cave-Dimensions-legacy):
- `License.txt` add my copyright info
- Generate vanilla `data` (for datapack file and structure) and `reports` for biome parameters from server.jar
    - command: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports --output generated`
    - Now the files are in folder `generated` (Use `.gitignore` to ignore this folder)
- Merge overlays (only support latest versions); `pack.mcmeta` adapt to latest version requirements
- Rename to better cave dimensions
- Create dimension definition
    - [An example from legacy branch](https://raw.githubusercontent.com/wujinjun-MC/Better-Cave-Dimensions/d52f84c7076c3999e43257f777801b3e0e87192a/Better_Cave_Dimensions/data/better_cave_dimensions/dimension/cave.json)
    - Step by step:
        - Prepare biome list (with condition info) from "generated"
            - files: `generated/reports/biome_parameters/minecraft/*.json`
        - (optional, enabled) merge overworld and nether to allow nether biomes in cave dimension. (in `$.biomes` array, copy those in `nether.json` into `overworld.json`)
        - Replace the namespace of biome: `minecraft` -> `better_cave_dimensions` (named `all_biomes.json`)
            - Before:
                ```json
                {
                  "biomes": [
                    {
                      "biome": "minecraft:mushroom_fields",
                      "parameters": {...}
                    },
                    ...
                  ]
                }
                ```
            - After:
                ```json
                {
                  "biomes": [
                    {
                      "biome": "better_cave_dimensions:mushroom_fields",
                      "parameters": {...}
                    },
                    ...
                  ]
                }
                ```
            - Trick: find `"biome": "minecraft:`, "replace all" with `"biome": "better_cave_dimensions:`
        - Use this template, fill in `$.generator.biome_source.biomes` with `$.biomes` in `all_biomes.json`
            ```json
            {
              "type": "better_cave_dimensions:cave",
              "generator": {
                "type": "minecraft:noise",
                "settings": "better_cave_dimensions:cave",
                "biome_source": {
                  "type": "minecraft:multi_noise",
                  "biomes": [...]
                }
              }
            }
            ```
        - Finally you will get:
            ```json
            {
              "type": "better_cave_dimensions:cave",
              "generator": {
                "type": "minecraft:noise",
                "settings": "better_cave_dimensions:cave",
                "biome_source": {
                  "type": "minecraft:multi_noise",
                  "biomes": [
                    {
                      "biome": "better_cave_dimensions:mushroom_fields",
                      "parameters": {
                        "continentalness": [
                          -1.2,
                          -1.05
                        ],
                        "depth": 0.0,
                        "erosion": [
                          -1.0,
                          1.0
                        ],
                        "humidity": [
                          -1.0,
                          1.0
                        ],
                        "offset": 0.0,
                        "temperature": [
                          -1.0,
                          1.0
                        ],
                        "weirdness": [
                          -1.0,
                          1.0
                        ]
                      }
                    },
                    ...
                  ]
                }
              }
            }
            ```
        - Place in `Better_Cave_Dimensions/data/better_cave_dimensions/dimension/cave.json`
    - After: Also rename `Better_Cave_Dimensions/data/better_cave_dimensions/dimension_type/overworld.json`->`Better_Cave_Dimensions/data/better_cave_dimensions/dimension_type/cave.json` because the template uses `$.generator.settings`=`better_cave_dimensions:cave`
- Rename and Adjust `dimension_type` (dimension settings)
    - `has_skylight` -> true: For players who prefer building over the ceiling
    - `$.attributes.minecraft:visual/cloud_height` -> 128: Lower cloud height
    - `min_y` -> -128, `height` and `logical_height` -> 448: Height range -128~320 (with later `noise_settings` changes, players can build over the ceiling 256~320 or below the bedrock -128~-64)
- Rename and Adjust `worldgen/noise_settings`
    - `overworld.json`->`cave.json`
    - `sea_level` -> 32
    - `$.noise.height` -> 384: See above ("Height range")
    - In `$.noise_router`, replace `better_cave_worlds:overworld`->`better_cave_dimensions:cave`
    - Replace other `better_cave_worlds`->`better_cave_dimensions`
    - Find all `biome_is`, replace namespace `minecraft`->`better_cave_dimensions`
- Adjust/Add `configured_feature`
    - Replace `better_cave_worlds`->`better_cave_dimensions` for `$.config.features[*].feature` and `$.config.default` if `"type": "minecraft:random_selector"`
- Adjust/Add `placed_feature`
    - Replace `better_cave_worlds`->`better_cave_dimensions`
- Add biomes in `worldgen/biome` (TODO; should do after `configure_feature` and `placed_feature` are ready)
    - Path: `Better_Cave_Dimensions/data/better_cave_dimensions/worldgen/biome`
    - Step by step:
        - 

---

## Bug Fix

- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))

---
---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
