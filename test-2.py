from naoqi import ALProxy
import time
textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)
#textSpeakProxy = ALProxy("ALTextToSpeech", "zhanat-K56CB", 37826) 
#motionProxy = ALProxy("ALMotion", "zhanat-K56CB", 37826)

#10.1.198.45
handName = "LHand"

useSen = 0


while(1):

	x = motionProxy.getAngles(handName, useSen)

	print(x[0])
        
	motionProxy.move(x[0], 0.0, 0.0)

        
        time.sleep(0.100)


        #motionProxy.move(0.0, 0.0, 0.0)

