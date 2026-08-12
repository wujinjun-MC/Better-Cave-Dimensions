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

- [x] Pillager Outposts
- Villages
    - [x] Desert
    - [x] Plains
    - [x] Savanna
    - [x] Snowy
    - [x] Taiga

### Vanilla Structure Support
> [!WARNING]
> Do **not** run `/locate structure` for Bastion Remnant(?) and Ocean Monuments, as it will crash your game/server.

- [x] Ancient City
- [x] Bastion Remnant [^1]
- [x] Buried Treasure [^2]
- [x] Desert Pyramid [^2]
- [x] End City [^1]
- [x] Igloo [^2]
- [x] Jungle Pyramid [^2]
- [x] Mineshaft
- [x] Nether Fortress [^1]
- [x] Nether Fossil [^1]
- [x] Ocean Monument (Rare or nonexistent)
- [x] Ocean Ruins [^2]
- [x] Shipwreck [^2]
- [x] Stronghold
- [x] Swamp Hut [^2]
- [x] Trial Chambers
- [x] Woodland Mansion [^2]

### Third-Party Datapack Compatibility
*Note: Compatibility addons are not in this datapack and will be hosted in separate repositories.*

This datapack must be loaded *after* datapacks mentioned below.
- If you are starting a fresh server: Rename this datapack file name (e.g. Add prefix "Z") so that it is the last one alphabetically.
- If you are adding this datapack or the datapack(s) that needs compatibility to existing server: DO NOT enable compatibility addons initially. Add datapacks, completely start and stop server, open "level.dat" in NBT editor (if using bukkit/spigot/paper (or forks), also open that in other world/dimension folders), expand "DataPacks", place this datapack below the others, save, finally enable compatibility addons and start.

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

## Addons

### Enable addon

1. Open `pack.mcmeta`
2. Use `Ctrl+F` to search "Overlay name"
3. Change `min_format` range to the value of `$.pack.min_format`

### List
#### Vanilla
<details>
<summary>Unlimited vanilla structures</summary>

- Overlay name: `overlay_addon_unlimited_vanilla_structures`
- Supported Minecraft version: (same as datapack supported version)
- Features:
    1. Structure definition
        1. Structures can be placed in any biomes
        2. Change `terrain_adaption` to expose structures
        3. Change `spawn_overrides` to allow mob generation
        4. Change `step` (feature order) to allow some structures to override neighborhoods
        4. For structures using jigsaws
            1. Always `use_expansion_hack`
            2. Maximize `size` and `max_distance_from_center` (Requires strong CPU)
            3. Maximize `start_height` range ([min height +16] ~ [max height -16])
            4. Remove `dimension_padding`
    2. Structure set
        1. `placement`.`spacing` (or `placement`.`distance`) -> max(1,min(16, half_spacing))
        2. `placement`.`separation` -> 0
        3. `placement`.`spread_type` -> default
        4. `placement`.`frequency_reduction_method` -> default
        5. `placement`.`exclusion_zone` -> none
        6. `placement`.`frequency` -> double (if present)
        7. Strong hold count -> 1024 ; `preferred_biomes` -> all
</details>

<details>
<summary>Dimension type tweaks</summary>

- Overlay name: `overlay_addon_dimension_type_tweaks`
- Supported Minecraft version: (same as datapack supported version)
- Features:
    - `$.attributes`
        1. `gameplay/bed_rule` `can_sleep` = always: Can always sleep to skip night or whole day
        2. `gameplay/piglins_zombify` = false: Piglins will not convert to zombified ones
        3. `gameplay/respawn_anchor_works` = true: Can use respawn anchor to set spawn, without exploading
        4. `gameplay/snow_golem_melts` = false: Snow golem can't take damage by heat
        5. `visual/cloud_height` = 256.33: Higher cloud height
</details>

<span id = "addon_height_extend"><details></span>
<summary>Extend height range</summary>

- Overlay name: `overlay_addon_height_extend`
- Supported Minecraft version: (same as datapack supported version)
- Features:
    1. All Changes in `overlay_addon_dimension_type_tweaks`
    2. Build height extends to -128~512
    3. Noise height (the height of cave part) extends to -64~384
    4. Density functions fit the new noise height.
    5. Cloud height change to 448
- Side effects:
    - The base height of a structure is too limited (-32~80 in default setting for vanilla ones) so that it is not possible to see any structures in the upper cave space. You can just enable `overlay_addon_unlimited_vanilla_structures` and/or `overlay_addon_compat_*_larger` to fix.
