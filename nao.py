# Importing necessary modules
import naoqi
from naoqi import ALProxy
import time
import math

# Initializing proxies for text to speech and motion services
speechProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionService = ALProxy("ALMotion", "127.0.0.1", 9559)

# Defining the shoulder and wrist joints identifiers
shoulderJointName = "LShoulderPitch"
wristJointName = "LWristYaw"

# Setting initial values for sensor usage flags
sensorFlag = 0
sensorFlag1 = 0

# Defining the Greet function which contains the choreographed movement data
def Greet():
    # Initializing lists to store movement parameters
    actionNames = list()
    actionTimes = list()
    actionKeys = list()

    actionNames.append("LElbowRoll")
    actionTimes.append([0.4, 0.68, 0.92, 1.24, 1.6])
    actionKeys.append([[-1.02625, [3, -0.146667, 0], [3, 0.0933333, 0]], [-0.53058, [3, -0.0933333, 0], [3, 0.08, 0]], [-1.17286, [3, -0.08, 0], [3, 0.106667, 0]], [-0.692896, [3, -0.106667, 0], [3, 0.12, 0]], [-1.22697, [3, -0.12, 0], [3, 0, 0]]])

    actionNames.append("LElbowYaw")
    actionTimes.append([0.4])
    actionKeys.append([[-1.34565, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("LHand")
    actionTimes.append([0.4])
    actionKeys.append([[0.62, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("LShoulderPitch")
    actionTimes.append([0.4])
    actionKeys.append([[-0.560251, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("LShoulderRoll")
    actionTimes.append([0.4])
    actionKeys.append([[0.792379, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("LWristYaw")
    actionTimes.append([0.4])
    actionKeys.append([[0.490438, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RElbowRoll")
    actionTimes.append([0.4])
    actionKeys.append([[0.431299, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RElbowYaw")
    actionTimes.append([0.4])
    actionKeys.append([[1.21708, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RHand")
    actionTimes.append([0.4])
    actionKeys.append([[0.307073, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RShoulderPitch")
    actionTimes.append([0.4])
    actionKeys.append([[1.44608, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RShoulderRoll")
    actionTimes.append([0.4])
    actionKeys.append([[-0.212005, [3, -0.146667, 0], [3, 0, 0]]])

    actionNames.append("RWristYaw")
    actionTimes.append([0.4])
    actionKeys.append([[0.104329, [3, -0.146667, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motionInstance = ALProxy("ALMotion", "127.0.0.1", 9559)
      # motionInstance = ALProxy("ALMotion")
      motionInstance.angleInterpolationBezier(actionNames, actionTimes, actionKeys)
    except BaseException, err:
      print err

# Invoking the Greet function to execute the initial movement
Greet()
# Making the robot utter a greeting
speechProxy.say("Hello! I am excited to play with you!")

# Defining the LiftLeftArm function which contains the choreographed movement data
def LiftLeftArm():
    # Initializing lists to store movement parameters
    actionNames = list()
    actionTimes = list()
    actionKeys = list()

    actionNames.append("LElbowRoll")
    actionTimes.append([0.96])
    actionKeys.append([[-0.79587, [3, -0.333333, 0], [3, 0, 0]]])

    actionNames.append("LElbowYaw")
    actionTimes.append([0.96])
    actionKeys.append([[-0.226893, [3, -0.333333, 0], [3, 0, 0]]])

    actionNames.append("LHand")
    actionTimes.append([0.96])
    actionKeys.append([[0.73, [3, -0.333333, 0], [3, 0, 0]]])

    actionNames.append("LShoulderPitch")
    actionTimes.append([0.96])
    actionKeys.append([[-1.09956, [3, -0.333333, 0], [3, 0, 0]]])

    actionNames.append("LShoulderRoll")
    actionTimes.append([0.96])
    actionKeys.append([[0.738274, [3, -0.333333, 0], [3, 0, 0]]])

    actionNames.append("LWristYaw")
    actionTimes.append([0.96])
    actionKeys.append([[-1.42593, [3, -0.333333, 0], [3, 0, 0]]])

    try:
        # Creating a motion proxy to execute the movement
        motionInstance = ALProxy("ALMotion", "127.0.0.1", 9559)
        # Executing the movement using the angleInterpolationBezier method
        motionInstance.angleInterpolationBezier(actionNames, actionTimes, actionKeys)
    except BaseException as err:
        # Printing any errors that occur
        print(err)

# Invoking the LiftLeftArm function to execute the movement
LiftLeftArm()

# Setting the arm movement preferences during motion
leftArmActive  = False
rightArmActive = True
motionService.setMoveArmsEnabled(leftArmActive, rightArmActive)

# Starting an infinite loop to continuously monitor the joint angles and adjust the robot's movement accordingly
while True:
    # Retrieving the current angle of the shoulder joint
    velocity = motionService.getAngles(shoulderJointName, sensorFlag)
    # Converting the shoulder joint angle from radians to degrees
    velocity_angle = (2 * 89 * velocity[0]) / math.pi

    # Retrieving the current angle of the wrist joint
    rotation = motionService.getAngles(wristJointName, sensorFlag1)
    # Converting the wrist joint angle from radians to degrees
    rotation_angle = (2 * 89 * rotation[0]) / math.pi
    # Calculating the rotation rate based on the wrist joint angle
    rotation_speed = (-rotation_angle - 91) / 91

    # Evaluating the shoulder joint angle and adjusting the robot's forward speed accordingly
    if -74 < velocity_angle < 7:
        print("We are advancing quickly")
        motionService.move(2, 0.0, 0.0)
    elif 7 < velocity_angle < 54:
        print("We are advancing slowly")
        motionService.move(1, 0.0, 0.0)
    else:
        print("I am stopping")
        motionService.move(0.0, 0.0, 0.0)

    # Evaluating the wrist joint angle and adjusting the robot's rotation speed accordingly
    if rotation_angle < -92:
        print("We are turning right")
        motionService.move(0.0, 0.0, -8 * rotation_speed)
    elif rotation_angle > 17:
        print("We are turning left")
        motionService.move(0.0, 0.0, -rotation_speed)

    # Adding a brief pause before the next iteration of the loop
    time.sleep(0.105)