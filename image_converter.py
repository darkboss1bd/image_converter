import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os
import threading
import time

# Main Application
class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 darkboss1bd - Advanced Image Converter")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0e0e0e")

        self.file_path = ""
        self.supported_formats = ["PNG", "JPG", "JPEG", "BMP", "GIF", "ICO", "TIFF", "WEBP"]

        # Start hacker animation in thread
        self.animation_running = True
        threading.Thread(target=self.hacker_animation, daemon=True).start()

        self.setup_ui()

    def hacker_animation(self):
        animation_text = """
    ▄█ █   █▀█ █░█ █▀▀ █▀█ ░ █▀▀ █ █▀█ █▄░█ █▀▀ █▀█
    ░█ █   █▀▀ █▀█ ██▄ █▀▄ █ █▄▄ █ █▄█ █░▀█ ██▄ █▀▄
    [✓] SYSTEM BREACHED... INITIATING DARKBOSS1BD MODULE
    [✓] ENABLING SECURE CONVERSION ENGINE...
    [✓] LOADING PAYLOAD: IMAGE_TRANSFORMER v3.0
    [✓] TARGET FORMAT DETECTED: *.png, *.jpg, *.ico...
    [✓] ALL SYSTEMS GREEN. READY FOR UPLOAD.
        """
        lines = animation_text.strip().split('\n')
        label = tk.Label(self.root, bg="#0e0e0e", fg="#0f0", font=("Courier", 10), justify="left")
        label.place(x=20, y=100)

        while self.animation_running:
            for line in lines:
                if not self.animation_running:
                    break
                label.config(text=line)
                time.sleep(0.4)
                self.root.update()

    def setup_ui(self):
        # Stop animation when UI loads
        self.animation_running = False

        # Banner
        banner = tk.Label(
            self.root,
            text="🔐 darkboss1bd - Image Converter Pro",
            font=("Consolas", 18, "bold"),
            bg="#000000",
            fg="#00ff00"
        )
        banner.pack(fill=tk.X, pady=10)

        # Info Frame
        info_frame = tk.Frame(self.root, bg="#111")
        info_frame.pack(pady=10, fill=tk.X, padx=20)

        tk.Label(info_frame, text="👤 Telegram: @darkvaiadmin | 🌐 Website: https://serialkey.top/", 
                 bg="#111", fg="#00ffaa", font=("Arial", 10)).pack()

        # Upload Button
        self.upload_btn = tk.Button(
            self.root,
            text="📁 Upload Image",
            font=("Arial", 14, "bold"),
            bg="#006400",
            fg="white",
            command=self.upload_image
        )
        self.upload_btn.pack(pady=20)

        # File Label
        self.file_label = tk.Label(self.root, text="No file selected", bg="#0e0e0e", fg="#aaa", font=("Arial", 10))
        self.file_label.pack(pady=5)

        # Format Selection
        format_frame = tk.Frame(self.root, bg="#0e0e0e")
        format_frame.pack(pady=10)

        tk.Label(format_frame, text="📤 Convert to:", font=("Arial", 12), bg="#0e0e0e", fg="white").pack()
        self.format_var = tk.StringVar(value="PNG")
        self.format_menu = ttk.Combobox(format_frame, values=self.supported_formats, textvariable=self.format_var, state="readonly", width=10, font=("Arial", 11))
        self.format_menu.pack(pady=5)

        # Convert Button
        self.convert_btn = tk.Button(
            self.root,
            text="⚡ CONVERT IMAGE",
            font=("Arial", 14, "bold"),
            bg="#8B0000",
            fg="white",
            state="disabled",
            command=self.convert_image
        )
        self.convert_btn.pack(pady=20)

        # Footer
        footer = tk.Label(
            self.root,
            text="🔐 darkboss1bd | Telegram: @darkvaiadmin | Website: https://serialkey.top/",
            bg="#0e0e0e",
            fg="#555",
            font=("Arial", 9),
            wraplength=700
        )
        footer.pack(side="bottom", pady=20)

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.ico *.tiff *.webp"),
                ("All Files", "*.*")
            ]
        )
        if self.file_path:
            filename = os.path.basename(self.file_path)
            self.file_label.config(text=f"✅ Selected: {filename}", fg="#00ff00")
            self.convert_btn.config(state="normal")
        else:
            self.file_label.config(text="❌ No file selected", fg="#ff0000")

    def convert_image(self):
        if not self.file_path:
            messagebox.showerror("Error", "❌ No image selected!")
            return

        output_format = self.format_var.get()
        save_path = filedialog.asksaveasfilename(
            defaultextension=f".{output_format.lower()}",
            filetypes=[(f"{output_format} File", f"*.{output_format.lower()}")]
        )

        if not save_path:
            return  # Cancelled by user

        try:
            img = Image.open(self.file_path)

            # Handle RGBA to RGB for JPG
            if output_format in ["JPG", "JPEG"] and img.mode in ["RGBA", "LA"]:
                rgb_img = Image.new("RGB", img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                img = rgb_img

            img.save(save_path, format=output_format)
            messagebox.showinfo("Success", f"✅ Image successfully converted to {output_format} and saved!")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Conversion failed: {str(e)}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()