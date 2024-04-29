import tkinter as tk
from tkinter import Label,messagebox,Entry,Button,Frame,font
from PIL import Image,ImageTk
import mysql.connector

class Hr:
    def __init__(self):
        self.name = None
        self.position = None
        self.department = None
        self.mainpic = None
        self.surname = ""
        self.firstname = ""
        self.middlename = ""
        self.suffix = ""
        self.sex = ""
        self.birthday = ""
        self.birthplace = ""
        self.address = ""
        self.civilstatus = ""
        self.contactnumber = ""
        self.religion = ""
        self.email = ""
        self.id = 0
        self.elementary = ""
        self.juniorhigh = ""
        self.seniorhigh = ""
        self.college = ""
        self.course = ""
        self.graduateStudies = ""
        self.post_graduate = ""
        self.prcIdpic= ""
        self.civilCertificatepic = ""
        self.cpdSeminarpic = ""
        self.tesdaPic = ""
        self.trainTitle1 = ""
        self.trainTitle2 = ""
        self.trainTitle3 = ""
        self.trainDate1 = ""
        self.trainDate2 = ""
        self.trainDate3 = ""
        self.trainPic1 = ""
        self.trainPic2 = ""
        self.trainPic3 = ""
        self.empHistoryDate1 = ""
        self.empHistoryDate2 = ""
        self.empHistoryDate3 = ""
        self.empHistoryDesc1 = ""
        self.empHistoryDesc2 = ""
        self.empHistoryDesc3 = ""
        self.serviceDate1 = ""
        self.serviceDate2 = ""
        self.serviceDate3 = ""
        self.serviceInfo1 = ""
        self.serviceInfo2 = ""
        self.serviceInfo3 = ""
        
        self.mybd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "micopogi_88",
            database = "hr"
        )
        self.mycursor = self.mybd.cursor()
            
    def mainform(self): #form for fucntion of the program
        global List
        List = tk.Toplevel()
        List.geometry("760x600")
        header = tk.Frame(List, width=800, height=50, borderwidth=2, relief="solid", bg="#86a3c2")
        
        title = tk.Label(header, text="FACULTY / EMPLOYEE PROFILE", font=("Arial", 20), bg="#86a3c2")
        header.pack(fill=tk.X)
        title.pack()
        
        iframe = Frame(List,width=800,height=550,bg="#7ebfe0")
        iframe.pack(fill=tk.BOTH)
        idpicPath = "Pictures/picID/"
        self.image = Image.open(idpicPath+self.mainpic)
        final = self.image.resize((200,200))
        self.mainpic = ImageTk.PhotoImage(final)
        pic = Label(iframe,image=self.mainpic)
        pic.grid(row=0,column=0,rowspan=3,sticky="n",pady=5,padx=20)
        
        name = Label(iframe,text=self.name,font=("Arial",15),width=19,height=2,border=1,relief="solid",bg="#61a2c2")
        name.grid(row=3,column=0,padx=10)
        
        position = Label(iframe,text=self.position,font=("Arial",15),width=19,height=2,border=1,relief="solid",bg="#61a2c2")
        position.grid(row=4,column=0,padx=10,pady=10)
        
        department = Label(iframe,text=self.department,font=("Arial",15),width=19,height=2,border=1,relief="solid",bg="#61a2c2")
        department.grid(row=5,column=0,padx=10,pady=10)
        
        b1 = Button(iframe,text="PERSONAL INFORMATION",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.personalInfo)
        b1.grid(row=0,column=1,padx=50,pady=10,ipadx=100)
        
        b2 = Button(iframe,text="ACADEMIC BACKGROUND",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.academicbackground)
        b2.grid(row=1,column=1,padx=10,pady=10,ipadx=100)
        
        b3 = Button(iframe,text="ELIGIBILITY",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.eligibility)
        b3.grid(row=2,column=1,padx=10,pady=10,ipadx=100)
        
        b4 = Button(iframe,text="TRAININGS / SEMINARS",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.training)
        b4.grid(row=3,column=1,padx=10,pady=10,ipadx=100)
        
        b5 = Button(iframe,text="EMPLOYMENT HISTORY",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.employeeHistory)
        b5.grid(row=4,column=1,padx=10,pady=10,ipadx=100)
        
        b6 = Button(iframe,text="SERVICE RECORD",width=30,height=3,bg="#961a1a",fg="#FFFFFF",command=self.ServiceRecord)
        b6.grid(row=5,column=1,padx=10,pady=10,ipadx=100)
    def academicbackground(self):
        academic = tk.Tk()
        academic.geometry("860x600")    
        academic.config(bg="#fedbd0")
        labelTitle = Label(academic, text="ACADEMIC BACKGROUND", bg="#fedbd0", fg="#442c2e",font=("Arial",20))
        labelTitle.grid(row=0,column=0,padx=10,pady=10)
        self.academicSearch()
        self.labelElementary = Label(academic, text="Elementary School: " + self.elementary, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelJuniorHigh = Label(academic, text="Junior High School: " + self.juniorhigh, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelSeniorHigh = Label(academic, text="Senior High School: " + self.seniorhigh, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelCollege = Label(academic, text="College: " + self.college, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelCourse = Label(academic, text="Course: " + self.course, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelGraduateStudies = Label(academic, text="Graduate Studies: " + self.graduateStudies, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        self.labelPostGraduate = Label(academic, text="Post Graduate: " + self.post_graduate, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=70, font=("Arial", 15))
        
        self.labelElementary.grid(row=1, column=0, padx=10, pady=10)
        self.labelJuniorHigh.grid(row=2, column=0, padx=10, pady=10)
        self.labelSeniorHigh.grid(row=3, column=0, padx=10, pady=10)
        self.labelCollege.grid(row=4, column=0, padx=10, pady=10)
        self.labelCourse.grid(row=5, column=0, padx=10, pady=10)
        self.labelGraduateStudies.grid(row=6, column=0, padx=10, pady=10)
        self.labelPostGraduate.grid(row=7, column=0, padx=10, pady=10)
    def academicSearch(self):
        self.mycursor.execute("SELECT * FROM academicbackground WHERE EmployeeID = %s",(self.id,))
        result = self.mycursor.fetchall()
        for row in result:
            self.elementary = row[2]
            self.juniorhigh = row[3]
            self.seniorhigh = row[4]
            self.college = row[5]
            self.course = row[6]
            self.graduateStudies = row[7]
            self.post_graduate = row[8]   
            
    def personalInfoSearch(self):
        self.mycursor.execute("SELECT * FROM personalinfo WHERE EmployeeID = %s",(self.id,))
        result = self.mycursor.fetchall()
        for row in result:
            self.contactnumber = str(row[2])
            self.birthday = str(row[3])
            self.surname = row[4]
            self.firstname = row[5]
            self.middlename = row[6]
            self.suffix = row[7]
            self.address = row[8]
            self.civilstatus = row[9]
            self.sex = row[10]
            self.birthplace = row[11]
            self.religion = row[12]
            self.email = row[13]
    def personalInfo(self):
        personal = tk.Toplevel()
        personal.geometry("580x830") 
        personal.config(bg="#fedbd0")
        self.personalInfoSearch()
        labelTitle = Label(personal, text="PERSONAL INFORMATION", bg="#fedbd0", fg="#442c2e",font=("Arial",20))
        self.labelFname = Label(personal, text="First Name: " + self.firstname, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelLname = Label(personal, text="Last Name: " + self.surname, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelMname = Label(personal, text="Middle Name: " + self.middlename, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelSuffix = Label(personal, text="Suffix: " + self.suffix, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelSex = Label(personal, text="Sex: " + self.sex, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelBirthday = Label(personal, text="Birthday: " + self.birthday, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelBirthplace = Label(personal, text="Birthplace: " + self.birthplace, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelAddress = Label(personal, text="Address: " + self.address, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelCivilstatus = Label(personal, text="Civil Status: " + self.civilstatus, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelContactNum = Label(personal, text="Contact Number: " + self.contactnumber, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelReligion = Label(personal, text="Religion: " + self.religion, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        self.labelEmail = Label(personal, text="Email: " + self.email, bg="#fedbd0", fg="#442c2e", borderwidth=2, relief="solid", height=2, width=50,font=("Arial",15))
        
        labelTitle.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.labelFname.grid(row=1, column=0, pady=5,padx=10)
        self.labelLname.grid(row=2, column=0, pady=5,padx=10)
        self.labelMname.grid(row=3, column=0, pady=5,padx=10)
        self.labelSuffix.grid(row=4, column=0, pady=5,padx=10)
        self.labelSex.grid(row=5, column=0, pady=5,padx=10)
        self.labelBirthday.grid(row=6, column=0, pady=5,padx=10)
        self.labelBirthplace.grid(row=7, column=0, pady=5,padx=10)
        self.labelAddress.grid(row=8, column=0, pady=5,padx=10)
        self.labelCivilstatus.grid(row=9, column=0, pady=5,padx=10)
        self.labelContactNum.grid(row=10, column=0, pady=5,padx=10)
        self.labelReligion.grid(row=11, column=0, pady=5,padx=10)
        self.labelEmail.grid(row=12, column=0, pady=5,padx=10)
    def eligibility(self):
        eligibility = tk.Toplevel()
        eligibility.geometry("650x850")
        eligibility.config(bg="#fedbd0")
        self.eligibilityQuery()
        title = Label(eligibility, text="Eligibility", bg="#fedbd0", fg="#442c2e", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        prcPath = "Pictures/Eligibility/"
        civilPath = "Pictures/Eligibility/"
        cpdPath = "Pictures/Eligibility/"
        tesdaPath = "Pictures/Eligibility/"
        
        
        lab1 = Label(eligibility, text="PRC ID", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab2 = Label(eligibility, text="Civil Service Certificate", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab3 = Label(eligibility, text="CPD Seminar", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab4 = Label(eligibility, text="Tesda Certificate", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        
        lab1.grid(row=1,column=0,padx=10,pady=10)
        lab2.grid(row=1,column=1,padx=10,pady=10)
        lab3.grid(row=3,column=0,padx=10,pady=10)
        lab4.grid(row=3,column=1,padx=10,pady=10)
    
        # Load and resize images
        prc_image = Image.open(prcPath + self.prcIdpic)  # Assuming "prc_image.jpg" is the file name
        prc_final = prc_image.resize((300, 300))
        self.prcIdpic = ImageTk.PhotoImage(prc_final)
        
        civil_image = Image.open(civilPath +self.civilCertificatepic)  # Assuming "civil_image.jpg" is the file name
        civil_final = civil_image.resize((300, 300))
        self.civilCertificatepic = ImageTk.PhotoImage(civil_final)
        
        cpd_image = Image.open(cpdPath +self.cpdSeminarpic)  # Assuming "cpd_image.jpg" is the file name
        cpd_final = cpd_image.resize((300, 300))
        self.cpdSeminarpic = ImageTk.PhotoImage(cpd_final)
        
        tesda_image = Image.open(tesdaPath + self.tesdaPic)  # Assuming "tesda_image.jpg" is the file name
        tesda_final = tesda_image.resize((300, 300))
        self.tesdaPic = ImageTk.PhotoImage(tesda_final)
        
        # Create labels with images
        prc_label = Label(eligibility, image=self.prcIdpic)
        prc_label.grid(row=2, column=0, padx=10, pady=10)

        civil_label = Label(eligibility, image=self.civilCertificatepic)
        civil_label.grid(row=2, column=1, padx=10, pady=10)

        cpd_label = Label(eligibility, image=self.cpdSeminarpic)
        cpd_label.grid(row=4, column=0, padx=10, pady=10)

        tesda_label = Label(eligibility, image=self.tesdaPic)
        tesda_label.grid(row=4, column=1, padx=10, pady=10)
    def eligibilityQuery(self):
        query = "SELECT * FROM Eligibility WHERE EmployeeId = %s"
        self.mycursor.execute(query,(self.id,))
        result = self.mycursor.fetchall()
        if result:
            for x in result:
                self.prcIdpic = x[2]
                self.civilCertificatepic = x[3]
                self.cpdSeminarpic = x[4]
                self.tesdaPic = x[5]
                
    def training(self):
        training = tk.Toplevel()
        training.geometry("1270x600")
        training.config(bg="#fedbd0")
        self.trainingQuery()
        title = Label(training, text="Training/Seminars Certificates", bg="#fedbd0", fg="#442c2e", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        lab1 = Label(training, text="Title", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab2 = Label(training, text="Date", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab3 = Label(training, text="Certificate", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab4 = Label(training, text="Title", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab5 = Label(training, text="Date", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab6 = Label(training, text="Certificate", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab7 = Label(training, text="Title", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab8 = Label(training, text="Date", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab9 = Label(training, text="Certificate", bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        
        Title1 = Label(training, text=self.trainTitle1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        Title2 = Label(training, text=self.trainTitle2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        Title3 = Label(training, text=self.trainTitle3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        Date1 = Label(training, text=self.trainDate1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        Date2 = Label(training, text=self.trainDate2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        Date3 = Label(training, text=self.trainDate3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        trainingCertPath = "Pictures/Training/"
        
        cert1 = Image.open(trainingCertPath+self.trainPic1)
        certF1 = cert1.resize((400,200))
        self.trainPic1 = ImageTk.PhotoImage(certF1)
        
        cert2 = Image.open(trainingCertPath+self.trainPic2)
        certF2 = cert2.resize((400,200))
        self.trainPic2 = ImageTk.PhotoImage(certF2)
        
        cert3 = Image.open(trainingCertPath+self.trainPic3)
        certF3 = cert3.resize((400,200))
        self.trainPic3 = ImageTk.PhotoImage(certF3)

        
        image1 = Label(training, image=self.trainPic1)
        image2 = Label(training, image=self.trainPic2)
        image3 = Label(training, image=self.trainPic3)
        
        
        lab1.grid(column=0,row=1,padx=10,pady=10)
        lab4.grid(column=1,row=1,padx=10,pady=10)
        lab7.grid(column=2,row=1,padx=10,pady=10)
        
        Title1.grid(row=2,column=0,padx=10,pady=10)
        Title2.grid(row=2,column=1,padx=10,pady=10)
        Title3.grid(row=2,column=2,padx=10,pady=10)
        
        lab2.grid(row=3,column=0,padx=10,pady=10)
        lab5.grid(row=3,column=1,padx=10,pady=10)
        lab8.grid(row=3,column=2,padx=10,pady=10)
        
        Date1.grid(row=4,column=0,padx=10,pady=10)
        Date2.grid(row=4,column=1,padx=10,pady=10)
        Date3.grid(row=4,column=2,padx=10,pady=10)
        
        lab3.grid(row=5,column=0,padx=10,pady=10)
        lab6.grid(row=5,column=1,padx=10,pady=10)
        lab9.grid(row=5,column=2,padx=10,pady=10)
        
        image1.grid(row=6,column=0,padx=10,pady=10)
        image2.grid(row=6,column=1,padx=10,pady=10)
        image3.grid(row=6,column=2,padx=10,pady=10)
        
    def trainingQuery(self):
        query = "SELECT * FROM training_seminar WHERE EmployeeId = %s"
        self.mycursor.execute(query,(self.id,))
        result = self.mycursor.fetchall()
        if result:
            for x in result:
                self.trainDate1 = x[2]
                self.trainTitle1 = x[3]
                self.trainPic1 = x[4]
                self.trainDate2 = x[5]
                self.trainTitle2 = x[6]
                self.trainPic2 = x[7]
                self.trainDate3 = x[8]
                self.trainTitle3 = x[9]
                self.trainPic3 = x[10]
                
    def ServiceRecord(self):
        service= tk.Toplevel()
        service.config(bg="#fedbd0")
        service.geometry("550x300")
        self.serviceQuery()
        lab1 = Label(service,text="Service Records", bg="#fedbd0", fg="#442c2e", font=("Arial", 20))
        
        lab1.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
        
        lab2 = Label(service,text="Service Info",bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        lab3 = Label(service,text="Date",bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        
        lab2.grid(row=1,column=0,padx=10,pady=10)
        lab3.grid(row=1,column=3,columnspan=3,padx=10,pady=10)
        
        ser1 = Label(service,text=self.serviceDate1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        ser2 = Label(service,text=self.serviceDate2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        ser3 = Label(service,text=self.serviceDate3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        ser4 = Label(service,text=self.serviceInfo1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        ser5 = Label(service,text=self.serviceInfo2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        ser6 = Label(service,text=self.serviceInfo3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        ser1.grid(row=2,column=3,columnspan=3,padx=10,pady=10)
        ser2.grid(row=3,column=3,columnspan=3,padx=10,pady=10)
        ser3.grid(row=4,column=3,columnspan=3,padx=10,pady=10)
        
        ser4.grid(row=2,column=0,padx=10,pady=10)
        ser5.grid(row=3,column=0,padx=10,pady=10)
        ser6.grid(row=4,column=0,padx=10,pady=10)
    def serviceQuery(self):
        query = "SELECT * FROM servicerecords WHERE EmployeeId = %s"
        self.mycursor.execute(query,(self.id,))
        result = self.mycursor.fetchall()
        if result:
            for x in result:
                self.serviceDate1 = x[2]
                self.serviceInfo1 = x[3]
                self.serviceDate2 = x[4]
                self.serviceInfo2 = x[5]
                self.serviceDate3 = x[6]
                self.serviceInfo3 = x[7]
        
    def employeeHistory(self):
        history = tk.Toplevel()
        history.geometry("600x300")
        history.config(bg="#fedbd0")
        title = Label(history, text="Employment History", bg="#fedbd0", fg="#442c2e", font=("Arial", 20))
        self.historyQuery()
        date = Label(history,text="Date",bg="#fedbd0", fg="#442c2e",font=("Arial",15))
        description = Label(history,text="Description",bg="#fedbd0", fg="#442c2e",font=("Arial",15))
            
        title.grid(row=0,column=0,columnspan=2,pady=10)
        date.grid(row=1,column=0,padx=10,pady=10)
        description.grid(row=1,column=2,columnspan=2,padx=10,pady=10)
        text = Label(history,text="                              ",bg="#fedbd0").grid(row=1,column=1,)
        
        date1 = Label(history,text=self.empHistoryDate1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        date2 = Label(history,text=self.empHistoryDate2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        date3 = Label(history,text=self.empHistoryDate3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        desc1 = Label(history,text=self.empHistoryDesc1, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        desc2 = Label(history,text=self.empHistoryDesc2, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        desc3 = Label(history,text=self.empHistoryDesc3, bg="#fedbd0", fg="#442c2e",font=("Arial",15,"underline"))
        
        date1.grid(row=2,column=0,padx=10,pady=10)
        date2.grid(row=3,column=0,padx=10,pady=10)
        date3.grid(row=4,column=0,padx=10,pady=10)
        
        desc1.grid(row=2,column=2,columnspan=2,padx=10,pady=10)
        desc2.grid(row=3,column=2,columnspan=2,padx=10,pady=10)
        desc3.grid(row=4,column=2,columnspan=2,padx=10,pady=10)  
          
    def historyQuery(self):
        query = "SELECT * FROM employmenthistory WHERE EmployeeId = %s"
        self.mycursor.execute(query,(self.id,))
        result = self.mycursor.fetchall()
        if result:
            for x in result:
                self.empHistoryDesc1 = x[2]
                self.empHistoryDate1 = x[3]
                self.empHistoryDesc2 = x[4]
                self.empHistoryDate2 = x[5]
                self.empHistoryDesc3 = x[6]
                self.empHistoryDate3 = x[7]          
    def menuform(self): #form for employee search
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.config(bg="#fedbd0")
        self.root.title("HRMD Server")
        
        
        pic = "Pictures/logo.png"
        logo = Image.open(pic)
        final = logo.resize((120,100))
        self.logo = ImageTk.PhotoImage(final)
        
        header = Frame(self.root, width=500, height=100, bg="#fedbd0")
        footer = Frame(self.root, width=500, height=100, bg="#fedbd0")
        body = Frame(self.root, width=500, height=300, bg="#fedbd0")
        
        labelT = Label(header, text="HUMAN RESOURCES\nMANAGEMENT DEPARTMENT", width=38, bg="#fedbd0", fg="#442c2e", font=("Arial", 16, "bold"))
        labelS = Label(body, text="Search Employee", bg="#fedbd0", font=("Arial", 15))
        self.entryName = Entry(body, bg="#fedbd0", font=("Arial", 20))
        b = Button(body, text="Search", bg="#fedbd0", command=self.search,font=("Arial",10))
        header.grid(row=0, column=0, columnspan=2)
        labelT.pack(pady=20)
        
        body.grid(row=1, column=0, columnspan=2)
        logopic = Label(body,image=self.logo, bg="#fedbd0").pack()
        labelS.pack(padx=10)
        self.entryName.pack(padx=10, pady=10)
        b.pack(padx=10, pady=10)
        
        footer.grid(row=2, column=0, columnspan=2)
    def search(self):
        name = self.entryName.get()
        query = "SELECT * FROM employee WHERE FullName = %s"
        self.mycursor.execute(query, (name,))
        self.myresult = self.mycursor.fetchall()
        if self.myresult:
          for x in self.myresult:
              self.id = int(x[0])
              self.name = x[1]
              self.position = x[2]
              self.department = x[3]
              self.mainpic = x[4]
              self.mainform()
        else:
            messagebox.showerror("Error", "Employee not found")
 
    def start(self):
        self.menuform()
        self.root.mainloop()
        
hr = Hr()
hr.start()