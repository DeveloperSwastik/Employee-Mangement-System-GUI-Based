import datetime
import os
import random
import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from PIL import Image, ImageDraw, ImageFont

import calculator as calc

root = Tk()

appWidth = 550
appHeigth = 400

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.geometry(
    f"{appWidth}x{appHeigth}+{int((screenWidth - appWidth)/2)}+{int((screenHeight - appHeigth)/5)}")
root.resizable(0, 0)
root.title("Employee Management System")

rootMenu = Menu(root)
root.config(menu=rootMenu)

accountMenu = Menu(rootMenu, tearoff=OFF)
rootMenu.add_cascade(label="Account", menu=accountMenu)
themeMenu = Menu(rootMenu, tearoff=OFF)
rootMenu.add_cascade(label="Themes", menu=themeMenu)
toolMenu = Menu(rootMenu, tearoff=OFF)
rootMenu.add_cascade(label="Tools", menu=toolMenu)


def createDataFolder():
    os.mkdir("C:\\Employee Management System")


def connection(dataBaseName):
    connectionObject = sqlite3.connect(
        f"C:\\Employee Management System\\{dataBaseName}")
    return connectionObject


def themeChanger(nameOfTheme):
    global currentActivebackgroundColour, currentActiveforegroundColour, currentTheme

    nameOfTheme = str(nameOfTheme).split()
    currentTheme = nameOfTheme[0]
    themeMenu.config(background=colourForMenu[currentTheme])
    accountMenu.config(background=colourForMenu[currentTheme])
    toolMenu.config(background=colourForMenu[currentTheme])
    currentActivebackgroundColour = colourForMenuActiveBackground[currentTheme]
    currentActiveforegroundColour = colourForMenuActiveForeground[currentTheme]
    elementOfMenuElement()

    if currentWindow == "loginWindow":
        try:
            duplicateFrameOfLoginFrame.destroy()
        except AttributeError:
            pass
        loginFrame()
    elif currentWindow == "signUpWindow":
        duplicateFrameOfSignUpFrame.destroy()
        signUpWindow()
    elif currentWindow == "changePasswordWindow":
        duplicateFrameOfChangePasswordFrame.destroy()
        changePasswordWindow()
    elif currentWindow == "forgotPasswordWindow":
        duplicateFrameOfForgotPasswordFrame.destroy()
        forgotPasswordWindow()
    elif currentWindow == "mainWindow":
        duplicateFrameOfFrameA.destroy()
        duplicateFrameOfFrameB.destroy()
        duplicateFrameOfFrameC.destroy()
        duplicateFrameOfFrameD.destroy()
        duplicateFrameOfFrameE.destroy()
        duplicateFrameOfFrameEA.destroy()
        duplicateFrameOfFrameF.destroy()
        mainWindow()
    elif currentWindow == "salaryManagementWindow":
        duplicateFrameOfFrameSalaryA.destroy()
        duplicateFrameOfFrameSalaryB.destroy()
        duplicateFrameOfFrameSalaryC.destroy()
        duplicateFrameOfFrameSalaryD.destroy()
        duplicateFrameOfFrameSalaryE.destroy()
        duplicateFrameOfFrameSalaryF.destroy()
        salaryMangementSystemWindow()


