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
- [ ] Support other vanilla structures
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

## Bug Fix
- [x] Some biomes are missing ([Upstream issue #9](https://github.com/klinbee/Better-Cave-Worlds/issues/9)) (Fixed by [my PR](https://github.com/klinbee/Better-Cave-Worlds/pull/10#event-19395656866))
- [ ] Some terrain generation can break bedrock roof (e.g. Cold biomes (bedrocks are replaced by snow blocks))

↓ Original README:

># Better Cave Worlds / Chaotic Caverns World
> Data Pack that generates the overworld as caves, with proper features and some structures.
