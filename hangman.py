import random
import anki_vector
import time

def get_guess():

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        dashes = "-" * len(secret_word)
        guesses_left = 10

        robot.behavior.drive_off_charger()
        time.sleep(1)
        robot.say_text("Let's play hang man")
        robot.anim.play_animation('anim_onboarding_reacttoface_happy_01')

        while guesses_left > 0 and not dashes == secret_word:

            print(dashes)
            robot.say_text("You have" + str(guesses_left) + "guesses remaining")

            guess = input("Guess:")

            if len(guess) != 1:
                robot.say_text("Your guess must have exactly one character!")
                robot.anim.play_animation('anim_dancebeat_cantdothat_01')

            elif guess in secret_word:
                robot.say_text("You have chosen")
                time.sleep(0.2)
                robot.say_text("Wisely")
                robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_-20')
                dashes = update_dashes(secret_word, dashes, guess)

            else:
                robot.say_text("You have chosen")
                time.sleep(0.2)
                robot.say_text("Un wisely")
                robot.anim.play_animation('anim_eyepose_sad_down')
                guesses_left -= 1

        if guesses_left < 1:
            robot.say_text("You lose. The word was: " + str(secret_word))
            robot.anim.play_animation('anim_eyepose_sad_instronspect')
            robot.behavior.drive_on_charger()

        else:
            robot.say_text("Congratulations! You win. The word was: " + str(secret_word))
            robot.anim.play_animation('anim_holiday_hyn_confetti_01')
            robot.behavior.drive_on_charger()

def update_dashes(secret, cur_dash, rec_guess):
    result = ""

    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess

        else:
            result = result + cur_dash[i]

    return result

words = ["human", "robot", "vector", "cube", "sensor", "camera", "tracks", "lift", "python", "japan", "battery", "motherboard", "motors", "eyes", "wireless", "bluetooth", "proximity", "animation", "photos", "exceptions", ]

secret_word = random.choice(words)
get_guess()
