#===================================================================
#    Purpose:   Demonstrate usage of a GUI
#===================================================================

from tkinter import* 

form=Tk()  
form.title("Change Counter") 
form.geometry("315x350")

# Button event
def buttonPress():

    # Quarters calculation
    quartersResult = round((int(quartersText.get()) * 25) / 100, 2)
    quartersValueText.delete(0, 'end')
    quartersValueText.insert(0, str(quartersResult))

    # Dimes calculation
    dimesResult = round((int(dimesText.get()) * 10) / 100, 2)
    dimesValueText.delete(0, 'end')
    dimesValueText.insert(0, str(dimesResult))

    # Nickels calculation
    nickelsResult = round((int(nickelsText.get()) * 5) / 100, 2)
    nickelsValueText.delete(0, 'end')
    nickelsValueText.insert(0, str(nickelsResult))

    # Pennies calculation
    penniesResult = round((int(penniesText.get()) * 1) / 100, 2)
    penniesValueText.delete(0, 'end')
    penniesValueText.insert(0, str(penniesResult))

    # Halfs calculation
    halfDollarsResult = round((int(halfDollarsText.get()) * 50) / 100, 2)
    halfDollarsValueText.delete(0, 'end')
    halfDollarsValueText.insert(0, str(halfDollarsResult))

    # Dollars calculation
    dollarsResult = round((int(dollarsText.get()) * 100) / 100, 2)
    dollarsValueText.delete(0, 'end')
    dollarsValueText.insert(0, str(dollarsResult))

    # Result calculation
    resultValueText.delete(0, 'end')
    result = round(quartersResult + dimesResult + nickelsResult + penniesResult + halfDollarsResult + dollarsResult, 2)
    resultValueText.insert(0, str(result))

# Variables
quarters = StringVar()
quartersValue = StringVar()

# Quarters
quartersLabel = Label(form, text="Quarters: ")
quartersLabel.place(x=10, y=10)
quartersText = Entry(form, textvariable=quarters, width=4, bd =5)
quartersText.place(x=75, y=10)

quartersValueLabel = Label(form, text="Quarters Value: ")
quartersValueLabel.place(x=115, y=10)
quartersValueText = Entry(form, textvariable=quartersValue, width=4, bd =5)
quartersValueText.place(x=210, y=10)

# Dimes
dimesLabel = Label(form, text="Dimes: ")
dimesLabel.place(x=10, y=50)
dimesText = Entry(form, width=4, bd =5)
dimesText.place(x=75, y=50)

dimesValueLabel = Label(form, text="Dimes Value: ")
dimesValueLabel.place(x=115, y=50)
dimesValueText = Entry(form, width=4, bd =5)
dimesValueText.place(x=210, y=50)

# Nickels
nickelsLabel = Label(form, text="Nickels: ")
nickelsLabel.place(x=10, y=90)
nickelsText = Entry(form, width=4, bd =5)
nickelsText.place(x=75, y=90)

nickelsValueLabel = Label(form, text="Nickels Value: ")
nickelsValueLabel.place(x=115, y=90)
nickelsValueText = Entry(form, width=4, bd =5)
nickelsValueText.place(x=210, y=90)

# Pennies
penniesLabel = Label(form, text="Pennies: ")
penniesLabel.place(x=10, y=130)
penniesText = Entry(form, width=4, bd =5)
penniesText.place(x=75, y=130)

penniesValueLabel = Label(form, text="Pennies Value: ")
penniesValueLabel.place(x=115, y=130)
penniesValueText = Entry(form, width=4, bd =5)
penniesValueText.place(x=210, y=130)

# Half Dollars
halfDollarsLabel = Label(form, text="Half Dol: ")
halfDollarsLabel.place(x=10, y=170)
halfDollarsText = Entry(form, width=4, bd =5)
halfDollarsText.place(x=75, y=170)

halfDollarsValueLabel = Label(form, text="Half Dol Value: ")
halfDollarsValueLabel.place(x=115, y=170)
halfDollarsValueText = Entry(form, width=4, bd =5)
halfDollarsValueText.place(x=210, y=170)

# Dollars
dollarsLabel = Label(form, text="Dollars: ")
dollarsLabel.place(x=10, y=210)
dollarsText = Entry(form, width=4, bd =5)
dollarsText.place(x=75, y=210)

dollarsValueLabel = Label(form, text="Dollars Value: ")
dollarsValueLabel.place(x=115, y=210)
dollarsValueText = Entry(form, width=4, bd =5)
dollarsValueText.place(x=210, y=210)

# Instructions label
instructionsLabel = Label(form, text="Enter the number of each coin type and hit, compute: ")
instructionsLabel.place(x=10, y=250)

# Results
resultValueLabel = Label(form, text="Total Value: ")
resultValueLabel.place(x=115, y=290)
resultValueText = Entry(form, width=4, bd =5)
resultValueText.place(x=210, y=290)

# Button
button = Button(form, text ="Compute", command = buttonPress)
button.place(x=30, y=290)

form.mainloop()