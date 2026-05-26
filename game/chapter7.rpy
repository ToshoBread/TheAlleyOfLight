label chapter7:
    scene bg library_night
    with dissolve
    show mc_sprite at center_sprite
    narrator "The library falls deathly silent."
    narrator "No more customers arrive."
    narrator "You are alone with the truth."
    narrator "A single final book materializes before you, glowing softly."
    narrator "It is your story."
    narrator "You open it."
    narrator "The rain. The crash. The moment between life and death."
    narrator "You read the final page."
    narrator "The library awaits your ending."
    $ ending = get_ending()
    if ending == "secret":
        jump ending_secret
    elif ending == "return":
        jump ending_return
    elif ending == "stay":
        jump ending_stay
    else:
        jump ending_let_go
