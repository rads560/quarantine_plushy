# Button code reference: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# Install through the command "pip install RPi.GPIO"
#Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

# Boolean to keep track of whether the button got pressed
button_pressed = False

# List of states
THINKING_STATE = 0
PODCAST_STATE = 1
SPOTIFY_STATE = 2
PLAYING_PODCAST_STATE = 3
PLAYING_SPOTIFY_STATE = 4
PAUSING_PODCAST_STATE = 5
PAUSING_SPOTIFY_STATE = 6

# Set initial state to thinking of you state
state = THINKING_STATE

def button_callback(channel):
    print("Button was pressed")
    button_pressed = True

# Ignore warning for now
GPIO.setwarnings(False)
# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)
# Set pin 8 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Setup event on pin 8 rising edge
# GPIO.add_event_detect(8, GPIO.RISING, callback=button_callback)

'''
To-Dos:
1. Add another button for turning all lights off? (sometimes the user might not want lights at all)
   This button could also act as the reject button.
2. While the podcast is being played, other requests should wait until the podcast is done playing.
3. While the spotify is being played, thinking of you messages can still be received (lights and audio should be separated).
4. If the podcast comes during a spotify connection, the plushy would blink and wait for the user to accept/reject the podcast
   while the spotify music is being played.
   If the user accepts the podcast, the plushy would stop blinking and start playing the podcast. The plushy would go back to
   the spotify mode after the podcast is done playing.
   If the user rejects the podcast, the plushy would blink again after 30 minutes.
'''

while True:
    if GPIO.input(8) == GPIO.HIGH:
        print("button was pushed!")
    # message = input("Press enter to quit\n\n")

    # The message can be either "podcast", "spotify", or "thinking"
    # arg = input("Please enter the type of message you want to send: \n")

    # # For debugging without an actual button:
    # # if arg == "button":
    # #     button_pressed = True
    
    # if arg == "thinking":
    #     state = THINKING_STATE
    #     print("thinking of you lights on")
    # elif arg == "podcast":
    #     state = PODCAST_STATE
    # elif arg == "spotify":
    #     state = SPOTIFY_STATE

    # if state == THINKING_STATE:
    #     if button_pressed:
    #         print("thinking of you lights off")
    #         button_pressed = False
   
    # elif state == PODCAST_STATE:
    #     print("lights blinking")
    #     if button_pressed:
    #         print("playing podcast")
    #         state = PLAYING_PODCAST_STATE
    #         button_pressed = False
    
    # elif state == PLAYING_PODCAST_STATE:
    #     if button_pressed:
    #         print("pausing podcast")
    #         state = PAUSING_PODCAST_STATE
    #         button_pressed = False
    
    # elif state == PAUSING_PODCAST_STATE:
    #     if button_pressed:
    #         print("playing podcast")
    #         state = PLAYING_PODCAST_STATE
    #         button_pressed = False
    
    # elif state == SPOTIFY_STATE:
    #     print("lights turn green")
    #     if button_pressed:
    #         print("playing spotify")
    #         state = PLAYING_SPOTIFY_STATE
    #         button_pressed = False

    # elif state == PLAYING_SPOTIFY_STATE:
    #     if button_pressed:
    #         print("pausing spotify")
    #         state = PAUSING_SPOTIFY_STATE
    #         button_pressed = False

    # elif state == PAUSING_SPOTIFY_STATE:
    #     if button_pressed:
    #         print("playing spotify")
    #         state = PLAYING_SPOTIFY_STATE
    #         button_pressed = False

# Clean up
GPIO.cleanup()