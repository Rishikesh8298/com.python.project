import tkinter as tk
import datetime
from random import randint
from tkinter import ttk, messagebox as msg
from template import Template
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, DuplicateKeyError

class PharmacyLogin(Template):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client["PharmacyManagement"]
    
    def __init__(self, win):
        self.win=win
        self.win.title("Pharmacy Management System")
        self.win.resizable(0, 0)
    # ================== Variable =====================
        self.username=tk.StringVar()
        self.password=tk.StringVar()
    # ================== Heading ======================
        tk.Label(self.win, text="Pharmacy Management System", font="Consolas 25 bold", foreground="#4ca1af").grid(column=0,row=0, padx=2, ipady=5, ipadx=3, pady=5)
    # ================== Login Design =================
        self.frame=tk.LabelFrame(self.win, bd=1)
        self.frame.grid(column=0, row=1,pady=10)
        self.labelEntry(window=self.frame, textData="Username", var=self.username, rowData=0)
        self.labelEntry(window=self.frame, textData="Password", var=self.password, rowData=1, status="*")
        for i in self.frame.winfo_children():
            i.grid_configure(pady=5, ipady=2, padx=3,ipadx=3)
    # ================== Enable Button ================
        enableButton=tk.LabelFrame(self.frame, bd=1)
        enableButton.grid(column=0, row=2, columnspan=2, ipadx=5)
        buttonTexts=["Login", "Reset", "ExitWindow"]
        buttonMethod=[self.login, self.reset, self.exitWindow]
        for i in range(len(buttonMethod)):
            self.button(window=enableButton, textData=buttonTexts[i], comData=buttonMethod[i], col=i, rowData=0)
        for i in enableButton.winfo_children():
            i.grid_configure(ipadx=2)
    # ================= Disabled Button ===============
        disableButton=tk.LabelFrame(self.win, bd=1)
        disableButton.grid(column=0, row=2, pady=5)
        self.patient=tk.Button(disableButton, text="Patient Registrations", command=self.registration, state="disabled")
        self.patient.grid(column=0, row=0)
        self.hospital=tk.Button(disableButton, text="Hospital Managements", command=self.hospial, state="disabled")
        self.hospital.grid(column=1, row=0)
        for i in disableButton.winfo_children():
            i.grid_configure(ipady=3, ipadx=3)
# ===================== Button Defining ===============
    def login(self):
        collection=self.database["admin"]
        try:
            for i in collection.find():
                if i["Username"]==self.username.get() and i["Password"] == self.password.get():
                    self.patient.configure(state="normal")
                    self.hospital.configure(state="normal")
                else: msg.showerror("Error", "Invaid User password")
        except ServerSelectionTimeoutError: msg.showerror("Error", "Please Turn ON your database!!")
        except DuplicateKeyError: msg.showerror("Error", "Duplicate Key Error!!")
        except: msg.showerror("Error", "Unkonwn error occur!!")

    def reset(self):
        self.username.set("")
        self.password.set("")
    
    def exitWindow(self):
        ms = msg.askyesno("Confirm", "Are you sure")
        if ms==True: exit(0)

    def registration(self):
        top=tk.Toplevel(self.win)
        patient=PatientRegistration(win=top)

    def hospial(self):
        top=tk.Toplevel(self.win)
        hp=Hospital(root=top)

