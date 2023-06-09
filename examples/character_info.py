from pathlib import Path

from starrailres import (
    CharacterBasicInfo,
    Index,
    LevelInfo,
    LightConeBasicInfo,
    RelicBasicInfo,
    SubAffixBasicInfo,
)

# replace with index folder
index = Index(Path("index") / "en")

basic_light_cone = LightConeBasicInfo(id="23001", rank=1, level=70, promotion=5)
basic_relics = [
    RelicBasicInfo(
        id="61081",
        level=12,
        main_affix_id="1",
        sub_affix_info=[
            SubAffixBasicInfo(id="2", cnt=3, step=1),
            SubAffixBasicInfo(id="3", cnt=1, step=0),
            SubAffixBasicInfo(id="6", cnt=3, step=3),
            SubAffixBasicInfo(id="9", cnt=1, step=2),
        ],
    ),
    RelicBasicInfo(
        id="61082",
        level=13,
        main_affix_id="1",
        sub_affix_info=[
            SubAffixBasicInfo(id="5", cnt=2, step=4),
            SubAffixBasicInfo(id="6", cnt=1, step=1),
            SubAffixBasicInfo(id="7", cnt=1, step=2),
            SubAffixBasicInfo(id="10", cnt=3, step=2),
        ],
    ),
    RelicBasicInfo(
        id="61083",
        level=15,
        main_affix_id="4",
        sub_affix_info=[
            SubAffixBasicInfo(id="3", cnt=3, step=4),
            SubAffixBasicInfo(id="4", cnt=1, step=1),
            SubAffixBasicInfo(id="10", cnt=3, step=2),
            SubAffixBasicInfo(id="12", cnt=1, step=0),
        ],
    ),
    RelicBasicInfo(
        id="61084",
        level=12,
        main_affix_id="4",
        sub_affix_info=[
            SubAffixBasicInfo(id="2", cnt=2, step=4),
            SubAffixBasicInfo(id="3", cnt=3, step=5),
            SubAffixBasicInfo(id="9", cnt=1),
            SubAffixBasicInfo(id="10", cnt=1, step=2),
        ],
    ),
    RelicBasicInfo(
        id="63065",
        level=15,
        main_affix_id="9",
        sub_affix_info=[
            SubAffixBasicInfo(id="2", cnt=2, step=1),
            SubAffixBasicInfo(id="5", cnt=2, step=1),
            SubAffixBasicInfo(id="6", cnt=3, step=2),
            SubAffixBasicInfo(id="10", cnt=2),
        ],
    ),
    RelicBasicInfo(
        id="63066",
        level=12,
        main_affix_id="4",
        sub_affix_info=[
            SubAffixBasicInfo(id="1", cnt=1, step=1),
            SubAffixBasicInfo(id="2", cnt=2, step=2),
            SubAffixBasicInfo(id="8", cnt=3, step=2),
            SubAffixBasicInfo(id="10", cnt=2, step=2),
        ],
    ),
]

basic = CharacterBasicInfo(
    id="1102",
    rank=0,
    level=70,
    promotion=5,
    skill_tree_levels=[
        LevelInfo(id="1102001", level=2),
        LevelInfo(id="1102002", level=5),
        LevelInfo(id="1102003", level=6),
        LevelInfo(id="1102004", level=5),
        LevelInfo(id="1102007", level=1),
        LevelInfo(id="1102101", level=1),
        LevelInfo(id="1102102", level=1),
        LevelInfo(id="1102201", level=1),
        LevelInfo(id="1102202", level=1),
    ],
    light_cone=basic_light_cone,
    relics=basic_relics,
)

character = index.get_character_info(basic)

# export json
if character:
    from msgspec.json import encode

    print(encode(character).decode())


# # export dict
# if character:
#     from msgspec import to_builtins

#     print(to_builtins(character))
