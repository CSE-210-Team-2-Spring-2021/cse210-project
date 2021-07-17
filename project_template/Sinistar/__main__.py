# program entry point
from data.sinistarwindow import SinistarWindow
import arcade
from data import constants
def main():

    window = SinistarWindow(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

    window.setup()
    
    arcade.run()

if __name__ == "__main__":
    main()   