class PatientRegistration(Template):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client["PharmacyManagement"]
    collection=database["Patient_Record"]
    def __init__(self, win):
    # ================= New Window ====================
        self.win=win
        self.win.title("Patient Registrations System")
        self.win.resizable(0,0)
    # ================= Variable ======================
        now=datetime.datetime.now()
        today=str(now.day)+"/"+str(now.month)+"/"+ str(now.year)
        self.reference=tk.StringVar()
        self.firstname=tk.StringVar()
        self.surename=tk.StringVar()
        self.address=tk.StringVar()
        self.postcode=tk.StringVar()
        self.telephone=tk.StringVar()
        self.current=tk.StringVar()
        self.proveId=tk.StringVar()
        self.typeMember=tk.StringVar()
        self.paymentMethod=tk.StringVar()
        self.fee=tk.StringVar()
        self.current.set(today)
    # ================= Frames ========================
        self.headerFrame=tk.Frame(self.win, width=945, height=100, bd=5, relief=tk.GROOVE, background="#4ca1af")
        self.headerFrame.grid(column=0, row=0, columnspan=2)
        self.mainFrame=tk.Frame(self.win, width=945, height=420, bd=5, relief=tk.GROOVE, background="#1F8AC0")
        self.mainFrame.grid(column=0, row=1, columnspan=2)
    # ================= Heading =======================
        tk.Label(self.win, text="Patient Registration System", font="Consolas 25 bold", background="#4ca1af", foreground="white").grid(column=0,row=0, padx=2, columnspan=2)
    # ================= main Left Frame ===============
        self.dataFrame=tk.LabelFrame(self.win, text="Customer Name", bd=3, relief=tk.GROOVE, background="#FFA781", foreground="white", font="Consolas 10 bold")
        self.dataFrame.grid(column=0,row=1, sticky='W', padx=4)
        tk.Label(self.dataFrame, text="Reference No", background="#FFA781", foreground="white").grid(column=0, row=0, sticky="W")
        self.refer=tk.Entry(self.dataFrame, textvariable=self.reference, width=25,bd=3, relief=tk.GROOVE, state=tk.DISABLED)
        self.refer.grid(column=1, row=0)
        varList=[self.firstname, self.surename, self.address, self.postcode, self.telephone, self.current]
        labelText=["Firstname", "Surname", "Address", "Postcode", "Telephone", "Date"]
        for i in range(len(labelText)):
            self.labelEntryPatient(self.dataFrame, textData=labelText[i], var=varList[i], rowData=i+1)
        comboText=["Prove of Id", "Type of Member", "Method of payment"]
        comboValue=[["Addhar Card", "Passport","Driving Licence", "Student Id", "Pancard"], ["Full Member", "Arrival Membership", "Pay as you go"], ["Visa Card", "Credit Card", "Debit Card"]]
        comboVar=[self.proveId, self.typeMember, self.paymentMethod]
        for i in range(len(comboText)):
            self.comboPatient(window=self.dataFrame, textData=comboText[i], var=comboVar[i], values=comboValue[i], rowdata=i+7)
        tk.Label(self.dataFrame, text="Patient Fees", background="#FFA781", foreground="white").grid(column=0, row=11, sticky="W")
        self.feeBox=tk.Entry(self.dataFrame, textvariable=self.fee, width=25,bd=3, relief=tk.GROOVE, state=tk.DISABLED)
        self.feeBox.grid(column=1, row=11)
        for i in self.dataFrame.winfo_children():
            i.grid_configure(ipady=2,pady=3, padx=4)
    # ================= main right Frame ==============
        self.displayframe=tk.LabelFrame(self.win, bd=3, relief=tk.GROOVE, background="#FFA781")
        self.displayframe.grid(column=1, row=1, sticky="W")
        listText=["Patient Ref", "Firstname", "Surename", "Address", "Date Reg.", "Telephone", "Patient Paid"]
        for i in range(len(listText)):
            tk.Label(self.displayframe, text=listText[i], background="#FFA781", foreground="white").grid(column=i, row=0, padx=4, ipady=5, sticky="W")
        self.textbox=tk.Text(self.displayframe, height=18, width=70)
        self.textbox.grid(column=0, row=1, columnspan=7)
        self.buttonFrame=tk.LabelFrame(self.displayframe, bd=0, background="#FFA781")
        self.buttonFrame.grid(column=0, row=2, columnspan=7)
        butText=["Recepit", "Reset", "Exit"]
        butDecal=[self.recepit, self.reset, self.exitWindow]
        for i in range(len(butText)):
            self.button(window=self.buttonFrame, textData=butText[i], comData=butDecal[i], col=i, rowData=0)
