from tkinter import *
import random
root = Tk()
root.geometry("520x200")
root.title("Alphabet generator")
alphabet = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu']




def generate_name():
    alp = random.choice(alphabet)
    num = str(random.randint(1, 15))
    name = alp + "-" + num
    lblname.configure(text = name)





frame1 = LabelFrame(root, )
lbl1 = Label(frame1, text="GENERATE NATO ALPHABET NAME:", font=("Arial Black", 18))
lblname = Label(frame1, text="", font=("Helvetica", 18))
btn1 = Button(root, text="generate", command = generate_name)



frame1.pack()
lbl1.pack(pady = 10, padx = 10)
lblname.pack(pady = 10, padx = 10)
btn1.pack(pady = 10, padx = 10)



root.mainloop()