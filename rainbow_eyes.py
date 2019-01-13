#!/usr/bin/env python3

import time
import anki_vector


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:

        time.sleep(1)
        robot.say_text("Richard")
        robot.behavior.set_eye_color(hue=0.00, saturation=1.00)

        robot.say_text("Of")
        robot.behavior.set_eye_color(hue=0.05, saturation=1.00)

        robot.say_text("York")
        robot.behavior.set_eye_color(hue=0.10, saturation=1.00)

        robot.say_text("Gave")
        robot.behavior.set_eye_color(hue=0.30, saturation=1.00)

        robot.say_text("Battle")
        robot.behavior.set_eye_color(hue=0.50, saturation=1.00)

        robot.say_text("In")
        robot.behavior.set_eye_color(hue=0.70, saturation=1.00)

        robot.say_text("Vain")
        robot.behavior.set_eye_color(hue=0.80, saturation=1.00)
        time.sleep(1)

if __name__ == '__main__':
    main()
