import tkinter as tk, os, webbrowser
from tkinter import ttk, colorchooser, messagebox, Tk
try:
    from PIL import Image, ImageTk
except ImportError and ImportWarning as Module_Error:
    print("There is a problem importing Pillow module", Module_Error)
else:
    pass

if os.path.exists("Icon.ico"):
    pass
else:
    print("Err! : Could not find Icon file")
    input()

class Window:
    def __init__(self, root):
        self.Parent = root
        self.Parent.title("GD Color Picker")
        self.Parent.geometry("440x420+400+100")
        self.Parent.resizable(0, 0)
        self.Parent.iconbitmap("Icon.ico")
        self.has_toplevel = False

        # Tkinter Widgets(Labels)
        self.Color_Label_Outline = ttk.Label(self.Parent, background="Black")
        self.Color_Label_Outline.place(x=10, y=10, width=106, height=106)
        self.Color_Label = ttk.Label(self.Parent, background="LightGray", text="None", font=(None, 10), anchor='center')
        self.Color_Label.place(x=13, y=13, width=100, height=100)
        self.Hex_Copy_Options_Label = ttk.Label(self.Parent, text='Copy Hex options :', font=(None, 12))
        self.Hex_Copy_Options_Label.place(x=10, y=170)
        self.RGB_Copy_Options_Label = ttk.Label(self.Parent, text='Copy RGB options :', font=(None, 12))
        self.RGB_Copy_Options_Label.place(x=10, y=270)

        # Tkinter Widgets(Labels for RGB)
        self.R_Label = ttk.Label(self.Parent, text="R :", font=(None, 10, "bold"))
        self.R_Label.place(x=150, y=5)
        self.G_Label = ttk.Label(self.Parent, text="G :", font=(None, 10, "bold"))
        self.G_Label.place(x=150, y=35)
        self.B_Label = ttk.Label(self.Parent, text="B :", font=(None, 10, "bold"))
        self.B_Label.place(x=150, y=65)
        self.Hex_Label = ttk.Label(self.Parent, text="Hex :", font=(None, 10, "bold"))
        self.Hex_Label.place(x=150, y=95)

        # Tkinter widgets(Buttons)
        self.Choose_Button = ttk.Button(self.Parent, text="Choose...", padding=5)
        self.Choose_Button.place(x=10, y=120)
        self.Choose_Button['command'] = self.Color_Picker
        self.Copy_Hex_Button = ttk.Button(self.Parent, text="Copy Hex", padding=5, width=20)
        self.Copy_Hex_Button.place(x=10, y=200)
        self.Copy_Hex_Button['command'] = self.Copy_Hex
        self.Copy_Hex1_Button = ttk.Button(self.Parent, text="Copy w/o '#'", padding=5, width=20)
        self.Copy_Hex1_Button.place(x=150, y=200)
        self.Copy_Hex1_Button['command'] = self.Copy_Hex_Nhash
        self.Copy_Hex2_Button = ttk.Button(self.Parent, text="Copy in brackets '( )'", padding=5, width=20)
        self.Copy_Hex2_Button.place(x=290, y=200)
        self.Copy_Hex2_Button['command'] = self.Copy_Hex_Brackets
        self.Copy_RGB_Button = ttk.Button(self.Parent, text="Copy RGB", padding=5, width=20)
        self.Copy_RGB_Button.place(x=10, y=300)
        self.Copy_RGB_Button['command'] = self.Copy_RGB
        self.Copy_RGB1_Button = ttk.Button(self.Parent, text="Copy w/o brackets", padding=5, width=20)
        self.Copy_RGB1_Button.place(x=150, y=300)
        self.Copy_RGB1_Button['command'] = self.Copy_RGB_Nbrackets
        self.Copy_RGB2_Button = ttk.Button(self.Parent, text="Copy w/o commas", padding=5, width=20)
        self.Copy_RGB2_Button.place(x=290, y=300)
        self.Copy_RGB2_Button['command'] = self.Copy_RGB_NComma
        self.Copy_RGB3_Button = ttk.Button(self.Parent, text="Copy w/o ',' or '( )'", padding=5, width=20)
        self.Copy_RGB3_Button.place(x=10, y=340)
        self.Copy_RGB3_Button['command'] = self.Copy_RGB_NCommaBrackets
        self.Copy_RGB4_Button = ttk.Button(self.Parent, text="Copy R only", padding=5, width=12)
        self.Copy_RGB4_Button.place(x=150, y=340)
        self.Copy_RGB4_Button['command'] = self.Copy_RGB_R
        self.Copy_RGB5_Button = ttk.Button(self.Parent, text="Copy G only", padding=5, width=12)
        self.Copy_RGB5_Button.place(x=244, y=340)
        self.Copy_RGB5_Button['command'] = self.Copy_RGB_G
        self.Copy_RGB6_Button = ttk.Button(self.Parent, text="Copy B only", padding=5, width=12)
        self.Copy_RGB6_Button.place(x=338, y=340)
        self.Copy_RGB6_Button['command'] = self.Copy_RGB_B
        self.About_Button = ttk.Button(self.Parent, text="About!", width=50, padding=5)
        self.About_Button.place(x=10, y=380)
        self.About_Button['command'] = self.Abt_Faris
        self.Help_Button = ttk.Button(self.Parent, text="Help", padding=5, width=13)
        self.Help_Button.place(x=333, y=380)
        self.Help_Button['command'] = self.Help_Message

    def Help_Message(self):
        messagebox.showinfo("Help", "This is Color Picker help message")

    def Color_Picker(self):
        self.PColor_Picker = colorchooser.askcolor()
        if self.PColor_Picker[1]:
            self.Hex_Str = str(self.PColor_Picker[1])
            self.Color_Label['background'] = self.PColor_Picker[1]
            self.Color_Label['text'] = ""
            self.Parent.title("GD Color Picker" + " - " + str(self.PColor_Picker[1]) + " " + str(self.HextoRGB(str(self.PColor_Picker[1]))))
            self.R_Label['text'] = ("R : " + str(R_val))
            self.G_Label['text'] = ("G : " + str(G_val))
            self.B_Label['text'] = ("B : " + str(B_val))
            self.Hex_Label['text'] = ("Hex : " + self.Hex_Str)
            # Print to console
            print(self.PColor_Picker[1])
            print(str(self.HextoRGB(str(self.PColor_Picker[1]))))
        else:
            print("Cancelled")

    def HextoRGB(self, hex_code):
        global R_val, G_val, B_val
        hex_code = hex_code.lstrip('#')       
        R_val = int(hex_code[0:2], 16)
        G_val = int(hex_code[2:4], 16)
        B_val = int(hex_code[4:6], 16)
        
        return R_val, G_val, B_val

    # Hex copy
    def Copy_Hex(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.PColor_Picker[1]))
            messagebox.showinfo("Done!", "Hex code copied to clipboard!")
            print("Done! Hex code copied to clipboard!")
            print(str(self.PColor_Picker[1]))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")
    
    def Copy_Hex_Nhash(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.PColor_Picker[1]).lstrip('#'))
            messagebox.showinfo("Done!", "Hex code without hash copied to clipboard!")
            print("Done! Hex code without hash copied to clipboard!")
            print(str(self.PColor_Picker[1]).lstrip('#'))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_Hex_Brackets(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append("(" + str(self.PColor_Picker[1]) + ")")
            messagebox.showinfo("Done!", "Hex code in brackets copied to clipboard!")
            print("Done! Hex code in brackets copied to clipboard!")
            print("(" + str(self.PColor_Picker[1]) + ")")
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    # RGB copy
    def Copy_RGB(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.HextoRGB(str(self.PColor_Picker[1]))))
            messagebox.showinfo("Done!", "RGB values copied to clipboard!")
            print("Done! RGB values copied to clipboard!")
            print(str(self.HextoRGB(str(self.PColor_Picker[1]))))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")
    
    def Copy_RGB_Nbrackets(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace("(", "").replace(")", ""))
            messagebox.showinfo("Done!", "RGB values without brackets copied to clipboard!")
            print("Done! RGB values without brackets copied to clipboard!")
            print(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace("(", "").replace(")", ""))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_RGB_NComma(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace(",", ""))
            messagebox.showinfo("Done!", "RGB values without commas copied to clipboard!")
            print("Done! RGB values without commas copied to clipboard!")
            print(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace(",", ""))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_RGB_NCommaBrackets(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace(",", "").replace("(", "").replace(")", ""))
            messagebox.showinfo("Done!", "RGB values without commas and brackets copied to clipboard!")
            print("Done! RGB values without commas and brackets copied to clipboard!")
            print(str(self.HextoRGB(str(self.PColor_Picker[1]))).replace(",", "").replace("(", "").replace(")", ""))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_RGB_R(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(R_val))
            messagebox.showinfo("Done!", "R value copied to clipboard!")
            print("Done! R value copied to clipboard!")
            print(str(R_val))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_RGB_G(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(G_val))
            messagebox.showinfo("Done!", "G value copied to clipboard!")
            print("Done! G value copied to clipboard!")
            print(str(G_val))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Copy_RGB_B(self):
        try:
            self.Clip_Board = Tk()
            self.Clip_Board.withdraw()
            self.Clip_Board.clipboard_clear()
            self.Clip_Board.clipboard_append(str(B_val))
            messagebox.showinfo("Done!", "B value copied to clipboard!")
            print("Done! B value copied to clipboard!")
            print(str(B_val))
        except:
            messagebox.showerror("Error", "No selected color to copy")
            print("Error No selected color to copy")

    def Src_Code(self, event=None):
        webbrowser.open_new_tab("https://github.com/FarisGd/GD-color-picker")

    def Abt_Faris(self):
        if not self.has_toplevel:
            try:
                self.SpikeBoi_Cube = Image.open("FarisGD.png")
                self.SpikeBoi_Label_img = ImageTk.PhotoImage(self.SpikeBoi_Cube)
            except FileNotFoundError or FileExistsError:
                messagebox.showerror("Error", "Failed to import SpikeBoi")
                print("Failed to import SpikeBoi")
            self.Tp_Lvl = tk.Toplevel(self.Parent)
            self.Tp_Lvl.geometry("350x220+450+250")
            self.Tp_Lvl.title("About!")
            self.Tp_Lvl.iconbitmap("Icon.ico")
            self.Tp_Lvl.configure(background="#d7d7d7")
            self.SpikeBoi_Label = ttk.Label(self.Tp_Lvl, image=self.SpikeBoi_Label_img, background="#d7d7d7")
            self.SpikeBoi_Label.pack()
            self.Tp_Lvl_Text_Label = ttk.Label(self.Tp_Lvl, text="GD Color Picker v1.0 By Faris", font=(None, 15, "bold"), background="#d7d7d7")
            self.Tp_Lvl_Text_Label.pack()
            self.Module_Info_Label = ttk.Label(self.Tp_Lvl, text="Tcl/Tk 8.6-Pillow 10.2.0", background="#d7d7d7")
            self.Module_Info_Label.pack()
            self.Style = ttk.Style(self.Tp_Lvl)
            self.Src_Code_Label = ttk.Label(self.Tp_Lvl, text="Source Code", font=(None, 10, 'underline'), foreground="blue", cursor="hand2", background="#d7d7d7")
            self.Src_Code_Label.pack()
            self.Src_Code_Label.bind("<Button-1>", self.Src_Code)
            self.Tp_Lvl.protocol("WM_DELETE_WINDOW", self.Set_Tplvl_Crte)
            self.has_toplevel = True
            print("Tcl/Tk ver 8.6\nPillow ver 10.2.0")
            self.Tp_Lvl.mainloop()

    def Set_Tplvl_Crte(self):
        self.has_toplevel = False
        self.Tp_Lvl.destroy()   

if __name__ == "__main__":
    if os.path.exists("FarisGD.png"):
        print("[Optional] : U can copy RGB and Hex from here.\nGD color picker by Faris")
        root = tk.Tk()
        app = Window(root)
        root.mainloop()
    else:
        print("Get the Spikeboi png first to use the program")
        input("Type anything and hit return to exit (or just hit return) :")