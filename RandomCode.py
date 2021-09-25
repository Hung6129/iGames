# # In ngược chuỗi
# txt = "Nguyễn Phúc Quý Hưng"[::-1]
# print(txt)

# # In ngược dãy số
# arr = ["Hung", 2, 3, 4, 5, 6, 7, 8, 9][::-1]
# print(arr)

# # Bảng cưu chương
# inputNum = int(input("Hãy nhập 1 số: "))
# for i in range(1, 11):
#     print(inputNum, "x", i, "=", inputNum*i)

# # Phép tính + - * / 2 số
# inputA = int(input("Nhập số a: "))
# inputB = int(input("Nhập số b: "))
# congAB = inputA + inputB
# truAB = inputA - inputB
# nhanAB = inputA * inputB
# chiaAB = 0
# if inputA < inputB:
#     chiaAB = "không chia được do a < b"
# else:
#     chiaAB = inputA // inputB
# print("a + b = ", congAB,"\n",
#       "a - b = ", truAB,"\n",
#       "a * b = ", nhanAB,"\n",
#       "a / b = ", chiaAB)


# # Cộng dần với kết quả
# rdNum = input("Hãy nhập 1 số để bắt đầu cộng dồn: ")

# num1 = 0
# num2 = int(rdNum)
# num3 = int(rdNum)
# for i in range(20):
#     num1 = num2 + num3
#     print(f'{num2} + {num3} = {num1}')
#     num2 = num3
#     num1 = num1
