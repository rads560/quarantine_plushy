from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pprint import pprint

class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass

    def presence(self, pubnub, presence):
        pprint(presence.__dict__)

    def message(self, pubnub, message):
        pprint(message.__dict__)

def my_publish_callback(envelope, status):
    print(envelope, status)

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-d6f1853a-38ed-11eb-99ef-fa1b309c1f97"
pnconfig.publish_key = "pub-c-63771edf-cfc7-4d18-b066-24b1e7f0e40c"

pubnub = PubNub(pnconfig)

pubnub.add_listener(MySubscribeCallback())

pubnub.subscribe()\
    .channels("pubnub_onboarding_channel")\
    .with_presence()\
    .execute()\

pubnub.publish()\
    .channel("pubnub_onboarding_channel")\
    .message({"sender": pnconfig.uuid, "content": "Hello From Python SDK"})\
    .pn_async(my_publish_callback)