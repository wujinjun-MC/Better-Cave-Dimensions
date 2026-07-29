# Better Cave Worlds Updated

This is an unofficial fork of [klinbee/Better-Cave-Worlds](https://github.com/klinbee/Better-Cave-Worlds) to support newer Minecraft versions, as the original author [klinbee](https://github.com/klinbee) stopped maintaining since Oct 18, 2025. ([last commit](https://github.com/klinbee/Better-Cave-Worlds/commit/cd8e17e98e29c024fc554cecf6763d1b8783f1c3))

AI / LLM is not used in datapack development (for best precision and accuracy) but may be used in README/icon/other assets generation.

Install: [Modrinth](https://modrinth.com/datapack/better-cave-worlds-updated)

Tools used:
- [Data Pack Generators - Versions Explorer](https://misode.github.io/versions/): Compare datapack structure and check for breaking changes among versions
- [Minecraft Assets Explorer](https://mcasset.cloud/): Compare file in vanilla datapack between two versions side by side.
    - Example: [1.21.10 vs. 1.21.11 data/minecraft/dimension_type/overworld.json](https://mcasset.cloud/1.21.11...1.21.10/data/minecraft/dimension_type/overworld.json)
- [Minecraft wiki: Tutorial:Running the data generator](https://minecraft.wiki/w/Tutorial:Running_the_data_generator):
    - command: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports`
    - Generate server-side datapack structure
        - `The contents of the vanilla data pack (except "pack.mcmeta") will be generated to "generated" directory in the run directory of the command line interface.`
    - Generate `data/minecraft/dimension/overworld.json` (datapack path) from hardcoded dimension definition (places in `./generated/reports/biome_parameters/minecraft`). More useful for [Better-Cave-Dimensions](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/main).
- [minecraft-server-jar-downloads.md](https://gist.github.com/cliffano/77a982a7503669c3e1acb0a0cf6127e9#file-minecraft-server-jar-downloads-md): Quick links for server.jar
- [How to Upgrade Datapacks (Youtube playlist)](https://www.youtube.com/playlist?list=PLgbPk8f9bw9rtYmnIpcd0__q9cjVqmx1l): Breaking changes and how to solve
    - [1.21.11](https://www.youtube.com/watch?v=9QuRZOP3Gcw)
    - [26.1.x](https://www.youtube.com/watch?v=4FFFRFIyqIs)
    - [26.2](https://www.youtube.com/watch?v=k53YFmA8Oe0)
    - [Tutorial files](https://drive.google.com/drive/folders/17h79rkR0QulQbeR--SPpC5So3vAU_1ga)

<details>
<summary>Changes that are needed to adapt:</summary>

- [1.21.11](https://misode.github.io/versions/?id=1.21.11&tab=changelog):
    - [25w42a](https://misode.github.io/versions/?id=25w42a):
        - Pack format version: 90.0, [90, 0]
        - [dimension] [breaking] Many dimension type fields have been migrated to Environment Attributes: `ultrawarm`, `bed_works`, `respawn_anchor_works`, `cloud_height`, `piglin_safe`, and `has_raids`.
        - [dimension] The dimension type `natural` field has not been removed but its functionality has been migrated to `gameplay/nether_portal_spawns_piglin` Environment Attribute.
        - See [Dimension type](https://minecraft.wiki/w/Dimension_type#History), [Environment attribute](https://minecraft.wiki/w/Environment_attribute)
    - [25w45a](https://misode.github.io/versions/?id=25w45a):
        - Pack format version: 93.0, [93, 0]
        - [dimension] Added optional `timelines` field to dimension types to specify which timelines are active. Format: timeline ID, list of timeline IDs, or timeline tag.
        - See [Timeline](https://minecraft.wiki/w/Timeline)
- [26.1](https://misode.github.io/versions/?id=26.1&tab=changelog):
    - [snapshot-1](https://misode.github.io/versions/?id=26.1-snapshot-1):
        - Pack format version: 95.0, [95, 0]
        - [environment-attribute] Added `visual/ambient_light_color` attribute to define both the ambient light tint and brightness. Default values: Overworld `#0A0A0A`, ...
    - [snapshot-3](https://misode.github.io/versions/?id=26.1-snapshot-3):
        - Pack format version: 97.0, [97, 0]
        - [dimension] Added `default_clock` field to dimension types. This optional field specifies the default clock that will be used for the `/time` command.
    - [snapshot-6](https://misode.github.io/versions/?id=26.1-snapshot-6):
        - Pack format version: 99.0, [99, 0]
        - [dimension] Added `has_ender_dragon_fight` boolean field to dimension types. Controls whether it is possible for an ender dragon fight to exist in the dimension.
        - [worldgen] [breaking] `forest_rock` feature has been renamed to `block_blob`.
            - However there is no change in `data/minecraft/worldgen/placed_feature/forest_rock.json` comparing versions before and after. Ignore.
        - [worldgen] [breaking] `ice_spike` feature has been renamed to `spike`.
            - However there is no change in `data/minecraft/worldgen/placed_feature/ice_spike.json` comparing versions before and after. Ignore.
    - [pre-1](https://misode.github.io/versions/?id=26.1-pre-1):
        - Pack format version: 101.0, [101, 0]
        - [worldgen] [breaking] Removed the `flower`, `flower_no_bonemeal`, and `random_patch` feature types
            - Instead, patches can be expressed as a sequence of `count` and `random_offset` placement modifiers
            - Affected:
                - `data/minecraft/worldgen/placed_feature`: `sea_pickle.json`, `seagrass_cold.json`, `seagrass_deep_cold.json`, `seagrass_deep_warm.json`, `seagrass_deep.json`, `seagrass_normal.json`, `seagrass_river.json`, `seagrass_swamp.json`, `seagrass_warm.json`:
                	- "tries" is now a "minecraft:count" placement setting
                    - "xz_spread" and "y_spread" are now a single "random_offset" placement setting, using "trapezoid" number providers
                    - "config.feature.placement" is now merged with "placement" in the placed_feature
                - `data/minecraft/worldgen/configured_feature`: `sea_pickle.json`, `seagrass_mid.json`, `seagrass_short.json`, `seagrass_slightly_less_short.json`, `seagrass_tall.json`:
                    - The configured feature itself (the entire file) should now be what was previously under ".config.feature.feature"
                - Any other `data/minecraft/worldgen/placed_feature`s that reference affected `configured_feature`s: Modify `.feature` string to match new name + merge `tries` and `*_spread`
    - [others](https://misode.github.io/versions/?id=26.1-undefined) (not mentioned in Versions Explorer):
        - Pack format version: ?.0, [?, 0] (Surely 94.1~101.1)
        - `data/minecraft/worldgen/placed_feature`: `.placement.predicate.type` `minecraft:matching_blocks`->`minecraft:matching_block_tag`, with `.placement.predicate.blocks`->`.placement.predicate.tag`. Affected: `grass_bonemeal.json`
        - `data/minecraft/worldgen/noise_settings/caves.json`: `.noise_router.temperature` and `.noise_router.vegetation` are set to 0.0 instead of generating via `minecraft:shifted_noise`.
            - However, this will eliminate some biomes including `minecraft:cold_ocean`. Ignore.
    - Notes:
        - Hardest version advancement (spent longest time to support this version)
        - In `data/minecraft/worldgen/placed_feature` and `data/overlay_*/worldgen/placed_feature` there are some JSONs that have no diff compared to vanilla, PLEASE CONSIDER REMOVING THEM FOR BETTER MAINTAINABILITY !!!
            - Including but not limited to: `flower_plain.json`, `grass_bonemeal.json`, some `patch_*.json`
- [26.2](https://misode.github.io/versions/?id=26.2&tab=changelog):
    - [others](https://misode.github.io/versions/?id=26.2-undefined) (not mentioned in Versions Explorer):
        - Pack format version: ?.0, [?, 0] (Surely 101.1~107.1)
        - `data/minecraft/worldgen`:
            - When removing the `flower` feature types, `placed_feature`s (`flower_default.json` and `flower_warm.json`) are affected by `configured_feature`s but (Mojang) forgot to modify. Now they are added to 26.2 support (overlay_26_2) to fix, but will not be added to 26.1 support (overlay_26_1), to match vanilla functionality.
            - Remove `.placement.noise_offset` in `placed_feature`s: `kelp_cold.json`, `kelp_warm.json`, `warm_ocean_vegetation.json`
            - `density_function/overworld/final_density.json`: Sync `data/minecraft/worldgen/noise_settings/caves.json` `.noise_router.final_density.argument` changes (before: outer is `type=minecraft:mul`, `type=minecraft:interpolated` is under an `argument`; after: swapped)
            - `data/minecraft/worldgen/noise_settings/overworld.json`:
                - Add support for sulfur caves
                - For `type=minecraft:biome` condition, if `biome_is` only contain one value, directly `biome_is=""` instead of `biome_is=[""]`
                    - Example: `"biome_is": ["minecraft:wooded_badlands"]` -> `"biome_is": "minecraft:wooded_badlands"`
- Original author (klinbee) forgot to adapt to old updates
    - Some `placed_feature`s contain `{"type": "minecraft:in_square"}, {"type": "minecraft:heightmap", "heightmap": "*"}` in `.placement`. Must be replaced by `{"type": "minecraft:count_on_every_layer", "count": * (default =1)}` or the feature will not be placed.
        - List:
            - 1.20.1 (datapack base/minimum version)
            - 1.21.5
                - [patch_bush.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_bush.json)
                - [patch_dry_grass_badlands.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_dry_grass_badlands.json)
                - [patch_dry_grass_desert.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_dry_grass_desert.json)
                - [patch_firefly_bush_near_water.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_firefly_bush_near_water.json)
                - [patch_firefly_bush_near_water_swamp.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_firefly_bush_near_water_swamp.json)
                - [patch_firefly_bush_swamp.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_firefly_bush_swamp.json)
                - [patch_grass_meadow.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_grass_meadow.json)
                - [patch_leaf_litter.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/patch_leaf_litter.json)
                - [wildflowers_birch_forest.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/wildflowers_birch_forest.json)
                - [wildflowers_meadow.json](https://mcasset.cloud/1.21.5...1.21.4/data/minecraft/worldgen/placed_feature/wildflowers_meadow.json)
        - In `26.1-pre-1` files are changed because of feature types removal, but were not tracked without re-check due to non existence!
</details>

Want an independent cave dimension? Check my `Better Cave Dimensions` ([1.21.4~1.21.8](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy) or [26.2+](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later)).

---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
