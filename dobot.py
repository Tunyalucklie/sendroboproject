#Magician
import math

dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)

moveX=52;moveY=52;moveZ=22.3306;moveFlag=-1
pos = dType.GetPose(api)
rHead = pos[3]

dType.SetPTPCmd(api, 2, 202.485,75.168,-43.5334, rHead, 1)

# first position
in_x =  202.485;in_y = 75.168;normal_z = -43.5334

# checkoint position
check_x = 191.8864; check_y = 171.8675
#coin step
moveZ_coin = 0

#stacking
for i in range(4):
	next_y  = in_y + i*moveY
	for j in range(3):
		next_x = in_x + j*moveX
		dType.SetPTPCmd(api, 2, next_x, next_y, normal_z, rHead, 1)
		dType.SetPTPCmd(api, 2, next_x, next_y, normal_z-moveZ, rHead, 1)
		dType.SetEndEffectorSuctionCup(api, 1,1,1)
		dType.SetPTPCmd(api, 2, next_x, next_y, normal_z, rHead, 1)
		dType.SetPTPCmd(api, 2, check_x,check_y,normal_z, rHead, 1)
		dType.SetPTPCmd(api, 2, check_x,check_y,normal_z-moveZ+moveZ_coin, rHead, 1)
		dType.SetEndEffectorSuctionCup(api, 1,0,1)
		dType.SetPTPCmd(api, 2, check_x,check_y,normal_z, rHead, 1)
		moveZ_coin += 1.75

