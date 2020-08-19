n = 2
while True:
	password =input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤！還有', n, '次機會')
		n = n - 1
		if n < 0:
			print('登入失敗')
			break