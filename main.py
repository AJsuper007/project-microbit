record.start_recording(record.BlockingState.BLOCKING)
def on_forever():
    record.play_audio(record.BlockingState.BLOCKING)
    basic.show_leds("""
        . # # # .
        . . . # .
        . # # # .
        . . . # .
        . # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        . . . # .
        . # # . .
        . # . . .
        . # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        # . . . .
        # . # # #
        # . . # .
        # # # # .
        """)
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        # . # . #
        # . # . #
        # . # . #
        . . . . .
        # . # . #
        """)
    basic.show_leds("""
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
    """)
basic.forever(on_forever)
