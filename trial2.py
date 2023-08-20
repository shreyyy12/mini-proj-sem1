from tkinter import *
from forex_python.converter import *
from math import *
#Creating the mainscreen window
window=Tk()
window.title("main window")
lbl=Label(window, text = "STANDARD UNIT CONVERTER",font = ("arial black", 24),bg='#ffffff')#printing the title

lbl.place(x=355, y=20)#placement
window.geometry("1300x1275")#size
window['background']='#ffffff'#background color

#converting length
def length_converter():
    global lengthwindow
    lengthwindow=Toplevel(window)
    lengthwindow.title("Length window")
    lengthwindow.geometry("720x500")#size
    lengthwindow['background']="#ffc1b6"#background color
    length_selection=["Select Unit","meter - m","decimeter - dm","centimeter - cm", "millimeter - mm",
                  "micrometer - μm","nanometer - nm","picometer - pm","kilometer - km","inch - in","foot - ft","yard - yd","mile - mi","nautical mile - nmi"]
    length_units={"meter - m":1, "centimeter - cm":100,"decimeter - dm": 10, "micrometer - μm": pow(10,6), 
                  "foot - ft":3.28084, "millimeter - mm": 1000, "kilometer - km": pow(10,-3),"nanometer - nm": pow(10,9),
                  "picometer - pm":pow(10,12),"inch - in":39.37008,"yard - yd":1.09361296,
                  "mile - mi": 0.000621371,'nautical mile - nmi':0.00053995682073434}

    title_label=Label(lengthwindow,text="LENGTH UNIT CONVERTER",bg = "#ffc1b6",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=120,y=20)
    text_label=Label(lengthwindow,text="Length is defined as the measurement of how long something is in size or the distance from one end to other.It's SI unit is meter.",
                     bg = "#ffc1b6",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=10,y=90)

    def close_win():
        lengthwindow.destroy()

    def reset():
        calc_length.delete(0,END)
        enter_length.delete(0,END)
        input_unit.set(length_selection[0])
        output_unit.set(length_selection[0])

    def length_convert():
        try:
            if input_unit.get() in length_units and output_unit.get() in length_units:
                calc_length.delete(0, END)  
                calc_length.insert(0, round(float(enter_length.get()) * float(length_units[output_unit.get()] / length_units[input_unit.get()]), 5))
        except:
            calc_length.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(length_selection[0])  
    output_unit.set(length_selection[0])

    #labels for text display
    input_label = Label(lengthwindow,text = "From:",bg="#ffc1b6",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(lengthwindow,text = "To:",bg = "#ffc1b6",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_length = Entry(lengthwindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_length = Entry(lengthwindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_length.place(x=250,y=150)  
    calc_length.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(lengthwindow,input_unit,*length_selection)  
    output_menu = OptionMenu(lengthwindow,output_unit,*length_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for length conversion
    convert_button = Button(lengthwindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = length_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(lengthwindow,text = "RESET",bg = "#9a9a9a",fg = "#ffffff",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(lengthwindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)

#converting data
def data_converter():
    global datawindow
    datawindow=Toplevel(window)
    datawindow.title("Data window")
    datawindow.geometry("720x500")#size
    datawindow['background']='#f1dadf'#background color
    data_selection=["Select Unit ","Bit ","Kilobit ","Kibibit ","Megabit ","Mebibit ","Gigabit ","Gibibit ",
                        "Terabit ","Tebibit ","Petabit ","Pebibit ","Nibble ","Byte ","Kilobyte ","Kibibyte ",
                        "Megabyte ","Mebibyte ", "Gigabyte ","Gibibyte ","Terabyte ", "Tebibyte ","Petabyte ","Pebibyte "]
                       
    data_units={"Bit ":8,"Kilobit ":(8*(pow(10,-3))),"Kibibit ":0.0078125,"Megabit ":(8*(pow(10,-6))),"Mebibit ":(7.6294*(pow(10,-6))),"Gigabit ":(8*(pow(10,-9))),
                    "Gibibit ":(7.4506*(pow(10,-9))),"Terabit ":(8*(pow(10,-12))),"Tebibit ":(7.276*(pow(10,-6))),"Petabit ":(8*(pow(10,-15))),"Pebibit ":(7.1054*(pow(10,-15))),
                    "Nibble ":2,"Byte B":1,"Kilobyte ":pow(10,-3),"Kibibyte ":(9.76563*(pow(10,-4))),"Megabyte ":pow(10,-6),"Mebibyte ":(9.5367*(pow(10,-7))), 
                    "Gigabyte ":pow(10,-9),"Gibibyte ":(9.3132*(pow(10,-10))),"Terabyte ":pow(10,-12),"Tebibyte ":(9.0949*(pow(10,-13))),"Petabyte ":pow(10,-15),
                    "Pebibyte ":(8.8818*(pow(10,-16)))}

    title_label=Label(datawindow,text="DIGITAL DATA STORAGE UNIT CONVERTER",bg = "#f1dadf",fg = "#000000",font=("Imprint Mt shadow",20,"bold"))
    title_label.place(x=27,y=20)
    text_label=Label(datawindow,text="Digital data storage units is defined as the terms that describe different amounts of binary information stored on digital devices.",
                     bg = "#f1dadf",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=10,y=90)
    def close_win():
        datawindow.destroy()

    def reset():
        calc_data.delete(0,END)
        enter_data.delete(0,END)
        input_unit.set(data_selection[0])
        output_unit.set(data_selection[0])

    def data_convert():
        try:
            if input_unit.get() in data_units and output_unit.get() in data_units:
                calc_data.delete(0, END)  
                calc_data.insert(0, round(float(enter_data.get()) * float(data_units[output_unit.get()] / data_units[input_unit.get()]), 5))
        except:
            calc_data.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(data_selection[0])  
    output_unit.set(data_selection[0])

    #labels for text display
    input_label = Label(datawindow,text = "From:",bg = "#f1dadf",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(datawindow,text = "To:",bg = "#f1dadf",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_data = Entry(datawindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_data = Entry(datawindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_data.place(x=250,y=150)  
    calc_data.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(datawindow,input_unit,*data_selection)  
    output_menu = OptionMenu(datawindow,output_unit,*data_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for mass conversion
    convert_button = Button(datawindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = data_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(datawindow,text = "RESET",bg = "#9a9a9a",fg = "#ffffff",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(datawindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)

#converting volume
def vol_converter():
    global volwindow
    volwindow=Toplevel(window)
    volwindow.title("volume window")
    volwindow.geometry("720x500")#size
    volwindow['background']='#bde7ea'#background color
    vol_selection=["Select Unit"," cubic meter"," cubic centimeter"," cubic decimeter", "cubic micrometer",
              "cubic foot", " cubic millimeter","cubic kilometer"," cubic nanometer",\
              " cubic picometer"," cubic inch"," cubic yard",\
              "cubic mile"," litre"," milli liter"]
    volume_units={" cubic meter":1, " cubic centimeter":1000000,\
              " cubic decimeter": 1000, "cubic micrometer": (pow(10,18)), \
              "cubic foot":35.3147248, " cubic millimeter": 1000000000, \
              "cubic kilometer": (pow(10,-9))," cubic nanometer": (pow(10,27)),\
              " cubic picometer":(pow(10,36))," cubic inch":61023.7," cubic yard":1.30795,\
              "cubic mile": (2.3991*(pow(10,-10))),\
              " litre": 1000," milli liter":(pow(10,6))}

    title_label=Label(volwindow,text="VOLUME UNIT CONVERTER",bg = "#bde7ea",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=115,y=20)
    text_label=Label(volwindow,text="Volume is defined as the space occupied within the boundaries of an object in three-dimensional space.It's SI unit is cubic meter",\
                 bg = "#bde7ea",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=10,y=90)
    def close_win():
        volwindow.destroy()

    def reset():
        calc_vol.delete(0,END)
        enter_vol.delete(0,END)
        input_unit.set(vol_selection[0])
        output_unit.set(vol_selection[0])
    
    def vol_convert():
        try:
            if input_unit.get() in volume_units and output_unit.get() in volume_units:
                calc_vol.delete(0, END)  
                calc_vol.insert(0, round(float(enter_vol.get()) * float(volume_units[output_unit.get()] / volume_units[input_unit.get()]), 5))
        except:
                calc_vol.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(vol_selection[0])  
    output_unit.set(vol_selection[0])

    #labels for text display
    input_label = Label(volwindow,text = "From:",bg = "#bde7ea",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(volwindow,text = "To:",bg = "#bde7ea",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_vol = Entry(volwindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_vol = Entry(volwindow,bg = "#e8f8f5")  
  
    # using the grid() method to set the position of the above entry fields   
    enter_vol.place(x=250,y=150)  
    calc_vol.place(x=250,y=200)  
  
    # adding the option menus to the main window  
    input_menu = OptionMenu(volwindow,input_unit,*vol_selection)  
    output_menu = OptionMenu(volwindow,output_unit,*vol_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for vol conversion
    convert_button = Button(volwindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = vol_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(volwindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(volwindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)

#converting temperature
def temperature_converter():
    global tempwindow
    tempwindow=Toplevel(window)
    tempwindow.title("Temperature window")
    tempwindow.geometry("720x500")#size
    tempwindow['background']='#E8CEDB'#background color
    temp_selection=["Select Unit","celsius","fahrenheit","kelvin"]
    temperature_units=["celsius","fahrenheit","kelvin"]


    title_label=Label(tempwindow,text="TEMPERATURE UNIT CONVERTER",bg = "#E8CEDB",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=50,y=20)
    text_label=Label(tempwindow,text="Temperature is a physical quantity that expresses quantitatively the perceptions of hotness and coldness.It's SI unit is Kelvin",\
                     bg = "#E8CEDB",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=15,y=90)

    def close_win():
        tempwindow.destroy()

    def reset():
        calc_temp.delete(0,END)
        enter_temp.delete(0,END)
        input_unit.set(temp_selection[0])
        output_unit.set(temp_selection[0])
        
    def temp_convert():
        try:
            if input_unit.get() in temperature_units and output_unit.get() in temperature_units:
                if input_unit.get() == "celsius" and output_unit.get() == "fahrenheit":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float(enter_temp.get())*1.8)+32)
                elif input_unit.get()== "fahrenheit" and output_unit.get()== "celsius":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float(enter_temp.get())-32)*5/9)
                elif input_unit.get() == "fahrenheit" and output_unit.get()== "kelvin":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float(enter_temp.get())-32)*5/9+273.15)
                elif input_unit.get() == "kelvin" and output_unit.get()== "celsius":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float(enter_temp.get())-273.15))
                elif input_unit.get() == "kelvin" and output_unit.get()== "fahrenheit":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float((enter_temp.get())-273.15)*1.8+32))
                elif input_unit.get() == "celsius" and output_unit.get()== "kelvin":
                    calc_temp.delete(0,END)
                    calc_temp.insert(0,(float(enter_temp.get())+273.15))

        except:
            calc_temp.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(temp_selection[0])  
    output_unit.set(temp_selection[0])

    #labels for text display
    input_label = Label(tempwindow,text = "From:",bg = "#E8CEDB",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(tempwindow,text = "To:",bg = "#E8CEDB",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_temp = Entry(tempwindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_temp = Entry(tempwindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_temp.place(x=250,y=150)  
    calc_temp.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(tempwindow,input_unit,*temp_selection)  
    output_menu = OptionMenu(tempwindow,output_unit,*temp_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for temp conversion
    convert_button = Button(tempwindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = temp_convert)
    convert_button.place(x=230,y=250)

    # RESET button  
    reset_button = Button(tempwindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(tempwindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)


def mass_converter():
    global masswindow
    masswindow=Toplevel(window)
    masswindow.title("Mass window")
    masswindow.geometry("720x500")#size
    masswindow['background']='#ab92b3'#background color
    mass_selection=["Select Unit","kilogram - kg","gram - g","milligram - mg", "microgram - μg","tonne - t","pound - lb",
                    "quintal - q","carat - ct","dram - dr","grain - gr","ounce - oz","short ton - sh.t","long ton - l.t","stone - st"]
    mass_units={"kilogram - kg":1, "gram - g":1000,"milligram - mg": pow(10,6), "microgram - μg": pow(10,9), 
                  "tonne - t":pow(10,-3), "pound - lb": 2.20462262, "quintal - q": pow(10,-2),"carat - ct": 5000,
                  "dram - dr":564.383391,"grain - gr":15432.3584,"ounce - oz":35.2739619,
                  "short ton - sh.t": 0.00110231131,"long ton - l.t":0.000984206528,"stone - st": 0.157473044}

    title_label=Label(masswindow,text="MASS UNIT CONVERTER",bg = "#ab92b3",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=120,y=20)
    text_label=Label(masswindow,text="Mass is defined as the the amount of matter in an object.It's SI unit is kilogram.",
                     bg = "#ab92b3",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=120,y=90)
    
    def close_win():
        masswindow.destroy()

    def reset():
        calc_mass.delete(0,END)
        enter_mass.delete(0,END)
        input_unit.set(mass_selection[0])
        output_unit.set(mass_selection[0])

    def mass_convert():
        try:
            if input_unit.get() in mass_units and output_unit.get() in mass_units:
                calc_mass.delete(0, END)  
                calc_mass.insert(0, round(float(enter_mass.get()) * float(mass_units[output_unit.get()] / mass_units[input_unit.get()]), 5))
        except:
            calc_mass.insert(0, "ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(mass_selection[0])  
    output_unit.set(mass_selection[0])

    #labels for text display
    input_label = Label(masswindow,text = "From:",bg = "#ab92b3",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(masswindow,text = "To:",bg = "#ab92b3",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_mass = Entry(masswindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_mass = Entry(masswindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_mass.place(x=250,y=150)  
    calc_mass.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(masswindow,input_unit,*mass_selection)  
    output_menu = OptionMenu(masswindow,output_unit,*mass_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for mass conversion
    convert_button = Button(masswindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = mass_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(masswindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(masswindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)


def currency_converter():
    global curwindow
    curwindow=Toplevel(window)
    curwindow.title("currency window")
    curwindow.geometry("720x500")#size
    curwindow['background']='#f3d8a7'#background color

    cur_list=["Select Unit","USD","Euro","Yen","Sterling","Australian dollar",
    "Canadian dollar","Chinese renminbi","Swiss franc","Hong Kong dollar","Singapore dollar",
    "Swiss krona","South Korean won","Norwegian krone","New Zealand dollar","Indian rupee",
    "Mexican peso","South African rand","Brazilian real","Danish krone",
    "Polish zloty","Thai baht","Indonesian rupiah","Czech koruna",
    "Turkish lira","Hungarian forint","Philippine peso",
    "Malaysian ringgit","Romanian leu","British pound","Bulgaraian Lev"
   ,"Icelands Krona","Croatian Kuna"]
              
    cur_sel={"USD":"USD","Euro":"EUR","Yen":"JPY","Sterling":"GBP","Australian dollar":"AUD",
    "Canadian dollar":"CAD","Chinese renminbi":"CNY","Swiss franc":"CHF","Hong Kong dollar":"HKD",
    "Singapore dollar":"SGD","Swiss krona":"SEK","South Korean won":"KRW","Norwegian krone":"NOK",
    "New Zealand dollar":"NZD","Indian rupee":"INR","Mexican peso":"MXN",
    "South African rand":"ZAR","Brazilian real":"BRL","Danish krone":"DKK",
    "Polish zloty":"PLN","Thai baht":"THB",
    "Indonesian rupiah":"IDR","Czech koruna":"CZK","Turkish lira":"TRY",
    "Hungarian forint":"HUF","Philippine peso":"PHP",
    "Malaysian ringgit":"MYR","Romanian leu":"RON","British pound":"GBP",
    "Bulgarian Lev":"BGN",
    "Icelands Krona":"ISK","Croatian Kuna":"HRK"}

    title_label=Label(curwindow,text="CURRENCY UNIT CONVERTER",bg = "#f3d8a7",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=90,y=20)
    text_label=Label(curwindow,text="A currency is a standardization of money in any form, in use or circulation as a medium of exchange.",\
                     bg = "#f3d8a7",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=90,y=90)
    cr=CurrencyRates()
    
    def close_win():
        curwindow.destroy()
        
    def reset():
        calc_cur.delete(0,END)
        enter_cur.delete(0,END)
        input_unit.set(cur_list[0])
        output_unit.set(cur_list[0])
             
    def cur_convert():
        try:
            if input_unit.get() in cur_sel and output_unit.get() in cur_sel:
                    from1=cur_sel[input_unit.get()]
                    to1=cur_sel[output_unit.get()]
                    amt=float(enter_cur.get())
                    val=cr.convert(from1,to1,amt)
                    calc_cur.delete(0,END)
                    calc_cur.insert(0,round(val,3))
        except:
            calc_cur.insert(0,"ERROR")

    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(cur_list[0])  
    output_unit.set(cur_list[0])

    #labels for text display
    input_label = Label(curwindow,text = "From:",bg = "#f3d8a7",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(curwindow,text = "To:",bg = "#f3d8a7",fg = "#000000")
    output_label.place(x=180,y=200)

    # input field to enter data  
    enter_cur = Entry(curwindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_cur = Entry(curwindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_cur.place(x=250,y=150)  
    calc_cur.place(x=250,y=200)  
      
    # adding the option menus to the main window
    input_menu = OptionMenu(curwindow,input_unit,*cur_list)  
    output_menu = OptionMenu(curwindow,output_unit,*cur_list)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for cur conversion
    convert_button = Button(curwindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = cur_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(curwindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(curwindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)


def time_converter():
    global timewindow
    timewindow=Toplevel(window)
    timewindow.title("Time window")
    timewindow.geometry("720x500")#size
    timewindow['background']='#B8AFEF'#background color
    time_selection=["Select Unit","millisecond","microsecond","second", "hours", "days", "years","minute","week"]
    time_units={"second":1, "millisecond":1000,\
                   "microsecond": (pow(10,6)), \
                  "hours":0.0002778, "days": (1.1574074074074*(pow(10,-5))), \
                  "years": 3.1688764615413*(pow(10,-8)),"minute": 0.0166667,\
                  "week":(1.6534391534392*(pow(10,-6)))}

    title_label=Label(timewindow,text="TIME CONVERTER",bg = "#B8AFEF",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=180,y=20)
    text_label=Label(timewindow,text="The second, symbolised with 's', is the SI unit of time.The unperturbed ground-state hyperfine transition frequency",bg = "#B8AFEF",fg = "#000000",font=("Helvetica",9))
    text_label1=Label(timewindow,text='of the caesium 133 atom, to be 9192631770 when expressed in the unit Hz, which is equal to s^−1.',\
                     bg = "#B8AFEF",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=25,y=90)
    text_label1.place(x=20,y=110)

    def close_win():
        timewindow.destroy()
        
    def reset():
        calc_time.delete(0,END)
        enter_time.delete(0,END)
        input_unit.set(time_selection[0])
        output_unit.set(time_selection[0])
        
    def time_convert():
        try:
            if input_unit.get() in time_units and output_unit.get() in time_units:
                calc_time.delete(0, END)  
                calc_time.insert(0, round(float(enter_time.get()) * float(time_units[output_unit.get()] / time_units[input_unit.get()]), 5))
        except:
                calc_time.insert(0,"ERROR")
                
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(time_selection[0])  
    output_unit.set(time_selection[0])

    #labels for text display
    input_label = Label(timewindow,text = "From:",bg = "#B8AFEF",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(timewindow,text = "To:",bg = "#B8AFEF",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_time = Entry(timewindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_time = Entry(timewindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_time.place(x=250,y=150)  
    calc_time.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(timewindow,input_unit,*time_selection)  
    output_menu = OptionMenu(timewindow,output_unit,*time_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for vol conversion
    convert_button = Button(timewindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = time_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(timewindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(timewindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)



def area_converter():
    global areawindow
    areawindow=Toplevel(window)
    areawindow.title("area window")
    areawindow.geometry("720x500")#size
    areawindow['background']='#ccccc4'#background color

    area_selection=["select Unit","square picometer","square nanometer", \
            "square micrometer","square millimeter","square centimeter",
            "square meter","square decimeter",\
            "square kilometer","acre","hectare",\
            "square feet","square inch","square yard"]
    area_units={"square meter":1, "square centimeter":10000,\
                "square decimeter": 100, "square micrometer": (pow(10,12)), \
                "square feet":10.76391, "square millimeter": (pow(10,6)), \
                "square kilometer": (pow(10,-6)),"square nanometer": (pow(10,18)),\
                "square picometer":(pow(10,24)),"square inch":1550.003,"square yard":1.19599,\
                "acre": (2.471052*(pow(10,-4))),"hectare": (pow(10,-4))\
                }

    title_label=Label(areawindow,text="AREA CONVERTER",bg = "#ccccc4",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=180,y=20)
    text_label=Label(areawindow,text="Area is defined as the space occupied within the boundaries of an object in three-dimensional space. It's SI unit is square meter",\
                     bg = "#ccccc4",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=10,y=90)

    def close_win():
        areawindow.destroy()

    def reset():
        calc_area.delete(0,END)
        enter_area.delete(0,END)
        input_unit.set(area_selection[0])
        output_unit.set(area_selection[0])
    def area_convert():
        try:
            if input_unit.get() in area_units and output_unit.get() in area_units:
                calc_area.delete(0, END)  
                calc_area.insert(0, round(float(enter_area.get()) * float(area_units[output_unit.get()] / area_units[input_unit.get()]), 5))
        except:
            calc_area.insert(0,"ERROR")

    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(area_selection[0])  
    output_unit.set(area_selection[0])

    #labels for text display
    input_label = Label(areawindow,text = "From:",bg = "#ccccc4",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(areawindow,text = "To:",bg = "#ccccc4",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_area = Entry(areawindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_area = Entry(areawindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_area.place(x=250,y=150)  
    calc_area.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(areawindow,input_unit,*area_selection)  
    output_menu = OptionMenu(areawindow,output_unit,*area_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for vol conversion
    convert_button = Button(areawindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = area_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(areawindow,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(areawindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)
    

def speed_converter():
    global speed_window
    speed_window=Toplevel(window)
    speed_window.title("speed window")
    speed_window.geometry("720x500")#size
    speed_window['background']='#f7cfc0'#background color
    speed_selection=["Select Unit","centimeter/second - cm/s","centimeter/hour - cm/hr","meter/second - m/s","meter/hour - m/hr /","kilometer/second - km/s", "kilometer/hour - km/hr",\
                  "miles/second - mps","miles/hour - mph","foot/second - fps","foot/hour - fph","knots - kn"]
    speed_units={"meter/second - m/s" :1, "centimeter/second - cm/s":100,\
              "centimeter/hour - cm/hr": 360000, "kilometer/second - km/s": 0.001, \
              "kilometer/hour - km/hr":3.6, "meter/hour - m/hr": 3600, \
              "miles/second - mps": 0.00062,\
              "miles/hour - mph": 2.23694,"foot/second - fps":3.28084,"foot/hour - fph":11811.02,\
              "knots - kn": 1.94384}

    title_label=Label(speed_window,text="SPEED UNIT CONVERTER",bg = "#f7cfc0",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=150,y=20)
    text_label=Label(speed_window,text="Speed is defined as the distance covered in a unit time. The SI unit of speed is meters per second (m/s)",\
                     bg = "#f7cfc0",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=65,y=90)

    def close_win():
        speed_window.destroy()

    def reset():
        calc_speed.delete(0,END)
        enter_.delete(0,END)
        input_unit.set(speed_selection[0])
        output_unit.set(speed_selection[0])
        
    def speed_convert():
        try:
            if input_unit.get() in speed_units and output_unit.get() in speed_units:
                calc_speed.delete(0, END)  
                calc_speed.insert(0, round(float(enter_.get()) * float(speed_units[output_unit.get()] / speed_units[input_unit.get()]), 5))
        except:
            calc_speed.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(speed_selection[0])  
    output_unit.set(speed_selection[0])

    #labels for text display
    input_label = Label(speed_window,text = "From:",bg = "#f7cfc0",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(speed_window,text = "To:",bg = "#f7cfc0",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_ = Entry(speed_window,bg = "#e8f8f5")  
    # output field to display result  
    calc_speed = Entry(speed_window,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_.place(x=250,y=150)  
    calc_speed.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(speed_window,input_unit,*speed_selection)  
    output_menu = OptionMenu(speed_window,output_unit,*speed_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for vol conversion
    convert_button = Button(speed_window,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = speed_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(speed_window,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(speed_window, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)
    
#converting pressure
def pressure_converter():
    global pressurewindow
    pressurewindow=Toplevel(window)
    pressurewindow.title("Pressure window")
    pressurewindow.geometry("720x500")#size
    pressurewindow['background']="#c4dfaa"#background color
    pressure_selection=["Select Unit","pascal - Pa","decipascal - dPa","centipascal - cPa", "millipascal - mPa","micropascal - μPa","nanopascal - nPa","dekapascal - daPa",
                  "hectopascal - hPa","kilopascal - kPa","megapascal  - MPa","gigapascal - Gpa","terapascal - TPa","bar - bar","milibar - mbar","microbar - μbar","ksi - ksi","psi - psi",
                  "standard atmosphere - atm","atmosphere technical - at","torr - Torr","foot water (4°C) - ftAq","inch water (4°C) - inAq","foot water (60°F) - ftAq",
                  "inch water (60°F) - inAq","millimeter water (4°C)","centimeter water (4°C)","millimeter mercury (0°C)","centimeter mercury (0°C)","inch mercury (32°F)","inch mercury (60°F)"]
    pressure_units={"pascal - Pa":1, "decipascal - dPa":0.1,"centipascal - cPa": 0.01, "millipascal - mPa": pow(10,-3),"micropascal - μPa": pow(10,-6), "nanopascal - nPa": pow(10,-9),  
                  "dekapascal - daPa":10, "hectopascal - hPa": 100, "kilopascal - kPa": pow(10,3),"megapascal  - MPa": pow(10,6),"gigapascal - Gpa": pow(10,9),
                  "terapascal - TPa": pow(10,12),"bar - bar":pow(10,5),"milibar - mbar":100,"microbar - μbar": 0.1,"ksi - ksi":6894757.2931783,"psi - psi":6894.7572931783,
                  "standard atmosphere - atm":101325,'atmosphere technical - at':98066.500000003,"torr - Torr":133.3223684211,"foot water (4°C) - ftAq":2988.98,
                  "inch water (4°C) - inAq":249.082,"foot water (60°F) - ftAq":2986.116,"inch water (60°F) - inAq":248.843,"millimeter water (4°C)":9.80638,"centimeter water (4°C)":98.0638,
                  "millimeter mercury (0°C)":133.322,"centimeter mercury (0°C)":1333.22,"inch mercury (32°F)":3386.38,"inch mercury (60°F)":3376.85}

    title_label=Label(pressurewindow,text="PRESSURE UNIT CONVERTER",bg = "#c4dfaa",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=120,y=20)
    text_label=Label(pressurewindow,text="Pressure is defined as the continuous physical force exerted on or against an object by",\
                     bg = "#c4dfaa",fg = "#000000",font=("Helvetica",9))
    text_label1=Label(pressurewindow,text="something in contact with it.It's SI unit is pascal.",\
                      bg = "#c4dfaa",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=100,y=85)
    text_label1.place(x=200,y=105)

    def close_win():
        pressurewindow.destroy()

    def reset():
        calc_pressure.delete(0,END)
        enter_pressure.delete(0,END)
        input_unit.set(pressure_selection[0])
        output_unit.set(pressure_selection[0])

    def pressure_convert():
        try:
            if input_unit.get() in pressure_units and output_unit.get() in pressure_units:
                calc_pressure.delete(0, END)  
                calc_pressure.insert(0, round(float(enter_pressure.get()) * float(pressure_units[output_unit.get()] / pressure_units[input_unit.get()]), 5))
        except:
            calc_pressure.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(pressure_selection[0])  
    output_unit.set(pressure_selection[0])

    #labels for text display
    input_label = Label(pressurewindow,text = "From:",bg="#c4dfaa",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(pressurewindow,text = "To:",bg = "#c4dfaa",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_pressure = Entry(pressurewindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_pressure = Entry(pressurewindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_pressure.place(x=250,y=150)  
    calc_pressure.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(pressurewindow,input_unit,*pressure_selection)  
    output_menu = OptionMenu(pressurewindow,output_unit,*pressure_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for pressure conversion
    convert_button = Button(pressurewindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = pressure_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(pressurewindow,text = "RESET",bg = "#9a9a9a",fg = "#ffffff",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(pressurewindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)

#converting energy
def energy_converter():
    global energywindow
    energywindow=Toplevel(window)
    energywindow.title("energy window")
    energywindow.geometry("720x500")#size
    energywindow['background']="#ffc1b6"#background color
    energy_selection=["Select Unit","joules - J","kilojoule - KJ","kilowatt-hour - KWh","watt-hour - Wh","calorie - cal","kilocalorie - kcal",
                        "megajoule - MJ","millijoule - mJ","microjoule - μJ","gigajoule - GJ","nanojoule - nJ","watt-second - Ws","kilowatt-second - KWs",
                        "electron-volt - eV","kiloelectron-volt - KeV","erg","gigawatt-hour - GWh","megawatt-hour - MWh","newton meter - Nm","ton","megaton - Mton",
                        "kiloton - Kton","horsepower hour- hp h","kilohorsepower hour- Khp h","gram-force meter - gfm","gram-force centimeter - gfcm",
                        "kilogram force meter - kgfm","kilogram force centimeter - kgfcm"]
    
    energy_units={"joules - J":1,"kilojoule - KJ":0.001,"kilowatt-hour - KWh":2.77*pow(10,-7),"watt-hour - Wh":0.000278,"calorie - cal":0.238,
                        "kilocalorie - kcal":0.000239,"megajoule - MJ":0.000001,"millijoule - mJ":1000,"microjoule - μJ":1000000,"gigajoule - GJ":pow(10,-10),
                        "nanojoule - nJ":pow(10,9),"watt-second - Ws":1,"kilowatt-second - KWs":0.001,"electron-volt - eV":6.24*pow(10,18),
                        "kiloelectron-volt - KeV":6.24*pow(10,15),"erg":10000000,"gigawatt-hour - GWh":2.77*pow(10,-13),"megawatt-hour - MWh":2.77*pow(10,-10),
                        "newton meter - Nm":1,"ton":2.39*pow(10,-10),"megaton - Mton":2.39*pow(10,-16),"kiloton - Kton":2.39*pow(10,-13),
                        "horsepower hour- hp h":3.77*pow(10,-7),"kilohorsepower hour- Khp h":3.77*pow(10,-10),"gram-force meter - gfm":101.97,
                        "gram-force centimeter - gfcm":10197.16,"kilogram force meter - kgfm":0.10197,"kilogram force centimeter - kgfcm":10.197}
    

    title_label=Label(energywindow,text="ENERGY UNIT CONVERTER",bg = "#ffc1b6",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=120,y=20)
    text_label=Label(energywindow,text="Energy is the quantitative property that is transferred to a body or to a physical system",\
                     bg = "#ffc1b6",fg = "#000000",font=("Helvetica",9))
    text_label1=Label(energywindow,text="recognizable in the performance of work and in the form of heat and light.It's SI unit is Joules.",\
                      bg = "#ffc1b6",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=120,y=90)
    text_label1.place(x=100,y=110)
    def close_win():
        energywindow.destroy()

    def reset():
        calc_energy.delete(0,END)
        enter_energy.delete(0,END)
        input_unit.set(energy_selection[0])
        output_unit.set(energy_selection[0])

    def energy_convert():
        try:
            if input_unit.get() in energy_units and output_unit.get() in energy_units:
                calc_energy.delete(0, END)  
                calc_energy.insert(0, round(float(enter_energy.get()) * float(energy_units[output_unit.get()] / energy_units[input_unit.get()]), 5))
        except:
            calc_energy.insert(0,"ERROR")
    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(energy_selection[0])  
    output_unit.set(energy_selection[0])

    #labels for text display
    input_label = Label(energywindow,text = "From:",bg="#ffc1b6",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(energywindow,text = "To:",bg = "#ffc1b6",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_energy = Entry(energywindow,bg = "#e8f8f5")  
    # output field to display result  
    calc_energy = Entry(energywindow,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_energy.place(x=250,y=150)  
    calc_energy.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(energywindow,input_unit,*energy_selection)  
    output_menu = OptionMenu(energywindow,output_unit,*energy_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for energy conversion
    convert_button = Button(energywindow,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = energy_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(energywindow,text = "RESET",bg = "#9a9a9a",fg = "#ffffff",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(energywindow, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)

#converting power
def power_converter():
    power_window=Toplevel(window)
    power_window.title("power window")
    power_window.geometry("720x500")#size
    power_window['background']='#c8f2ef'#background color
    power_selection=["Select Unit", "Watt","Deciwatt","centiwatt","milliwatt","microwatt","nanowatt",\
                "Decawatt","Hectowatt","Kilowatt","Megawatt",\
                "Gigawatt","Terawatt","Horsepower", "Erg per second", "Calories per second",\
                "Foot Pounds","British Thermal Unit (BTU)"]
    power_units={ "Watt":1,"Deciwatt":(pow(10,-1)),"centiwatt":(pow(10,-2)),"milliwatt":(pow(10,-3)),\
                "microwatt":(pow(10,-6)),"nanowatt":(pow(10,-9)),\
                "Decawatt":(pow(10,1)),"Hectowatt":(pow(10,2)),"Kilowatt":(pow(10,3)),"Megawatt":(pow(10,6)),\
                "Gigawatt":(pow(10,9)),"Terawatt":(pow(10,12)),"Horsepower":735.499, "Erg per second":(pow(10,-7)), 
                "Calories per second":4.167,"Foot Pounds":1.356,"British Thermal Unit (BTU)":(0.105*pow(10,4))
                 }

    title_label=Label(power_window,text="POWER UNIT CONVERTER",bg = "#c8f2ef",fg = "#000000",font=("Imprint Mt shadow",25,"bold"))
    title_label.place(x=130,y=20)
    text_label=Label(power_window,text="Power is referred to as the rate at which work is done upon an object.It is a time-based quantity",\
                     bg = "#c8f2ef",fg = "#000000",font=("Helvetica",9))
    text_label1=Label(power_window,text="that is related to how fast a job is done. It's SI unit is Watt (W)",\
                     bg = "#c8f2ef",fg = "#000000",font=("Helvetica",9))
    text_label.place(x=80,y=85)
    text_label1.place(x=150,y=105)
    
    def close_win():
        power_window.destroy()

    def reset():
        calc_power.delete(0,END)
        enter_power.delete(0,END)
        input_unit.set(power_selection[0])
        output_unit.set(power_selection[0])
        
    def power_convert():
        try:
        
            if input_unit.get() in power_units and output_unit.get() in power_units:
                calc_power.delete(0, END)  
                calc_power.insert(0, round(float(enter_power.get()) * float(power_units[output_unit.get()] / power_units[input_unit.get()]), 5))
        except:
            calc_power.insert(0,"ERROR")

    #input_unit snd output_unit to select units..these are the dropdown menu objects
    input_unit = StringVar()  
    output_unit = StringVar()
    input_unit.set(power_selection[0])  
    output_unit.set(power_selection[0])

    #labels for text display
    input_label = Label(power_window,text = "From:",bg = "#c8f2ef",fg = "#000000")
    input_label.place(x=180,y=150)
    output_label = Label(power_window,text = "To:",bg = "#c8f2ef",fg = "#000000")
    output_label.place(x=180,y=200)


    # input field to enter data  
    enter_power = Entry(power_window,bg = "#e8f8f5")  
    # output field to display result  
    calc_power = Entry(power_window,bg = "#e8f8f5")  
      
    # using the grid() method to set the position of the above entry fields   
    enter_power.place(x=250,y=150)  
    calc_power.place(x=250,y=200)  
      
    # adding the option menus to the main window  
    input_menu = OptionMenu(power_window,input_unit,*power_selection)  
    output_menu = OptionMenu(power_window,output_unit,*power_selection)
    input_menu.place(x=420,y=145)  
    output_menu.place(x=420,y=190)
    #calling function for vol conversion
    convert_button = Button(power_window,text = "CONVERT",bg = "#0b5345",fg = "#ffffff",width=10,command = power_convert)
    convert_button.place(x=230,y=250)
    # RESET button  
    reset_button = Button(power_window,text = "RESET",bg = "#9a9a9a",fg = "#000000",width=10, command = reset)
    reset_button.place(x=330,y=250)
    #close button
    close_button= Button(power_window, text= "CLOSE",bg = "#9a9a9a",fg = "#ffffff",width=10,command= close_win)
    close_button.place(x=430,y=250)



    
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\length2.png")
photo = photo.subsample(2,2)
photo2=PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\data2.png")
photo2 = photo2.subsample(2,2)
photo3 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\volume2.png")
photo3 = photo3.subsample(2,2)
photo4 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\temperature2.png")
photo4 = photo4.subsample(2,2)
photo5 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\mass2.png")
photo5 = photo5.subsample(2,2)
photo6 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\curr2.png")
photo6 = photo6.subsample(2,2)
photo7 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\time.png")
photo7 = photo7.subsample(2,2)
photo8 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\area.png")
photo8 = photo8.subsample(2,2)
photo9 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\speed.png")
photo9 = photo9.subsample(2,2)
photo10 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\pressure.png")
photo10 = photo10.subsample(2,2)
photo11 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\energy.png")
photo11 = photo11.subsample(2,2)
photo12 =PhotoImage(file = r"C:\Users\srika\OneDrive\Desktop\mini proj-sem1\power.png")
photo12 = photo12.subsample(2,2)
# here, image option is used to
# set image on button
Button(window, image = photo,borderwidth=0, bg='#ffffff',fg='#ffffff',command=length_converter).place(x=200,y=157)
Button(window, image = photo2,borderwidth=0, bg='#ffffff',fg='#ffffff',command=data_converter).place(x=470,y=150)
Button(window, image = photo3,borderwidth=0, bg='#ffffff',fg='#ffffff',command=vol_converter).place(x=700,y=150)
Button(window, image = photo4,borderwidth=0, bg='#ffffff',fg='#ffffff',command=temperature_converter).place(x=200,y=353)
Button(window, image = photo5,borderwidth=0, bg='#ffffff',fg='#ffffff',command=mass_converter).place(x=470,y=363)
Button(window, image = photo6,borderwidth=0, bg='#ffffff',fg='#ffffff',command=currency_converter).place(x=700,y=368)
Button(window, image = photo7,borderwidth=0, bg='#ffffff',fg='#ffffff',command=time_converter).place(x=200,y=530)
Button(window, image = photo8,borderwidth=0, bg='#ffffff',fg='#ffffff',command=area_converter).place(x=470,y=550)
Button(window, image = photo9,borderwidth=0, bg='#ffffff',fg='#ffffff',command=speed_converter).place(x=700,y=548)
Button(window, image = photo10,borderwidth=0, bg='#ffffff',fg='#ffffff',command=pressure_converter).place(x=930,y=153)
Button(window, image = photo11,borderwidth=0, bg='#ffffff',fg='#ffffff',command=energy_converter).place(x=930,y=360)
Button(window, image = photo12,borderwidth=0, bg='#ffffff',fg='#ffffff',command=power_converter).place(x=930,y=547)
mainloop()
