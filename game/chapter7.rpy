label chapter7:
    scene bg library_cool
    with dissolve
    show mc_sprite at center_sprite with dissolve
    narrator "The library falls deathly silent."
    narrator "No more customers arrive."
    narrator "You are alone with the truth."
    scene bg book_desk_dim
    with dissolve
    $ renpy.pause(0.5, hard=True)
    play sound bgsfx_book_turn_sound volume 1.0
    pause 2.5
    show book_overlay
    with dissolve
    narrator "A single final book materializes before you, glowing softly."
    narrator "It is your story."
    narrator "You open it."
    narrator "The rain. The crash. The moment between life and death."
    narrator "You read the final page."
    narrator "The library awaits your ending."
    stop music fadeout 5.0
    $ ending = get_ending()
    if ending == "secret":
        jump ending_secret
    elif ending == "return":
        jump ending_return
    elif ending == "stay":
        jump ending_stay
    else:
        jump ending_let_go
