# Better Cave Worlds Updated

This is an unofficial fork of [klinbee/Better-Cave-Worlds](https://github.com/klinbee/Better-Cave-Worlds) to support newer Minecraft versions, as the original author [klinbee](https://github.com/klinbee) stopped maintaining since Oct 18, 2025. ([last commit](https://github.com/klinbee/Better-Cave-Worlds/commit/cd8e17e98e29c024fc554cecf6763d1b8783f1c3))

Tools used:
- [Data Pack Generators - Versions Explorer](https://misode.github.io/versions/): Compare datapack structure and check for breaking changes among versions
- [Minecraft wiki: Tutorial:Running the data generator](https://minecraft.wiki/w/Tutorial:Running_the_data_generator):
    - command: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports`
    - Generate server-side datapack structure
        - `The contents of the vanilla data pack (except "pack.mcmeta") will be generated to "generated" directory in the run directory of the command line interface.`
    - Generate `data/minecraft/dimension/overworld.json` (datapack path) from hardcoded dimension definition (places in `./generated/reports/biome_parameters/minecraft`). More useful for [Better-Cave-Dimensions](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/main).
- [minecraft-server-jar-downloads.md](https://gist.github.com/cliffano/77a982a7503669c3e1acb0a0cf6127e9#file-minecraft-server-jar-downloads-md): Quick links for server.jar

<details>
<summary>Changes that are needed to adapt:</summary>

- 1.21.11:
    - [25w42a](https://misode.github.io/versions/?id=25w42a):
        - Pack format version: 90.0, [90, 0]
        - [dimension] [breaking] Many dimension type fields have been migrated to Environment Attributes: `ultrawarm`, `bed_works`, `respawn_anchor_works`, `cloud_height`, `piglin_safe`, and `has_raids`.
        - [dimension] The dimension type `natural` field has not been removed but its functionality has been migrated to `gameplay/nether_portal_spawns_piglin` Environment Attribute.
        - See [Dimension type](https://minecraft.wiki/w/Dimension_type#History), [Environment attribute](https://minecraft.wiki/w/Environment_attribute)
    - [25w45a](https://misode.github.io/versions/?id=25w45a):
        - Pack format version: 93.0, [93, 0]
        - [dimension] Added optional `timelines` field to dimension types to specify which timelines are active. Format: timeline ID, list of timeline IDs, or timeline tag.
        - See [Timeline](https://minecraft.wiki/w/Timeline)
</details>

Want an independent cave dimension (1.21.4+)? Check my another fork/branch [Better-Cave-Dimensions](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/main)

---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
