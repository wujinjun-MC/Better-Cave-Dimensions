# Description
An unofficial fork that turns it into a standalone dimension so that overworld is not affected.

Height extends to -128~256

May only support 1.21.4+

# FAQ

1. > This branch is _ commits ahead of, _ commits behind `klinbee/Better-Cave-Worlds:main`

    - Don't worry. "Sync fork" can not be used due to different path, but I track upstream changes and apply to correct files.

2. How to enter this dimension?
    - Vanilla: `/execute in better_cave_dimensions:cave tp 0 256 0`
    - With Multiverse plugin: `/mv tp world_better_cave_dimensions_cave`

# Goals
- Structure fix:
    - Full generation:
        - [x] Pillager outpost
        - Villages
            - [x] Desert
            - [x] Plains
            - [x] Savanna
            - [x] Snowy
            - [x] Taiga
- [x] Support other vanilla structures
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
    - [x] Ocean Monument (May not be placed. Don't use "/locate structure" to find, or your game/server will be crashed)
    - [x] Ocean Ruins [^2]
    - [x] Shipwreck [^2]
    - [x] Stronghold
    - [x] Swamp Hut [^2]
    - [x] Trial Chambers
    - [x] Woodland Mansion [^2]
- Support third-party structure datapacks:
    - [x] [Dungeons and Taverns(DnT)](https://modrinth.com/user/NovaWostra)
        - Full support:
            - [x] [Main](https://modrinth.com/datapack/dungeons-and-taverns)
            - [x] [Ancient City Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-ancient-city-overhaul)
            - [x] [Desert Temple Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-desert-temple-overhaul)
            - [x] [End Castle Standalone](https://modrinth.com/datapack/dungeons-and-taverns-end-castle-standalone)
            - [x] [Nether Fortress Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-nether-fortress-overhaul)
            - [x] [Pillager Outpost Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-pillager-outpost-overhaul)
            - [x] [Stronghold Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-stronghold-overhaul)
    - [x] [Explorify](https://modrinth.com/datapack/explorify)
    - [x] [Structory](https://modrinth.com/datapack/structory)
- [ ] Extend-able height (e.g. -128~512)
- [ ] Guidelines to create more cave dimensions / Cave dimension preset

[^1]: Can not be placed due to missing biomes. Use addon `Unlimited vanilla structures` can fix it.
[^2]: May break bedrock roof

# Addons
## List
<details>
<summary>Unlimited vanilla structures</summary>

- Overlay name: `overlay_addon_unlimited_vanilla_structures`
- Supported Minecraft version: 1.21.4+
- Features:
    1. Structure definition
        1. Structures can be placed in any biomes
        2. Change `terrain_adaption` to expose structures
        3. Change `spawn_overrides` to allow mob generation
        4. Change `step` (feature order) to allow some structures to override neighborhoods
        4. For structures using jigsaws
            1. Always `use_expansion_hack`
            2. Maximize `size` and `max_distance_from_center` (Requires strong CPU)
            3. Maximize `start_height` range (-32 ~ [max height -16])
                - Lowest height can not < -55, or lava-logged
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
- Supported Minecraft version: same as datapack supported version
- Features:
    1. `piglin_safe`: Piglins will not convert to zombified ones
    2. `respawn_anchor_works`
    3. `cloud_height` -> 64
    4. Enable skylight
</details>

<details>
<summary>Extend noise height range</summary>

- Overlay name: `overlay_addon_noise_height_extend`
- Supported Minecraft version: same as datapack supported version
- Features:
    1. Terrain noise height range syncs with dimension height range (aka. no building space above bedrock roof)
    2. Without cave height range configuration, there may be only lava lakes in y 128~256
    3. (Recommend) enable `overlay_addon_unlimited_vanilla_structures` and/or `overlay_addon_compact_*_larger`, since original height range doesn't allow structure placement in y 128~256.
- Side effects:
    - Some structures can only be placed on bedrock roof. After enabling, they are not placed correctly
</details>

<details>
<summary>Configurable cave</summary>

- Overlay name: `overlay_addon_custom_cave_config`
- Supported Minecraft version: same as datapack supported version
- Features:
    1. Customize cave generation, including height range and density!
- Config:
    - Path: `overlay_addon_custom_cave_config/data/better_cave_dimensions/worldgen/density_function/cave/final_density.json`
    - Json path:
        - Cave bottom: `input`.`argument`.`argument2`.`argument`.`argument`.`argument2`.`argument1` (line 20~26)
        - Cave main: `input`.`argument`.`argument2`.`argument`.`argument`.`argument2`.`argument2`.`argument2`.`argument2`.`argument1` (line 35~41)
    - Definition:
        - `from_y` and `to_y`: Cave roof/base height range
            - `from_y` < `to_y`
            - Must be in range of noise height range
                - `to_y` <= 128, or
                - `to_y` <= 256 (with `overlay_addon_noise_height_extend`)
            - Suggestion: `cave_bottom`.`to_y` >= -50, to avoid hard-coded lava layer
        - `to_value` (for cave bottom, > `from_value`) and `from_value` (for cave main, < `to_value`): Control cave density
            - Higher value -> Lower density
            - \> 1: Unexpected behavior, including: bedrock roof breaker, infinite lava ocean
            - If value is too low, noise caves(like underground vanilla caves) still generate
    - Default tweaks:
        - Cave main: `from_y` = 224, `to_y` = 256 -- more space to survive!
    - Sometimes world can be chaotic!
        - e.g. `to_y` > [noise height range] -> bedrock roof breaker
            <details>
            <summary>Images: Bedrock roof breaker</summary>

            ![bedrock-roof-breaker-1](assets/images/overlay_addon_custom_cave_config/bedrock-roof-breaker-1.png)
            ![bedrock-roof-breaker-2](assets/images/overlay_addon_custom_cave_config/bedrock-roof-breaker-2.png)
            ![bedrock-roof-breaker-3](assets/images/overlay_addon_custom_cave_config/bedrock-roof-breaker-3.png)
            </details>
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

<details>
<summary>Dungeons and Taverns compat</summary>

- Overlay name: `overlay_addon_compact_dnt`
- Supported Minecraft version: Unknown(latest?)
- Features:
    1. Fix partial generation, but affects generation in other dimensions. (data/\*/worldgen/template_pool/\*\* - all .json, `elements`.*.`element`.`projection`: terrain_matching -> rigid)
    2. structure definition or structure set may use ones from DnT to make sure provided strucutres can be placed or for better placement
- Notice:
    1. May change generation in other dimensions
    2. This addon can be removed due to license(strict license or ARR)
    3. To fully function, this datapack must take priority (load after `DnT`). In singleplayer, select `DnT`s first and select this; In dedicated server, add `DnT`, start and stop server, then add this. Make sure the name appears after `DnT`'s in `/datapack list`
    4. The namespace of structures spawning in this dimension is `better_cave_dimensions`, not `nova_structures`
    5. All DnT packs listed in "Goals" must be loaded successfully
</details>

<details>
<summary>Dungeons and Taverns compat - larger structures</summary>

- Overlay name: `overlay_addon_compact_dnt_larger`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_dnt`
- Recommend: `overlay_addon_unlimited_vanilla_structures`(Because some DnT structures replace vanilla ones)
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Change/Optimize `size`
            - Normally size will be doubled/maximized
            - Cannot change all sizes (crash)
            - Some structures don't have enough parts to enlarge. Lower sizes can gain performance benefit (~20%)
        - Chunk generation may take a long time due to large structures
            - Suggestion:
                - If add dp for the 1st time: Don't enable this addon until "Preparing spawn area" completes
                - Use chunk pregeneration tool like "Chunky"
</details>

<details>
<summary>Dungeons and Taverns compat - high density</summary>

- Overlay name: `overlay_addon_compact_dnt_high_density`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_dnt`
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Structure set `spacing`:
            - if spacing > 50: -> max(50,min(100,half_spacing))
            - if spacing <= 50: unchanged
        - Chunk generation may take a long time due to large structures
            - Suggestion: see suggestion in `Dungeons and Taverns compat - larger structures`
</details>

<details>
<summary>Explorify compat</summary>

- Overlay name: `overlay_addon_compact_explorify`
- Supported Minecraft version: Unknown(latest?)
- Features:
    1. Fix particial generation
    2. structure definition or structure set may use ones from Explorify to make sure provided strucutres can be placed or for better placement
- Notice:
    1. May change generation in other dimensions
    2. This addon can be removed due to license(strict license or ARR)
    3. To fully function, this datapack must take priority (load after `Explorify`). In singleplayer, select `Explorify` first and select this; In dedicated server, add `Explorify`, start and stop server, then add this. Make sure the name appears after `Explorify`'s in `/datapack list`
    4. The namespace of structures spawning in this dimension is `better_cave_dimensions`, not `nova_structures`
</details>

<details>
<summary>Explorify compat - larger structures</summary>

- Overlay name: `overlay_addon_compact_explorify_larger`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_explorify`
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Change/Optimize `size`
            - Normally size will be doubled/maximized
            - Cannot change all sizes (crash)
            - Some structures don't have enough parts to enlarge. Lower sizes can gain performance benefit (~20%)
        - Chunk generation may take a long time due to large structures
            - Suggestion: see suggestion in `Dungeons and Taverns compat - larger structures`
</details>

<details>
<summary>Explorify compat - high density</summary>

- Overlay name: `overlay_addon_compact_explorify_high_density`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_explorify`
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Structure set `spacing` -> 1/2
        - Chunk generation may take a long time due to large structures
            - Suggestion: see suggestion in `Dungeons and Taverns compat - larger structures`
</details>

<details>
<summary>Structory compat</summary>

- Overlay name: `overlay_addon_compact_structory`
- Supported Minecraft version: Unknown(latest?)
- Features:
    1. Fix particial generation
    2. structure definition or structure set may use ones from Structory to make sure provided strucutres can be placed or for better placement
- Notice:
    1. May change generation in other dimensions
    2. This addon can be removed due to license(strict license or ARR)
    3. To fully function, this datapack must take priority (load after `Structory`). In singleplayer, select `Structory` first and select this; In dedicated server, add `Structory`, start and stop server, then add this. Make sure the name appears after `Structory`'s in `/datapack list`
    4. The namespace of structures spawning in this dimension is `better_cave_dimensions`, not `nova_structures`
</details>
<details>
<summary>Structory compat - larger structures</summary>

- Overlay name: `overlay_addon_compact_structory_larger`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_structory`
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Change/Optimize `size`
            - Normally size will be doubled/maximized
            - Cannot change all sizes (crash)
            - Some structures don't have enough parts to enlarge. Lower sizes can gain performance benefit (~20%)
        - Chunk generation may take a long time due to large structures
            - Suggestion: see suggestion in `Dungeons and Taverns compat - larger structures`
</details>
<details>
<summary>Structory compat - high density</summary>

- Overlay name: `overlay_addon_compact_structory_high_density`
- Supported Minecraft version: Unknown(latest?)
- Dependencies: `overlay_addon_compact_structory`
- Features:
    1. Unlock structure limits like "Unlimited vanilla structures"
        - Structure set `spacing` -> 1/2
        - Chunk generation may take a long time due to large structures
            - Suggestion: see suggestion in `Dungeons and Taverns compat - larger structures`
</details>

## How to enable addon
1. Open `pack.mcmeta`
2. Use `Ctrl+F` to search "Overlay name"
3. Change `formats` range to 1~999 ("formats": [1, 999],)

# Bug Fix
- [x] Some biomes are missing ([Upstream issue #9](https://github.com/klinbee/Better-Cave-Worlds/issues/9)) (Fixed by [my PR](https://github.com/klinbee/Better-Cave-Worlds/pull/10#event-19395656866))
- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))
- [x] DnT's template pool missing (DnT's bug) (`[WARN]: Empty or non-existent pool: nova_structures:pale_residence/resi_window_slim_right` (or left))

↓ Original README:

># Better Cave Worlds / Chaotic Caverns World
> Data Pack that generates the overworld as caves, with proper features and some structures.
