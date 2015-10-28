blocked_users = ['whoeverest', 'someone']

conversation = [
	{'user': 'whoeverest', 'msg': 'hey dude! where did you disappear'}, 
	{'user':'nick', 'msg': 'you awake?'}
]

# for usermsg in conversation:
# 	for buser in blocked_users:
# 		if usermsg['user'] == buser:
# 			continue
# 		print(usermsg['user'] + ": " + usermsg['msg'])


for usermsg in conversation:
	if not usermsg['user'] in blocked_users:
		print(usermsg['user'] + ": " + usermsg['msg'])