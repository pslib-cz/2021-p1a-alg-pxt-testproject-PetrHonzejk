def on_button_pressed_a():
    basic.show_leds("""
        . . . # #
                        . . . # #
                        . . . # #
                        . # # # #
                        # # # # #
    """)
    basic.pause(25)
    basic.show_leds("""
        . . . # #
                        . . . # #
                        . # # # #
                        . # # # .
                        # # # . .
    """)
    basic.pause(25)
    for index in range(6):
        basic.show_leds("""
            . # # # .
                                    . # # # .
                                    . . # . .
                                    . # # # .
                                    # # . # .
        """)
        basic.pause(10)
        basic.show_leds("""
            . # # # .
                                    . # # # .
                                    . . # . .
                                    . # # # .
                                    . # . # #
        """)
        basic.pause(5)
        basic.show_leds("""
            # # # . .
                                    # # # . .
                                    . # . . .
                                    . # . . .
                                    # . # . .
        """)
        basic.pause(5)
        basic.show_leds("""
            . . # # #
                                    . . # # #
                                    . . . # .
                                    . . . # .
                                    . . # . #
        """)
    basic.show_leds("""
        # # # # .
                        # . . . .
                        # . . # .
                        # . . . #
                        # # # # #
    """)
    basic.pause(5)
    basic.show_leds("""
        # # # # .
                        # . . . .
                        # # # . .
                        # . . . .
                        # # # # .
    """)
    basic.pause(5)
    basic.show_leds("""
        # # # # #
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
    """)
    basic.show_string("RICK ROLLED")
input.on_button_pressed(Button.A, on_button_pressed_a)

music.set_volume(255)
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(523, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(466, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(262, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(523, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(466, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(523, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.HALF))
music.play_tone(523, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.play_tone(349, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.DOUBLE))
music.rest(music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(262, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.QUARTER))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(440, music.beat(BeatFraction.QUARTER))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.QUARTER))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.QUARTER))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.play_tone(349, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(262, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(294, music.beat(BeatFraction.QUARTER))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(392, music.beat(BeatFraction.HALF))
music.rest(music.beat(BeatFraction.SIXTEENTH))
music.play_tone(330, music.beat(BeatFraction.QUARTER))