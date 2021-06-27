# program entry point
from data.sinistarwindow import SinistarWindow
import arcade
from data import constants
def main():

    window = SinistarWindow(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

    window.setup()
    
    theme = arcade.load_sound("project_template/Sinistar/sounds/bensound-scifi.mp3", True)
    arcade.play_sound(theme, 0.8, 0, True)
    
    arcade.run()

if __name__ == "__main__":
    main()