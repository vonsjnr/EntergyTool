from tkinter import *
from tkinter import filedialog, messagebox
import csv
import os
from time import localtime, strftime
'''
dailyReportPath = "C:/Users/a760916/Desktop/users.txt"
envDBdevicesPath = "C:/Users/a760916/Desktop/devices.txt"
envDBUsersPath = "C:/Users/a760916/Desktop/users.txt"'''

def generateList():  

    usersInWeeklyReport = []
    devicesInEnv = []
    splittedUsersInReport = []
    splittedUsersInEnv = []
    #try:
    with open(envDBUsersPath) as txt_file:
        txt_reader = csv.reader(txt_file, delimiter=',')
        line_count = 0
        for userInWeeklyReport in txt_reader:
            if bool(userInWeeklyReport) == False:
                pass
            else:
                usersInWeeklyReport.append(userInWeeklyReport[0].lower())
            line_count += 1
    
    for userInWeeklyReport in usersInWeeklyReport:
        splittedUserInReport = userInWeeklyReport.split("@")
        if splittedUserInReport[0].startswith("anonymous "):
            anonUser = splittedUserInReport[0].split('"')
            splittedUsersInReport.append(anonUser[1])
            print("This is double user:", anonUser)
        else:
            splittedUsersInReport.append(splittedUserInReport[0])

    print("Users in users file w/ doubles filter:",len(splittedUsersInReport))
    
    with open(envDBdevicesPath) as txt_file2:
        txt_reader2 = csv.reader(txt_file2, delimiter=',')
        line_count = 0
        for deviceInEnv in txt_reader2:
            if bool(deviceInEnv) == False:
                pass
            else:
                devicesInEnv.append(deviceInEnv[0])
            line_count += 1
                
    for userInEnv in devicesInEnv:
        splittedUserInEnv = userInEnv.split("@")
        if splittedUserInEnv[0].startswith("anonymous "):
            anonUser = splittedUserInEnv[0].split('"')
            splittedUsersInEnv.append(anonUser[1])
        else:
            splittedUsersInEnv.append(splittedUserInEnv[0])
            
    print("Devices in envDB w/ doubles filter:", len(splittedUsersInEnv),"\n")

    
    usersOnlyInUsersReport = []
    for allUser in splittedUsersInReport:
        if allUser not in splittedUsersInEnv:
            usersOnlyInUsersReport.append(allUser)
    print("Users in users (file), not in devices (w/ doubles):", len(usersOnlyInUsersReport))
    
    usersOnlyInUsersReport = list(dict.fromkeys(usersOnlyInUsersReport))
    print("Users in users (file), not in devices (w/w doubles):",len(usersOnlyInUsersReport))
    

    
    #Define current's date
    currentDate = strftime("%Y.%m.%d %H-%M-%S", localtime())
    #Define file's name
    txtfilename = "Entergy users report {}.txt".format(currentDate)
    # Create new .txt file
    txtReport = open(txtfilename, 'w')
    # Add same users to the file
    txtReport.write("Entergy \nReport created on {}\n\nUsers not existing in devices file:\n{}".format(currentDate,str(usersOnlyInUsersReport)))
    # Close the file
    txtReport.close()
    #Opens report after complete
    os.startfile(txtfilename)
    
    window.destroy()
    #except NameError:
        #pass
        #messagebox.showerror(title="Error", message="Report or database is not selected")
    #except:
       # messagebox.showerror(title="Error", message="There is an error with a file. Correct and try again.")
    

def browse_usersDb():
    global envDBUsersPath
    envDBUsersPath = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetype=(("txt files","*.txt"),("All files","*.*")))
    print(envDBUsersPath)
    return envDBUsersPath

def browse_devicesDb():
    global envDBdevicesPath
    envDBdevicesPath = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetype=(("txt files","*.txt"),("All files","*.*")))
    print(envDBdevicesPath)
    return envDBdevicesPath

def browse_fileReport():
    global dailyReportPath
    dailyReportPath = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetype=(("txt files","*.txt"),("All files","*.*")))
    return dailyReportPath


def createGui():
    # Configure gui main window/frame
    global window
    window = Tk()
    window.iconbitmap("24230187_300x300__1__2lX_icon.ico")
    window.title("Entergy")
    window.configure(background = "white", padx=0)

    #Frame with logo and title
    mainFrame = Frame(window, background="#E4002B")
    mainFrame.grid (row = 0, column = 0, sticky = W)


    #Frame with buttons
    btnFrame = Frame(window, background="white")
    btnFrame.grid (row = 1, column = 0, sticky = W, pady=10)
    # Add logo of NG
    logoNG = PhotoImage(file = "resizedLogowhite.png")
    Label (mainFrame, image = logoNG, bg = "white") .grid(row = 0, column = 0, sticky=W)
    # Create label with title
    Label (mainFrame, text = "Generate list of users", fg = "white", bg="#E4002B", font = "Bahnschrift 12 bold").grid(padx = 10, pady = 10, row = 1, column = 0, sticky = W)
    # Label with description
    Label (btnFrame, text = "Select report and database", bg = "white", fg="black", font = "Bahnschrift 12 bold").grid(padx = 10, pady = 20, row = 0, column = 0, sticky = W)
    
    #Extra line
    canvas = Canvas(btnFrame,width=100, height=3, background="#E4002B", highlightthickness=0)
    #canvas.grid(row=1,column=0, sticky=W, padx=15)
    canvas.create_line(150, 10, 150, 10, width=10, fill="red")
    canvas.place(x="13", y="48")
    # Create button to select report
    #browseReport = Button (btnFrame, text = "Daily Report (.csv)", font = "Bahnschrift 11 bold", bg = "#E4002B", fg = "white", width=17)
    #browseReport.grid(row = 2, column = 0, sticky = W, padx=15, pady=20)
    # Create button to select users in DB
    browseDBUsers = Button (btnFrame, text = "Database users (.txt)", command= browse_usersDb,  font = "Bahnschrift 10 bold", bg = "#E4002B", fg = "white", width=20)
    browseDBUsers.grid(row = 3, column = 0,sticky = W, padx=15, pady=20)
    # Create button to select devices in DB
    browseDBDevices = Button (btnFrame, text = "Database devices (.txt)", command=browse_devicesDb, font = "Bahnschrift 10 bold", bg = "#E4002B", fg = "white", width=20)
    browseDBDevices.grid(row = 3, column = 0,sticky = E, padx=15, pady=20)
    # Create exit button
    Button (btnFrame, text = "GENERATE", height = 2, width = 40,command=generateList, font = "Bahnschrift 11 bold", bg = "black", fg = "white", bd = 1) .grid(padx = 12.5, pady = 20, row = 4, column = 0)
    # Create lfooter
    Label (btnFrame, text = "Tool created by Atos PL WSDS DevOps Team", bg = "white", fg = "black", font = "Arial 7") .grid(padx = 10, pady = 2, row = 5, column = 0)
    # Run gui
    window.mainloop()

createGui()