import tkinter as tk
from tkinter import messagebox
import csv

# CSV faila nosaukums
csv_file = 'registrations.csv'

# Funkcija, lai saglabātu datus CSV failā
def save_registration(student_name, student_surname, student_phone, parent_name, parent_phone, club, day, time):
    # Atvērt CSV failu pieraksta režīmā
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_name, student_surname, student_phone, parent_name, parent_phone, club, day, time])
    
    # Paziņojums par veiksmīgu saglabāšanu
    messagebox.showinfo("Veiksmīgi", "Pieteikums ir veiksmīgi saglabāts!")

# Funkcija, lai apstrādātu pieteikumu
def submit():
    # Iegūt ievadītās vērtības no lietotāja
    student_name = entry_student_name.get()
    student_surname = entry_student_surname.get()
    student_phone = entry_student_phone.get()
    parent_name = entry_parent_name.get()
    parent_phone = entry_parent_phone.get()
    club = club_var.get()
    day = day_var.get()
    time = time_var.get()
    
    # Pārbaudīt, vai visi lauki ir aizpildīti
    if all([student_name, student_surname, student_phone, parent_name, parent_phone, club, day, time]):
        # Saglabāt datus CSV failā
        save_registration(student_name, student_surname, student_phone, parent_name, parent_phone, club, day, time)
        
        # Notīrīt ievades laukus
        entry_student_name.delete(0, tk.END)
        entry_student_surname.delete(0, tk.END)
        entry_student_phone.delete(0, tk.END)
        entry_parent_name.delete(0, tk.END)
        entry_parent_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildiet visus laukus!")

# Izveidot GUI logu
root = tk.Tk()
root.title("Pieteikšanās pulciņiem")

# Skolēna dati
tk.Label(root, text="Skolēna vārds:").grid(row=0, column=0, padx=10, pady=5)
entry_student_name = tk.Entry(root)
entry_student_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Skolēna uzvārds:").grid(row=1, column=0, padx=10, pady=5)
entry_student_surname = tk.Entry(root)
entry_student_surname.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Skolēna tālrunis:").grid(row=2, column=0, padx=10, pady=5)
entry_student_phone = tk.Entry(root)
entry_student_phone.grid(row=2, column=1, padx=10, pady=5)

# Vecāku dati
tk.Label(root, text="Vecāka vārds:").grid(row=3, column=0, padx=10, pady=5)
entry_parent_name = tk.Entry(root)
entry_parent_name.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Vecāka tālrunis:").grid(row=4, column=0, padx=10, pady=5)
entry_parent_phone = tk.Entry(root)
entry_parent_phone.grid(row=4, column=1, padx=10, pady=5)

# Pulciņa izvēle
tk.Label(root, text="Pulciņš:").grid(row=5, column=0, padx=10, pady=5)
club_var = tk.StringVar()
club_dropdown = tk.OptionMenu(root, club_var, "Futbols", "Zīmēšana", "Programmēšana", "Šahs")
club_dropdown.grid(row=5, column=1, padx=10, pady=5)

# Dienas izvēle
tk.Label(root, text="Diena:").grid(row=6, column=0, padx=10, pady=5)
day_var = tk.StringVar()
day_dropdown = tk.OptionMenu(root, day_var, "Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena")
day_dropdown.grid(row=6, column=1, padx=10, pady=5)

# Laika izvēle
tk.Label(root, text="Laiks:").grid(row=7, column=0, padx=10, pady=5)
time_var = tk.StringVar()
time_dropdown = tk.OptionMenu(root, time_var, "10:00", "12:00", "14:00", "16:00")
time_dropdown.grid(row=7, column=1, padx=10, pady=5)

# Pieteikuma iesniegšanas poga
submit_button = tk.Button(root, text="Pieteikties", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Palaist GUI
root.mainloop()
