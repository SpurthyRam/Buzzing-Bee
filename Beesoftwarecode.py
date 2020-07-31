import tkinter as tk
from tkinter import *
from tkinter import messagebox
import xlrd
from xlrd import open_workbook
import time
#import xlwt
#from xlwt import open_workbook
import datetime
from datetime import date
from xlutils.copy import copy
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter.ttk import *
import math
     
h1=700
w1=1200
top = tk.Tk()


def test_function(var):
    print("starting....")
    mes=""
    count=0
    high=0
    loc="query (4).csv"

    wb=xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)

    rowval=xlrd.open_workbook("ibm db.xls")
    shrow=rowval.sheet_by_index(0)

    rb = open_workbook("ibm db.xls")
    wb = copy(rb)
    sheet1 = wb.get_sheet(0)
    
    for y in range(1,sheet.nrows) :
        val=str(sheet.cell_value(y,0))
        val1=str(sheet.cell_value(y,1))
        val2=float(sheet.cell_value(y,2))
        val3=float(sheet.cell_value(y,3))
        place=str(sheet.cell_value(y,13))
        dval=val[:10]
        dyr=int(val[:4])
        dmo=int(val[5:7])
        dda=int(val[8:10])
        tval=val[11:19]
        sheet1.write(y,0,dval)
        sheet1.write(y,1,str(tval))
        sheet1.write(y,2,float(val1))
        sheet1.write(y,3,float(val2))
        sheet1.write(y,4,float(val3))
        sheet1.write(y,5,place)
        todaydate=date.today()
        td=str(todaydate)
        toyr=int(td[:4])
        tomm=int(td[5:7])
        toda=int(td[8:])
        sheet1.write(y,6,todaydate)
        sheet1.write(y,7,int(dyr))
        sheet1.write(y,8,int(dmo))
        sheet1.write(y,9,int(dda))
        sheet1.write(y,10,int("00"))
        sheet1.write(y,11,int(td[:4]))
        sheet1.write(y,12,int(td[5:7]))
        sheet1.write(y,13,int(td[8:]))
        sheet1.write(y,14,int(tval[:2]))
        sheet1.write(y,15,int(tval[3:5]))
        datediff=int(((toyr-dyr)*365)+((tomm-dmo)*30)+(toda-dda))          
        sheet1.write(y,16,datediff)
        secdiff=(int(tval[:2])*60*60)+(int(tval[3:5])*60)
        sheet1.write(y,17,secdiff)
        sectotal=secdiff+(datediff*86400)
        sheet1.write(y,17,secdiff+(datediff*86400))
        coplat=float("17.4408")
        coplong=float("77.0415")
        sheet1.write(y,18,float("17.4408"))
        sheet1.write(y,19,float("77.0415"))
        latdiff=abs(float(val2)-coplat)
        longdiff=abs(float(val3)-coplong)
        distance=math.sqrt((latdiff*latdiff)+(longdiff*longdiff))
        sheet1.write(y,20,distance)
        if(val2-coplat>=0&&val3-coplong>=0):
            if((1/math.tan(longdiff/latdiff)<=45)):
                angle=45-(1/math.tan(longdiff/latdiff))
             else :
                 angle=(1/math.tan(longdiff/latdiff))-45
        elif(val2-coplat<0):
            angle=(1/math.tan(latdiff/longdiff))+45
        elif(val3-coplong<0):
            angle=(1/math.tan(longdiff/latdiff))+45
        else:
            angle=1/math.cos(1)
        sheet1.write(y,21,angle)
        mag=float(sheet.cell_value(y,4))
        sheet1.write(y,22,mag)
        edev=(10**(5.24+(1.44*mag)))
        sheet1.write(y,23,edev)
        Ec=3570000000*9.8*200
        sheet1.write(y,24,Ec)
        ecal=((Ec*sectotal*val3*(math.cos(angle)))/(distance*3150000000))
        if(ecal<0):
            ecal=ecal*(-1)
        sheet1.write(y,25,ecal)
        diffe=ecal-edev
        if(diffe<0):
            diffe=diffe*(-1)
        sheet1.write(y,26,diffe)
        ratio=diffe/ecal
        sheet1.write(y,27,ratio)
        if((ratio>0.8)&&(ratio<1)):
            fratio=1
        else:
            fratio=0
        sheet1.write(y,28,fratio)
        tleft=((distance*edev*3150000000)/(Ec*val3*(math.cos(angle))))
        if(tleft<0):
            tleft=tleft*(-1)
        sheet1.write(y,29,tleft)
        tescape=secdiff-tleft
        tremain=tescape%tleft
        sheet1.write(y,30,tremain)
        trehour=tremain/(60*60)
        sheet1.write(y,31,trehour)
        
        
        
        
        
        
    wb.save('ibm db.xls')
    
    messagebox.showinfo("ibm project", shrow.nrows)
    print("done\n\n")
    #dis['text']=str(shrow.nrows)+"\trolls\t"+str(shrow.ncols)
    
 
