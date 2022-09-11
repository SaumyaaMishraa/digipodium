from tkinter import*

from sqlalchemy import FetchedValue
field = ('number of payment','loan principle','monthly payment')
root =Tk()
entries={}
for field in field:
    row= Frame(root)
lab= Label (row, width=90,text=field+':', anchor='w')
ent = Entry (row)
ent.insert (0,"0")
row.pack(side=TOP,fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
ent.pack(side= RIGHT ,expand =YES ,fill=X)
entries[field]= ent
root.bind('<Return>', (lambda event , e = entries: FetchedValue(e)))

b1=Button(root, text = 'Submit' ,command = None)
b1.pack(side=LEFT,padx=25, pady=25)
b2=Button(root, text = 'cancel' ,command = None)
b2.pack(side=LEFT,padx=20, pady=20)
root.mainloop()