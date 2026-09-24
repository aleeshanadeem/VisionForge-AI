# 🎨 VisionForge AI

### Turn Your Imagination into Images with Generative AI

![Uploading ChatGPT Image Sep 24, 2026, 09_45_06 AM.png…]()


**VisionForge AI** is an AI-powered text-to-image application that transforms natural language prompts into visually creative images.

The application provides a simple and modern interface where users can describe an image, choose a visual style, generate the image, and download the final result.

---

## ✨ Features

* 🖼️ **Text-to-Image Generation**
* 🎨 **Multiple Image Styles**

  * Photorealistic
  * Cinematic
  * Digital Art
  * Anime
  * 3D Render
  * Watercolor
* ⚡ **Simple and Interactive UI**
* 🌙 **Modern Dark-Themed Dashboard**
* ⬇️ **Download Generated Images**
* 🤖 **Generative AI Integration**
* 💻 **Built with Python and Streamlit**

---

## 🖥️ Interface

The application includes:

* **Aleesha Nadeem — 2(AN)K** profile section
* AI & ML Engineer / Gen AI branding
* Image prompt input
* Style selector
* Image generation button
* Generated image preview
* Download option
* Quick prompt section
* Feature overview

---

## 🛠️ Tech Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Core programming language |
| Streamlit        | Web application interface |
| Generative AI    | Image generation          |
| Hugging Face API | AI model/API integration  |
| PIL              | Image processing          |

---

## 📂 Project Structure

```text
VisionForge-AI/
│
├── app.py
├── generator.py
├── requirements.txt
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/VisionForge-AI.git
```

### 2. Move into the project directory

```bash
cd VisionForge-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

VisionForge AI requires an API token for the image generation provider.

Create an environment file:

```text
.env
```

Add your token:

```env
HF_TOKEN=your_token_here
```

> **Important:** Never upload your API token or `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

## 🚀 Run the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Streamlit will open the application in your browser.

---

## 🎯 How It Works

The basic workflow is:

```text
User Prompt
     ↓
Style Selection
     ↓
Final Prompt Creation
     ↓
Generative AI Model
     ↓
Image Generation
     ↓
Image Preview
     ↓
Download Image
```

---

## 💡 Example Prompt

Try a prompt like:

```text
A futuristic city on Mars at sunset,
with glowing skyscrapers, flying vehicles,
cinematic lighting and highly detailed architecture.
```

Then select:

```text
Cinematic
```

and click:

**✨ Generate Image**

---

## 🔮 Future Improvements

Planned features include:

* 📐 Aspect ratio selection
* 🖼️ Multiple image generation
* 🕘 Generation history
* ⚡ Quick prompt buttons
* 🧩 Advanced prompt controls
* 🎨 More artistic styles
* 📥 Improved download options
* 🌐 Deployment for public access

---

## 👩‍💻 About the Developer

**Aleesha Nadeem (2(AN)K)**

Aspiring **AI & ML Engineer** with an interest in:

* Generative AI
* Machine Learning
* Data Science
* Deep Learning
* AI-powered applications

VisionForge AI is a learning and development project focused on exploring how Generative AI can be integrated into practical applications.

---

## 📌 Project Status

🚧 **Active Development**

VisionForge AI is currently being improved with new features, better UI, and additional generative AI capabilities.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---

### Built with 💙 using Python, Streamlit & Generative AI

**VisionForge AI — Imagine. Create. Generate.**
