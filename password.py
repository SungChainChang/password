password = 'a123456'
n = 3
while n > 0:
	n = n - 1
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功')
		break
	else:
		if n > 0:
		    print('密碼錯誤！還有', n ,'次機會')
		else:
			print('登入失敗')
