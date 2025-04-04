import msvcrt
import time

tsks = [
    " -Pray",
    "Read the Bible",
    "Crucify the flesh",
    "Study",
    "Focus"
]

how = input("How are you man? ")
print(" hm. Sometimes it happens...\n You shouldn't lose hope tho, God is still good")
fallen = input("You fell? (yes/no): ").strip().lower()
if fallen.startswith("y"):
    print("Do not even walk near it, man, please. This is your past self saying this to you: It drains every vitality you have.")
else:
    print("Good! Stay strong and keep going!")
honest = input("Be honest, you have something to do you're skipping rn? ").lower()
if honest == "no" or honest =="yes":
    print("Then go get something to do, now. Here's a list of possible things: ")
    print(*tsks, sep = "\n -")

time.sleep(2)
print("You know, it's been a while you don't program, your cpu misses your instructions.")
print("I know we aren't the best of the world in programming, but... Why did you stop?")
time.sleep(3)
print("Also, it's been a while you talked with God bro, don't mess up again, don't throw my efforts to waste man... Please..")
time.sleep(2)
print("Hey, btw, you better contribute to your tommorrow self, so that yk, you die well, and the tommorrow gets greater. Any effort is considered my dude, so what are you waiting for? Go work, now.")
time.sleep(1)
want = input("Quick question, want to add more tasks to the list? y/n ")
if want == "y":
    amo = int(input("How many tasks you wan tto add? "))
    for _ in range(amo):
        tsks.append(input("Add a new task you want to focus on: "))


completed_tasks = []

time.sleep(2)


fini = input("When you finish a task, say y. If you wanna quit say anything else to me alr?")
if fini == "w":
        task = input("Which task did you complete? ")
        if task in tsks:
            completed_tasks.append(task)
            tsks.remove(task)
            print(f"Great job! You've completed: {task}")









