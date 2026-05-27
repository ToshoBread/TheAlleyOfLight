label chapter2:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite
    narrator "The next visitor is a middle-aged woman."
    narrator "She cannot stop crying."
    show grieving_mother_sprite at right_sprite
    with dissolve
    grieving_mother "I keep reliving that night..."
    grieving_mother "I should have been there."
    grieving_mother "My baby is gone because of me."
    menu:
        "Take all the time you need. I'm here to listen.":
            mc "Take all the time you need. I'm here to listen, not to judge."
            $ clarity += 1
            show screen notify("+1 Clarity")
            hide grieving_mother_sprite with dissolve
            show grieving_mother_sprite_a at right_sprite with dissolve
            grieving_mother "I... I was arguing with my husband. I wasn't paying attention."
            hide grieving_mother_sprite_a with dissolve
            show grieving_mother_sprite_end at right_sprite with dissolve
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch2")
            jump chapter3
        "What really happened the night you lost your child?":
            mc "You keep avoiding that memory."
            mc "What really happened the night you lost your child?"
            mc "Facing it might set you free."
            $ memory_fragments += 1
            show screen notify("+1 Memory Fragment")
            hide grieving_mother_sprite with dissolve
            show grieving_mother_sprite_b at right_sprite with dissolve
            grieving_mother "You're right. I need to forgive myself."
            hide grieving_mother_sprite_b with dissolve
            show grieving_mother_sprite_end at right_sprite with dissolve
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch2")
            jump chapter3
        "Sometimes the bravest thing is to write the final line yourself.":
            mc "Every soul here carries an unfinished page."
            mc "Sometimes the bravest thing is to write the final line yourself."
            $ empathy += 1
            show screen notify("+1 Empathy")
            hide grieving_mother_sprite with dissolve
            show grieving_mother_sprite_c at right_sprite with dissolve
            grieving_mother "No one ever just listened before... Thank you."
            hide grieving_mother_sprite_c with dissolve
            show grieving_mother_sprite_end at right_sprite with dissolve
            show screen notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch2")
            jump chapter3
