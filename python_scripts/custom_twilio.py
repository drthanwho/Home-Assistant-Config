# Python Script to Extend Features of the Twilio Call Component

# Parameters
# The following are optional
# voice: [man | woman | alice] # default man
# delay: [1;10] # delay before message is said.  Default is 0. 
#                 This allows time for someone to pickup the phone.
# loop: [1:3] # plays message multiple times.  Default is once.
# language: see https://www.twilio.com/docs/api/twiml/say
# speed: [normal|slow} # default is normal
# message: # the text of the message
# phone: # recipient phone number

# Example Service Call
      # - service: python_script.my_twilio_call
        # data:
          # delay: '1'
          # loop: '2'
          # voice: 'alice'
          # language: 'en-CA'
          # speed: 'slow'
          # message: 'text of the message'
          # phone: 'recipient phone number'

# Get option parameters

# Voice Parameter
voice = data.get('voice', '0')
logger.info("voice {}".format(voice))

if voice != '0':
	url_voice = '%20voice%3D%22' + voice + '%22'
else:
	url_voice = ''

# Delay Parameter
delay = data.get('delay', '0')
#logger.info("delay {}".format(delay))
if int(delay) > 0 :
# <Pause length="delay"/>
	url_delay = '%3CPause%20length%3D%22' + delay + '%22%2F%3E%0A'
else:
	url_delay = ''	

# Loop Parameter
loop = data.get('loop', '0')
logger.info("loop {}".format(loop))
if int(loop) > 0 :
	url_loop = '%20loop%3D%22' + loop + '%22'
else:
	url_loop = ''

# Language Parameter
language = data.get('language', '0')
logger.info("language {}".format(language))

if language != '0':
	url_language = '%20language%3D%22' + language + '%22'
else:
	url_language = ''

# Speed Parameter
speed = data.get('speed', '0')
logger.info("speed {}".format(speed))
#I replaced spaces with commas just too slow down the text to speech
#Use %20 to speed up
if speed == 'slow':
	spacer = '%2C'
else:
	spacer = '%20'



# Message Parameter
message = data.get('message', '0')
#logger.info("message {}".format(message))

if message == '0':
        exit()


# Phone Parameter
phone = data.get('phone', '0')
#logger.info("phone {}".format(phone))

if phone == '0':
        exit()



#Format message for a url transmission.  ie no spaces

url_message = '%3E' + message.replace(' ',spacer) + spacer
url_root = 'https://twimlets.com/echo?Twiml=%3CResponse%3E%0A'
url_say = '%3CSay'
url_close = '%3C%2FSay%3E%0A%3C%2FResponse%3E%0A&'
#Assemble complete url message
url = url_root + url_delay + url_say + url_voice + url_language \
	+ url_loop + url_message + url_close

logger.info("{}".format(url))
# Paste url output in homeassistant.log into a chrome browser to test.

# send url to notify.twilio service
data = { "message" : url, "target" : phone }

#substitute 'twilio_test_call' with the name of your notifier
hass.services.call('notify', 'twilio', data)
# EOF