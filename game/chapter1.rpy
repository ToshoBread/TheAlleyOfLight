label chapter1:
    scene bg library
    with dissolve
    show mc_sprite at left_sprite with dissolve
    stop music fadeout 7.0
    narrator "Days pass. You learn the rhythm of the library."
    narrator "Lost souls arrive. You help them find their endings."
    narrator "Then one evening, a young man appears."
    play music bgm_customer_with_grief_music fadein 1.0 volume 0.5 loop
    show regretful_writer_sprite at right_sprite
    with dissolve
    regretful_writer "I... I died before I could write the ending."
    regretful_writer "My story feels so empty."
    play sound bgsfx_book_turn_sound volume 1.0
    pause 2.5
    narrator "His book opens to blank last pages."
    menu:
        "Tell me about the ending you always dreamt of writing.":
            mc "It's okay. You don't have to rush."
            mc "Tell me about the ending you always dreamt of writing."
            $ empathy += 1
            $ renpy.notify("+1 Empathy")
            hide regretful_writer_sprite with dissolve
            show regretful_writer_sprite_a at right_sprite with dissolve
            regretful_writer "I wanted it to end with hope... maybe redemption."
            hide regretful_writer_sprite_a with dissolve
            show regretful_writer_sprite_end at right_sprite with dissolve
            pause 2.0
            $ renpy.notify("Saving...")
            $ renpy.pause(0.1, hard=True)
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch1")
            jump chapter2
        "What do you truly need to let go of to end it?":
            mc "The story can't stay unfinished forever."
            mc "What do you truly need to let go of to end it?"
            $ clarity += 1
            $ renpy.notify("+1 Clarity")
            hide regretful_writer_sprite with dissolve
            show regretful_writer_sprite_b at right_sprite with dissolve
            regretful_writer "You're right... I was always running away from the truth."
            hide regretful_writer_sprite_b with dissolve
            show regretful_writer_sprite_end at right_sprite with dissolve
            pause 2.0
            $ renpy.notify("Saving...")
            $ renpy.pause(0.1, hard=True)
            $ renpy.take_screenshot()
            $ renpy.save("auto_ch1")
            jump chapter2
