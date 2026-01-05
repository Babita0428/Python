import random
def otp_generator():
    OTP=random.randint(1000,9999)
    return OTP

def otp_verification (OTP):
    chances=0
    while chances < 5:
        if chances==4:
            print("this is your last chance!")
        user_OTP=int(input("enter otp: "))
        if user_OTP==OTP:
            print("OTP verified")
            return
        else:
            print("try again")
            chances=chances+1
    print("OTP bloced Too many attempts!")


def main():
    OTP=otp_generator()     
    print("Generated OTP: ",OTP)   
    otp_verification(OTP)
main()    