import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline

def GenerateImage():
    pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
    description = description_entry.get()  # Get the text from the entry widget
    if description == "":
        messagebox.showerror("Input Error", "Description cannot be empty.")
        return

    try:
        # Generate the image
        image = pipe(description).images[0]
        image.save("output.png")  # Save the generated image to a file
    except Exception as e:
        messagebox.showerror("Generation Error", str(e))
        return

    try:
        # Open the saved image and convert it to a format Tkinter can use
        pil_image = Image.open("output.png")
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # Update the img_label with the new image
        img_label.config(image=tk_image)
        img_label.image = tk_image
        img_label.config(text="")
    except Exception as e:
        messagebox.showerror("Display Error", str(e))
        return

    spinner.stop()

# Create the interface
app = tk.Tk()
app.config(bg="#ff9800")
app.title("Tkinter Application UI")
app.geometry("450x450")

# Description label and entry
description_label = tk.Label(app, text="Description:")
description_label.pack(side="left")
description_label.place(x=0, y=40)
description_label.config(bg="#ff9800")
description_entry = ttk.Entry(app)
description_entry.pack(side="right")
description_entry.place(x=100, y=40, width=200, height=20)

# Generate button
generate_button = tk.Button(app, text="Generate Image", command=GenerateImage, bg="#6c757d")
generate_button.pack()
generate_button.place(x=320, y=40)

# Image display frame and label
frame = tk.Frame(app, bg="gray")
frame.pack(pady=10)
frame.place(x=75, y=150, width=300, height=200)
img_label = tk.Label(frame, text="L'image sera générée ici")
img_label.pack()
img_label.place(x=85, y=85)

# Loading spinner
spinner = ttk.Progressbar(app, mode="indeterminate")
spinner.pack()
spinner.place(x=175, y=115)

# Start the app
app.mainloop()
