import time

total_min = 0
checkmark = 0

def tasks(task):
    global total_min
    global checkmark
    mins = 0
    print(f"Timer started. Start your task of {task} for 25 minutes.")
    while mins <= 24:
        time.sleep(60)
        mins += 1
        print(f"{mins} minutes have passed.")
    print("End of Pomodoro")
    checkmark += 1
    print(f"Total checkmarks is {checkmark}")

def breaks():
    global checkmark
    mins = 0
    if checkmark < 4:
        print("Take a short break.")
        while mins != 3:
            time.sleep(60)
            mins += 1
            print(f"{mins} minutes break completed.")
        print("Your short break is over.")

    elif checkmark >=4:
        print("Take a long break.")
        while mins != 10:
            time.sleep(60)
            mins += 1
            print(f"{mins} minutes break completed.")
        checkmark = 0
        print("Your long break is over.")
def main():
    carry_on = 'y'
    task = input("Welcome to Pomodoro Timer\n What task do you want to work on? ")
    while carry_on == "y" or carry_on == "Y":
        tasks(task)
        breaks()
        carry_on = input("Do you want to carry on? (y/n) ")


if __name__ == '__main__':
    main()




