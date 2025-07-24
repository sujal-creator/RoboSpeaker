import tkinter as tk
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can try voices[1] for female
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak():
    text = entry.get()
    if text.strip():
        speak_text(text)

def clear():
    entry.delete(0, tk.END)

def exit_app():
    root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Sujal RoboSpeaker")
root.geometry("450x250")
root.config(bg="#f5f5f5")

# Set icon (optional)
try:
    root.iconbitmap("robospeaker.ico")
except:
    pass

# Title
label = tk.Label(root, text="🤖 Sujal RoboSpeaker", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
label.pack(pady=15)

# Entry box
entry = tk.Entry(root, font=("Arial", 14), width=35)
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Speak", font=("Arial", 12), width=10, command=speak).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", font=("Arial", 12), width=10, command=clear).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Exit", font=("Arial", 12), width=10, command=exit_app).grid(row=0, column=2, padx=5)

# Run the GUI
root.mainloop()

