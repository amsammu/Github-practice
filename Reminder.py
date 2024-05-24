import time
import os

from win10toast import ToastNotifier

def remind():
    # Display a Windows notification every hour
    toaster = ToastNotifier()
    toaster.show_toast("It's time to drink water", duration=3600)



def main():
    while True:
        remind()

        


if __name__=="__main__":
    main()