def newwin():
    win= tk.Tk()
    win.title("ibm projects")
    win.geometry('2000x5000')
    
    top.title("ibm porject")
    ca=tk.Canvas(top,height=h1,width=w1)
    ca.pack()
    fr=tk.Frame(win,bg='#04433A')
    fr.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.9)
    hello=tk.Label(fr,text="BEE CODE",bg="#04433A",fg="white",font=("Arial",20))
    hello.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.2)
    label=tk.Label(fr,text="PREDICTION OF EARTHQUAKE",bg="black",fg="white")
    label.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.05)
    label=tk.Label(fr,text="ENTER LOCATION NAME",bg="#f0f0f0",fg="black")
    label.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.07)
    entry=tk.Entry(fr,bg="white")
    entry.place(relx=0.35,rely=0.1,relwidth=0.45,relheight=0.07)
    B = tk.Button(fr, text ="SEARCH",width=10,activebackground="#04433A",activeforeground="red",bg='#f0f0f0',fg="black",command=lambda:search_func(entry.get()))
    B.place(relx=0.5,rely=0.2,relwidth=0.15,relheight=0.05)
    dis= tk.Message(fr,bg="#22DFAE",fg="black")
    dis.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.60)
    B2 = tk.Button(fr, text ="STOP AND QUIT",width=10,activebackground="#04433A",activeforeground="red",bg='black',fg="white",command=lambda:end(win))
    B2.place(relx=0.75,rely=0.92,relwidth=0.15,relheight=0.07)
    win.mainloop()
	
def end(val):
    val.destroy()
def search_func(var):
    print("starting....")
    messagebox.showinfo("ibm project", "loading\n please wait")
    mes=""
    count=0
    high=0
    loc="ibm db.xls"
    wb=xlrd.open_workbook(loc)
    sheet2=wb.sheet_by_index(0)
    for y in range(1,sheet2.nrows) :
        
            if(sheet2.cell_value(y,38)==1):
                if(var in sheet2.cell_value(y,11)):
                    if(sheet2.cell_value(y,45)<50):
                        count+=1
                        if(sheet2.cell_value(y,45)>high):
                            high=sheet2.cell_value(y,45)
                        if(count<=5):
                            mes=mes+str(count)                    
                            mes=mes+") time left : "+str(int(sheet2.cell_value(y,45)))+" hours"
                            mes=mes+"\n   magnitude : "+str(sheet2.cell_value(y,9))
                            mes=mes+"\n\n"
                   
        
    messagebox.showinfo("ibm project", "ur result is here")
    print("done\n\n")
    mes=mes+"\ntotal:"+str(count)
    dis['text']="hello"
		
top.title("ibm porject")
ca=tk.Canvas(top,height=h1,width=w1)
ca.pack()

fr=tk.Frame(top,bg='#ABA907')
fr.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.9)
photoupdate =ImageTk.PhotoImage(Image.open( "C:\\Users\\family\\Desktop\\desktop files\\kishore\\project\\ibm\\image\\download.png"))
photobecode =ImageTk.PhotoImage(Image.open( "C:\\Users\\family\\Desktop\\desktop files\\kishore\\project\\ibm\\image\\beecodeimage.png"))
photoquit =ImageTk.PhotoImage(Image.open( "C:\\Users\\family\\Desktop\\desktop files\\kishore\\project\\ibm\\image\\quitimage.png"))

#ca.create_image(0,0,anchor="nw",image=photo1)
#ca.place()


hello=tk.Label(fr,text="BEE CODE",image=photobecode,compound="left",bg="#ABA907",fg="white",font=("Arial",32))

hello.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.2)

label=tk.Label(fr,text="PREDICTION OF EARTHQUAKE",bg="black",fg="white",font=("Arial",20))
label.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.05)

label=tk.Label(fr,text="ENTER FILE NAME",borderwidth=5,bg="#f0f0f0",fg="black",font=("Arial",16))
label.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.07)

entry=tk.Entry(fr,bg="white",borderwidth=5)
entry.place(relx=0.35,rely=0.4,relwidth=0.45,relheight=0.07)

B2 = tk.Button(fr, text ="CLICK HERE TO SEARCH \nSOME RESULTS",borderwidth=5,width=10,activebackground="#04433A",activeforeground="red",bg='#f0f0f0',fg="black",command=lambda:newwin())
B2.place(relx=0.1,rely=0.1,relwidth=0.15,relheight=0.07)


B = tk.Button(fr,text="UPDATE",image=photoupdate,width=10,compound="left",font=("Arial",16),activebackground="#04433A",activeforeground="red",bg='#f0f0f0',fg="black",command=lambda:test_function(entry.get()))
B.place(relx=0.5,rely=0.5,relwidth=0.15,relheight=0.05)
B2 = tk.Button(fr,image=photoquit,compound="left",width=10,activebackground="black",borderwidth=5,activeforeground="red",bg='black',fg="white",command=lambda:end(top))
B2.place(relx=0.7,rely=0.7,relwidth=0.15,relheight=0.1)              
    
top.mainloop()