# ================== button Defining ==================
    def recepit(self):
        self.refer.configure(state="normal")
        self.feeBox.configure(state="normal")
        ref=randint(100000, 999999)
        self.reference.set(ref)
        self.fee.set(str("500"+"RS"))
        document={
            "_id":self.reference.get(),
            "First Name":self.firstname.get(),
            "Sure Name":self.surename.get(),
            "Address":self.address.get(),
            "Postcode":self.postcode.get(),
            "Telephone":self.telephone.get(),
            "Today Date":self.current.get(),
            "Prove ID":self.proveId.get(),
            "Type of Member":self.typeMember.get(),
            "Payment Method":self.paymentMethod.get(),
            "Fee":self.fee.get(),
        }
        self.insertData(document)

    def reset(self):
        listVar=[self.reference, self.firstname, self.surename, self.address, self.postcode, self.telephone, self.proveId, self.typeMember
        ,self.paymentMethod]
        for i in listVar:
            i.set("")

    def exitWindow(self):
        ms = msg.askyesno("Confirm", "Are you sure")
        if ms==True: exit(0)
# ================ Database Interaction ===============
    def insertData(self, document):
        try: self.collection.insert_one(document)
        except ServerSelectionTimeoutError: msg.showerror("Error", "Please turn ON your database server!!!")
        except DuplicateKeyError: self.recepit()
        except: msg.showerror("Error", "Unknown error occur!!")
        else:
            msg.showinfo("Success", "Data successfully inserted!!")
            self.display()
    
    def display(self):
        self.textbox.delete("1.0", "end-1c")
        self.textbox.insert(tk.INSERT, str(self.reference.get())+ "\t   "+ self.firstname.get()+"\t   "+self.address.get()+"\t   "+self.current.get()+"\t   "+self.telephone.get()+ "\t   "+self.fee.get())

        
