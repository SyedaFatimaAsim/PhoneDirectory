def add():
    b=enN.get()
    c=enT.get()
    d=enC.get()
    f=open('db.txt','a')
    f.write(b+' ')
    f.write(str(c)+' ')
    f.write(d+'|')
    f.close()



def search_contacts():  
    e=enNN.get()
    addressbook=open("db.txt")
    for line in addressbook:
        records=line.split('|')
        for record in records:
                if e in record:
                    contacts.insert(END,record)
                    break
                else:
                    print("Name not found,unlucky!!")
                    continue
                 
def contact():  
    e=enNN.get()
    addressbook=open("db.txt")
    for line in addressbook:
        records=line.split('|')
        for record in records:
                    contacts.insert(END,record)
                                     
#ADD CONTACTS  
from tkinter import*

def add_contacts():
 ae=Tk()
 ae.title('ADD CONTACTS')
 ae.configure(background="#000000")
 ae.geometry('300x500')
 global fr1
 fr1=Frame(ae,background="#000000",padx=15, pady=15)
 fr1.pack()

 labN=Label(fr1,text="Name",background="#1DE4F1",font='Times 20 bold')
 labN.grid(row=0,column=0)
 global enN
 enN=Entry(fr1,background="#1DE4F1")
 enN.grid(row=0,column=1)

 labT=Label(fr1,text="telephone",background="#1DE4F1",font='Times 20 bold')
 labT.grid(row=1,column=0,padx=10, pady=10)


 global enT
 enT=Entry(fr1,background="#1DE4F1")
 enT.grid(row=1,column=1)

 labA=Label(fr1,text='address',background="#1DE4F1",font='Times 20 bold')
 labA.grid(row=2,column=0)
 global enC
 enC=Entry(fr1,background="#1DE4F1")
 enC.grid(row=2,column=1)
 
 fr2=Frame(ae,background="#1DE4F1")
 fr2.pack()
 
 addB=Button(fr2,text='add',background="#1DE4F1",command=add,font='Times 20 bold')
 addB.grid(row=0,column=0)

#SEARCH CONTACTS
#from tkinter import*

def searchhh_contacts():
 search=Tk()
 search.title('SEARCH CONTACTS')
 search.configure(background="#000000")
 search.geometry('300x500')
 global fr3
 fr3=Frame(search)
 fr3.pack()

 labNN=Label(fr3,text='Name')
 labNN.grid(row=1,column=1)
 global enNN 
 enNN=Entry(fr3)
 enNN.grid(row=1,column=2)


 fr4=Frame(search)
 fr4.pack()

 searchF=Button(fr4,text='search',command=search_contacts)
 searchF.grid(row=0,column=2)

 fr5=Frame(search)
 fr5.pack()
 global contacts
 contacts=Listbox(fr5,height=30,width=60)
 contacts.pack()

#DELETE CONTACTS
#from tkinter import*
def delete_contacts():
 delete=Tk()
 delete.title('DELETE CONTACTS')
 delete.configure(background="#000000")
 delete.geometry('300x500')

 fr6=Frame(delete) 
 fr6.pack()

 labNNN=Label(fr6,text='Name')
 labNNN.grid(row=2,column=1)

 enNNN=Entry(fr6)
 enNNN.grid(row=5,column=2)


 fr7=Frame(delete)
 fr7.pack()

 deleteF=Button(fr7,text='delete')
 deleteF.grid(row=5,column=2)

 fr8=Frame(delete)
 fr8.pack()

 deletes=Listbox(fr8,height=30,width=60)
 deletes.pack()

#phonebook
#from tkinter import*
main=Tk()
main.title('PHONE BOOK')
main.configure(background="#34495E")
main.geometry('300x500')

fr9=Frame(main,background="#34495E",padx=15, pady=15)
fr9.pack()

adddB=Button(fr9,text="ADD CONTACTS",command=add_contacts,background='#BFC9CA')
adddB.grid(row=0,column=0,padx=25, pady=25)

ddelB=Button(fr9,text="DELETE CONTACTS",command=delete_contacts,background='#BFC9CA')
ddelB.grid(row=1,column=0,padx=25, pady=25)

ssearchB=Button(fr9,text="SEARCH CONTACT",command=searchhh_contacts,background='#BFC9CA')
ssearchB.grid(row=2,column=0,padx=25, pady=25)

