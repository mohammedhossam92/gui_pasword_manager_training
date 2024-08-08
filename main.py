from tkinter import *
from tkinter import messagebox
import random
import pyclip
import json

# ---------------------------search password --------------------------------#


def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            websites = data.keys()
            website_to_find = web_site_entry.get()
            # or we can check by
            # if website in data ==> to check if the website in the dict data
            if website_to_find in websites:
                email = data[website_to_find]["email"]
                password = data[website_to_find]["password"]
                messagebox.showinfo("data",
                                    f" your email is:  {email}\n"
                                    f"password is:  {password}")
            elif website_to_find not in websites:
                messagebox.showinfo("data",
                                    f"{website_to_find} does not exist"
                                    f"  in data base")
    except FileNotFoundError:
        messagebox.showinfo("Error", "no data found")

# ---------------------------- PASSWORD GENERATOR -------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = random.choices(letters, k=int(
        nr_letters))
    # random.choices(list_name,
    # k <== is the size of the returned list)
    # or
    # random_letters = [random.choice(letters) for _ in range (nr_letters)]
    # print(random_letters)
    random_numbers = random.choices(numbers, k=int(
        nr_symbols))  # random.choices(list_name, k <== is the size of the
    # returned list)

    random_symbols = random.choices(symbols, k=int(
        nr_numbers))  # random.choices(list_name,
    # k <== is the size of the returned list)

    final_password = random_letters + random_numbers + random_symbols
    password = "".join(final_password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # print(password)
    # copying password wo clipboard
    # password_entry.clipboard_clear()
    # password_entry.clipboard_append(password)

    # -----------------------------------------
    # another way using pyclip
    pyclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if (len(website) == 0 or len(email) == 0 or len(password) == 0
            or website == ' ' or email == ' ' or password == ' '):
        messagebox.showerror("Error", "Please don't "
                                      "leave any field empty")
    else:
        is_ok = messagebox.askyesno(title=website,
                                    message=f"these are details "
                                            f"entered \n Email: "
                                            f"{email} \n "
                                            f"Password: "
                                            f"{password}\nIs it "
                                            f"ok to save ?")
        if is_ok:
            # with open("passwords.txt", "a") as f:
            #     f.write(f"{website} | {email} | {password}\n")

            # loading data from json file
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                # updating data for the json file
                data.update(new_data)

                # write data to a json file
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_site_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------------ #


# create screen with title and icon
screen = Tk()
screen.title("password manager")
screen.iconbitmap('lock.ico')
screen.config(padx=20, pady=20, background="black")

# row 0
# create logo image
canvas = Canvas(width=200, height=200, background="black",
                highlightthickness=0)
logo_image = PhotoImage(file='lock200.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


# Sticky Parameter:
# Added sticky='E' for labels to align them to the east (right)
# and sticky='W' for entries to align them to the west (left).
# This ensures that labels and entries start from the same position.

# row 1
web_site_label = Label(text="Website:", bg="black",
                       fg="white")
web_site_label.grid(column=0, row=1, sticky='E')

web_site_entry = Entry(width=35)
web_site_entry.focus()
web_site_entry.grid(column=1, row=1, columnspan=2, sticky='W')

web_site_search = Button(text="Search", bg="#0092cc", width=13, padx=5,
                         command=find_password)
web_site_search.grid(column=2, row=1, columnspan=2, sticky='E')

# # row 2
email_label = Label(text="Email/UserName:", bg="black", fg="white")
email_label.grid(column=0, row=2, sticky='E')

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2,  sticky='W')
# email_entry.insert(0, "mohammedhossam5000@gmail.com")


# row 3
password_label = Label(text="Password:", bg="black", fg="white")
password_label.grid(column=0, row=3, sticky='E')

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3,  sticky='W')

generate_password_button = Button(text="Generate Password",
                                  bg="#0092cc", fg="black",
                                  command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='W', padx=(5, 0),
                              )


# row 4
add_password_button = Button(text="Add", bg="#779933", fg="white",
                             width=36, relief="raised", command=save_data)

add_password_button.grid(column=1, row=4, columnspan=2, sticky='W')


screen.mainloop()
