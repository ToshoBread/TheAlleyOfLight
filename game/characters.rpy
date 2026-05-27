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
