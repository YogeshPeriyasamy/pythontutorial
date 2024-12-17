class ClassAssignment():
    def printsubfields():
        array=["sub_fields in AI :","ML","NN","Vision","Robotics"]
        for arr in array:
            print(arr)

    def Odd_Even():
        number=int(input("Enter number"))
        if(number%2==0):
            print(f"{number} is Even number")
        else:
            print(f"{number} is Odd number")

    def Marriage_eligibility():
        gender=input("gender")
        age=int(input("age"))
        print(f"Gender: {gender} Age: {age}")
        if(gender=="male" and age>=23):
            print("eligible")
        elif(gender=="female" and age>=21):
            print("eligible")
        else:
            print("not eligible")