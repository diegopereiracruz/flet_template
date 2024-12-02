# Python Flet App Template

This repository provides a **template for building Python applications with Flet**, designed for simplicity, modularity, and customization. The template includes essential features like navigation bar activation, custom footer integration, and system tray icon functionality using Pystray. It's structured to help you start quickly while keeping the code clean and maintainable.  

---

## 🛠️ **Features**

### 1. **Navigation Bar and Footer Options**  
- Enable or disable a **custom navigation bar**.
- Enable or disable a **custom footer**.  

### 2. **System Tray Integration (Pystray)**  
- Add a **system tray icon** with Pystray for running the app in the background.  
- Includes a context menu with customizable options, such as opening the app and exiting.  

### 3. **Page Routing System**  
- Built-in routing system with **separate files for each page**.  
- Simple navigation between different app pages using Flet’s `Router`.  

### 4. **Modular Architecture**  
- The project is divided into **separate files** for each feature and function:
  - Pages folder
  - Navigation bar  
  - Footer  
  - Page router
- Ensures that the code is easy to maintain, scale, and reuse.  

---

## 🚀 **Getting Started**

### 1. **Clone the Repository**
```bash
git clone https://github.com/diegopereiracruz/flet_template
cd flet_template
```

### 2. **Install Dependencies**  
Ensure you have Python 3.8+ installed. Then, run:  
```bash
pip install flet pystray PIL
```

### 3. **Run the App**  
Execute the main script to start the application:  
```bash
python3 main.py
```

---

## 📂 **Project Structure**
Here's an overview of the template structure:  

```
flet_template/
├── app
│   ├── assets             # Medias folder (images, icons, etc)
│   │   └── tray_icon
│   ├── pages              # Pages folder
│   │   └── home.py
│   ├── system
│   │   └── FletRouter.py  # Routing system
│   └── ui
│       ├── footer.py      # Custom footer bar
│       └── navigation.py  # Custom navigation bar
└── main.py                # Entry point of the app
```

---

## 📝 **Customization Guide**

### **Enable/Disable Features**  
In the `main.py` file, you can toggle some features by modifying some variables:  
```python
enable_tray   = False
enable_navbar = False
enable_footer = False
```

### **Add Pages**  
1. Create the page file in `app/pages/`. e.g., `app/pages/settings.py`
2. In `app/system/FletRouter.py` import the page. e.g., `from app.pages.settings import settings_page`
2. Put the path of the page inside `self.routes = {...}`. e.g., `"/settings": settings_page(page),`

---

## 📦 **Dependencies**
- **[Flet](https://flet.dev/):** For building the user interface.  
- **[Pystray](https://pystray.readthedocs.io/):** For system tray functionality.  

---

## 📃 **License**  
This project is licensed under the [MIT License](LICENSE).  

Feel free to use, modify, and distribute this template for your own projects!  

---

## 🙌 **Contributions**  
Contributions are welcome! If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.  

---

## ✨ **Acknowledgments**  
Special thanks to the **Flet** and **Pystray** communities for their excellent tools that power this template.  

--- 

Enjoy coding with Flet! 🚀  
