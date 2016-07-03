import Skype4Py
import isSkypeOpen
import time
from subprocess import Popen , PIPE , STDOUT


if isSkypeOpen.check() == False:
	
	print("skype not open")

	isSkypeOpen.openSkype()
	
	time.sleep(4)

	# Create an instance of the Skype class.
	skype = Skype4Py.Skype()

	# Connect the Skype object to the Skype client.
	skype.Attach()
	skype.PlaceCall( "echo123" )

else:

	# Create an instance of the Skype class.
	skype = Skype4Py.Skype()

	# Connect the Skype object to the Skype client.
	skype.Attach()
	skype.PlaceCall( "echo123" )	

