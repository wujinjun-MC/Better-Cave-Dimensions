# Better Cave Worlds

EN | [简体中文 (TODO)](https://github.com/wujinjun-MC/Better-Cave-Dimensions/blob/Better-Cave-Worlds-updated/README-modrinth.md)

## THIS IS A FORK

This is a fork of the datapack [Better Cave Worlds](https://modrinth.com/datapack/better-cave-worlds) ([Github repo](https://github.com/klinbee/Better-Cave-Worlds)), it exist because the original developer doesn't actively maintain and and newer Minecraft versions introduced multiple datapack breaking changes.

This fork exists to keep the project alive by:
- updating it for new Minecraft releases
- fixing broken world generation caused by Mojang changes
- maintaining compatibility going forward
- fixing bugs
- accepting contributes from issues and pull requests

For developers/contributors, see README on Github ([En](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Worlds-updated) | [简体中文 (TODO)](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Worlds-updated))

<details>
<summary>A little story</summary>

Previously I deeply involved in my derivative, Better Cave Dimensions (for [26.2](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-26.2_or_later) (may also publish to Modrinth later) or [1.21.4~1.21.8](https://github.com/wujinjun-MC/Better-Cave-Dimensions/tree/Better-Cave-Dimensions-legacy)), and had a joyful experience in Singleplayer and with fellows/friends in `1A1S SMP`. Because development by the original creators has ceased, other players who love this project—myself included—are forced to remain on old Minecraft version. With no one in the player community maintaining the project, I believe it is time to bring the datapack to the latest Minecraft releases.

Update [20260815]: The "Better Cave Dimensions" for 26.2 or later is stable now (It will turn this datapack into a standalone dimension so that the overworld is not affected). Currently it is only available on [Github Releases](https://github.com/wujinjun-MC/Better-Cave-Dimensions/releases) and will publish to Modrinth later.

Update [20260816]: The "1A1S SMP" is revived now with "Better Cave Dimensions" installed. You may test it in the server.
- server ip: lightseeking.eu.org
- to enter the dimension: `/mvtp world_better_cave_dimensions_cave` or through the "portal"

</details>

---

## Original Description

This is Datapack enables Cave World generation with biomes and allows foliage, aquifers, and large ore veins to generate. Unfortunately, you cannot change the height at which most structures generate with a datapack, so most of them generate on the bedrock roof. You should still be able to do everything you normally could, but it will be a challenge to do so!

### Generation Notes

- The following structures generate on/near the roof:
    - Buried Treasure
    - Desert Pyramids
    - Igloos
    - Jungle Pyramids
    - Mansions
    - Ocean Ruins
    - Shipwrecks
    - Witch Huts
- Passive Mobs obey [vanilla spawning rules](https://minecraft.wiki/w/Mob_spawning):
    - They require high light-levels to spawn, meaning only near light sources (lava or glowberries) on worldgen
        - Also, from structures like underground village animal pens
    - They can also spawn naturally, but there is a creature mob cap of 10, which means that you need to have very few creatures loaded (keep spawn chunks in mind! and understand mob categories from the Wiki as well) and also light levels, and additional spawn mechanics you will need to research in rare cases
- Snow top layers are hardcoded to generate on the surface, so won't generate underground
