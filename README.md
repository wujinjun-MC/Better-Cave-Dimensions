# Better Cave Worlds Updated

**EN** | [简体中文](./README.zh_hans.md)

This is an unofficial fork of [klinbee/Better-Cave-Worlds](https://github.com/klinbee/Better-Cave-Worlds) to support newer Minecraft versions, as the original author [klinbee](https://github.com/klinbee) stopped maintaining since Oct 18, 2025. ([last commit](https://github.com/klinbee/Better-Cave-Worlds/commit/cd8e17e98e29c024fc554cecf6763d1b8783f1c3))

Also see README for Modrinth ([EN](https://modrinth.com/datapack/better-cave-worlds-updated) | [简体中文](./README-modrinth.zh_hans.md))

## Install

See [Modrinth](https://modrinth.com/datapack/better-cave-worlds-updated)

## Developer

### AI Policy

See [docs/AI_policy](docs/AI_policy.md)

### Tools Used

- [Data Pack Generators - Versions Explorer](https://misode.github.io/versions/): Compare datapack structure and check for breaking changes among versions
- [Minecraft Assets Explorer](https://mcasset.cloud/): Compare file in vanilla datapack between two versions side by side.
    - Example: [1.21.10 vs. 1.21.11 data/minecraft/dimension_type/overworld.json](https://mcasset.cloud/1.21.11...1.21.10/data/minecraft/dimension_type/overworld.json)
- [Minecraft wiki: Tutorial:Running the data generator](https://minecraft.wiki/w/Tutorial:Running_the_data_generator):
    - command: `java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --reports`
    - Generate server-side datapack structure
        - `The contents of the vanilla data pack (except "pack.mcmeta") will be generated to "generated" directory in the run directory of the command line interface.`
    - Generate `data/minecraft/dimension/overworld.json` (datapack path) from hardcoded dimension definition (places in `./generated/reports/biome_parameters/minecraft`). More useful for [Better-Cave-Dimensions](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later).
- [minecraft-server-jar-downloads.md](https://gist.github.com/cliffano/77a982a7503669c3e1acb0a0cf6127e9#file-minecraft-server-jar-downloads-md): Quick links for server.jar
- [How to Upgrade Datapacks (Youtube playlist)](https://www.youtube.com/playlist?list=PLgbPk8f9bw9rtYmnIpcd0__q9cjVqmx1l): Breaking changes and how to solve
    - [1.21.11](https://www.youtube.com/watch?v=9QuRZOP3Gcw)
    - [26.1.x](https://www.youtube.com/watch?v=4FFFRFIyqIs)
    - [26.2](https://www.youtube.com/watch?v=k53YFmA8Oe0)
    - [Tutorial files](https://drive.google.com/drive/folders/17h79rkR0QulQbeR--SPpC5So3vAU_1ga)
- [Blockbench](https://blockbench.net/): Make .bbmodel model file for the icon
    - Used plugin:
        - [Minecraft Title Generator](https://www.blockbench.net/plugins/minecraft_title_generator)

### Development details

For how I update to support new Minecraft versions: See [docs/Updating_to_modern_Minecraft_version](docs/Updating_to_modern_Minecraft_version.md)

---

Want an independent cave dimension? Check my `Better Cave Dimensions` ([1.21.4~1.21.8](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy) or [26.2+](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later)).

---

↓ Original README

# Better Cave Worlds / Chaotic Caverns World
 Data Pack that generates the overworld as caves, with proper features and some structures.
