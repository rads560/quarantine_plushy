from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import wget
from playsound import playsound

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-d6f1853a-38ed-11eb-99ef-fa1b309c1f97"
pnconfig.publish_key = "pub-c-63771edf-cfc7-4d18-b066-24b1e7f0e40c"
pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        print("error")

class LightUpCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost

        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            pubnub.publish().channel('raspberry-control').message('Hello channel!').pn_async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.

    def message(self, pubnub, message):
        # Handle new message stored in message.message
        print('message is: ' + str(message.message))
        if(message.message == 'pink'):
            state = 'lit'
            pubnub.publish().channel('raspberry-control').message(state).pn_async(my_publish_callback)

pubnub.add_listener(LightUpCallback())

def play_sound():
    url = 'http://quarantineplushy.herokuapp.com/uploads/podcast.wav'
    wget.download(url, 'podcast.wav')
    playsound('podcast.wav')

play_sound()
pubnub.subscribe().channels('raspberry-control').execute()