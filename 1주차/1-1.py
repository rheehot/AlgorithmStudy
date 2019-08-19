# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 입력받을 횟수
input_count = int(input())
# 모음들 집합
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
# 모음 문자열
vowels_temp = ""
# 사용자가 입력할 반복문
for i in range(input_count):
	# 문자열 입력
	string_data = input()
	# 입력받은 문자열에 대해서 한 글자씩 모음인지 아닌지 판단하여 문자열에 추가하는 형태
	for j in range(len(string_data)):
		if string_data[j] in vowels:
			vowels_temp += string_data[j]
	# 길이가 0이면 ??? 출력
	if len(vowels_temp) == 0:
		print("???")
	else: # 길이가 존재하면 모음이 존재한다는 의미로 모음 출력 이후 초기화
		for k in range(len(vowels_temp)):
			print(vowels_temp[k], end='')
		print()
		vowels_temp = ""