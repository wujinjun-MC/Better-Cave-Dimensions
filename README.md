# Description
An unofficial fork that turns it into a standalone dimension so that overworld is not affected.

Height extends to -128~256

May only support 1.21.4+

WIP.

## Goals
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
    - [x] Bastion Remnant (Can not be placed due to missing biomes)
    - [x] Buried Treasure (May break bedrock roof)
    - [x] Desert Pyramid (May break bedrock roof)
    - [x] End City (Can not be placed due to missing biomes)
    - [x] Igloo (May break bedrock roof)
    - [x] Jungle Pyramid (May break bedrock roof)
    - [x] Mineshaft
    - [x] Nether Fortress (Can not be placed due to missing biomes)
    - [x] Nether Fossil (Can not be placed due to missing biomes)
    - [x] Ocean Monument (May not be placed. Don't use "/locate structure" to find, or your game/server will be crashed)
    - [x] Ocean Ruins (May break bedrock roof)
    - [x] Shipwreck (May break bedrock roof)
    - [x] Stronghold
    - [x] Swamp Hut (May break bedrock roof)
    - [x] Trial Chambers
    - [x] Woodland Mansion (May break bedrock roof)
- Support third-party structure datapacks:
    - [Dungeons and Taverns(DnT)](https://modrinth.com/user/NovaWostra)
        - [ ] [Main](https://modrinth.com/datapack/dungeons-and-taverns)
        - [ ] [Ancient City Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-ancient-city-overhaul)
        - [ ] [Desert Temple Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-desert-temple-overhaul)
        - [ ] [End Castle Standalone](https://modrinth.com/datapack/dungeons-and-taverns-end-castle-standalone)
        - [ ] [Nether Fortress Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-nether-fortress-overhaul)
        - [ ] [Pillager Outpost Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-pillager-outpost-overhaul)
        - [ ] [Stronghold Overhaul](https://modrinth.com/datapack/dungeons-and-taverns-stronghold-overhaul)
        - [ ] [Woodland Mansion Replacement](https://modrinth.com/datapack/dungeons-and-taverns-woodland-mansion-replacement)
    - [ ] [Explorify](https://modrinth.com/datapack/explorify)
    - [ ] [Structory](https://modrinth.com/datapack/structory)
- [ ] Extend-able height (e.g. -128~512)
- [ ] Guidelines to create more cave dimensions / Cave dimension preset

## Addons
### List
<details>
<summary>Unlimited vanilla structures</summary>

- Overlay name: `overlay_addon_unlimited_vanilla_structures`
- Supported Minecraft version: 1.21+ (or same as datapack supported version if `trial_chambers.json` are removed in overlay folder)
- Features:
    1. Structure definition
        1. Structures can be placed in any biomes
        2. Change `terrain_adaption` to expose structures
        3. Change `spawn_overrides` to allow mob generation
        4. Change `step` (feature order) to allow some structures to override neighborhoods
        4. For structures using jigsaws
            1. Always `use_expansion_hack`
            2. Maximize `size` and `max_distance_from_center`
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

### How to enable addon
1. Open `pack.mcmeta`
2. Use `Ctrl+F` to search "Overlay name"
3. Change `formats` range to 1~999 ("formats": [1, 999],)


## Bug Fix
- [x] Some biomes are missing ([Upstream issue #9](https://github.com/klinbee/Better-Cave-Worlds/issues/9)) (Fixed by [my PR](https://github.com/klinbee/Better-Cave-Worlds/pull/10#event-19395656866))
- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))

↓ Original README:

># Better Cave Worlds / Chaotic Caverns World
> Data Pack that generates the overworld as caves, with proper features and some structures.
