label chapter3:
    scene bg library_dim
    with dissolve
    show mc_sprite at left_sprite with dissolve
    pause 2.0
    narrator "A man walks in. He looks at you strangely."
    play music bgm_chapter_3_music volume 0.5 loop
    narrator "Something about him is unsettlingly familiar."
    show mirror_man_sprite at right_sprite
    with dissolve
    mirror_man "You... you feel so familiar. Have we met?"
    mirror_man "Your eyes... I swear I've seen them before."
    menu:
        "Tell me everything you remember about me.":
            mc "You know me?"
            mc "Please tell me everything you remember about me."
            $ suspicion += 1
            $ renpy.notify("+1 Suspicion")
            hide mirror_man_sprite with dissolve
            show mirror_man_sprite_2 at right_sprite with dissolve
            mirror_man "You were in an accident... there was rain, headlights..."
            mirror_man "Wait, was that you?!"
            stop music fadeout 3.0
            pause 2.0
            $ renpy.notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch3")
            jump chapter4
        "Let's focus on your story first.":
            mc "Let's focus on your story first."
            mc "The book is waiting for your ending."
            $ clarity += 1
            $ renpy.notify("+1 Clarity")
            mirror_man "Alright... but something about you feels unfinished too."
            stop music fadeout 3.0
            pause 2.0
            $ renpy.notify("Saving...")
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch3")
            jump chapter4
