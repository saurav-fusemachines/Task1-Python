computer_parts = ["computer","monitor","keyboard","mouse","mouse mat"]
print(computer_parts)
print()

print("Replacing a 4th item in list")
computer_parts[3]='trackball'
print(computer_parts)

computer_parts[3:]=["trackball"]
print(computer_parts)
print("As we see after 3rd position all other items were replaced by track ball")