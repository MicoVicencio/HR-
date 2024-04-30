import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200))  # Resize the image if needed
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to avoid garbage collection
        
        # Rename and save the image to a specific folder
        folder_path = "path/to/your/folder"
        new_file_name = "uploaded_image.png"  # You can modify the new file name as needed
        new_file_path = os.path.join(folder_path, new_file_name)
        img.save(new_file_path)
        print(f"Image saved as {new_file_path}")

# Create the tkinter window
root = tk.Tk()
root.title("Image Uploader")

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Create a button to open the file dialog
button = tk.Button(root, text="Open Image", command=open_file)
button.pack()

# Run the tkinter main loop
root.mainloop()