</details>

<details>
<summary>Vanilla biome tag tweaks</summary>

- Overlay name: `overlay_addon_biome_tag_tweaks_vanilla`
- Supported Minecraft version: 1.21.4+
- Features:
    1. No biome blocks mineshaft
    2. Polar bears can spawn on ice blocks in all biomes
    3. Snow golem can not smelt in all biomes
    4. Pillager Patrol can spawn in all biomes
    5. Wandering Trader can spawn in all biomes
    6. Zombie Siege can spawn in all biomes
</details>

---

## Dev Details

Note: `$.`... represents JSON path, e.g. `$.generator.settings` means the value of key `settings` in object `generator`.

<details>
<summary>Stage 1: Make it a seperate dimension</summary>

Following the path in [Better-Cave-Dimensions-legacy](https://github.com/wujinjun-MC/Better-Cave-Dimensions/commits/Better-Cave-Dimensions-legacy):
- `License.txt` add my copyright info
- Generate vanilla `data` (for datapack file except structures) and `reports` for biome parameters from server.jar
    - command: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports --output generated`
    - Now the files are in folder `generated` (Use `.gitignore` to ignore this folder)
- Extract structure .nbt files from server.jar (Located in `data/minecraft/structures`)
- Merge overlays (only support latest versions); `pack.mcmeta` adapt to latest version requirements
- Rename to better cave dimensions
    - `better_cave_worlds`->`better_cave_dimensions`
    - Scan potential unconverted files:
        - Search `worlds`
- Remove redundancies
    - Search `minecraft:no_op`
        - Example: `Better_Cave_Dimensions/data/better_cave_dimensions/worldgen/placed_feature/fancy_oak_bees_0002.json`
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
- Adjust/Add `worldgen/configured_feature`
    - Replace `better_cave_worlds`->`better_cave_dimensions` for `$.config.features[*].feature` and `$.config.default` if `"type": "minecraft:random_selector"`
- Adjust/Add `worldgen/placed_feature`
    - Remove redundancy (no diff compared to vanilla)
    - Replace `better_cave_worlds`->`better_cave_dimensions`
    - Scan rest of files in vanilla. If contains strict rules (below) that make it impossible to generate in this dimension, simply import and eliminate/modify.
        - Strict `height_range`
            - Suggestion: `[0/5 blocks above "min_y"]~[0/5 blocks below max height]` or directly remove
            - Example:
                - `amethyst_geode`: It should allow to generate in wider height range since the whole dimension is cave
            - Ores (`ore_*`) are excepted (Or you can enable addon `TODO` to unlock)
        - `in_square`+`heightmap`
            - 1
                - Pattern:
                    ```json
                    {
                      "type": "minecraft:in_square"
                    },
                    {
                      "type": "minecraft:heightmap",
                      "heightmap": * (WORLD_SURFACE_WG, MOTION_BLOCKING)
                    }
                    ```
                - Replace:
                    ```json
                    {
                      "type": "minecraft:count_on_every_layer",
                      "count": 1
                    }
                    ```
            - 2
                - Pattern:
                    ```json
                    {//this part is optional
                      "type": "minecraft:in_square"
                    },
                    {
                      "type": "minecraft:surface_water_depth_filter",
                      "max_water_depth": 0
                    },
                    {
                      "type": "minecraft:heightmap",
                      "heightmap": "OCEAN_FLOOR"
                    }
                    ```
                - Replace:
                    ```json
                    {
                      "type": "minecraft:count_on_every_layer",
                      "count": 1
                    },
                    {
                      "type": "minecraft:block_predicate_filter",
                      "predicate": {
                        "type": "minecraft:matching_blocks",
                        "offset": [
                          0,
                          0,
                          0
                        ],
                        "blocks": "minecraft:air"
                      }
                    }
                    ```
        - Other `heatmap`
            - Pattern:
                ```json
                {
                  "type": "minecraft:surface_relative_threshold_filter",
                  "heightmap": "OCEAN_FLOOR_WG",
                  "max_inclusive": *
                }
                ```
            - Replace:
                ```json
                {
                  "type": "minecraft:count_on_every_layer",
                  "count": 1
                }
                ```
        - Bug fix:
            - Feature placing race condition:
                - Example: `[01:09:01] [Worker-Main-6/ERROR]: Detected unsafe terrain read during worldgen: reading from chunk [26, -30] while generating chunk [28, -31] (distance: 2, write radius: 1), step: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / better_cave_dimensions:glow_lichen]`
                - type `count`+`count_on_every_layer` combo (or other kinda over-counted placement)
                - Try to remove `count_on_every_layer`
- Add biomes in `worldgen/biome`
    - Path: `Better_Cave_Dimensions/data/better_cave_dimensions/worldgen/biome`
    - Step by step:
        - Import all biomes from vanilla (End biomes (which are not exist in this dimension) can skip)
        - In `$.features`, if the `placed_features` name exists, replace namespace `minecraft`->`better_cave_dimensions`
            - Trick: In VScode, F2 -> Ctrl+C to copy name, paste into all files search (click `...` and `files to include`=`Better_Cave_Dimensions/data/better_cave_dimensions/worldgen/biome`), if there are results, replace `minecraft:*`->`better_cave_dimensions:*`
- Fix and adjust `worldgen/density_function`
    - Rename folder `overworld`->`cave`
    - Replace `better_cave_worlds:overworld`->`better_cave_dimensions:cave` then `better_cave_worlds`->`better_cave_dimensions`.
    - Adjust `final_density.json`:
        - In `$.input.argument.argument.argument2.argument.argument2.argument2.argument2.argument2.argument1`:
            - `from_y`=240, `to_y`=256
            - Expand the internal cavity. The original cave ceiling height range was 104~128. After expanding the cave height range (setting it to -64~256 in `noise_setting`), the 128~256 area only contained stone and a few noisy caves, wasting remaining value. By adjusting it to 240~256, there are only 16 blocks in the ceiling, giving players more space and reducing their reliance on the space above bedrock.
        - In `$.input.argument.argument.argument2.argument.argument2.argument1`: No need to adjust currently. If lowest height is changed, `from_y` and `to_y` should be moved.
    - `aquifer/fluid_level_floodedness.json`, `vein/ridged.json` and `vein/toggle.json`: Fit height range.
- Fix structure not generate properly (Structure Generation Fixes and Vanilla Structure Support)
    - Approach 1: Only add tags with `tags/worldgen/biome/has_structure/*` under namespace `minecraft:`
        - Deprecated: Inefficient for further customization (e.g. fix over-roof generation)
    - Approach 2: Import structures (nbt, definition and set)
        - Since the sturctures are not changed 1.21.8~26.2, some files are imported from old branch `Better-Cave-Dimensions-legacy`.
        - Affected: `worldgen/structure`, `worldgen/structure_set`, `tags/worldgen` biome and structure, `template_pool`
        - Step by step:
            - Check all `structure` in vanilla (tag with "Step 1")
                - Use [NBTstudio](https://github.com/tryashtar/nbt-studio) (or zh_CN: https://github.com/firesahc/nbt-studio-language) or VS code extension ([NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt) and [snbt](https://marketplace.visualstudio.com/items?itemName=Tnze.snbt))
                - Extract S-NBT and text find `pool` (equal SNBT path: `.blocks[*].nbt.pool`). If references existing `worldgen/template_pool`, include and replace namespace `minecraft`->`better_cave_dimensions`
            - Check all `worldgen/template_pool` in vanilla (tag with "Step 2")
                - If any `$.elements[*].element.projection`=`terrain_matching`, include and replace with `rigid` (or the structure can break the ceiling).
                - If "Step 1" included .nbt file, related `template_pool` should be included and replace namespace `minecraft`->`better_cave_dimensions` (only affected).
            - Repeat "Step 1" and "Step 2" until no new modifications are found.
                - Boring one by one .nbt edit? Use the [tool](./assets/tools/nbt-text-search-and-replace_namespace.py)
                    - Requires nbtlib (pip install nbtlib)
                    - Prepare vanilla structure .nbt files in a seperate folder (e.g. D:\structures-processing), leaving only "names" in template_pool (currently `pillager_outpost` and `village`).
                    - Usage: `python nbt-text-search-and-replace_namespace.py --dir D:\structures-processing --replace-namespace "minecraft" "better_cave_dimensions" --search-val <val1> --search-val <val2> ...`
                        - Obtain `val*`: Base on `template_pool` root folder, add all file paths without ".json" (e.g. `pillager_outpost/base_plates`) (On Windows, convert backslashes to forward slashes).
                    - Command (as of 26.2): `python assets/tools/nbt-text-search-and-replace_namespace.py --dir D:\structures-processing --replace-namespace "minecraft" "better_cave_dimensions" --search-val pillager_outpost/base_plates --search-val pillager_outpost/feature_plates --search-val village/desert/streets --search-val village/desert/terminators --search-val village/desert/town_centers --search-val village/desert/zombie/streets --search-val village/desert/zombie/terminators --search-val village/plains/houses --search-val village/plains/streets --search-val village/plains/terminators --search-val village/plains/town_centers --search-val village/plains/zombie/houses --search-val village/plains/zombie/streets --search-val village/savanna/streets --search-val village/savanna/terminators --search-val village/savanna/town_centers --search-val village/savanna/zombie/streets --search-val village/savanna/zombie/terminators --search-val village/snowy/streets --search-val village/snowy/terminators --search-val village/snowy/town_centers --search-val village/snowy/zombie/streets --search-val village/taiga/streets --search-val village/taiga/terminators --search-val village/taiga/town_centers --search-val village/taiga/zombie/streets`
            - Import all `tags/worldgen/biome` and `tags/worldgen/structure` (place at `Better_Cave_Dimensions/data/minecraft/tags/worldgen/structure`) from vanilla and replace namespace `minecraft`->`better_cave_dimensions`.
                - If referring to tags (start with `#`), also put related tags in `better_cave_dimensions` namespace
                    - `dolphin_located.json`: Only contains tags (`ocean_ruin` and `shipwreck`). Copy `ocean_ruin.json` and `shipwreck.json` to `better_cave_dimensions` namespace.
                - If related to vanilla behaviour (e.g. `allows_surface_slime_spawns`), move to `minecraft` namespace
                    - But if it is also used by other tags (e.g. `is_ocean`), do not remove from `better_cave_dimensions` namespace
                        - Should check the "chain"
                        - e.g. `is_badlands` is referred by `spawns_warm_variant_farm_animals` and `spawns_warm_variant_frogs` and these "upper" tags only change vanilla behaviour. If these two "upper" tags are the only tags that refer to `is_badlands`, all three tags should be moved to `minecraft` namespace. However, the other two "upper" tags `has_structure/mineshaft_mesa` and `has_structure/ruined_portal_mountain` control the biomes that the two structures can appear in in `better_cave_dimensions:cave`. Eventually, `is_badlands` is copied to `minecraft` namespace, not to be moved to.
            - Import all `worldgen/structure` and `worldgen/structure_set` from vanilla (do not overwrite existing files). If leave ones un-imported, those structures will not generate in this dimension.
            - In `worldgen/structure`
                - Replace namespace `minecraft`->`better_cave_dimensions` in `$.biomes`.
                - If `$.start_pool` exists:
                    - Replace namespace `minecraft`->`better_cave_dimensions` if the file `worldgen/template_pool/<string>.json` exists after removing `minecraft:` at the beginning
                        - Example: pillager_outpost.json: `$.start_pool`=`minecraft:pillager_outpost/base_plates`, `worldgen/template_pool/pillager_outpost/base_plates.json` exists, then replace with `better_cave_dimensions:pillager_outpost/base_plates`.
                - Adjust `terrain_adaptation`
                    - none: nether_fossil
                    - beard_box: bastion_remnant, desert_pyramid, fortress, igloo, pillager_outpost, village_*
                - Adjust `step` (change priority of generation)
                    - top_layer_modification: mineshaft, mineshaft_mesa
                - Remove `project_start_to_heightmap`
                - Adjust `start_height`
                    - Recommended setting:
                        ```
                        "start_height": {
                          "type": "minecraft:uniform",
                          "min_inclusive": {
                            "absolute": -32
                          },
                          "max_inclusive": {
                            "absolute": 80
                          }
                        }
                        ```
                - Ruined portals (ruined_portal.json): `$.setups[0].placement`=`underground` (except nether) and delete `$.setups[1]`
            - In `worldgen/structure_set`
                - Replace namespace `minecraft`->`better_cave_dimensions` in `$.structures[*].structure`, `$.placement.exclusion_zone.other_set` and `$.placement.preferred_biomes`.

---

## Bug Fix

- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))
- [x] Throwing eye of ender causes server crash due to unable to find anywhere

---

## AI/LLM/Agent Usage

Open mind: AI commits/bug fixes are welcome, but please ensure that the code is thoroughly reviewed and tested before merging. The goal is to maintain a high standard of quality and reliability in the codebase.

---

## License

This data pack is licensed under the MIT License. See the LICENSE file for more details.

---
---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
