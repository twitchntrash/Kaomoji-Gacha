import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random

common_kaomoji = [("Common", "(*¯︶¯*)"), ("Common", "ಠ_ಠ"), ("Common", "ヽ(´▽)ﾉ"), ("Common", "(¬‿¬)"), ("Common", "( ❛ ᴗ ❛)")]
uncommon_kaomoji = [("Uncommon", "(✧ω✧)"), ("Uncommon", "(≧∇≦)"), ("Uncommon", "(´｡• ω •｡)")]
rare_kaomoji = [("Rare", "(✯◡✯)"), ("Rare", "(╥﹏╥)"), ("Rare", "(*^▽^*)")]
epic_kaomoji = [("Epic", "(╬`益´)"), ("Epic", "(҂ `з´ )"), ("Epic", "(`皿´＃)")]
legendary_kaomoji = [("Legendary", "(っ´ω`)ﾉ(╥ω╥)"), ("Legendary", "ヽ(￣ω￣(。。 )ゝ"), ("Legendary", "(ｏ・_・)ノ”(ノ_<、)")]

def choose_random_kaomoji():
    kaomoji_list = random.choice([common_kaomoji, uncommon_kaomoji, rare_kaomoji, epic_kaomoji, legendary_kaomoji])
    selected_kaomoji = random.choice(kaomoji_list)
    label_rarity.config(text="Rarity: " + selected_kaomoji[0])
    label_kaomoji.config(text=selected_kaomoji[1])

root = tk.Tk()
root.title("Kaomoji Gacha")
root.geometry("400x300")

style = ThemedStyle(root)
style.set_theme("plastik")

label_rarity = ttk.Label(root, text="", font=("Comic Sans MS", 12))
label_rarity.pack(pady=10)

label_kaomoji = ttk.Label(root, text="", font=("Comic Sans MS", 30))
label_kaomoji.pack(pady=20)

choose_random_kaomoji()

choose_button = ttk.Button(root, text="Try again", command=choose_random_kaomoji)
choose_button.pack(pady=10)

def close_window():
    root.destroy()

close_button = ttk.Button(root, text="Exit", command=close_window)
close_button.pack(pady=10)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.mainloop()
