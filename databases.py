from tkinter import *
import customtkinter
import ttkbootstrap as tp
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
import sqlite3
root = Tk()
root.title("My Records")
#  connect the database or create
conn = sqlite3.connect('my_database.db')
# Create a cursor
c = conn.cursor()

# table creation

"""
c.execute(""
    CREATE TABLE address(
    first_name text,
    second_name text,
    age integer,
    city text,
    country text
    )
"")
"""


def fill():
    record_id = dlt_user.get()
    conn = sqlite3.connect("my_database.db")
    show = conn.cursor()

    show.execute("""UPDATE address SET 
    first_name = :first,
    second_name = :last,
    age = :age,
    city = :city,
    country = :country 
    WHERE oid = :oid""", {
        'first': f_name_editor.get(),
        'last': s_name_editor.get(),
        'age': age_editor.get(),
        'city': city_editor.get(),
        'country': country_editor.get(),
        'oid': record_id
    })
    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect("my_database.db")

    c = conn.cursor()

    c.execute("INSERT INTO address values(:f_name, :s_name, :age, :city, :country)",
              {
                  'f_name': f_name.get(),
                  's_name': s_name.get(),
                  'age': age.get(),
                  'city': city.get(),
                  'country': country.get()
              })
    conn.commit()

    conn.close()
    # clearing the text boxes
    f_name.delete(0, END)
    s_name.delete(0, END)
    age.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)


def display():
    users = Tk()
    users.title("Records")
    users.geometry("400x400")

    conn = sqlite3.connect('my_database.db')
    show = conn.cursor()

    show.execute("SELECT *, oid FROM address")
    data = show.fetchall()
    get_info = ''
    for record in data:
        get_info += str(record[5]) + '\t' + str(record[0]).title() + ' ' + str(record[1]).title() + ' of ' + str(
            record[3]).title() + ', ' + str(record[4]).title() + "\n"

    # a Query label
    head = Label(users, text='AVAILABLE USERS')
    head.grid(row=0, column=3, columnspan=2, ipadx=140)
    rcd = Label(users, text=get_info)
    rcd.grid(row=1, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close db
    conn.close()

    users.mainloop()


def clear():
    conn = sqlite3.connect("my_database.db")

    cls = conn.cursor()
    cls.execute("DELETE FROM address")

    # commit changes
    conn.commit()

    # close db
    conn.close()


def delete():
    conn = sqlite3.connect("my_database.db")

    dlt = conn.cursor()

    dlt.execute("DELETE from address WHERE oid = " + dlt_user.get())

    # commit changes
    conn.commit()

    # close db
    conn.close()

    dlt_user.delete(0, END)


# Updating the database records
def update():
    edt = Tk()
    edt.title("Update Data")
    # icon = PhotoImage("download.ico")
    # edt.icon-photo(False, icon)

    record_id = dlt_user.get()
    conn = sqlite3.connect("my_database.db")
    show =  conn.cursor()
    show.execute("SELECT * FROM address WHERE oid = " + record_id)
    data = show.fetchall()

    # setting values to be global
    global f_name_editor
    global s_name_editor
    global city_editor
    global country_editor
    global age_editor

    # text areas
    f_name_editor = Entry(edt, width=30)
    s_name_editor = Entry(edt, width=30)
    age_editor = Entry(edt, width=30)
    city_editor = Entry(edt, width=30)
    country_editor = Entry(edt, width=30)

    f_name_editor.grid(row=0, column=1, padx=20)
    s_name_editor.grid(row=1, column=1, padx=20)
    age_editor.grid(row=2, column=1, padx=20)
    city_editor.grid(row=3, column=1, padx=20)
    country_editor.grid(row=4, column=1, padx=20)

    # labels
    f_name_label_ed = Label(edt, text="First Name")
    s_name_label_ed = Label(edt, text="Second Name")
    age_label_ed = Label(edt, text="Age")
    city_label_ed = Label(edt, text="City Name")
    country_label_ed = Label(edt, text="Country Name")

    f_name_label_ed.grid(row=0, column=0)
    s_name_label_ed.grid(row=1, column=0)
    age_label_ed.grid(row=2, column=0)
    city_label_ed.grid(row=3, column=0)
    country_label_ed.grid(row=4, column=0)

    sbt_ed = Button(edt, text="Add to Database", command=fill)
    sbt_ed.grid(row=5, column=0, columnspan=4, padx=10, pady=10, ipadx=150)

    updt = conn.cursor()
    # commit changes
    conn.commit()
    # close db
    conn.close()

    dlt_user.delete(0, END)

    for users in data:
        f_name_editor.insert(0, users[0])
        s_name_editor.insert(0, users[1])
        age_editor.insert(0, users[2])
        city_editor.insert(0, users[3])
        country_editor.insert(0, users[4])


# text areas
f_name = Entry(root, width=30)
s_name = Entry(root, width=30)
age = Entry(root, width=30)
city = Entry(root, width=30)
country = Entry(root, width=30)
dlt_user = Entry(root, width=30)

f_name.grid(row=0, column=1, padx=20)
s_name.grid(row=1, column=1, padx=20)
age.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
country.grid(row=4, column=1, padx=20)
dlt_user.grid(row=7, column=1, padx=20)

# labels
f_name_label = Label(root, text="First Name")
s_name_label = Label(root, text="Second Name")
age_label = Label(root, text="Age")
city_label = Label(root, text="City Name")
country_label = Label(root, text="Country Name")
user_dlt = Label(root, text='Enter Name')

f_name_label.grid(row=0, column=0)
s_name_label.grid(row=1, column=0)
age_label.grid(row=2, column=0)
city_label.grid(row=3, column=0)
country_label.grid(row=4, column=0)
user_dlt.grid(row=7, column=0)

# submit buttons
sbt = Button(root, text="Add to Database", command=submit)
sbt.grid(row=5, column=0, columnspan=4, padx=10, pady=10, ipadx=150)

# show records
display = Button(root, text="Show Records", command=display)
display.grid(row=6, column=0, columnspan=4, padx=10, pady=10, ipadx=155)

# delete all
dlt = Button(root, text="Clear Records", command=clear)
dlt.grid(row=9, column=0, columnspan=4, padx=10, pady=10, ipadx=155)

# delete record
dlt_s_user = Button(root, text='Delete user', command=delete)
dlt_s_user.grid(row=8, column=0, columnspan=4, padx=10, pady=10, ipadx=160)

# edit the records
update = Button(root, text='Edit', command=update)
update.grid(row=10, column=0, columnspan=4, padx=10, pady=10, ipadx=185)

# commit your changes in the database
conn.commit()
# closing the connectio
conn.close()

root.mainloop()