def elementOfMenuElement():

    def callWindow(num):
        try:
            duplicateFrameOfLoginFrame.destroy()
        except AttributeError:
            pass
        if num == 1:
            signUpWindow()
        elif num == 2:
            changePasswordWindow()
        elif num == 3:
            forgotPasswordWindow()

    def tools(num):
        if num == 1:
            calc.calculator()

    themeMenu.delete(0, 5)
    accountMenu.delete(0, 2)
    toolMenu.delete(0)

    themeMenu.add_cascade(label="Rose",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Rose theme"))

    themeMenu.add_cascade(label="Sky",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Sky theme"))

    themeMenu.add_cascade(label="Lemon",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Lemon theme"))

    themeMenu.add_cascade(label="Nature",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Nature theme"))

    themeMenu.add_cascade(label="Dark",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Dark theme"))

    themeMenu.add_cascade(label="Light (Default)",
                          activebackground=currentActivebackgroundColour,
                          activeforeground=currentActiveforegroundColour,
                          command=lambda: themeChanger("Light theme"))

    accountMenu.add_cascade(label="Create Account",
                            activebackground=currentActivebackgroundColour,
                            activeforeground=currentActiveforegroundColour,
                            command=lambda: callWindow(1))

    accountMenu.add_cascade(label="Change Password",
                            activebackground=currentActivebackgroundColour,
                            activeforeground=currentActiveforegroundColour,
                            command=lambda: callWindow(2))

    accountMenu.add_cascade(label="Forgot Password",
                            activebackground=currentActivebackgroundColour,
                            activeforeground=currentActiveforegroundColour,
                            command=lambda: callWindow(3))
    toolMenu.add_cascade(label="Calculator",
                         activebackground=currentActivebackgroundColour,
                         activeforeground=currentActiveforegroundColour,
                         command=lambda: tools(1))


def mainFunction():
    try:
        createDataFolder()
    except FileExistsError:
        pass
    connectionObjectOfUserDataDatabase = connection("USERDATA.db")
    cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()
    try:
        cursorOfMainDatabase.execute('''
        CREATE TABLE DATAOFUSER(
        userName varchar(50),
        password varchar(50),
        sequrityQuestion varchar(50)
        );
        ''')
    except sqlite3.OperationalError:
        pass
    cursorOfMainDatabase.close()
    connectionObjectOfUserDataDatabase.close()
    themeChanger("Light theme")


def idVerificationOfUserId(conditionalNumber, functionNumber=1):
    returnValue = None
    userNameList = []
    symbolFound = False
    spaceFound = False
    punctuation = ["!", "#", "$", "%", "&", "\\", "'", '"', "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<",
                   "=", ">", "?", "@", "[", "]", "^", "`", "{", "|", "}", "~"]

    if conditionalNumber == 1:
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()
        userName = textVar3.get()
        fetchedData = cursorOfMainDatabase.execute('''
                        SELECT * FROM DATAOFUSER ;
                        ''').fetchall()
        for element in fetchedData:
            userNameList.append(element[0])
        for character in userName:
            for symbol in punctuation:
                if character == symbol:
                    symbolFound = True
                    break
        for character in userName:
            if character == " ":
                spaceFound = True
                break
        if userName.isdigit() == True:
            messagebox.showerror(
                title="Invalid Entry", message="User name does not contain only numbers.")
        elif symbolFound == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not cointain any special symbol.")
        elif userName.isspace() == True:
            messagebox.showerror(
                title="Invalid Entry", message="User name does not contain only space.")
        elif spaceFound == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not cointain any space.")
        elif userName.isupper() == False:
            messagebox.showerror(
                title="Invalid Entry", message="All Character in user name is in uppercase.")
        elif len(userName) == 0:
            messagebox.showerror(
                title="Invalid Entry", message="Please enter the combination of characters(Uppercase) and numeric value.")
        elif userName.isupper() == True and userName.isspace() == False:
            if len(userNameList) != 0:
                for element in userNameList:
                    if element == userName:
                        returnValue = True
                        break
                else:
                    returnValue = False
            else:
                returnValue = False
        cursorOfMainDatabase.close()
        connectionObjectOfUserDataDatabase.close()

    if conditionalNumber == 2:
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()
        if functionNumber == 1:
            userName = textVar7.get()
        elif functionNumber == 2:
            userName = textVar11.get()
        elif functionNumber == 3:
            userName = textVar1.get()
        fetchedData = cursorOfMainDatabase.execute('''
                        SELECT * FROM DATAOFUSER ;
                        ''').fetchall()
        for element in fetchedData:
            userNameList.append(element[0])
        if len(userNameList) != 0:
            for element in userNameList:
                if element == userName:
                    returnValue = True
                    break
            else:
                returnValue = False
        else:
            returnValue = False
        cursorOfMainDatabase.close()
        connectionObjectOfUserDataDatabase.close()

    return returnValue


def createUserDatabaseTable(user):
    connectionObjectOfSingleUserDataDatabase = connection(
        f"_{user}_DataBase.db")
    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
    cursorOfSingleUserDatabase.execute('''
    CREATE TABLE EMPLOYEEDATA(
        employeeId varchar(50),
        name varchar(50),
        designation varchar(50),
        address varchar(50),
        gmail varchar(50),
        contactNumber varchar(50),
        salary varchar(50)
        );
    ''')
    cursorOfSingleUserDatabase.close()
    connectionObjectOfSingleUserDataDatabase.close()


def createEmployeeDatabaseTable(user, emp):
    connectionObjectOEmployeeDataDatabase = connection(f"_{user}_DataBase.db")
    cursorOfEmployeeDatabase = connectionObjectOEmployeeDataDatabase.cursor()
    cursorOfEmployeeDatabase.execute(f'''
    CREATE TABLE SALARYTRANSACTIONTABLE_{emp}(
        transactionId varhar(50),
        date varhar(50),
        time varhar(50),
        amount varhar(50)
        );
    ''')
    cursorOfEmployeeDatabase.close()
    connectionObjectOEmployeeDataDatabase.close()


def loginFrame():
    global currentWindow, duplicateFrameOfLoginFrame, appWidth, appHeigth

    def signInProcess():
        global user
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()
        userName = textVar1.get()
        password = textVar2.get()
        passwordList = []
        userNameList = []
        fetchedData = cursorOfMainDatabase.execute('''
                        SELECT * FROM DATAOFUSER ;
                        ''').fetchall()

        for element in fetchedData:
            userNameList.append(element[0])
            passwordList.append(element[1])
        if userName != "" and password != "":
            idVerificationValue = idVerificationOfUserId(2, 3)
            if idVerificationValue == True:
                userNameIndex = userNameList.index(userName)
                if password == passwordList[userNameIndex]:
                    user = userName
                    textVar1.set("")
                    textVar2.set("")
                    cursorOfMainDatabase.close()
                    connectionObjectOfUserDataDatabase.close()
                    mainWindow()
                else:
                    messagebox.showerror(
                        title="Invalid Entry", message="Entered Password is incorrect")
            elif idVerificationValue == False:
                messagebox.showerror(title="Invalid Entry",
                                     message="Entered User name not found")
        else:
            if userName == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill User Name Entry")
            elif password == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Password Entry")
        try:
            cursorOfMainDatabase.close()
            connectionObjectOfUserDataDatabase.close()
        except sqlite3.ProgrammingError:
            pass

    appWidth = 550
    appHeigth = 400
    root.geometry(
        f"{appWidth}x{appHeigth}+{int((screenWidth - appWidth)/2)}+{int((screenHeight - appHeigth)/5)}")
    textVar1.set("")
    textVar2.set("")
    loginFrame_ = Frame(root, background=colourForWindow[currentTheme])
    loginFrame_.place(x=0, y=0, width=appWidth, height=appHeigth)

    root.title("Employee Management System")
    currentWindow = "loginWindow"
    duplicateFrameOfLoginFrame = loginFrame_

    frameLable = Label(loginFrame_,
                       text="SIGN IN",
                       font=("Bahnschrift", 30),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    frameLable.place(x=200, y=20)

    userNameLable = Label(loginFrame_,
                          text="User Name :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    userNameLable.place(x=80, y=115)

    passwordLable = Label(loginFrame_,
                          text="Password    :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    passwordLable.place(x=80, y=165)

    userNameEntry = Entry(loginFrame_,
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar1)
    userNameEntry.place(x=210, y=118)

    passwordEntry = Entry(loginFrame_,
                          show="*",
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar2)
    passwordEntry.place(x=210, y=168)

    signInBtn = Button(loginFrame_,
                       text="Sign In",
                       cursor="hand2",
                       width=41,
                       height=1,
                       background=colourForButtonBackground[currentTheme],
                       foreground=colourForButtonForeground[currentTheme],
                       activebackground=colourForButtonActiveBackground[currentTheme],
                       font=("Bahnschrift", 13),
                       command=signInProcess)
    signInBtn.place(x=80, y=230)


def signUpWindow():
    global currentWindow, duplicateFrameOfSignUpFrame, appHeigth, appWidth

    def backToPriviousMenu():
        signUpFrame_.destroy()
        for element in item:
            accountMenu.entryconfig(element, state="active")
        loginFrame()

    def signUpProcess():
        global user
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()
        userName = textVar3.get()
        password = textVar4.get()
        renteredPassword = textVar5.get()
        sequrityQuestion = textVar6.get()
        if userName != "" and password != "" and renteredPassword != "" and sequrityQuestion != "":
            idVerificationValue = idVerificationOfUserId(1)
            if idVerificationValue == False:
                if password == renteredPassword:
                    cursorOfMainDatabase.execute('''
                    INSERT INTO DATAOFUSER
                    VALUES (?,?,?)
                    ''', (userName, password, sequrityQuestion))
                    connectionObjectOfUserDataDatabase.commit()
                    user = userName
                    textVar3.set("")
                    textVar4.set("")
                    textVar5.set("")
                    textVar6.set("Sequrity Question")
                    createUserDatabaseTable(userName)
                    cursorOfMainDatabase.close()
                    connectionObjectOfUserDataDatabase.close()
                    mainWindow()
                else:
                    messagebox.showerror(
                        title="Invalid Entry", message="Renterd password not match")
            elif idVerificationValue == True:
                messagebox.showerror(title="Invalid Entry",
                                     message="Entered User Name Already Exists")
        else:
            if userName == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill User Name Entry")
            elif password == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Password Entry")
            elif renteredPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Renterd Password Entry")
            elif sequrityQuestion == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Squrity Qusetion Entry")
        try:
            cursorOfMainDatabase.close()
            connectionObjectOfUserDataDatabase.close()
        except sqlite3.ProgrammingError:
            pass

    root.title("Employee Management System - Sign Up")

    signUpFrame_ = Frame(root, background=colourForWindow[currentTheme])
    signUpFrame_.place(x=0, y=0, width=appWidth, height=appHeigth)

    for element in item:
        accountMenu.entryconfig(element, state="disable")
    currentWindow = "signUpWindow"
    duplicateFrameOfSignUpFrame = signUpFrame_

    frameLable = Label(signUpFrame_,
                       text="SIGN UP",
                       font=("Bahnschrift", 30),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    frameLable.place(x=200, y=20)

    userNameLable = Label(signUpFrame_,
                          text="User Name                                      :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    userNameLable.place(x=30, y=115)

    passwordLable = Label(signUpFrame_,
                          text="Password                                         :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    passwordLable.place(x=30, y=165)

    reEnterPasswordLable = Label(signUpFrame_,
                                 text="Renter Password                   :",
                                 font=("Bahnschrift", 15),
                                 background=colourForLableBackground[currentTheme],
                                 foreground=colourForLableForeground[currentTheme])
    reEnterPasswordLable.place(x=30, y=215)

    sequrityQuestionLable = Label(signUpFrame_,
                                  text="Your Favorite Teacher  \n Name",
                                  font=("Bahnschrift", 15),
                                  background=colourForLableBackground[currentTheme],
                                  foreground=colourForLableForeground[currentTheme])
    sequrityQuestionLable.place(x=30, y=250)

    colenLable = Label(signUpFrame_, text=":",
                       font=("Bahnschrift", 15),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    colenLable.place(x=240, y=263)

    userNameEntry = Entry(signUpFrame_,
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar3)
    userNameEntry.place(x=260, y=118)

    passwordEntry = Entry(signUpFrame_,
                          show="*",
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar4)
    passwordEntry.place(x=260, y=168)

    reEnterPasswordEntry = Entry(signUpFrame_,
                                 show="*",
                                 width=27,
                                 font=("Bahnschrift", 13),
                                 background=colourForEntryBackground[currentTheme],
                                 foreground=colourForEntryForeground[currentTheme],
                                 textvariable=textVar5)
    reEnterPasswordEntry.place(x=260, y=218)

    sequrityQuestionEntry = Entry(signUpFrame_,
                                  width=27,
                                  font=("Bahnschrift", 13),
                                  background=colourForEntryBackground[currentTheme],
                                  foreground=colourForEntryForeground[currentTheme],
                                  textvariable=textVar6)
    textVar6.set("Sequrity Question")
    sequrityQuestionEntry.place(x=260, y=268)

    signUpBtn = Button(signUpFrame_,
                       text="Sign Up",
                       cursor="hand2",
                       width=52,
                       height=1,
                       background=colourForButtonBackground[currentTheme],
                       foreground=colourForButtonForeground[currentTheme],
                       activebackground=colourForButtonActiveBackground[currentTheme],
                       font=("Bahnschrift", 13),
                       command=signUpProcess)
    signUpBtn.place(x=30, y=318)

    backBtn = Button(signUpFrame_,
                     text="<─",
                     cursor="hand2",
                     bd=0,
                     background=colourForBackButtonBackground[currentTheme],
                     foreground=colourForBackButtonForeground[currentTheme],
                     activebackground=colourForBackButtonActiveBackground[currentTheme],
                     font=("Bahnschrift", 13),
                     command=backToPriviousMenu)
    backBtn.place(x=0, y=0)


def changePasswordWindow():
    global currentWindow, duplicateFrameOfChangePasswordFrame, appWidth, appHeigth

    def backToPriviousMenu():
        changePasswordFrame_.destroy()
        for element in item:
            accountMenu.entryconfig(element, state="active")
        loginFrame()

    def changePasswordProcess():
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()

        userNameList = []
        passwordList = []
        userName = textVar7.get()
        oldPassword = textVar8.get()
        newPassword = textVar9.get()
        renteredNewPassword = textVar10.get()
        fetchedData = cursorOfMainDatabase.execute('''
                        SELECT * FROM DATAOFUSER ;
                        ''').fetchall()

        for element in fetchedData:
            userNameList.append(element[0])
            passwordList.append(element[1])

        if userName != "" and oldPassword != "" and renteredNewPassword != "" and newPassword != "":
            idVerificationValue = idVerificationOfUserId(2)
            if idVerificationValue == True:
                userNameIndex = userNameList.index(userName)
                if oldPassword == passwordList[userNameIndex]:
                    if newPassword == renteredNewPassword:
                        cursorOfMainDatabase.execute('''
                        UPDATE DATAOFUSER
                        SET password = ?
                        WHERE userName = ?;
                        ''', (newPassword, userName))
                        connectionObjectOfUserDataDatabase.commit()
                        textVar7.set("")
                        textVar8.set("")
                        textVar9.set("")
                        textVar10.set("")
                        messagebox.showinfo(
                            title="Process Complete Info", message="User account password change succesfully")
                    else:
                        messagebox.showerror(
                            title="Invalid Entry Error", message="Rentered Password not match")
                else:
                    messagebox.showerror(
                        title="Invalid Entry Error", message="Entered Password is incorrect")
            elif idVerificationValue == False:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Entered User name not found")
        else:
            if userName == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill User Name Entry")
            elif oldPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Old Password Entry")
            elif renteredNewPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Rentered New Password Entry")
            elif newPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill New Password Entry")

        cursorOfMainDatabase.close()
        connectionObjectOfUserDataDatabase.close()

    root.title("Employee Management System - Change Password")

    changePasswordFrame_ = Frame(
        root, background=colourForWindow[currentTheme])
    changePasswordFrame_.place(x=0, y=0, width=appWidth, height=appHeigth)

    for element in item:
        accountMenu.entryconfig(element, state="disable")
    currentWindow = "changePasswordWindow"
    duplicateFrameOfChangePasswordFrame = changePasswordFrame_

    frameLable = Label(changePasswordFrame_,
                       text="CHANGE PASSWORD",
                       font=("Bahnschrift", 30),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    frameLable.place(x=90, y=20)

    userNameLable = Label(changePasswordFrame_,
                          text="User Name                    :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    userNameLable.place(x=60, y=115)

    passwordLable = Label(changePasswordFrame_,
                          text="Old Password            :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    passwordLable.place(x=60, y=165)

    newPasswordLable = Label(changePasswordFrame_,
                             text="New Password         :",
                             font=("Bahnschrift", 15),
                             background=colourForLableBackground[currentTheme],
                             foreground=colourForLableForeground[currentTheme])
    newPasswordLable.place(x=60, y=215)

    renterNewPasswordLable = Label(changePasswordFrame_,
                                   text="Renter Password  :",
                                   font=("Bahnschrift", 15),
                                   background=colourForLableBackground[currentTheme],
                                   foreground=colourForLableForeground[currentTheme])
    renterNewPasswordLable.place(x=60, y=265)

    userNameEntry = Entry(changePasswordFrame_,
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar7)
    userNameEntry.place(x=230, y=118)

    passwordEntry = Entry(changePasswordFrame_,
                          show="*",
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar8)
    passwordEntry.place(x=230, y=168)

    newPasswordEntry = Entry(changePasswordFrame_,
                             show="*",
                             width=27,
                             font=("Bahnschrift", 13),
                             background=colourForEntryBackground[currentTheme],
                             foreground=colourForEntryForeground[currentTheme],
                             textvariable=textVar9)
    newPasswordEntry.place(x=230, y=218)

    renterNewPasswordEntry = Entry(changePasswordFrame_,
                                   show="*",
                                   width=27,
                                   font=("Bahnschrift", 13),
                                   background=colourForEntryBackground[currentTheme],
                                   foreground=colourForEntryForeground[currentTheme],
                                   textvariable=textVar10)
    renterNewPasswordEntry.place(x=230, y=268)

    changePasswordBtn = Button(changePasswordFrame_,
                               text="Change Password",
                               cursor="hand2",
                               width=45,
                               height=1,
                               background=colourForButtonBackground[currentTheme],
                               foreground=colourForButtonForeground[currentTheme],
                               activebackground=colourForButtonActiveBackground[currentTheme],
                               font=("Bahnschrift", 13),
                               command=changePasswordProcess)
    changePasswordBtn.place(x=60, y=310)

    backBtn = Button(changePasswordFrame_,
                     text="<─",
                     cursor="hand2",
                     bd=0,
                     background=colourForBackButtonBackground[currentTheme],
                     foreground=colourForBackButtonForeground[currentTheme],
                     activebackground=colourForBackButtonActiveBackground[currentTheme],
                     font=("Bahnschrift", 13),
                     command=backToPriviousMenu)
    backBtn.place(x=0, y=0)


def forgotPasswordWindow():
    global currentWindow, duplicateFrameOfForgotPasswordFrame, appHeigth, appWidth

    def backToPriviousMenu():
        forgotPasswordFrame_.destroy()
        for element in item:
            accountMenu.entryconfig(element, state="active")
        loginFrame()

    def changePasswordProcess():
        connectionObjectOfUserDataDatabase = connection("USERDATA.db")
        cursorOfMainDatabase = connectionObjectOfUserDataDatabase.cursor()

        userNameList = []
        sequrityQuestionList = []
        userName = textVar11.get()
        sequrityQuestion = textVar12.get()
        newPassword = textVar13.get()
        renteredNewPassword = textVar14.get()
        fetchedData = cursorOfMainDatabase.execute('''
                        SELECT * FROM DATAOFUSER ;
                        ''').fetchall()

        for element in fetchedData:
            userNameList.append(element[0])
            sequrityQuestionList.append(element[2])

        if userName != "" and sequrityQuestion != "" and renteredNewPassword != "" and newPassword != "":
            idVerificationValue = idVerificationOfUserId(2, 2)
            if idVerificationValue == True:
                userNameIndex = userNameList.index(userName)
                if sequrityQuestion == sequrityQuestionList[userNameIndex]:
                    if newPassword == renteredNewPassword:
                        cursorOfMainDatabase.execute('''
                        UPDATE DATAOFUSER
                        SET password = ?
                        WHERE userName = ?;
                        ''', (newPassword, userName))
                        connectionObjectOfUserDataDatabase.commit()
                        textVar11.set("")
                        textVar12.set("Sequrity Question")
                        textVar13.set("")
                        textVar14.set("")
                        messagebox.showinfo(
                            title="Process Complete Info", message="User account password change succesfully")
                    else:
                        messagebox.showerror(
                            title="Invalid Entry Error", message="Rentered Password not match")
                else:
                    messagebox.showerror(
                        title="Invalid Entry Error", message="Entered Answer of sequrity question is incorrect")
            elif idVerificationValue == False:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Entered User name not found")
        else:
            if userName == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill User Name Entry")
            elif sequrityQuestion == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Old Password Entry")
            elif renteredNewPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Rentered New Password Entry")
            elif newPassword == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill New Password Entry")

        cursorOfMainDatabase.close()
        connectionObjectOfUserDataDatabase.close()
    root.title("Employee Management System - Forgot Password")

    forgotPasswordFrame_ = Frame(
        root, background=colourForWindow[currentTheme])
    forgotPasswordFrame_.place(x=0, y=0, width=appWidth, height=appHeigth)

    for element in item:
        accountMenu.entryconfig(element, state="disable")
    currentWindow = "forgotPasswordWindow"
    duplicateFrameOfForgotPasswordFrame = forgotPasswordFrame_

    frameLable = Label(forgotPasswordFrame_,
                       text="FORGOT PASSWORD",
                       font=("Bahnschrift", 30),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    frameLable.place(x=90, y=20)

    userNameLable = Label(forgotPasswordFrame_,
                          text="User Name                                     :",
                          font=("Bahnschrift", 15),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    userNameLable.place(x=30, y=115)

    sequrityQuestionLable = Label(forgotPasswordFrame_,
                                  text="Your Favorite Teacher\nName",
                                  font=("Bahnschrift", 15),
                                  background=colourForLableBackground[currentTheme],
                                  foreground=colourForLableForeground[currentTheme])
    sequrityQuestionLable.place(x=30, y=148)

    colenLable = Label(forgotPasswordFrame_,
                       text=":",
                       font=("Bahnschrift", 15),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    colenLable.place(x=240, y=165)

    newPasswordLable = Label(forgotPasswordFrame_,
                             text="New Password                          :",
                             font=("Bahnschrift", 15),
                             background=colourForLableBackground[currentTheme],
                             foreground=colourForLableForeground[currentTheme])
    newPasswordLable.place(x=30, y=215)

    renterNewPasswordLable = Label(forgotPasswordFrame_,
                                   text="Renter Password                   :",
                                   font=("Bahnschrift", 15),
                                   background=colourForLableBackground[currentTheme],
                                   foreground=colourForLableForeground[currentTheme])
    renterNewPasswordLable.place(x=30, y=265)

    userNameEntry = Entry(forgotPasswordFrame_,
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar11)
    userNameEntry.place(x=260, y=118)

    sequrityQuestionEntry = Entry(forgotPasswordFrame_,
                                  width=27,
                                  font=("Bahnschrift", 13),
                                  background=colourForEntryBackground[currentTheme],
                                  foreground=colourForEntryForeground[currentTheme],
                                  textvariable=textVar12)
    textVar12.set("Sequrity Question")
    sequrityQuestionEntry.place(x=260, y=168)

    passwordEntry = Entry(forgotPasswordFrame_,
                          show="*",
                          width=27,
                          font=("Bahnschrift", 13),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar13)
    passwordEntry.place(x=260, y=218)

    reEnterPasswordEntry = Entry(forgotPasswordFrame_,
                                 show="*",
                                 width=27,
                                 font=("Bahnschrift", 13),
                                 background=colourForEntryBackground[currentTheme],
                                 foreground=colourForEntryForeground[currentTheme],
                                 textvariable=textVar14)
    reEnterPasswordEntry.place(x=260, y=268)

    changePasswordBtn = Button(forgotPasswordFrame_,
                               text="CHANGE PASSWORD",
                               cursor="hand2",
                               width=52,
                               height=1,
                               background=colourForButtonBackground[currentTheme],
                               activebackground=colourForButtonActiveBackground[currentTheme],
                               foreground=colourForButtonForeground[currentTheme],
                               font=("Bahnschrift", 13),
                               command=changePasswordProcess)
    changePasswordBtn.place(x=30, y=318)

    backBtn = Button(forgotPasswordFrame_,
                     text="<─",
                     cursor="hand2",
                     bd=0,
                     background=colourForBackButtonBackground[currentTheme],
                     foreground=colourForBackButtonForeground[currentTheme],
                     font=("Bahnschrift", 13),
                     command=backToPriviousMenu)
    backBtn.place(x=0, y=0)


def idVerificationOfEmployeeId(conditionalNumber, functionNumber=1):
    returnValue = None
    userIdList = []
    symbolFound = False
    spaceFound = False
    punctuation = ["!", "#", "$", "%", "&", "\\", "'", '"',
                   "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "`", "{", "|", "}", "~"]
    if conditionalNumber == 1:
        connectionObjectOfSingleUserDataDatabase = connection(
            f"_{user}_DataBase.db")
        cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
        userName = textVar15.get()
        fetchedData = cursorOfSingleUserDatabase.execute('''
                        SELECT * FROM EMPLOYEEDATA ;
                        ''').fetchall()
        for element in fetchedData:
            userIdList.append(element[0])
        for character in userName:
            for symbol in punctuation:
                if character == symbol:
                    symbolFound = True
                    break
        for character in userName:
            if character == " ":
                spaceFound = True
                break
        if userName.isdigit() == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not contain only numbers.")
        elif symbolFound == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not cointain any special symbol.")
        elif userName.isspace() == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not contain only space.")
        elif spaceFound == True:
            messagebox.showerror(
                title="Invalid Entry", message="Employee Id does not cointain any space.")
        elif userName.isupper() == False:
            messagebox.showerror(
                title="Invalid Entry", message="All Character in user name is in uppercase.")
        elif len(userName) == 0:
            messagebox.showerror(
                title="Invalid Entry", message="Please enter the combination of characters(Uppercase) and numeric value.")
        elif userName.isupper() == True and userName.isspace() == False:
            if len(userIdList) != 0:
                for element in userIdList:
                    if element == userName:
                        returnValue = True
                        break
                else:
                    returnValue = False
            else:
                returnValue = False
        cursorOfSingleUserDatabase.close()
        connectionObjectOfSingleUserDataDatabase.close()

    elif conditionalNumber == 2:
        connectionObjectOfSingleUserDataDatabase = connection(
            f"_{user}_DataBase.db")
        cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
        if functionNumber == 1:
            userName = textVar22.get()
        elif functionNumber == 2:
            userName = textVar25.get()
        elif functionNumber == 3:
            userName = textVar26.get()
        elif functionNumber == 4:
            userName = textVar33.get()
        elif functionNumber == 5:
            userName = textVar38.get()
        elif functionNumber == 6:
            userName = textVar40.get()
        elif functionNumber == 7:
            userName = textVar42.get()
        fetchedData = cursorOfSingleUserDatabase.execute('''
                        SELECT * FROM EMPLOYEEDATA ;
                        ''').fetchall()
        for element in fetchedData:
            userIdList.append(element[0])
        if len(userIdList) != 0:
            for element in userIdList:
                if element == userName:
                    returnValue = True
                    break
            else:
                returnValue = False
        else:
            returnValue = False
        cursorOfSingleUserDatabase.close()
        connectionObjectOfSingleUserDataDatabase.close()
    return returnValue


def mainWindow():
    global currentWindow, appHeigth, appWidth, duplicateFrameOfFrameA, duplicateFrameOfFrameB, duplicateFrameOfFrameC, duplicateFrameOfFrameD, duplicateFrameOfFrameE, duplicateFrameOfFrameEA, duplicateFrameOfFrameF

    duplicateFrameOfLoginFrame.destroy()

    def logOut():
        global appHeigth, appWidth, user
        appWidth = 550
        appHeigth = 400
        root.geometry(
            f"{appWidth}x{appHeigth}+{int((screenWidth - appWidth)/2)}+{int((screenHeight - appHeigth)/5)}")
        frameA.destroy()
        frameB.destroy()
        frameC.destroy()
        frameD.destroy()
        frameE.destroy()
        frameEA.destroy()
        frameF.destroy()
        for element in item:
            accountMenu.entryconfig(element, state="active")
        listOfStringVar = [textVar1, textVar2, textVar3, textVar4, textVar5, textVar6, textVar7, textVar8, textVar9, textVar10, textVar11, textVar12,
                           textVar13, textVar14, textVar15, textVar16, textVar17, textVar18, textVar19, textVar20, textVar21, textVar22, textVar23, textVar24]
        for element in listOfStringVar:
            element.set("")
        user = None
        loginFrame()

    def salaryMangementSystemWindowOpen():
        frameA.destroy()
        frameB.destroy()
        frameC.destroy()
        frameD.destroy()
        frameE.destroy()
        frameF.destroy()
        salaryMangementSystemWindow()

    def hoverOnBtn(a):
        if a == 1:
            salaryManagementSystemJumpBtn.config(
                background=colourForLowerMenuOnHoverBackground[currentTheme], foreground=colourForLowerMenuOnHoverForeground[currentTheme])
        elif a == 2:
            salaryManagementSystemJumpBtn.config(
                background=colourForLowerMenuBackground[currentTheme], foreground=colourForLableForeground[currentTheme])
        elif a == 5:
            logOutBtn.config(
                background=colourForLowerMenuOnHoverBackground[currentTheme], foreground=colourForLowerMenuOnHoverForeground[currentTheme])
        elif a == 6:
            logOutBtn.config(
                background=colourForLowerMenuBackground[currentTheme], foreground=colourForLableForeground[currentTheme])

    root.title("Employee Management System - Control Center")

    frameA = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameA.place(x=0, y=0, width=384, height=325)

    frameB = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameB.place(x=384, y=0, width=384, height=325)

    frameC = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameC.place(x=768, y=0, width=384, height=325)

    frameD = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameD.place(x=0, y=325, width=384, height=295)

    frameE = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameE.place(x=384, y=325, width=768, height=295)

    frameEA = Frame(frameE,
                    background=colourForWindow[currentTheme])
    frameEA.place(x=0, y=40, width=764, height=250)

    frameF = Frame(root,
                   background=colourForWindow[currentTheme],
                   highlightbackground=colourForFrameHighlightBackground[currentTheme],
                   highlightthickness=2)
    frameF.place(x=0, y=620, width=1152, height=30)

    appWidth = 1152
    appHeigth = 650

    root.geometry(
        f"{appWidth}x{appHeigth}+{int((screenWidth - appWidth)/2)}+{int((screenHeight - appHeigth)/5)}")

    for element in item:
        accountMenu.entryconfig(element, state="disable")

    currentWindow = "mainWindow"
    duplicateFrameOfFrameA = frameA
    duplicateFrameOfFrameB = frameB
    duplicateFrameOfFrameC = frameC
    duplicateFrameOfFrameD = frameD
    duplicateFrameOfFrameE = frameE
    duplicateFrameOfFrameEA = frameEA
    duplicateFrameOfFrameF = frameF

    def contactNumberVerification(contactNumber):
        returnValue = None
        contactNumberB = contactNumber.isdigit()
        if (contactNumberB == True):
            contactNumberC = int(contactNumber)
            if (contactNumberC > 999999999) and (contactNumberC < 10000000000):
                returnValue = True
            elif(len(contactNumber) == 10 and contactNumberC <= 999999999):
                messagebox.showerror(
                    title="Invalid Entry Error", message="Contact number can't be exixt")
            else:
                messageDisplay = str("Contact number is not a 10 digit Number you enter a " +
                                     str(len(str(contactNumber))) + " digit no. Please, Enter a valid number")
                messagebox.showerror(
                    title="Invalid Entry Error", message=messageDisplay)
        else:
            messagebox.showerror(
                title="Invalid Entry Error", message="Please, Enter only Numeric value in Contact number entry")
        return returnValue

    def addEmployeeProcess():
        empId = textVar15.get()
        empName = textVar16.get()
        empDesignation = textVar17.get()
        empAddress = textVar18.get()
        empGmail = textVar19.get()
        empContactNumber = textVar20.get()
        empSalary = textVar21.get()
        if empId != "" and empName != "" and empDesignation != "" and empAddress != "" and empGmail != "" and empContactNumber != "" and empSalary != "":
            idVerificationValue = idVerificationOfEmployeeId(1)
            if idVerificationValue == False:
                contactNumberVerificationValue = contactNumberVerification(
                    empContactNumber)
                if contactNumberVerificationValue == True:
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    cursorOfSingleUserDatabase.execute('''
                    INSERT INTO EMPLOYEEDATA
                    VALUES (?,?,?,?,?,?,?)
                    ''', (empId, empName, empDesignation, empAddress, empGmail, empContactNumber, empSalary))
                    connectionObjectOfSingleUserDataDatabase.commit()
                    messagebox.showinfo(
                        title="Process Complete Info", message="Employee details added succesfully")
                    textVar15.set("")
                    textVar16.set("")
                    textVar17.set("")
                    textVar18.set("")
                    textVar19.set("@gmail.com")
                    textVar20.set("")
                    textVar21.set("\u20B9")
                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                    createEmployeeDatabaseTable(user, empId)
            elif idVerificationValue == True:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Employee Id Already Exists")
        else:
            if empId == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Id Entry")
            elif empName == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Name Entry")
            elif empDesignation == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Designation Entry")
            elif empAddress == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Address Entry")
            elif empGmail == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Gmail Entry")
            elif empContactNumber == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Contact Number Entry")
            elif empSalary == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Salary Entry")

    frameALable = Label(frameA,
                        text="ADD EMPLOYEE DETAILS",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameALable.place(x=75, y=5)

    empIdLable = Label(frameA,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    empNameLable = Label(frameA,
                         text="Name                                     :",
                         font=("Bahnschrift", 12),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme])
    empNameLable.place(x=30, y=80)

    empDesignationLable = Label(frameA,
                                text="Designation                       :",
                                font=("Bahnschrift", 12),
                                background=colourForLableBackground[currentTheme],
                                foreground=colourForLableForeground[currentTheme])
    empDesignationLable.place(x=30, y=110)

    empAddressLable = Label(frameA,
                            text="Address                                :",
                            font=("Bahnschrift", 12),
                            background=colourForLableBackground[currentTheme],
                            foreground=colourForLableForeground[currentTheme])
    empAddressLable.place(x=30, y=140)

    empGmailLable = Label(frameA,
                          text="Gmail                                      :",
                          font=("Bahnschrift", 12),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    empGmailLable.place(x=30, y=170)

    empContactNumberLable = Label(frameA,
                                  text="Contact Number             :",
                                  font=("Bahnschrift", 12),
                                  background=colourForLableBackground[currentTheme],
                                  foreground=colourForLableForeground[currentTheme])
    empContactNumberLable.place(x=30, y=200)

    empSalaryLable = Label(frameA,
                           text="Salary [Per month /-] :",
                           font=("Bahnschrift", 12),
                           background=colourForLableBackground[currentTheme],
                           foreground=colourForLableForeground[currentTheme])
    empSalaryLable.place(x=30, y=230)

    empIdEntry = Entry(frameA,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar15)
    empIdEntry.place(x=200, y=50)

    empNameEntry = Entry(frameA,
                         width=17,
                         font=("Bahnschrift", 12),
                         background=colourForEntryBackground[currentTheme],
                         foreground=colourForEntryForeground[currentTheme],
                         textvariable=textVar16)
    empNameEntry.place(x=200, y=80)

    empDesignationEntry = Entry(frameA,
                                width=17,
                                font=("Bahnschrift", 12),
                                background=colourForEntryBackground[currentTheme],
                                foreground=colourForEntryForeground[currentTheme],
                                textvariable=textVar17)
    empDesignationEntry.place(x=200, y=110)

    empAddressEntry = Entry(frameA,
                            width=17,
                            font=("Bahnschrift", 12),
                            background=colourForEntryBackground[currentTheme],
                            foreground=colourForEntryForeground[currentTheme],
                            textvariable=textVar18)
    empAddressEntry.place(x=200, y=140)

    empGmailEntry = Entry(frameA,
                          width=17,
                          font=("Bahnschrift", 12),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar19)
    textVar19.set("@gmail.com")
    empGmailEntry.place(x=200, y=170)

    empContactNumberEntry = Entry(frameA,
                                  width=17,
                                  font=("Bahnschrift", 12),
                                  background=colourForEntryBackground[currentTheme],
                                  foreground=colourForEntryForeground[currentTheme],
                                  textvariable=textVar20)
    empContactNumberEntry.place(x=200, y=200)

    empSalaryEntry = Entry(frameA,
                           width=17,
                           font=("Bahnschrift", 12),
                           background=colourForEntryBackground[currentTheme],
                           foreground=colourForEntryForeground[currentTheme],
                           textvariable=textVar21)
    textVar21.set("\u20B9")
    empSalaryEntry.place(x=200, y=230)

    addEmpDetailsBtn = Button(frameA,
                              text="Add Employee Details",
                              cursor="hand2",
                              width=45,
                              height=1,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 10),
                              command=addEmployeeProcess)
    addEmpDetailsBtn.place(x=30, y=270)

    frameBLable = Label(frameB,
                        text="UPDATE EMPLOYEE DETAILS",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameBLable.place(x=60, y=5)

    def updateDetailsProcess(field):
        global selectedField
        idVerificationValue = idVerificationOfEmployeeId(2, 1)

        def textVar23Update(field):
            connectionObjectOfSingleUserDataDatabase = connection(
                f"_{user}_DataBase.db")
            cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
            fetchedData = cursorOfSingleUserDatabase.execute(f'''
                          SELECT {field} FROM EMPLOYEEDATA
                          WHERE employeeId = ?;
                          ''', (textVar22.get(),)).fetchall()
            textVar23.set(fetchedData[0][0])
            cursorOfSingleUserDatabase.close()
            connectionObjectOfSingleUserDataDatabase.close()

        if idVerificationValue == True:
            if field == "Name":
                selectedField = "Name"
                textVar23Update("name")
                updateFieldOldLable.configure(
                    text="Old Name                            : ")
                updateFieldNewLable.configure(
                    text="New Name                         :")
            elif field == "Designation":
                selectedField = "Designation"
                textVar23Update("designation")
                updateFieldOldLable.configure(
                    text="Old Designation             : ")
                updateFieldNewLable.configure(
                    text="New Designation          :")
            elif field == "Address":
                selectedField = "Address"
                textVar23Update("address")
                updateFieldOldLable.configure(
                    text="Old Address                      : ")
                updateFieldNewLable.configure(
                    text="New Address                   :")
            elif field == "Gmail":
                selectedField = "Gmail"
                textVar23Update("gmail")
                textVar24.set("@gmail.com")
                updateFieldOldLable.configure(
                    text="Old Gmail                            : ")
                updateFieldNewLable.configure(
                    text="New Gmail                         :")
            elif field == "Contact":
                selectedField = "Contact"
                textVar23Update("contactNumber")
                updateFieldOldLable.configure(text="Old Contact Number    : ")
                updateFieldNewLable.configure(text="New Contact Number :")
            elif field == "Salary":
                selectedField = "Salary"
                textVar23Update("salary")
                textVar24.set("\u20B9")
                updateFieldOldLable.configure(
                    text="Old Salary                          : ")
                updateFieldNewLable.configure(
                    text="New Salary                       :")

        elif idVerificationValue == False:
            selectedField = ""
            textVar23.set("")
            updateFieldOldLable.configure(
                text="Old                                           :")
            updateFieldNewLable.configure(
                text="New                                        :")
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    def updateDetailsProcess2():
        global selectedField
        idVerificationValue = idVerificationOfEmployeeId(2, 1)
        columnName = ""
        if idVerificationValue == True:
            if selectedField != "":
                idEntryValue = textVar22.get()
                feildUpdateEntryValue = textVar24.get()
                if feildUpdateEntryValue != "":
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    if selectedField == "Name":
                        columnName = "name"
                    elif selectedField == "Designation":
                        columnName = "designation"
                    elif selectedField == "Address":
                        columnName = "address"
                    elif selectedField == "Gmail":
                        columnName = "gmail"
                    elif selectedField == "Contact":
                        columnName = "contactNumber"
                    elif selectedField == "Salary":
                        columnName = "salary"
                    if selectedField != "Contact":
                        cursorOfSingleUserDatabase.execute(f'''
                        UPDATE EMPLOYEEDATA
                        SET {columnName} = ?
                        WHERE employeeId = ?;
                        ''', (feildUpdateEntryValue, idEntryValue))
                        messagebox.showinfo(
                            title="Process Complete Info", message=f"Employee {columnName} updated succesfully")
                    elif selectedField == "Contact":
                        verification = contactNumberVerification(
                            feildUpdateEntryValue)
                        if verification == True:
                            cursorOfSingleUserDatabase.execute(f'''
                            UPDATE EMPLOYEEDATA
                            SET {columnName} = ?
                            WHERE employeeId = ?;
                            ''', (feildUpdateEntryValue, idEntryValue))
                            messagebox.showinfo(
                                title="Process Complete Info", message=f"Employee contact number updated succesfully")
                    textVar22.set("")
                    textVar23.set("")
                    textVar24.set("")
                    updateFieldOldLable.configure(
                        text="Old                                           :")
                    updateFieldNewLable.configure(
                        text="New                                        :")
                    selectedField = ""
                    connectionObjectOfSingleUserDataDatabase.commit()

                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                elif feildUpdateEntryValue == "":
                    messagebox.showerror(
                        title="Invalid Entry Error", message="Employee Id Not Exists")
            elif selectedField == "":
                messagebox.showerror(
                    title="Null Field Selection Error", message="Updation Field Not Selected")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    empIdLable = Label(frameB,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    updateFieldOldLable = Label(frameB,
                                text="Old                                           :",
                                font=("Bahnschrift", 12),
                                background=colourForLableBackground[currentTheme],
                                foreground=colourForLableForeground[currentTheme])
    updateFieldOldLable.place(x=30, y=155)

    updateFieldNewLable = Label(frameB,
                                text="New                                        :",
                                font=("Bahnschrift", 12),
                                background=colourForLableBackground[currentTheme],
                                foreground=colourForLableForeground[currentTheme])
    updateFieldNewLable.place(x=30, y=185)

    empIdEntry = Entry(frameB,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar22)
    empIdEntry.place(x=200, y=50)

    updateEmpNameBtn = Button(frameB,
                              text="Name",
                              cursor="hand2",
                              width=15,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 8),
                              command=lambda: updateDetailsProcess("Name"))
    updateEmpNameBtn.place(x=30, y=85)

    updateEmpDesignationBtn = Button(frameB,
                                     text="Designation",
                                     cursor="hand2",
                                     width=15,
                                     background=colourForButtonBackground[currentTheme],
                                     foreground=colourForButtonForeground[currentTheme],
                                     activebackground=colourForButtonActiveBackground[currentTheme],
                                     font=("Bahnschrift", 8),
                                     command=lambda: updateDetailsProcess("Designation"))
    updateEmpDesignationBtn.place(x=140, y=85)

    updateEmpAddressBtn = Button(frameB,
                                 text="Address",
                                 cursor="hand2",
                                 width=15,
                                 background=colourForButtonBackground[currentTheme],
                                 foreground=colourForButtonForeground[currentTheme],
                                 activebackground=colourForButtonActiveBackground[currentTheme],
                                 font=("Bahnschrift", 8),
                                 command=lambda: updateDetailsProcess("Address"))
    updateEmpAddressBtn.place(x=250, y=85)

    updateEmpGmailBtn = Button(frameB,
                               text="Gmail",
                               cursor="hand2",
                               width=15,
                               background=colourForButtonBackground[currentTheme],
                               foreground=colourForButtonForeground[currentTheme],
                               activebackground=colourForButtonActiveBackground[currentTheme],
                               font=("Bahnschrift", 8),
                               command=lambda: updateDetailsProcess("Gmail"))
    updateEmpGmailBtn.place(x=30, y=120)

    updateEmpContactNumberBtn = Button(frameB,
                                       text="Contact Number",
                                       cursor="hand2",
                                       width=15,
                                       background=colourForButtonBackground[currentTheme],
                                       foreground=colourForButtonForeground[currentTheme],
                                       activebackground=colourForButtonActiveBackground[currentTheme],
                                       font=("Bahnschrift", 8),
                                       command=lambda: updateDetailsProcess("Contact"))
    updateEmpContactNumberBtn.place(x=140, y=120)

    updateEmpSalaryBtn = Button(frameB,
                                text="Salary",
                                cursor="hand2",
                                width=15,
                                background=colourForButtonBackground[currentTheme],
                                foreground=colourForButtonForeground[currentTheme],
                                activebackground=colourForButtonActiveBackground[currentTheme],
                                font=("Bahnschrift", 8),
                                command=lambda: updateDetailsProcess("Salary"))
    updateEmpSalaryBtn.place(x=250, y=120)

    empFieldOldEntry = Entry(frameB,
                             width=17,
                             font=("Bahnschrift", 12),
                             background=colourForEntryBackground[currentTheme],
                             foreground=colourForEntryForeground[currentTheme],
                             textvariable=textVar23)
    empFieldOldEntry.place(x=200, y=155)

    empFieldNewEntry = Entry(frameB,
                             width=17,
                             font=("Bahnschrift", 12),
                             background=colourForEntryBackground[currentTheme],
                             foreground=colourForEntryForeground[currentTheme],
                             textvariable=textVar24)
    empFieldNewEntry.place(x=200, y=185)

    updateDetailsBtn = Button(frameB,
                              text="Update Employee Detail",
                              cursor="hand2",
                              width=45,
                              height=1,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 10),
                              command=updateDetailsProcess2)
    updateDetailsBtn.place(x=30, y=225)

    frameCLable = Label(frameC,
                        text="DELETE EMPLOYEE DETAILS",
                        font=("Bahnschrift", 15,),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameCLable.place(x=60, y=5)

    def deleteDetailsProcess(yesOrNoLocal):
        global yesOrNo
        idVerificationValue = idVerificationOfEmployeeId(2, 2)
        if idVerificationValue == True:
            if yesOrNoLocal == 1:
                yesOrNo = "Yes"
            elif yesOrNoLocal == 0:
                yesOrNo = ""
                messagebox.showinfo(
                    title="Process Intrupted Info", message=f"Employee Details deletation canceled")
                textVar25.set("")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    def deleteDetailsProcess2():
        global yesOrNo
        idVerificationValue = idVerificationOfEmployeeId(2, 2)
        if idVerificationValue == True:
            if yesOrNo == "Yes":
                connectionObjectOfSingleUserDataDatabase = connection(
                    f"_{user}_DataBase.db")
                cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                cursorOfSingleUserDatabase.execute('''
                DELETE FROM EMPLOYEEDATA
                WHERE employeeId = ?;
                ''', (textVar25.get(),))
                connectionObjectOfSingleUserDataDatabase.commit()
                cursorOfSingleUserDatabase.execute(f'''
                DROP TABLE SALARYTRANSACTIONTABLE_{textVar25.get()};
                ''')
                messagebox.showinfo(
                    title="Process Complete Info", message=f"Employee Detalis deleted succesfully")
                textVar25.set("")
                yesOrNo = ""
                connectionObjectOfSingleUserDataDatabase.commit()

                cursorOfSingleUserDatabase.close()
                connectionObjectOfSingleUserDataDatabase.close()
            elif yesOrNo == "":
                messagebox.showerror(
                    title="Null Field Selection Error", message="Yes or No field not selected")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    empIdLable = Label(frameC,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    messageLable = Label(frameC,
                         text="Really Want to delete Employee details ? ",
                         font=("Bahnschrift", 12),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme])
    messageLable.place(x=30, y=90)

    messageLable = Label(frameC,
                         text=(
                             "Note : You can't recover deleted data Please be \ncareful after deleting data"),
                         font=("Bahnschrift", 11),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme],
                         justify=LEFT)
    messageLable.place(x=30, y=205)

    empIdLable = Label(frameC,
                       text="Really Want to delete Employee details ? ",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=90)

    empIdEntry = Entry(frameC,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar25)
    empIdEntry.place(x=200, y=50)

    updateEmpdetailsAgreeBtn = Button(frameC,
                                      text="Yes, I agree",
                                      cursor="hand2",
                                      width=25,
                                      background=colourForButtonBackground[currentTheme],
                                      foreground=colourForButtonForeground[currentTheme],
                                      activebackground=colourForButtonActiveBackground[currentTheme],
                                      font=("Bahnschrift", 8),
                                      command=lambda: deleteDetailsProcess(1))
    updateEmpdetailsAgreeBtn.place(x=30, y=125)

    updateEmpDeatilsDisagreeBtn = Button(frameC,
                                         text="No, I don't agree",
                                         cursor="hand2",
                                         width=25,
                                         background=colourForButtonBackground[currentTheme],
                                         foreground=colourForButtonForeground[currentTheme],
                                         activebackground=colourForButtonActiveBackground[currentTheme],
                                         font=("Bahnschrift", 8),
                                         command=lambda: deleteDetailsProcess(0))
    updateEmpDeatilsDisagreeBtn.place(x=195, y=125)

    deleteDetailsBtn = Button(frameC,
                              text="Delete Employee Detail",
                              cursor="hand2",
                              width=45,
                              height=1,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 10),
                              command=deleteDetailsProcess2)
    deleteDetailsBtn.place(x=30, y=165)

    frameDLable = Label(frameD,
                        text="GET EMPLOYEE DETAILS",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameDLable.place(x=75, y=5)

    def addToClipBoard():
        idVerificationValue = idVerificationOfEmployeeId(2, 3)
        if idVerificationValue == True:
            empList = getData()[0]
            text = (
                f"Employee Name :{empList[1]}, Id :{empList[0]}, Designation  :{empList[2]}, Gmail :{empList[4]}, Contact Number :{empList[5]}, Address :{empList[3]}, Salary (Per month /-) :{empList[6]}")
            text = str(text)
            command = 'echo '+text.strip()+'| clip'
            os.system(command)
            getDetailProcess()
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    def getDetailProcess():
        idVerificationValue = idVerificationOfEmployeeId(2, 3)
        if idVerificationValue == True:
            empList = getData()[0]
            varList = [textVar27, textVar28, textVar29,
                       textVar30, textVar31, textVar32]
            for textvar in varList:
                textvar.set(empList[varList.index(textvar)+1])
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    def getData():
        connectionObjectOfSingleUserDataDatabase = connection(
            f"_{user}_DataBase.db")
        cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
        employeeData = cursorOfSingleUserDatabase.execute('''
                       SELECT * FROM EMPLOYEEDATA
                       WHERE employeeId = ?;
                       ''', (textVar26.get(),)).fetchall()
        cursorOfSingleUserDatabase.close()
        connectionObjectOfSingleUserDataDatabase.close()
        return employeeData

    def cleanEntry():
        varList = [textVar26, textVar27, textVar28,
                   textVar29, textVar30, textVar31, textVar32]
        for textVar in varList:
            textVar.set("")

    empIdLable = Label(frameD,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    empNameLable = Label(frameD,
                         text="Name                                     :",
                         font=("Bahnschrift", 12),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme])
    empNameLable.place(x=30, y=80)

    empDesignationLable = Label(frameD,
                                text="Designation                       :",
                                font=("Bahnschrift", 12),
                                background=colourForLableBackground[currentTheme],
                                foreground=colourForLableForeground[currentTheme])
    empDesignationLable.place(x=30, y=110)

    empAddressLable = Label(frameD,
                            text="Address                                :",
                            font=("Bahnschrift", 12),
                            background=colourForLableBackground[currentTheme],
                            foreground=colourForLableForeground[currentTheme])
    empAddressLable.place(x=30, y=140)

    empGmailLable = Label(frameD,
                          text="Gmail                                      :",
                          font=("Bahnschrift", 12),
                          background=colourForLableBackground[currentTheme],
                          foreground=colourForLableForeground[currentTheme])
    empGmailLable.place(x=30, y=170)

    empContactNumberLable = Label(frameD,
                                  text="Contact Number             :",
                                  font=("Bahnschrift", 12),
                                  background=colourForLableBackground[currentTheme],
                                  foreground=colourForLableForeground[currentTheme])
    empContactNumberLable.place(x=30, y=200)

    empSalaryLable = Label(frameD,
                           text="Salary [Per month /-] :",
                           font=("Bahnschrift", 12),
                           background=colourForLableBackground[currentTheme],
                           foreground=colourForLableForeground[currentTheme])
    empSalaryLable.place(x=30, y=230)

    empIdEntry = Entry(frameD,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar26)
    empIdEntry.place(x=200, y=50)

    empNameEntry = Entry(frameD,
                         width=17,
                         font=("Bahnschrift", 12),
                         background=colourForEntryBackground[currentTheme],
                         foreground=colourForEntryForeground[currentTheme],
                         textvariable=textVar27)
    empNameEntry.place(x=200, y=80)

    empDesignationEntry = Entry(frameD,
                                width=17,
                                font=("Bahnschrift", 12),
                                background=colourForEntryBackground[currentTheme],
                                foreground=colourForEntryForeground[currentTheme],
                                textvariable=textVar28)
    empDesignationEntry.place(x=200, y=110)

    empAddressEntry = Entry(frameD,
                            width=17,
                            font=("Bahnschrift", 12),
                            background=colourForEntryBackground[currentTheme],
                            foreground=colourForEntryForeground[currentTheme],
                            textvariable=textVar29)
    empAddressEntry.place(x=200, y=140)

    empGmailEntry = Entry(frameD,
                          width=17,
                          font=("Bahnschrift", 12),
                          background=colourForEntryBackground[currentTheme],
                          foreground=colourForEntryForeground[currentTheme],
                          textvariable=textVar30)
    empGmailEntry.place(x=200, y=170)

    empContactNumberEntry = Entry(frameD,
                                  width=17,
                                  font=("Bahnschrift", 12),
                                  background=colourForEntryBackground[currentTheme],
                                  foreground=colourForEntryForeground[currentTheme],
                                  textvariable=textVar31)
    empContactNumberEntry.place(x=200, y=200)

    empSalaryEntry = Entry(frameD,
                           width=17,
                           font=("Bahnschrift", 12),
                           background=colourForEntryBackground[currentTheme],
                           foreground=colourForEntryForeground[currentTheme],
                           textvariable=textVar32)
    empSalaryEntry.place(x=200, y=230)

    updateDetailsBtn = Button(frameD,
                              text="Get Employee Detail",
                              cursor="hand2",
                              width=25,
                              height=1,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 9),
                              command=getDetailProcess)
    updateDetailsBtn.place(x=30, y=260)

    copyDetailsBtn = Button(frameD,
                            text="Copy",
                            cursor="hand2",
                            width=5,
                            height=1,
                            background=colourForButtonBackground[currentTheme],
                            foreground=colourForButtonForeground[currentTheme],
                            activebackground=colourForButtonActiveBackground[currentTheme],
                            font=("Bahnschrift", 9),
                            command=addToClipBoard)
    copyDetailsBtn.place(x=270, y=260)

    resetBtn = Button(frameD,
                      text="Reset",
                      cursor="hand2",
                      width=5,
                      height=1,
                      background=colourForButtonBackground[currentTheme],
                      foreground=colourForButtonForeground[currentTheme],
                      activebackground=colourForButtonActiveBackground[currentTheme],
                      font=("Bahnschrift", 9),
                      command=cleanEntry)
    resetBtn.place(x=320, y=260)

    frameELable = Label(frameE,
                        text="ALL EMPLOYEE DETAILS LIST",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameELable.place(x=200, y=5)

    def showDetails():
        connectionObjectOfSingleUserDataDatabase = connection(
            f"_{user}_DataBase.db")
        cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
        employeeData = cursorOfSingleUserDatabase.execute('''
                       SELECT * FROM EMPLOYEEDATA
                       ORDER BY name;
                       ''').fetchall()
        cursorOfSingleUserDatabase.close()
        connectionObjectOfSingleUserDataDatabase.close()
        tree.tag_configure(
            'oddrow', background=colourForTreeviewOdd[currentTheme])
        tree.tag_configure(
            'evenrow', background=colourForTreeviewEven[currentTheme])
        count = 0
        tree.delete(*tree.get_children())
        for element in employeeData:
            if count % 2 != 0:
                tree.insert("", "end", values=("   "+element[1], "   "+element[0], "   "+element[2], "   " +
                            element[3], "   "+element[4], "   "+element[5], "   "+element[6]), tags=('evenrow',))
            elif count % 2 == 0:
                tree.insert("", "end", values=("   "+element[1], "   "+element[0], "   "+element[2], "   " +
                            element[3], "   "+element[4], "   "+element[5], "   "+element[6]), tags=('oddrow',))
            count += 1

    style = ttk.Style()

    style.theme_use('default')
    style.map('Treeview', background=[
              ('selected', colourForTreeviewSelectedFieldBackground[currentTheme])])
    style.configure(
        "Treeview", fieldbackground=colourForTreeviewFieldbackground[currentTheme])
    style.configure('Treeview.Heading', background=colourForTreeviewHeadingBackground[
                    currentTheme], foreground=colourForTreeviewHeadingForeground[currentTheme])
    tree = ttk.Treeview(frameEA, columns=[
                        "c1", "c2", "c3", "c4", "c5", "c6", "c7"], show="headings", height=13)

    tree.column("c1", anchor=W)
    tree.column("c2", anchor=W)
    tree.column("c3", anchor=W)
    tree.column("c4", anchor=W)
    tree.column("c5", anchor=W)
    tree.column("c6", anchor=W)
    tree.column("c7", anchor=W)

    tree.heading("c1", text="Name")
    tree.heading("c2", text="Id")
    tree.heading("c3", text="Designation")
    tree.heading("c4", text="Address")
    tree.heading("c5", text="Gmail")
    tree.heading("c6", text="Contact Number")
    tree.heading("c7", text="Salary")

    scrollbar = Scrollbar(frameEA)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    scrollbar1 = Scrollbar(frameEA, orient=HORIZONTAL)
    scrollbar1.pack(side=BOTTOM, fill=BOTH)
    tree.config(xscrollcommand=scrollbar1.set)
    scrollbar1.config(command=tree.xview)

    tree.pack(fill=BOTH)

    tree.tag_configure('odd',)
    tree.tag_configure('even',)

    tree.tag_configure(
        'oddrow', background=colourForTreeviewOdd[currentTheme], foreground="white")
    tree.tag_configure(
        'evenrow', background=colourForTreeviewEven[currentTheme])
    tree.pack()
    showDetails()

    refreshDataBtn = Button(frameE,
                            text="Refresh data",
                            cursor="hand2",
                            width=15,
                            background=colourForButtonBackground[currentTheme],
                            foreground=colourForButtonForeground[currentTheme],
                            activebackground=colourForButtonActiveBackground[currentTheme],
                            font=("Bahnschrift", 8),
                            command=showDetails)
    refreshDataBtn.place(x=655, y=7)
    currentUserNameLable = Label(frameF,
                                 text=f"User Name : {user}",
                                 font=("Bahnschrift", 8),
                                 background=colourForLableBackground[currentTheme],
                                 foreground=colourForLableForeground[currentTheme])
    currentUserNameLable.place(x=10, y=1)

    salaryManagementSystemJumpBtn = Button(frameF,
                                           text="Salary Management System",
                                           cursor="hand2",
                                           border=0,
                                           background=colourForLowerMenuBackground[currentTheme],
                                           foreground=colourForLowerMenuForeground[currentTheme],
                                           activebackground=colourForLowerMenuActiveBackground[currentTheme],
                                           font=("Bahnschrift", 10),
                                           command=salaryMangementSystemWindowOpen)
    salaryManagementSystemJumpBtn.place(x=935, y=1)
    salaryManagementSystemJumpBtn.bind("<Enter>",
                                       lambda event: hoverOnBtn(a=1))
    salaryManagementSystemJumpBtn.bind("<Leave>",
                                       lambda event: hoverOnBtn(a=2))

    logOutBtn = Button(frameF,
                       text="Logout",
                       cursor="hand2",
                       border=0,
                       background=colourForLowerMenuBackground[currentTheme],
                       foreground=colourForLowerMenuForeground[currentTheme],
                       activebackground=colourForLowerMenuActiveBackground[currentTheme],
                       font=("Bahnschrift", 10),
                       command=logOut)
    logOutBtn.place(x=1100, y=1)
    logOutBtn.bind("<Enter>",
                   lambda event: hoverOnBtn(a=5))
    logOutBtn.bind("<Leave>",
                   lambda event: hoverOnBtn(a=6))


def salaryMangementSystemWindow():
    global currentWindow, appHeigth, appWidth, duplicateFrameOfFrameSalaryA, duplicateFrameOfFrameSalaryB, duplicateFrameOfFrameSalaryC, duplicateFrameOfFrameSalaryD, duplicateFrameOfFrameSalaryE, duplicateFrameOfFrameSalaryF

    duplicateFrameOfLoginFrame.destroy()

    def back():
        frameSalaryA.destroy()
        frameSalaryB.destroy()
        frameSalaryC.destroy()
        frameSalaryD.destroy()
        frameSalaryE.destroy()
        frameSalaryF.destroy()
        varList = [textVar33, textVar34, textVar35, textVar36, textVar37,
                   textVar38, textVar39, textVar40, textVar41, textVar42, ]
        for textVar in varList:
            textVar.set("")
        mainWindow()

    def hoverOnBtn(a):
        if a == 1:
            backBtn.config(
                background=colourForLowerMenuOnHoverBackground[currentTheme], foreground=colourForLowerMenuOnHoverForeground[currentTheme])
        elif a == 2:
            backBtn.config(
                background=colourForLowerMenuBackground[currentTheme], foreground=colourForLableForeground[currentTheme])

    root.title("Salary Management System - Contol Center")

    frameSalaryA = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryA.place(x=0, y=0, width=384, height=325)

    frameSalaryB = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryB.place(x=384, y=0, width=384, height=325)

    frameSalaryC = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryC.place(x=768, y=0, width=384, height=325)

    frameSalaryD = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryD.place(x=0, y=325, width=384, height=295)

    frameSalaryE = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryE.place(x=384, y=325, width=768, height=295)

    frameSalaryF = Frame(root,
                         background=colourForWindow[currentTheme],
                         highlightbackground=colourForFrameHighlightBackground[currentTheme],
                         highlightthickness=2)
    frameSalaryF.place(x=0, y=620, width=1152, height=30)

    for element in item:
        accountMenu.entryconfig(element, state="disable")

    appWidth = 1152
    appHeigth = 650
    root.geometry(
        f"{appWidth}x{appHeigth}+{int((screenWidth - appWidth)/2)}+{int((screenHeight - appHeigth)/5)}")

    currentWindow = "salaryManagementWindow"
    duplicateFrameOfFrameSalaryA = frameSalaryA
    duplicateFrameOfFrameSalaryB = frameSalaryB
    duplicateFrameOfFrameSalaryC = frameSalaryC
    duplicateFrameOfFrameSalaryD = frameSalaryD
    duplicateFrameOfFrameSalaryE = frameSalaryE
    duplicateFrameOfFrameSalaryF = frameSalaryF
    frameALable = Label(frameSalaryA,
                        text="ADD TRANSACTION DETAILS",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameALable.place(x=65, y=5)

    def addTransaction():
        empId = textVar33.get()
        transactionId = textVar34.get()
        date = textVar35.get()
        time = textVar36.get()
        amount = textVar37.get()
        if empId != "" and transactionId != "" and date != "" and time != "" and amount != "":
            idVerificationValue = idVerificationOfEmployeeId(2, 4)
            if idVerificationValue == True:
                transactionIdVerifivationValue = transactionIdVerification(
                    empId, transactionId)
                if transactionIdVerifivationValue == False:
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    cursorOfSingleUserDatabase.execute(f'''
                    INSERT INTO SALARYTRANSACTIONTABLE_{empId}
                    VALUES (?,?,?,?)
                    ''', (transactionId, date, time, amount))
                    connectionObjectOfSingleUserDataDatabase.commit()
                    messagebox.showinfo(
                        title="Process Complete Info", message="Employee transaction details added succesfully")
                    textVar33.set("")
                    refreshDetails()
                    textVar37.set("\u20B9")
                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                elif transactionIdVerifivationValue == True:
                    refreshDetails()
                    addTransaction()
            elif idVerificationValue == False:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Employee Id Not Exists")
        else:
            if empId == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Employee Id Entry")
            elif transactionId == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Transaction Id Entry")
            elif date == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Date Entry")
            elif time == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Time Entry")
            elif amount == "":
                messagebox.showerror(
                    title="Null Entry Error", message="Please Fill Amount Entry")

    def transactionIdVerification(empId, transactionId):
        returnList = []
        returnValue = False
        connectionObjectOfSingleUserDataDatabase = connection(
            f"_{user}_DataBase.db")
        cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
        transactionIdList = cursorOfSingleUserDatabase.execute(f'''
                            SELECT transactionId FROM SALARYTRANSACTIONTABLE_{empId}
                            ''')
        for element in transactionIdList:
            returnList.append(element[0])
        cursorOfSingleUserDatabase.close()
        connectionObjectOfSingleUserDataDatabase.close()

        if len(returnList) != 0:
            for element in returnList:
                if element == transactionId:
                    returnValue = True
                    break
            else:
                returnValue = False
        else:
            returnValue = False
        return returnValue

    def refreshDetails():
        ascii_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ascii_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 1188 million {1,188,137,600}
        transactionId = f"{random.choice(ascii_uppercase)}{random.choice(ascii_lowercase)}{random.choice(ascii_uppercase)}{random.choice(ascii_lowercase)}{random.choice(ascii_uppercase)}{random.choice(digits)}{random.choice(digits)}{random.choice(digits)}"
        currentDate = datetime.datetime.now().strftime("%d")+"/" + \
            datetime.datetime.now().strftime("%m")+"/"+datetime.datetime.now().strftime("%Y")
        currentTime = datetime.datetime.now().strftime("%I")+":"+datetime.datetime.now().strftime("%M") + \
            ":"+datetime.datetime.now().strftime("%S")+" " + \
            datetime.datetime.now().strftime("%p")
        textVar34.set(transactionId)
        textVar35.set(currentDate)
        textVar36.set(currentTime)

    empIdLable = Label(frameSalaryA,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    transactionIdLable = Label(frameSalaryA,
                               text="Transaction ID                 :",
                               font=("Bahnschrift", 12),
                               background=colourForLableBackground[currentTheme],
                               foreground=colourForLableForeground[currentTheme])
    transactionIdLable.place(x=30, y=80)

    dateLable = Label(frameSalaryA,
                      text="Date                                        :",
                      font=("Bahnschrift", 12),
                      background=colourForLableBackground[currentTheme],
                      foreground=colourForLableForeground[currentTheme])
    dateLable.place(x=30, y=110)

    timeLable = Label(frameSalaryA,
                      text="Time                                       :",
                      font=("Bahnschrift", 12),
                      background=colourForLableBackground[currentTheme],
                      foreground=colourForLableForeground[currentTheme])
    timeLable.place(x=30, y=140)

    amountLable = Label(frameSalaryA,
                        text="Amount                                :",
                        font=("Bahnschrift", 12),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    amountLable.place(x=30, y=170)
    textVar37.set("\u20B9")

    empIdEntry = Entry(frameSalaryA,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar33)
    empIdEntry.place(x=200, y=50)

    transactionIdEntry = Entry(frameSalaryA,
                               width=17,
                               font=("Bahnschrift", 12),
                               background=colourForEntryBackground[currentTheme],
                               foreground=colourForEntryForeground[currentTheme],
                               textvariable=textVar34)
    transactionIdEntry.place(x=200, y=80)

    dateEntry = Entry(frameSalaryA,
                      width=17,
                      font=("Bahnschrift", 12),
                      background=colourForEntryBackground[currentTheme],
                      foreground=colourForEntryForeground[currentTheme],
                      textvariable=textVar35)
    dateEntry.place(x=200, y=110)

    timeEntry = Entry(frameSalaryA,
                      width=17,
                      font=("Bahnschrift", 12),
                      background=colourForEntryBackground[currentTheme],
                      foreground=colourForEntryForeground[currentTheme],
                      textvariable=textVar36)
    timeEntry.place(x=200, y=140)

    amountEntry = Entry(frameSalaryA,
                        width=17,
                        font=("Bahnschrift", 12),
                        background=colourForEntryBackground[currentTheme],
                        foreground=colourForEntryForeground[currentTheme],
                        textvariable=textVar37)
    amountEntry.place(x=200, y=170)

    if textVar34.get() == "":
        refreshDetails()

    addTransactionBtn = Button(frameSalaryA,
                               text="Refresh Autofill",
                               cursor="hand2",
                               height=1,
                               background=colourForButtonBackground[currentTheme],
                               foreground=colourForButtonForeground[currentTheme],
                               activebackground=colourForButtonActiveBackground[currentTheme],
                               font=("Bahnschrift", 8),
                               command=refreshDetails)
    addTransactionBtn.place(x=270, y=210)

    addTransactionBtn = Button(frameSalaryA,
                               text="Add Transaction Detail",
                               cursor="hand2",
                               width=45,
                               height=1,
                               background=colourForButtonBackground[currentTheme],
                               foreground=colourForButtonForeground[currentTheme],
                               activebackground=colourForButtonActiveBackground[currentTheme],
                               font=("Bahnschrift", 10),
                               command=addTransaction)
    addTransactionBtn.place(x=30, y=245)

    frameBLable = Label(frameSalaryB,
                        text="DELETE EMPLOYEE DETAILS",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameBLable.place(x=65, y=5)

    def deleteTransactionDetailsProcess(yesOrNoLocal):
        global yesOrNo2
        idVerificationValue = idVerificationOfEmployeeId(2, 5)
        if idVerificationValue == True:
            if yesOrNoLocal == 1:
                yesOrNo2 = "Yes"
            elif yesOrNoLocal == 0:
                yesOrNo2 = ""
                messagebox.showinfo(
                    title="Process Intrupted Info", message=f"Employee Details deletation canceled")
                textVar25.set("")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    def deleteTransactionDetailsProcess2():
        global yesOrNo2
        idVerificationValue = idVerificationOfEmployeeId(2, 5)
        if idVerificationValue == True:
            transactionIdVerifivationValue = transactionIdVerification(
                textVar38.get(), textVar39.get())
            if transactionIdVerifivationValue == True:
                if yesOrNo2 == "Yes":
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    cursorOfSingleUserDatabase.execute(f'''
                    DELETE FROM SALARYTRANSACTIONTABLE_{textVar38.get()}
                    WHERE transactionId = ?;
                    ''', (textVar39.get(),))
                    connectionObjectOfSingleUserDataDatabase.commit()
                    messagebox.showinfo(
                        title="Process Complete Info", message=f"Employee Transaction Detalis deleted succesfully")
                    textVar38.set("")
                    textVar39.set("")
                    yesOrNo2 = ""
                    connectionObjectOfSingleUserDataDatabase.commit()
                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                elif yesOrNo2 == "":
                    messagebox.showerror(
                        title="Null Field Selection Error", message="Yes or No field not selected")
            elif transactionIdVerifivationValue == False:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Transation Id Not Exists")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    empIdLable = Label(frameSalaryB,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    transactionIdLable = Label(frameSalaryB,
                               text="Transaction ID                 :",
                               font=("Bahnschrift", 12),
                               background=colourForLableBackground[currentTheme],
                               foreground=colourForLableForeground[currentTheme])
    transactionIdLable.place(x=30, y=80)

    messageLable = Label(frameSalaryB,
                         text="Really Want to delete Employee details ? ",
                         font=("Bahnschrift", 12),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme])
    messageLable.place(x=30, y=120)

    messageLable = Label(frameSalaryB,
                         text=(
                             "Note : You can't recover deleted data Please be \ncareful after deleting data"),
                         font=("Bahnschrift", 11),
                         background=colourForLableBackground[currentTheme],
                         foreground=colourForLableForeground[currentTheme],
                         justify=LEFT)
    messageLable.place(x=30, y=235)

    empIdLable = Label(frameSalaryB,
                       text="Really Want to delete Employee details ? ",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=120)

    empIdEntry = Entry(frameSalaryB,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar38)
    empIdEntry.place(x=200, y=50)

    transactionIdEntry = Entry(frameSalaryB,
                               width=17,
                               font=("Bahnschrift", 12),
                               background=colourForEntryBackground[currentTheme],
                               foreground=colourForEntryForeground[currentTheme],
                               textvariable=textVar39)
    transactionIdEntry.place(x=200, y=80)

    deleteEmpTransactiondetailsAgreeBtn = Button(frameSalaryB,
                                                 text="Yes, I agree",
                                                 cursor="hand2",
                                                 width=25,
                                                 background=colourForButtonBackground[currentTheme],
                                                 foreground=colourForButtonForeground[currentTheme],
                                                 activebackground=colourForButtonActiveBackground[currentTheme],
                                                 font=("Bahnschrift", 8),
                                                 command=lambda: deleteTransactionDetailsProcess(1))
    deleteEmpTransactiondetailsAgreeBtn.place(x=30, y=155)

    deleteEmpTransactionDeatilsDisagreeBtn = Button(frameSalaryB,
                                                    text="No, I don't agree",
                                                    cursor="hand2",
                                                    width=25,
                                                    background=colourForButtonBackground[currentTheme],
                                                    foreground=colourForButtonForeground[currentTheme],
                                                    activebackground=colourForButtonActiveBackground[
                                                        currentTheme],
                                                    font=("Bahnschrift", 8),
                                                    command=lambda: deleteTransactionDetailsProcess(0))
    deleteEmpTransactionDeatilsDisagreeBtn.place(x=195, y=155)

    deleteDetailsBtn = Button(frameSalaryB,
                              text="Delete Employee Detail",
                              cursor="hand2",
                              width=45,
                              height=1,
                              background=colourForButtonBackground[currentTheme],
                              foreground=colourForButtonForeground[currentTheme],
                              activebackground=colourForButtonActiveBackground[currentTheme],
                              font=("Bahnschrift", 10),
                              command=deleteTransactionDetailsProcess2)
    deleteDetailsBtn.place(x=30, y=195)

    frameCLable = Label(frameSalaryC,
                        text="GENERATE TRANSACTION RICEIPT",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameCLable.place(x=30, y=5)

    def selectFile():
        global filePath
        filePath = filedialog.askdirectory()

    def generateRecipt():
        global filePath
        idVerificationValue = idVerificationOfEmployeeId(2, 6)
        if idVerificationValue == True:
            transactionIdVerificationValue = transactionIdVerification(
                textVar40.get(), textVar41.get())
            if transactionIdVerificationValue == True:
                if filePath != "":
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    employeeNameList = cursorOfSingleUserDatabase.execute('''
                                       SELECT name FROM EMPLOYEEDATA
                                       WHERE employeeId = ?
                                       ''', (textVar40.get(),)).fetchall()
                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                    employeeName = employeeNameList[0][0]
                    connectionObjectOfSingleUserDataDatabase = connection(
                        f"_{user}_DataBase.db")
                    cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
                    transactionIdList = cursorOfSingleUserDatabase.execute(f'''
                                        SELECT date,time,amount FROM SALARYTRANSACTIONTABLE_{textVar40.get()}
                                        WHERE transactionId = ?
                                        ''', (textVar41.get(),)).fetchall()
                    cursorOfSingleUserDatabase.close()
                    connectionObjectOfSingleUserDataDatabase.close()
                    date = transactionIdList[0][0]
                    time = transactionIdList[0][1]
                    amount = transactionIdList[0][2]
                    font = ImageFont.truetype("arial.ttf", size=20)
                    messageA = "o\no\no\no\no\no\no\no\no\no\no\no\no"
                    messageB = "o\no\no\no\no\no\no\no\no\no\no\no\no"
                    messageC = "------Transaction Riceipt------"
                    messageD = f"Employee Name      :{employeeName}"
                    messageE = f"Employee Id            :{textVar40.get()}"
                    messageF = f"Transaction Id         :{textVar41.get()}"
                    messageG = f"Date                       :{date}"
                    messageH = f"Time                       :{time}"
                    messageI = f"Amount Transfered  :{amount}"
                    img = Image.new("RGB", (512, 312), color="White")
                    imgDraw = ImageDraw.Draw(img)
                    imgDraw.text((10, 5), messageA, font=font, fill="black")
                    imgDraw.text((490, 5), messageB, font=font, fill="black")
                    imgDraw.text((130, 10), messageC, font=font, fill="black")
                    imgDraw.text((60, 70), messageD, font=font, fill="black")
                    imgDraw.text((60, 110), messageE, font=font, fill="black")
                    imgDraw.text((60, 150), messageF, font=font, fill="black")
                    imgDraw.text((60, 190), messageG, font=font, fill="black")
                    imgDraw.text((60, 230), messageH, font=font, fill="black")
                    imgDraw.text((60, 270), messageI, font=font, fill="black")
                    img.save(
                        f"{filePath}/Riceipt-{textVar41.get()}-{textVar40.get()}-{random.randrange(1,1000000)}.png")
                    messagebox.showinfo(
                        title="Process Complete Info", message=f"Transaction Report Generated succesfully")
                    textVar40.set("")
                    textVar41.set("")
                    filePath = ""
                elif filePath == "":
                    messagebox.showerror(
                        title="Null Field Selection Entry Error", message="Filepath Not Selected")
            elif transactionIdVerificationValue == False:
                messagebox.showerror(
                    title="Invalid Entry Error", message="Transation Id Not Exists")
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")

    empIdLable = Label(frameSalaryC,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    transactionIdLable = Label(frameSalaryC,
                               text="Transaction ID                 :",
                               font=("Bahnschrift", 12),
                               background=colourForLableBackground[currentTheme],
                               foreground=colourForLableForeground[currentTheme])
    transactionIdLable.place(x=30, y=80)

    transactionIdLable = Label(frameSalaryC,
                               text="Save File Path                 :",
                               font=("Bahnschrift", 12),
                               background=colourForLableBackground[currentTheme],
                               foreground=colourForLableForeground[currentTheme])
    transactionIdLable.place(x=30, y=110)

    empIdEntry = Entry(frameSalaryC,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar40)
    empIdEntry.place(x=200, y=50)

    transactionIdEntry = Entry(frameSalaryC,
                               width=17,
                               font=("Bahnschrift", 12),
                               background=colourForEntryBackground[currentTheme],
                               foreground=colourForEntryForeground[currentTheme],
                               textvariable=textVar41)
    transactionIdEntry.place(x=200, y=80)

    filePathBtn = Button(frameSalaryC,
                         text="Select Path",
                         cursor="hand2",
                         width=24,
                         height=1,
                         background=colourForButtonBackground[currentTheme],
                         foreground=colourForButtonForeground[currentTheme],
                         activebackground=colourForButtonActiveBackground[currentTheme],
                         font=("Bahnschrift", 8),
                         command=selectFile)
    filePathBtn.place(x=200, y=110)

    generateRiceiptBtn = Button(frameSalaryC,
                                text="Generate Transaction Report",
                                cursor="hand2",
                                width=45,
                                height=1,
                                background=colourForButtonBackground[currentTheme],
                                foreground=colourForButtonForeground[currentTheme],
                                activebackground=colourForButtonActiveBackground[currentTheme],
                                font=("Bahnschrift", 10),
                                command=generateRecipt)
    generateRiceiptBtn.place(x=30, y=165)

    frameDLable = Label(frameSalaryD,
                        text="GET TRANSACTION DETAILS LIST",
                        font=("Bahnschrift", 15),
                        background=colourForLableBackground[currentTheme],
                        foreground=colourForLableForeground[currentTheme])
    frameDLable.place(x=35, y=5)

    def clearList():
        tree.delete(*tree.get_children())
        textVar42.set("")

    def showDetails():
        idVerificationValue = idVerificationOfEmployeeId(2, 7)
        if idVerificationValue == True:
            connectionObjectOfSingleUserDataDatabase = connection(
                f"_{user}_DataBase.db")
            cursorOfSingleUserDatabase = connectionObjectOfSingleUserDataDatabase.cursor()
            employeeData = cursorOfSingleUserDatabase.execute(f'''
                           SELECT * FROM SALARYTRANSACTIONTABLE_{textVar42.get()}
                           ORDER BY date,time;
                           ''').fetchall()
            cursorOfSingleUserDatabase.close()
            connectionObjectOfSingleUserDataDatabase.close()
        elif idVerificationValue == False:
            messagebox.showerror(title="Invalid Entry Error",
                                 message="Employee Id Not Exists")
        tree.tag_configure(
            'oddrow', background=colourForTreeviewOdd[currentTheme])
        tree.tag_configure(
            'evenrow', background=colourForTreeviewEven[currentTheme])
        count = 0
        tree.delete(*tree.get_children())
        for element in employeeData:
            if count % 2 != 0:
                tree.insert("", "end", values=(
                    "   "+element[0], "   "+element[1], "   "+element[2], "   "+element[3]), tags=('evenrow',))
            elif count % 2 == 0:
                tree.insert("", "end", values=(
                    "   "+element[0], "   "+element[1], "   "+element[2], "   "+element[3]), tags=('oddrow',))
            count += 1

    empIdLable = Label(frameSalaryD,
                       text="Employee ID                     :",
                       font=("Bahnschrift", 12),
                       background=colourForLableBackground[currentTheme],
                       foreground=colourForLableForeground[currentTheme])
    empIdLable.place(x=30, y=50)

    empIdEntry = Entry(frameSalaryD,
                       width=17,
                       font=("Bahnschrift", 12),
                       background=colourForEntryBackground[currentTheme],
                       foreground=colourForEntryForeground[currentTheme],
                       textvariable=textVar42)
    empIdEntry.place(x=200, y=50)

    clearListBtn = Button(frameSalaryD,
                          text="Clear list",
                          cursor="hand2",
                          height=1,
                          background=colourForButtonBackground[currentTheme],
                          foreground=colourForButtonForeground[currentTheme],
                          activebackground=colourForButtonActiveBackground[currentTheme],
                          font=("Bahnschrift", 8),
                          command=clearList)
    clearListBtn.place(x=300, y=95)

    getTransactionDetailsBtn = Button(frameSalaryD,
                                      text="Get Transactions list",
                                      cursor="hand2",
                                      width=45,
                                      height=1,
                                      background=colourForButtonBackground[currentTheme],
                                      foreground=colourForButtonForeground[currentTheme],
                                      activebackground=colourForButtonActiveBackground[currentTheme],
                                      font=("Bahnschrift", 10),
                                      command=showDetails)
    getTransactionDetailsBtn.place(x=30, y=135)

    style = ttk.Style()

    style.theme_use('default')
    style.map('Treeview', background=[
              ('selected', colourForTreeviewSelectedFieldBackground[currentTheme])])
    style.configure(
        "Treeview", fieldbackground=colourForTreeviewFieldbackground[currentTheme])
    style.configure('Treeview.Heading', background=colourForTreeviewHeadingBackground[
                    currentTheme], foreground=colourForTreeviewHeadingForeground[currentTheme])
    tree = ttk.Treeview(frameSalaryE, columns=[
                        "c1", "c2", "c3", "c4"], show="headings", height=13)

    tree.column("c1", anchor=W)
    tree.column("c2", anchor=W)
    tree.column("c3", anchor=W)
    tree.column("c4", anchor=W)

    tree.heading("c1", text="Transaction Id")
    tree.heading("c2", text="Date Of Transaction")
    tree.heading("c3", text="Time Of Transaction")
    tree.heading("c4", text="Amount Transfered")

    scrollbar = Scrollbar(frameSalaryE)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    scrollbar1 = Scrollbar(frameSalaryE, orient=HORIZONTAL)
    scrollbar1.pack(side=BOTTOM, fill=BOTH)
    tree.config(xscrollcommand=scrollbar1.set)
    scrollbar1.config(command=tree.xview)

    tree.pack(fill=BOTH)

    tree.tag_configure('odd',)
    tree.tag_configure('even',)

    tree.tag_configure(
        'oddrow', background=colourForTreeviewOdd[currentTheme], foreground="white")
    tree.tag_configure(
        'evenrow', background=colourForTreeviewEven[currentTheme])
    tree.pack()

    currentUserNameLable = Label(frameSalaryF,
                                 text=f"User Name : {user}",
                                 font=("Bahnschrift", 8),
                                 background=colourForLableBackground[currentTheme],
                                 foreground=colourForLableForeground[currentTheme])
    currentUserNameLable.place(x=10, y=1)

    backBtn = Button(frameSalaryF,
                     text="Back",
                     cursor="hand2",
                     background=colourForLowerMenuBackground[currentTheme],
                     foreground=colourForLowerMenuForeground[currentTheme],
                     activebackground=colourForLowerMenuActiveBackground[currentTheme],
                     bd=0,
                     font=("Bahnschrift", 10),
                     command=back)
    backBtn.place(x=1112, y=1)
    backBtn.bind("<Enter>",
                 lambda event: hoverOnBtn(a=1))
    backBtn.bind("<Leave>",
                 lambda event: hoverOnBtn(a=2))


colourForWindow = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                   "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForTreeviewEven = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                         "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForFrameHighlightBackground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                                     "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForMenu = {"Dark": "#5e5d5d", "Light": "#ebe9e9", "Rose": "#ffe4e9",
                 "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}
colourForTreeviewFieldbackground = {"Dark": "#5e5d5d", "Light": "#ebe9e9", "Rose": "#ffe4e9",
                                    "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForTreeviewOdd = {"Dark": "#5e5d5d", "Light": "#ebe9e9", "Rose": "#ffe4e9",
                        "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForLableBackground = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                            "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForLableForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                            "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForLowerMenuForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                                "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForLowerMenuBackground = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                                "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForLowerMenuActiveBackground = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                                      "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForLowerMenuOnHoverBackground = {"Dark": "#ffffff", "Light": "#b7b7b7", "Rose": "#e91e63",
                                       "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#01b701"}

colourForLowerMenuOnHoverForeground = {"Dark": "#000000", "Light": "#ffffff", "Rose": "#ffe4e9",
                                       "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForEntryBackground = {"Dark": "#5e5d5d", "Light": "#ebe9e9", "Rose": "#ffe4e9",
                            "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForEntryForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                            "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForMenuActiveForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                                 "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForMenuActiveBackground = {"Dark": "#292a2d", "Light": "#b7b7b7", "Rose": "#ffc0cb",
                                 "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForButtonForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#ffe4e9",
                             "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForTreeviewHeadingForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#ffe4e9",
                                      "Sky": "#a4d2e5", "Lemon": "#ebf984", "Nature": "#71ff98"}

colourForButtonBackground = {"Dark": "#35363a", "Light": "#b7b7b7", "Rose": "#e91e63",
                             "Sky": "#3f51b5", "Lemon": "#ffb23f", "Nature": "#01b701"}

colourForTreeviewSelectedFieldBackground = {"Dark": "#35363a", "Light": "#b7b7b7", "Rose": "#e91e63",
                                            "Sky": "#3f51b5", "Lemon": "#ffb23f", "Nature": "#01b701"}

colourForTreeviewHeadingBackground = {"Dark": "#35363a", "Light": "#b7b7b7", "Rose": "#e91e63",
                                      "Sky": "#3f51b5", "Lemon": "#ffb23f", "Nature": "#01b701"}

colourForBackButtonForeground = {"Dark": "#ffffff", "Light": "#000000", "Rose": "#e91e63",
                                 "Sky": "#3f51b5", "Lemon": "#ff9800", "Nature": "#008000"}

colourForBackButtonBackground = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                                 "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForButtonActiveBackground = {"Dark": "#ffffff", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                                   "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

colourForBackButtonActiveBackground = {"Dark": "#292a2d", "Light": "#f5f5f5", "Rose": "#ffc0cb",
                                       "Sky": "#87ceeb", "Lemon": "#e8ff42", "Nature": "#00ff46"}

currentActivebackgroundColour = None
currentActiveforegroundColour = None
currentTheme = "Light"
currentWindow = "loginWindow"
duplicateFrameOfLoginFrame = ""
duplicateFrameOfSignUpFrame = ""
duplicateFrameOfChangePasswordFrame = ""
duplicateFrameOfForgotPasswordFrame = ""
duplicateFrameOfFrameA = ""
duplicateFrameOfFrameB = ""
duplicateFrameOfFrameC = ""
duplicateFrameOfFrameD = ""
duplicateFrameOfFrameE = ""
duplicateFrameOfFrameF = ""
duplicateFrameOfFrameSalaryA = ""
duplicateFrameOfFrameSalaryB = ""
duplicateFrameOfFrameSalaryC = ""
duplicateFrameOfFrameSalaryD = ""
duplicateFrameOfFrameSalaryE = ""
duplicateFrameOfFrameSalaryEA = ""
duplicateFrameOfFrameSalaryF = ""
user = None
a = 0
selectedField = ""
yesOrNo = ""
yesOrNo2 = ""
filePath = ""
item = ["Create Account", "Change Password", "Forgot Password"]

textVar1 = StringVar()
textVar2 = StringVar()
textVar3 = StringVar()
textVar4 = StringVar()
textVar5 = StringVar()
textVar6 = StringVar()
textVar7 = StringVar()
textVar8 = StringVar()
textVar9 = StringVar()
textVar10 = StringVar()
textVar11 = StringVar()
textVar12 = StringVar()
textVar13 = StringVar()
textVar14 = StringVar()
textVar15 = StringVar()
textVar16 = StringVar()
textVar17 = StringVar()
textVar18 = StringVar()
textVar19 = StringVar()
textVar20 = StringVar()
textVar21 = StringVar()
textVar22 = StringVar()
textVar23 = StringVar()
textVar24 = StringVar()
textVar25 = StringVar()
textVar26 = StringVar()
textVar26 = StringVar()
textVar27 = StringVar()
textVar28 = StringVar()
textVar29 = StringVar()
textVar30 = StringVar()
textVar31 = StringVar()
textVar32 = StringVar()
textVar33 = StringVar()
textVar34 = StringVar()
textVar35 = StringVar()
textVar36 = StringVar()
textVar37 = StringVar()
textVar38 = StringVar()
textVar39 = StringVar()
textVar40 = StringVar()
textVar41 = StringVar()
textVar42 = StringVar()

try:
    mainFunction()
except EXCEPTION as error:
    messagebox.showwarning(title="Prorgraming Warning", message=f"{error}")

root.mainloop()
