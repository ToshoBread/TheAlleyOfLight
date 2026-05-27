define narrator = Character(None)
define customer = Character("Customer")
define regretful_writer = Character("The Regretful Writer")
define grieving_mother = Character("The Grieving Mother")
define mirror_man = Character("The Mirror Man")

default mc_name = "???"
default mc = Character("???")

image aine = "images/Assets/players/aine_1.png"
image lucian = "images/Assets/players/lucian_1.png"
image aine_select = "images/Assets/players/aine_1.png"
image lucian_select = "images/Assets/players/lucian_1.png"

image mc_sprite = ConditionSwitch(
    "mc_choice == 'Aine'", "aine",
    "True", "lucian"
)

image customer_sprite = "images/Assets/Customer_Suspicious/customer sus.png"
image customer_sprite_thanks = "images/Assets/Customer_Suspicious/customer sus_thanks.png"

image regretful_writer_sprite = "images/Assets/Writer/Writer_1.png"
image regretful_writer_sprite_a = "images/Assets/Writer/Writer_1A.png"
image regretful_writer_sprite_b = "images/Assets/Writer/Writer 1B.png"
image regretful_writer_sprite_end = "images/Assets/Writer/Writer_End.png"

image grieving_mother_sprite = "images/Assets/Mother/Mother_1.png"
image grieving_mother_sprite_a = "images/Assets/Mother/Mother_2A.png"
image grieving_mother_sprite_b = "images/Assets/Mother/Mother_2B.png"
image grieving_mother_sprite_c = "images/Assets/Mother/Mother_2C.png"
image grieving_mother_sprite_end = "images/Assets/Mother/Mother_End.png"

image mirror_man_f = "images/Assets/Mysterious/myst_f.png"
image mirror_man_m = "images/Assets/Mysterious/myst_m.png"
image mirror_man_f_2 = "images/Assets/Mysterious/myst_f_2.png"
image mirror_man_m_2 = "images/Assets/Mysterious/myst_m_2.png"

image mirror_man_sprite = ConditionSwitch(
    "mc_choice == 'Aine'", "mirror_man_f",
    "True", "mirror_man_m"
)
image mirror_man_sprite_2 = ConditionSwitch(
    "mc_choice == 'Aine'", "mirror_man_f_2",
    "True", "mirror_man_m_2"
)

image TAoL_title = "images/Assets/TAoL_title.png"
image glow:
    "images/Assets/TAoL title_glow.png"
    alpha 0.0
    easein 2.0 alpha 1.0
    easeout 2.0 alpha 0.3
    repeat

image bg dark_street = "images/Assets/bg/Dark_street.jpg"
image bg library = "images/Assets/bg/Library.jpg"
image bg book_desk = "images/Assets/bg/Book_desk.jpg"

image bg library_dim = Transform("bg library", matrixcolor=BrightnessMatrix(-0.10) * SaturationMatrix(0.7))
image bg library_cool = Transform("bg library", matrixcolor=TintMatrix((0.69, 0.77, 0.87, 1.0)) * BrightnessMatrix(-0.05))
image bg library_warm = Transform("bg library", matrixcolor=TintMatrix((1.0, 0.84, 0.0, 1.0)) * BrightnessMatrix(0.05))

image book_overlay = Transform("images/Assets/items/book.png", rotate=-10, align=(0.5, 0.5))

transform left_sprite:
    zoom 0.5 xalign 0.0 yalign 1.0
transform center_sprite:
    zoom 0.5 xalign 0.5 yalign 1.0
transform right_sprite:
    zoom 0.5 xalign 1.0 yalign 1.0
transform select_left:
    zoom 0.4 xalign 0.25 yalign 0.5
transform select_right:
    zoom 0.4 xalign 0.75 yalign 0.5

transform title_logo:
    zoom 0.25 xalign 0.5 yalign 0.15
