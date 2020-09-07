import pyautogui, time, webbrowser, schedule, sys


## URLs ##
url1 = "https://us04web.zoom.us/j/79522886104?pwd=czcxeUtyUUlvODRRTGZSTUpRdFIvUT09"
url2 = "https://us04web.zoom.us/j/73719308054?pwd=bjkyaTBwNHM3MnhPdXNDNlZ0V3ZIZz09"
url3 = "https://us04web.zoom.us/j/6493030972?pwd=S0VlNUx3Y1dTVVh1ZWYvRDdudTNVZz09"
url4 = "https://us04web.zoom.us/j/9355504263?pwd=cE5qaVI0RFlKeXl5TWRFajRRU2VsQT09"
urlx = "https://us04web.zoom.us/j/9599125014?pwd=VE9XVnJLdWVPQkU5TDdQV3drSy9pdz09"


## Time ##
##t = time.time()
##t0 = t + 60* 1
##current_time = time.strftime("%H:%M", time.localtime(t0))

##t1 = current_time

t1 = "09:00"
t2 = "09:50"
t3 = "11:05"
t4 = "11:55"
t5 = "12:45"

## Main ##
def main():
    print("Initiating A.Z.M.A.....")
    time.sleep(2)
    print("Waiting for class #1.....")
    while True:
        schedule.run_pending()
        time.sleep(60)
        pyautogui.click(2,4)

    
 ## Function for each classes:       

def class_1():
    pyautogui.click(956, 485)
    webbrowser.open(url1)
    print("Succesfully joined meeting #1")
##    time.sleep(2500)
##    leave_meeting()

def class_2():
    pyautogui.click(956, 485)
    webbrowser.open(url2)
    print("Succesfully joined meeting #2")
##    time.sleep(2500)
##    leave_meeting()

def class_3():
    pyautogui.click(956, 485)
    webbrowser.open(url3)
    print("Succesfully joined meeting #3")
##    time.sleep(2500)
##    leave_meeting()
    
def class_4():
    pyautogui.click(956, 485)
    webbrowser.open(url4)
    print("Succesfully joined meeting #4")
    sys.exit()
    
def class_x():
    time.sleep(60)
    pyautogui.click(956, 485)
    webbrowser.open(urlx)
    time.sleep(20)
    pyautogui.click(956, 485)
    print("Click")
    pyautogui.write("x7y8z9")
    print("Tippidy tap")
    pyautogui.click(967, 656)
    print("Succesfully joined meeting X")



## Schedule ##
schedule.every().day.at(t1).do(class_x)
schedule.every().day.at(t2).do(class_1)
schedule.every().day.at(t3).do(class_2)
schedule.every().day.at(t4).do(class_3)
schedule.every().day.at(t5).do(class_4)

main()