class Hospital(Template):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client["PharmacyManagement"]
    collection=database["Hospital_Record"]
    def __init__(self, root):
    # ======================= Variable ===========================
        self.root=root
        self.root.title("Hospital Management System")
        self.root.resizable(0,0)
        self.tabletName=tk.StringVar()
        self.reference=tk.StringVar()
        self.dose=tk.StringVar()
        self.number_of_tablets=tk.StringVar()
        self.lots=tk.StringVar()
        self.issuedDate=tk.StringVar()
        self.expDate=tk.StringVar()
        self.dailyDose=tk.StringVar()
        self.sideEffect=tk.StringVar()
        self.furtherInformation=tk.StringVar()
        self.storageAdvice=tk.StringVar()
        self.medication=tk.StringVar()
        self.drivingMachines=tk.StringVar()
        self.patientID=tk.StringVar()
        self.nhsNumber=tk.StringVar()
        self.patientName=tk.StringVar()
        self.dob=tk.StringVar()
        self.patientAddress=tk.StringVar()
    # ========================== Frame ===========================
        self.headerFrame=tk.Frame(self.root, bd=5, relief=tk.GROOVE, width=900, height=80, background="#077b8a")
        self.headerFrame.grid(column=0, row=0, columnspan=3)
        self.mainInfoFrame=tk.Frame(self.root, bd=5, relief=tk.GROOVE, width=900, height=250, background="#FFA781")
        self.mainInfoFrame.grid(column=0,row=1, columnspan=3)
        self.mainButtonFrame=tk.Frame(self.root, bd=5, relief=tk.GROOVE, width=900, height=50, background="#595775")
        self.mainButtonFrame.grid(column=0, row=2, columnspan=3)
        self.footerFrame=tk.Frame(self.root, bd=5, relief=tk.GROOVE, width=900, height=100, background="#F2EAED")
        self.footerFrame.grid(column=0, row=3, columnspan=3)
    # ========================= Heading ==========================
        tk.Label(self.root, text="Hospital Management System", background="#077b8a", font="Consolas 25 bold", foreground="white").grid(column=0, row=0, columnspan=3)
    # ====================== Input frame =========================
        self.inputFrame=tk.LabelFrame(self.root, text="Patient Information", bd=1, background="#FFA781", foreground="white", font="Consolas 10 bold")
        self.inputFrame.grid(column=0, row=1, columnspan=2, sticky="W")
    # =================== Left Frame Referenced ==================
        self.leftframe=tk.LabelFrame(self.inputFrame, bd=0, background="#FFA781")
        self.leftframe.grid(column=0,row=0, ipady=5, ipadx=5)
        tk.Label(self.leftframe, text="Name of Tablets: ", background="#FFA781", foreground="white").grid(column=0, row=0,sticky="W")
        self.combo=ttk.Combobox(self.leftframe, textvariable=self.tabletName, width=19, height=10, state ="readonly")
        self.combo['value']=['Noni', "respocare", "Aloe Vera", "Co-codamol", "Paracetamol", "Amlodipine"]
        self.combo.grid(column=1, row=0)
        leftText=["Reference No:", "Dose: ", "No. of Tablets: ", "Lots: ", "Issued Date: ", "Exp Date: ", "Daily Dose: ", "Side Effects: "]
        leftType=[self.reference, self.dose, self.number_of_tablets, self.lots, self.issuedDate, self.expDate, self.dailyDose, self.sideEffect]
        for i in range(len(leftText)):
            self.form(window=self.leftframe, textData=leftText[i], rowData=i+1, dataType=leftType[i])
    # =================== Right Frame Referenced =================
        self.rightFrame=tk.LabelFrame(self.inputFrame, bd=0, background="#FFA781")
        self.rightFrame.grid(column=1, row=0, ipady=5, ipadx=5)
        rightText=["Further Information:", "Storage Advice: ", "Driving Mechines", "Medication: ", "Patient ID: ", "NHS Number: ", "Patient Name: ", "Date of Birth: ", "Patient Address: "]
        rightType=[self.furtherInformation, self.storageAdvice, self.drivingMachines, self.medication, self.patientID, self.nhsNumber, self.patientName, self.dob, self.patientAddress]
        for i in range(len(rightText)):
            self.form(window=self.rightFrame, textData=rightText[i], rowData=i, dataType=rightType[i])
    # ======================= display Frame ======================
        self.rightmainframe=tk.LabelFrame(self.root, text="Prescription: ", bd=3, relief=tk.GROOVE, background="#FFA781", foreground="white", font="Consolas 10 bold")
        self.rightmainframe.grid(column=2,row=1, sticky="W")
        self.textBox=tk.Text(self.rightmainframe, height=13, width=35)
        self.textBox.grid(column=0, row=0)
    # ======================= button Frame =======================
        self.buttonFrame=tk.LabelFrame(self.root, bd=0, background="#595775")
        self.buttonFrame.grid(column=0, row=2, columnspan=3)
        butText=["Prescription", "Prescription Data", "Delete", "Reset", "Exit"]
        butDecl=[self.prescription, self.prescriptionData, self.delete, self.reset, self.exitWin]
        for i in range(len(butText)):
            self.buttonHp(window=self.buttonFrame, textData=butText[i], com=butDecl[i], col=i)
    # =================== Footer Frame Data=======================
        footer=tk.LabelFrame(self.root, bd=0, background="#F2EAED")
        footer.grid(column=0, row=3, columnspan=3)
        listtext=["Name of Tablets", "Reference No.","Doseage", "No. of Tablets", "Lot", "Issued Date", "Exp Date", "Daily Dose", "Storage Adv.", "NHS Number", "Patient Name", "DOB", "Address"]
        for i in range(len(listtext)):
            self.label(window=footer, textData=listtext[i], col=i)
        self.textBox2=tk.Text(footer, height=5, width=112)
        self.textBox2.grid(column=0, row=1, columnspan=20, sticky="W")
