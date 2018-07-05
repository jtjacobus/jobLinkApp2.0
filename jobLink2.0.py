import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from PIL import ImageTk
from tkinter import *
import pymysql
import tkinter.messagebox as tm

class JobLink(tk.Tk):


    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Job Link")
        self.geometry('{}x{}'.format(420, 700))

        #~~# Images #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.iconbitmap('jobLinkLogo.ico')  # does not work

        #~~# Dictionary #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.shared_data = {"username": StringVar(), "user_id": tk.StringVar(), "job_id": tk.StringVar(),"job_status": tk.StringVar(),
                            "company": tk.StringVar(), "user_first": tk.StringVar(), "job_type": tk.StringVar(),"req_start_date": tk.StringVar(),
                            "client_id": tk.StringVar(), "admin_id": tk.StringVar(), "tech_id": tk.StringVar()}

        self.shared_job_dict = {"j0": tk.StringVar(),"j1": tk.StringVar(),"j2": tk.StringVar(),"j3": tk.StringVar(),"j4": tk.StringVar(),"j5": tk.StringVar(),"j6": tk.StringVar()}


        self.shared_list = [] # this doesn't work, you can't get use .get function on a list

        #~~# Styles #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.title_font = tkfont.Font(family='Candara', size=18, weight="bold", slant="italic")

        #~~# Container and Frames #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        """The container contains a stack of frames. The visible frame is raised to the top."""
        container = tk.Frame(self)
        container.grid(row=0,column=0,sticky="NSEW")
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Home, JobScreen, AlertScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            """All of the pages in one location, the one on top is visible."""
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame("Login")

    #~~# JobLink Functions #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def show_frame(self, page_name):
        """Show a frame with the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame): ##########################################################################################################################

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(2,weight=2)

        #~~# Images #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.logo=ImageTk.PhotoImage(file="jobLinkLogo.png")

        #~~# Create Widget Styles #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #~~# Create Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        appName = Label(self, image=self.logo, text="  jobLink", font=controller.title_font, background="#aab7b8",compound="left")
        prompt = ttk.Label(self, text="User Login", font="Candara 14 bold")
        label_username = Label(self, text="Username: ", font="candara 18", background="#d6dbdf")
        entry_username = tk.Entry(self, font="candara 18", background="#aab7b8",textvariable=self.controller.shared_data["username"])
        label_password = Label(self, text="Password: ", font="candara 18", background="#d6dbdf")
        entry_password = Entry(self, font="candara 18", background="#aab7b8")
        checkbox = ttk.Checkbutton(self, text="Keep me logged in")
        logButton = ttk.Button(self, text="Login", command=lambda: Login.check_username(entry_username.get(),controller,self))

        #~~# Place Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        appName.grid(column=0, columnspan=4, row=0, sticky="EW", padx=0)
        prompt.grid(column=1, columnspan=1, row=2, sticky="EW", pady=35)
        label_username.grid(column=0, row=3, padx=10, pady=10, sticky="E")
        entry_username.grid(column=1, row=3, padx=10, pady=10, sticky="W")
        label_password.grid(column=0, row=4, padx=10, pady=10, sticky="E")
        entry_password.grid(column=1, row=4, padx=10, pady=10, sticky="W")
        checkbox.grid(column=0, row=5, padx=0, pady=35, sticky="E")
        logButton.grid(column=1, row=5, padx=25, pady=35, sticky="W")

        # Login Screen Functions #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def check_username(entry_username,controller,self):  #not complete, need to instantiate username for db
        """Checks to see if entry_username is a valid username in the database. If True, then it connects to that user's home screen.
            If False, then sends error message."""
        sql_user = 'SELECT User_ID FROM user WHERE UserName = "' + entry_username + '";'  # sets sql_user equal to User_ID for entry_username
        sql_assigned_jobs = 'SELECT * FROM assigned_jobs WHERE UserName ="' + entry_username + '";' #gets all data from assigned_jobs table
        sql_first = 'SELECT First_Name FROM user WHERE UserName ="' + entry_username + '";' #gets first name
        conn = pymysql.connect(host='localhost', user='root', password='Lm19orange@22', db='josc')
        a = conn.cursor()
        a.execute(sql_user)
        user_data = a.fetchall()
        a.execute(sql_assigned_jobs)
        ass_job_data = a.fetchall()
        a.execute(sql_first)
        first_data = a.fetchall()
        a.close()
        conn.close()

        if user_data == ():
            tm.showerror("Login error", "Incorrect username")
        else:
            found_user = Login._format_data(user_data)
            found_first = Login._format_data(first_data)
            job_data_dict = Login._format_data_j(ass_job_data)
            print (job_data_dict["j2"])

            self.controller.shared_job_dict["j0"].set(job_data_dict["j0"]) #this works and sends data to shared dict and then to button on home screen
            self.controller.shared_job_dict["j1"].set(job_data_dict["j1"])
            self.controller.shared_job_dict["j2"].set(job_data_dict["j2"])
            self.controller.shared_job_dict["j3"].set(job_data_dict["j3"])
            self.controller.shared_job_dict["j4"].set(job_data_dict["j4"])
            self.controller.shared_job_dict["j5"].set(job_data_dict["j5"])
            self.controller.shared_job_dict["j6"].set(job_data_dict["j6"])

            dict_job0 = self.controller.shared_job_dict["j0"].get() #these all work and print
            dict_job1 = self.controller.shared_job_dict["j1"].get()
            dict_job2 = self.controller.shared_job_dict["j2"].get()
            dict_job3 = self.controller.shared_job_dict["j3"].get()
            dict_job4 = self.controller.shared_job_dict["j4"].get()
            dict_job5 = self.controller.shared_job_dict["j5"].get()
            dict_job6 = self.controller.shared_job_dict["j6"].get()


            #value = self.controller.shared_job_dict.get('j1') #works

            self.controller.shared_data["user_id"].set(found_user)
            user_id = self.controller.shared_data["user_id"].get()

            self.controller.shared_data["user_first"].set(found_first)
            first_name = self.controller.shared_data["user_first"].get()

            username = self.controller.shared_data["username"].get()
            u_type_ID = Login._check_user_type(found_user)[0]  # (user_type)_ID

            user_type = Login._check_user_type(found_user)[1]

            return(self.controller.show_frame("Home"))


    def _format_data(user_data):
        """Formats data returned from MySQL DB to be a usable python data type."""
        data_set = []
        for n in user_data:
            data_set.append(n[0])
            format_data = data_set[0]
        return (format_data)

    def _format_data_test(ass_job_data):
        job_list = []
        for n in ass_job_data:
            job_list.append(n)
        return (job_list)



    def _format_data_j(ass_job_data):
        """Formats data returned from MySQL DB to be a python dictionary."""
        data_dict = {}
        job_no=[]
        i=0
        r=0
        for n in ass_job_data:
            job_no.append("j"+str(i))
            i += 1
        for n in job_no:
            data_dict.update({n:ass_job_data[r]})
            r += 1
        return (data_dict)

    def _check_user_type(found_user):
        """Checks tech, admin, client tables for existence of username. If exists, returns specific id."""
        tech_check = 'SELECT Tech_ID FROM technician WHERE User_ID = ' + str(found_user) + ';'
        admin_check = 'SELECT Admin_ID FROM admin WHERE User_ID = ' + str(found_user) + ';'
        client_check = 'SELECT Client_ID FROM client WHERE User_ID = ' + str(found_user) + ';'
        conn = pymysql.connect(host='localhost', user='root', password='Lm19orange@22', db='josc')
        a = conn.cursor()
        a.execute(tech_check)
        utype_data = a.fetchall()
        user_type = "technician"
        if utype_data == ():
            a.execute(admin_check)
            utype_data = a.fetchall()
            user_type = "admin"
            if utype_data == ():
                a.execute(client_check)
                utype_data = a.fetchall()
                user_type = "client"
        a.close()
        conn.close()
        return (Login._format_data(utype_data), user_type)




class Home(tk.Frame): #############################################################################################################################

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)

        #~~# Images #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.logo = ImageTk.PhotoImage(file="jobLinkLogo.png")
        self.homeImage = ImageTk.PhotoImage(file="home.png")  # make transparent
        self.logoutImage = ImageTk.PhotoImage(file="logout.png")  # make transparent
        self.userImage = ImageTk.PhotoImage(file="technician_pic.png")
        self.alertImage = ImageTk.PhotoImage(file="red_bell.png")  # make transparent
        self.jobImage = ImageTk.PhotoImage(file="job_green.png")  # make transparent
        self.jobImage2 = ImageTk.PhotoImage(file="job_orange.png") #make transparent

        #~~# Create Widget Styles #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        bStyle = ttk.Style()
        bStyle.configure("BW.TButton", width=8, foreground="black", background="#aab7b8", font="candara 10")
        bStyle.configure("Pink.BW.TButton", background="pink")
        bStyle.configure("Job.BW.TButton", width=25)
        bStyle.configure("Green.Job.BW.TButton", background="green")
        bStyle.configure("Orange.Job.BW.TButton", background="orange")


####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        un=self.controller.shared_data["username"]
        fn=(self.controller.shared_data["user_first"])

        dict_job0 = self.controller.shared_job_dict["j0"].get()
        dict_job1 = self.controller.shared_job_dict["j1"].get()
        dict_job2 = self.controller.shared_job_dict["j2"].get()
        dict_job3 = self.controller.shared_job_dict["j3"].get()
        dict_job4 = self.controller.shared_job_dict["j4"].get()
        dict_job5 = self.controller.shared_job_dict["j5"].get()
        dict_job6 = self.controller.shared_job_dict["j6"].get()

        print (dict_job0)





#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




        #~~# Create Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        appName = Label(self, image=self.logo,text="  jobLink", font=controller.title_font, background="#aab7b8",compound="left")
        button0 = ttk.Button(self,image=self.homeImage,compound="left",text=" HOME",style="BW.TButton",command=lambda: controller.show_frame("Home"))
        button3 = ttk.Button(self,image=self.logoutImage,compound="left",text=" LOGOUT",style="BW.TButton",command=lambda: controller.show_frame("Login"))
        usernameLabel = Label(self,textvariable=un,fg="#34495E", font="candara 18 bold")
        userAvatar = Button(self, image=self.userImage)
        uNameLabel = Label(self, textvariable=fn,fg="#34495E", font="candara 14 bold")
        uNameType = Label(self, text="Technician", fg="#34495E", font="candara 12 italic", height=1)
        uNameType2 = Label(self, text="Markraft Cabinets", fg="#34495E", font="candara 9 italic")
        completeJobs = Label(self, text="Completed Jobs (YTD): ", fg="black", font="candara 12")
        earnings = Label(self, text="Earnings (YTD): ", fg="black", font="candara 12")
        inProgress = Label(self, text="Jobs in Progress: ", fg="black", font="candara 12")
        cJint = Label(self, textvariable=self.controller.shared_data["user_id"], fg="black", font="candara 13 bold")
        e_int = Label(self, text="$54,040.41", fg="black", font="candara 13 bold")
        iPint = Label(self, text="2", fg="black", font="candara 13 bold")
        button2 = ttk.Button(self, image=self.alertImage, compound="left", style="Pink.BW.TButton", text=" ALERTS",command=lambda: controller.show_frame("AlertScreen"))

        recJob = Label(self, text="Recent Jobs: ", font=controller.title_font)
        jobLogoGreen0 = Label(self, image=self.jobImage)
        job_button0 = ttk.Button(self, style="Green.Job.BW.TButton", textvariable=self.controller.shared_job_dict["j0"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoGreen1 = Label(self, image=self.jobImage)
        job_button1 = ttk.Button(self, style="Green.Job.BW.TButton", textvariable=self.controller.shared_job_dict["j1"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoGreen2 = Label(self, image=self.jobImage)
        job_button2 = ttk.Button(self, style="Green.Job.BW.TButton", textvariable=self.controller.shared_job_dict["j2"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoGreen3 = Label(self, image=self.jobImage)
        job_button3 = ttk.Button(self, style="Green.Job.BW.TButton", textvariable=self.controller.shared_job_dict["j3"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoOrange4 = Label(self, image=self.jobImage2)
        job_button4 = ttk.Button(self, style="Orange.Job.BW.TButton",textvariable=self.controller.shared_job_dict["j4"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoOrange5 = Label(self, image=self.jobImage2)
        job_button5 = ttk.Button(self, style="Orange.Job.BW.TButton",textvariable=self.controller.shared_job_dict["j5"],command=lambda: controller.show_frame("JobScreen"))
        jobLogoOrange6 = Label(self, image=self.jobImage2)
        job_button6 = ttk.Button(self, style="Orange.Job.BW.TButton",textvariable=self.controller.shared_job_dict["j6"],command=lambda: controller.show_frame("JobScreen"))

        #~~# Place Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        appName.grid(column=0, columnspan=4, row=0, sticky="EW", padx=0)
        button0.grid(column=0, row=0, sticky="W",padx=4)  # background does not work
        button3.grid(column=2, row=0,sticky="E",padx=10)
        usernameLabel.grid(row=1,rowspan=1,column=0,pady=10,padx=8,sticky="SW")
        userAvatar.grid(row=2, rowspan=3, column=0, pady=0, padx=8,sticky="SW")
        uNameLabel.grid(row=5, column=0, pady=0, padx=4, sticky="SW")
        uNameType.grid(row=6, column=0, pady=0, padx=4, sticky="NW")
        uNameType2.grid(row=7, column=0, pady=0, padx=4, sticky="NW")
        completeJobs.grid(row=1, column=1, pady=4, padx=4, sticky="SW")
        earnings.grid(row=2,column=1,pady=0,padx=4,sticky="SW")
        inProgress.grid(row=3, column=1, pady=0, padx=4, sticky="SW")
        cJint.grid(row=1, column=2,sticky="SW",padx=15, pady=4)
        e_int.grid(row=2,column=2,sticky="SW",padx=15,pady=0)
        iPint.grid(row=3, column=2,sticky="SW", padx=15,pady=0)
        button2.grid(column=1, padx=4,pady=18,row=4, sticky="SW")

        recJob.grid(column=1,row=6)
        jobLogoGreen0.grid(column=0,row=7,pady=8,padx=2,sticky="SE")
        job_button0.grid(column=1,row=7,pady=8,sticky="SW")
        jobLogoGreen1.grid(column=0, row=8, pady=8, padx=2, sticky="SE")
        job_button1.grid(column=1, row=8, pady=8, sticky="SW")
        jobLogoGreen2.grid(column=0, row=9, pady=8, padx=2, sticky="SE")
        job_button2.grid(column=1, row=9, pady=8, sticky="SW")
        jobLogoGreen3.grid(column=0, row=10, pady=8, padx=2, sticky="SE")
        job_button3.grid(column=1, row=10, pady=8, sticky="SW")
        jobLogoOrange4.grid(column=0, row=11, pady=8, padx=2, sticky="SE")
        job_button4.grid(column=1, row=11, pady=8, sticky="SW")
        jobLogoOrange5.grid(column=0, row=12, pady=8, padx=2, sticky="SE")
        job_button5.grid(column=1, row=12, pady=8, sticky="SW")
        jobLogoOrange6.grid(column=0, row=13, pady=8, padx=2, sticky="SE")
        job_button6.grid(column=1, row=13, pady=8, sticky="SW")



    #~~# Home Screen Functions #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __str__(self):
        result = ""

    def __getitem__(self,item):
        return self.find.item

class JobScreen(tk.Frame):  #####################################################################################################################

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #~~# Images #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #~~# Create Widget Styles #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #~~# Create Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        label = tk.Label(self, text="This is Job Screen", font=controller.title_font)
        button = ttk.Button(self, text="Home", command=lambda: controller.show_frame("Home"))
        button2 = ttk.Button(self, text="Logout", command=lambda: controller.show_frame("Login"))

        #~~# Place Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        label.pack(side="top", fill="x", pady=10)
        button.pack()
        button2.pack()

    #~~# Job Screen Functions #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



class AlertScreen(tk.Frame): ####################################################################################################################

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #~~# Styles #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #~~# Create Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        label = tk.Label(self, text="This is AlertScreen", font=controller.title_font)
        button = ttk.Button(self, text="Home", command=lambda: controller.show_frame("Home"))
        button2 = ttk.Button(self, text="Logout", command=lambda: controller.show_frame("Login"))

        #~~# Place Widgets #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        label.pack(side="top", fill="x", pady=10)
        button.pack()
        button2.pack()

    #~~# Alert Screen Functions #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



if __name__ == "__main__":
    app = JobLink()
    app.mainloop()