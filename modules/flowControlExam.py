from random import randint

score=int(input("Enter Score"))

if score >= 90 :
    print("Grade A")
else:
    if score >= 80 :
        print("Grade B")
    else:
        if score >= 70 :
            print("Grade C")
        else:
            if score >= 60:
                print("Grade D")
            else:
                print("Grade F")

if score >= 90:
    print("Grade A.")
elif score >= 80:
    print("Grade B.")
elif score >= 70:
    print("Grade C.")
elif score >= 60:
    print("Grade D.")
else:
    print("Grade F.")


dyna_num=randint(1,10)

if dyna_num==10:
    print("The Number is X")
elif dyna_num==9:
    print("The Number is IX")
elif dyna_num == 8:
    print("The Number is VIII")
elif dyna_num == 7:
    print("The Number is VII")
elif dyna_num==6:
    print("The Number is VI")
elif dyna_num==5:
    print("The Number is V")
elif dyna_num==4:
    print("The Number is IV")
elif dyna_num==3:
    print("The Number is III")
elif dyna_num==2:
    print("The Number is II")
else:
    print("The Number is I")