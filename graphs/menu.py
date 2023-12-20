import tkinter as tk
from tkinter import messagebox
import os

class MenuProqrami:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Proqramı")

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        proqram_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Proqramlar", menu=proqram_menu)

        # Program 1 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən çəkisiz, istiqamətsiz qrafın qonşuluq matrisi verilib. Qrafı vizual olaraq göstərən proqram", "qraf1_tkinter.py")

        # Program 2 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən çəkili, istiqamətsiz qraf verilib. Qrafı vizual olaraq göstərən proqram", "qraf2_tkinter.py")

        # Program 3 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən çəkisiz qrafın qonşuluq matrisi verilib. Qrafın əlaqəli olub-olmadığını müəyyən edən proqram", "qraf3_tkinter.py")

        # Program 4 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Qrafın ağac olub-olmadığını müəyyən edən proqram", "qraf4_tkinter.py")

        # Program 5 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Bu qrafın ağac və ya meşə olub-olmadığını müəyyən edən proqram", "qraf5_tkinter.py")

        # Program 6 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Qrafın istiqamətli və ya istiqamətsiz olub-olmadığını müəyyən edən proqram", "qraf6_tkinter.py")

        # Program 7 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Qrafın 2 hissəli olub-olmadığını müəyyən edən proqram", "qraf7_tkinter.py")

        # Program 8 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Qrafın neçə əlaqəlilik komponenti olduğunu müəyyən edən proqram", "qraf8_tkinter.py")

        # Program 9 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən qrafın qonşuluq matrisi verilib. Qrafın tam olub-olmadığını müəyyən edən proqram", "qraf9_tkinter.py")

        # Program 11 alt menu
        self.add_program_menu(proqram_menu, "İstifadəçi tərəfindən daxil edilən qrafın çəki matrisinə uyğun olaraq qrafın daxilindəki bünövrə ağacı vizual olaraq göstərən proqram", "qraf11_tkinter.py")

        menubar.add_command(label="Bağla", command=self.programi_bagla)

    def add_program_menu(self, parent_menu, label, program_adı):
        program_menu = tk.Menu(parent_menu, tearoff=0)
        program_menu.add_command(label="İşə sal", command=self.ishe_sal(program_adı))
        parent_menu.add_cascade(label=label, menu=program_menu)

    def ishe_sal(self, program_adı):
        def callback():
            os.system(f"python {program_adı}")
            messagebox.showinfo("Əməliyyat uğurla başa çatdı", f"{program_adı} işə salındı.")
            self.root.lift()
            self.böyüt()

        return callback

    def programi_bagla(self):
        self.root.destroy()

    def böyüt(self):
        for item in self.root.winfo_children():
            if isinstance(item, tk.Menu):
                for element in item.winfo_children():
                    current_font = element.cget("font")
                    current_size = int(current_font.split("size:")[1].split("}")[0])
                    new_size = current_size * 2
                    new_font = current_font.replace(f"size:{current_size}", f"size:{new_size}")
                    element.configure(font=new_font)

                    element.configure(width=element.winfo_reqwidth()*2, height=element.winfo_reqheight()*2)

if __name__ == "__main__":
    root = tk.Tk()
    menu_proqrami = MenuProqrami(root)
    root.mainloop()