# ================== Button Defining ==================
    def prescription(self):
        labelList=["Name of tablets","Reference No:", "Dose: ", "No. of Tablets: ", "Lots: ", "Issued Date: ", "Exp Date: ", "Daily Dose: ", "Side Effects: ", "Further Information:", "Storage Advice: ", "Driving Mechines"]
        getList=[self.tabletName.get(),self.reference.get(), self.dose.get(), self.number_of_tablets.get(), self.lots.get(), self.issuedDate.get(), self.expDate.get(), self.dailyDose.get(), self.sideEffect.get(), self.furtherInformation.get(), self.storageAdvice.get(), self.drivingMachines.get()]
        self.textBox.configure(font="Arial 9 bold")
        self.textBox.delete("1.0", "end-1c")
        for i in range(len(labelList)):
            self.textBox.insert(tk.INSERT, labelList[i] + '\t\t' + getList[i]+"\n")
        self.connectivity()

    def prescriptionData(self):
        if self.textBox2.get("1.0", "end-1c")=="":
            for i in self.collection.find():
                self.textBox2.insert(tk.INSERT, i["Name of tablets"]+"\t" +i["_id"]+"\t"+i["Dose"]+"\t"+i["Number of Tablets"]+ "\t" +i["Lots"] +"\t" +i["Issued Date"]+"\t"+i["Exp Date"]+"\t" +i["Daily Dose"]+"\t"+ i["Storage Advice"]+"\t   "+i["NHS Number"]+"\t"+i["Patient Name"]+"\t"+i["Date of Birth"] +"\t"+i["Patient Address"]+"\n")
        else:
            self.textBox2.delete("1.0", "end-1c")
            self.prescriptionData()
    
    def delete(self):
        self.textBox.delete("1.0", "end-1c")
        self.textBox2.delete("1.0", "end-1c")
        self.reset()

    def reset(self):
       variableList=[self.tabletName,self.reference,self.dose,self.number_of_tablets,self.lots,self.issuedDate,self.expDate,self.dailyDose,self.sideEffect,self.furtherInformation,self.storageAdvice,self.medication,self.drivingMachines,self.patientID,self.nhsNumber,self.patientName,self.dob,self.patientAddress]
       for i in variableList:
           i.set("")    
    
    def exitWin(self):
        ms = msg.askyesno("Confirm", "Are you sure")
        if ms==True: exit(0)
# =============== Database Interaction ================
    def connectivity(self):
        document={
                "_id":self.reference.get(),
                "Name of tablets":self.tabletName.get(),
                "Dose":self.dose.get(),
                "Number of Tablets": self.number_of_tablets.get(),
                "Lots":self.lots.get(),
                "Issued Date":self.issuedDate.get(),
                "Exp Date":self.expDate.get(),
                "Daily Dose":self.dailyDose.get(), 
                "Side Effects":self.sideEffect.get(), 
                "Further Information":self.furtherInformation.get(),
                "Storage Advice":self.storageAdvice.get(), 
                "Driving Mechines": self.drivingMachines.get(), 
                "Medication":self.medication.get(),
                "Patient ID":self.patientID.get(),
                "NHS Number":self.nhsNumber.get(),
                "Patient Name":self.patientName.get(),
                "Date of Birth":self.dob.get(),
                "Patient Address":self.patientAddress.get(),
                "Submit Date": datetime.datetime.today(),
        }
        try: self.collection.insert_one(document)
        except ServerSelectionTimeoutError: msg.showerror("Error", "Please turn ON your Mongo db server!!")
        except DuplicateKeyError: msg.showerror("Error", "All ready inserted")
        
        else: msg.showinfo("Information", "Data stored!!")

if __name__ == "__main__":
    win=tk.Tk()
    pharam=PharmacyLogin(win)    
    win.mainloop()