import tkinter as tk
from tkinter import filedialog

# Fenster herstellen
root = tk.Tk()

# Fenstereinstellungen
root.title("FitAI Coach")
root.geometry("700x650")
root.configure(bg="#121212")

# Programmtitel
title = tk.Label(
    root,
    text="FITAI COACH",
    font=("Helvetica", 28, "bold"),
    fg="#00FFB2",
    bg="#121212"
)

title.pack(pady=20)
# -------- Name --------
name_label = tk.Label(
    root,
    text="Name:",
    font=("Arial", 14),
    fg="#EAEAEA",
    bg="#000000"
)
name_label.pack()

name_entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    borderwidth=0
)
name_entry.pack(pady=5)

# -------- Alter --------
age_label = tk.Label(
    root,
    text="Alter:",
    font=("Arial", 14),
    fg="#EAEAEA",
    bg="#121212"
)
age_label.pack()

age_entry = tk.Entry(
    root,
    font=("Arial", 14)
)
age_entry.pack(pady=5)

# -------- Größe --------
height_label = tk.Label(
    root,
    text="Größe (cm):",
    font=("Arial", 14),
    fg="#EAEAEA",
    bg="#121212"
)
height_label.pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 14)
)
height_entry.pack(pady=5)

# -------- Gewicht --------
weight_label = tk.Label(
    root,
    text="Gewicht (kg):",
    font=("Arial", 14),
    fg="#EAEAEA",
    bg="#121212"
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 14)
)
weight_entry.pack(pady=5)

# -------- Ziel --------
goal_label = tk.Label(
    root,
    text="Ziel:",
    font=("Arial", 14),
    fg="#EAEAEA",
    bg="#121212"
)
goal_label.pack()

# Zieloptionen
goals = [
    "Muskelaufbau",
    " Fettverbrennung",
    "Kraft",
    "Ausdauer",
    "Fitness "
]

# Auswahlvariable
selected_goal = tk.StringVar()
selected_goal.set(goals[0])

# Auswahlmenü
goal_menu = tk.OptionMenu(
    root,
    selected_goal,
    *goals
)

goal_menu.config(
    font=("Arial", 12),
    bg="#4CAF50",
    fg="#EAEAEA",
    width=20
)

goal_menu.pack(pady=10)

# Bildpfad
photo_path = ""

# Bildauswahl


def select_photo():
    global photo_path

    photo_path = filedialog.askopenfilename(
        title=" Bildauswahl",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    # wenn Bild ausgewählt
    if photo_path != "":
        photo_label.config(
            text="Bild ausgewählt   ✅"
        )


# Hauptfunktion


def generate_plan():
    name = name_entry.get()
    age = age_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()

    # Ziel ermitteln
    goal = selected_goal.get()

    # Größenumrechnung
    height_m = float(height) / 100

    # BMI-Berechnung
    bmi = float(weight) / (height_m ** 2)
    # ungefähre Kalorienberechnung
    calories = float(weight) * 30

    # Ausgabetext
    result_text = result_text = f"""
{name}  

Alter: {age}

Größe: {height} Zentimeter

Gewicht: {weight} Kilogramm

BMI: {round(bmi, 2)}

empfohlene tägliche Kalorienzufuhr  : {round(calories)} kcal
"""

    #  intelligente Analyse
    if bmi < 18.5:
        result_text += "\nIntelligente Analyse: Sie benötigen Muskelaufbau.\n"

    elif bmi < 25:
        result_text += "\nIntelligente Analyse: Ihr Körperzustand ist ausgeglichen.\n"

    else:
        result_text += "\nIntelligente Analyse: Eine Reduzierung des Körperfetts wird empfohlen.\n"

    # Trainingsprogramm
    if goal == "عضله سازی":
        result_text += "\nTrainingsprogramm: Push Pull Legs"

    elif goal == "چربی سوزی":
        result_text += "\nTrainingsprogramm: HIIT und Ausdauertraining"

    elif goal == "قدرت":
        result_text += "\nTrainingsprogramm: Powerlifting"

    elif goal == "استقامت":
        result_text += "\nTrainingsprogramm: Ausdauertraining"

    else:
        result_text += "\nTrainingsprogramm: allgemeine Fitness"

        # neues Fenster erstellen
    result_window = tk.Toplevel(root)

    result_window.title("Ihr Fitnessprogramm")

    result_window.geometry("500x500")

    result_window.configure(bg="#121212")

    # Ergebnis anzeigen
    result_text_label = tk.Label(
        result_window,
        text=result_text,
        font=("Arial", 13),
        fg="#EAEAEA",
        bg="#121212",
        justify="right"
    )

    result_text_label.pack(pady=20)

    # Benutzerdaten speichern
    with open("users.txt", "a", encoding="utf-8") as file:

        file.write(f"""
    Name: {name}
    Alter: {age}
    Größe: {height}
    Gewicht: {weight}
    Ziel: {goal}
    BMI: {round(bmi, 2)}
    -------------------------
    """)

# Reset-Funktion


def reset_fields():

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    selected_goal.set(goals[0])

    result_label.config(text="")

    photo_label.config(
        text="Kein Bild ausgewählt  "
    )


    # Bildstatus-Text
photo_label = tk.Label(
    root,
    text="Kein Bild ausgewählt ",
    font=("Arial", 11),
    fg="#EAEAEA",
    bg="#121212"
)

photo_label.pack()
# Bildrahmen und Aktualisierung
top_button_frame = tk.Frame(
    root,
    bg="#121212"
)

top_button_frame.pack(pady=10)

# Bild auswählen Button
photo_button = tk.Button(
    top_button_frame,
    text="SELECT PHOTO",
    font=("Helvetica", 11, "bold"),
    bg="#2979FF",
    fg="white",
    padx=12,
    pady=5,
    borderwidth=0,
    cursor="hand2",
    command=select_photo
)

photo_button.grid(row=0, column=0, padx=10)

# Aktualisieren Button
reset_button = tk.Button(
    top_button_frame,
    text="Zurücksetzen",
    font=("Helvetica", 10, "bold"),
    bg="#FF5252",
    fg="white",
    padx=10,
    pady=4,
    borderwidth=0,
    cursor="hand2",
    command=reset_fields
)

reset_button.grid(row=0, column=1, padx=10)


# Ergebnis anzeigen
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    fg="#EAEAEA",
    bg="#121212",
    justify="right"
)

result_label.pack(pady=20)
# Button-Frame
button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(pady=20)

# Generate-Button
generate_button = tk.Button(
    button_frame,
    text="Trainingsplan erstellen",
    font=("Helvetica", 14, "bold"),
    bg="#00C896",
    fg="black",
    padx=15,
    pady=8,
    borderwidth=0,
    cursor="hand2",
    command=generate_plan
)

generate_button.grid(row=0, column=0, padx=10)


# Programm ausführen
root.mainloop()
