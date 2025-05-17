# Osint-Phonenumber-tool


An Open Source Intelligence (OSINT) tool for analyzing and verifying phone numbers using public APIs, leaked metadata files, and third-party tools like TruecallerJS.

---

## 🚀 Features

- Validates phone numbers using the [apilayer.net](https://apilayer.com/) API
- Retrieves metadata: country, location, line type, carrier
- Searches country-specific leaked metadata
- Integrates with TruecallerJS for name lookup
- CLI interface with ASCII art banner

---

## 📂 Project Structure

```
.
├── main.py               # Main CLI application
├── requirements.txt      # Python dependencies
├── README.md             # Project instructions
└── *.txt                 # Country data files (downloaded manually)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/bell200/Osint-Phonenumber-tool.git
cd Osint-Phonenumber-tool
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Install TruecallerJS (optional but recommended)

```bash
npm install -g truecallerjs
truecallerjs login
```

---

## 📦 Metadata Files (Manual Download)

Please manually download the following `.txt` files and place them in the **same folder as `main.py`**.

| Country     | File Name | Download Link |
|-------------|-----------|----------------|
| 🇩🇪 Germany  | `de.txt`  | [Download](https://drive.google.com/file/d/1n73pXMhL0piY98sYmnKw55NCJFvc7KPm/view?usp=sharing) |
| 🇮🇱 Israel   | `il.txt`  | [Download]([https://drive.google.com/file/d/1mfth9--EpReULDi9jb8uw1fVg2uVClbP/view?usp=sharing](https://drive.google.com/file/d/1n73pXMhL0piY98sYmnKw55NCJFvc7KPm/view)) |
| 🇫🇷 France   | `fr.txt`  | [Download](https://drive.google.com/file/d/1MIQXedOUyQGgh8BvtsAwXnEg0ZjVAa8L/view?usp=sharing) |
| 🇪🇸 Spain    | `es.txt`  | [Download](https://drive.google.com/file/d/1YZlvfH8PGBKXwrRLL9K9gyI6IBuOSbRM/view?usp=sharing) |
| 🇺🇸 USA      | `us.txt`  | [Download](https://drive.google.com/file/d/1lD8mSILDsvjvCW1YqW552zBt20kMest1/view?usp=sharing) |
| 🇬🇧 UK       | `gb.txt`  | [Download](https://drive.google.com/file/d/1DUChTgNiZFl2RraqgJra9Py1ang66eSb/view?usp=sharing) |
| 🇮🇹 Italy    | `it.txt`  | [Download](https://drive.google.com/file/d/10mHVluuNcUBZu0QcA9sPERttzNAcKEE5/view?usp=sharing) |
| 🇯🇴 Jordan   | `jo.txt`  | [Download](https://drive.google.com/file/d/1D5wg5Z6dAdtabSJsXsrveRecQjeZuWss/view?usp=sharing) |

---

## 🧪 Usage

```bash
python3 main.py
```

You’ll be prompted to enter a number like `491607496006`. The script will validate it, identify its country, and search the relevant metadata file.

---

## ✅ Example

```
Enter your number without +: 491607496006

→ Validating number...
→ Country: Germany
→ Searching de.txt ...
→ Running TruecallerJS ...
```

---

## 📜 License

MIT License

---

## 👤 Author

**Yousef Haiek**  
📍 Heidelberg, Germany  
✉️ yousef55.haik@gmail.com
