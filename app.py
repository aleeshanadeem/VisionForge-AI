import streamlit as st
import io

# --------------------------------------------------
# SAFE IMPORT
# --------------------------------------------------
from generator import generate_image

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="VisionForge AI",
    page_icon="🎨",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(30, 64, 175, 0.20), transparent 35%),
            radial-gradient(circle at bottom right, rgba(124, 58, 237, 0.18), transparent 35%),
            #07111f;
        color: white;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #b8c4d6;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .profile-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(96, 165, 250, 0.25);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-bottom: 20px;
    }

    .profile-name {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin-top: 10px;
    }

    .profile-code {
        font-size: 1.1rem;
        color: #60a5fa;
        font-weight: 600;
    }

    .profile-role {
        margin-top: 12px;
        color: #cbd5e1;
        font-size: 0.95rem;
    }

    .glass-card {
        background: rgba(15, 23, 42, 0.70);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.25);
    }

    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #e2e8f0;
        margin-bottom: 12px;
    }

    .feature {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
        color: #cbd5e1;
    }

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 40px;
        font-size: 0.9rem;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* Style Streamlit buttons */
    .stButton > button {
        background: linear-gradient(90deg, #1e40af, #7c3aed);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #2563eb, #8b5cf6);
        transform: translateY(-1px);
    }

    .stTextArea textarea {
        background: rgba(30, 41, 59, 0.7) !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(148, 163, 184, 0.25) !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(30, 41, 59, 0.7) !important;
        color: white !important;
        border-radius: 12px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown('<div class="main-title">🎨 VisionForge AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Turn your imagination into stunning images using Generative AI.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SESSION STATE for prompt
# --------------------------------------------------
if "prompt_input" not in st.session_state:
    st.session_state.prompt_input = ""
if "generated_image" not in st.session_state:
    st.session_state.generated_image = None
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = ""


# --------------------------------------------------
# THREE COLUMN LAYOUT
# --------------------------------------------------
left_col, center_col, right_col = st.columns([1.1, 4.0, 1.4], gap="medium")


# ==================================================
# LEFT SIDEBAR / PROFILE
# ==================================================
with left_col:
    st.markdown(
        """
        <div class="profile-card">
            <div style="font-size: 3rem;">👩🏻‍💻</div>
            <div class="profile-name">Aleesha Nadeem</div>
            <div class="profile-code">2(AN)K</div>
            <div class="profile-role">
                AI & ML Engineer<br>
                Gen AI Enthusiast
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(
        """
        <br>
        <div style="text-align:center; color:#64748b; font-style:italic;">
            "Dream it.<br>Generate it."
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# CENTER — IMAGE GENERATOR
# ==================================================
with center_col:
    st.markdown(
        """
        <div class="glass-card">
            <div class="section-title">✨ Describe the image you want</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    prompt = st.text_area(
        "Image Prompt",
        value=st.session_state.prompt_input,
        placeholder="Example: A futuristic city on Mars at sunset, cinematic lighting, highly detailed...",
        height=160,
        key="prompt_area"
    )

    style = st.selectbox(
        "🎨 Choose image style",
        ["Photorealistic", "Cinematic", "Digital Art", "Anime", "3D Render", "Watercolor"],
        key="style_select"
    )

    generate_button = st.button("✨ Generate Image", use_container_width=True, key="gen_btn")

    if generate_button:
        if not prompt.strip():
            st.warning("⚠️ Please enter a prompt first.")
        else:
            final_prompt = f"""
Create an image based on this request:

{prompt}

Style:
{style}

Make the image visually detailed, coherent and high quality.
"""
            with st.spinner("🎨 Creating your image..."):
                try:
                    image = generate_image(final_prompt)

                    # Save to session state
                    st.session_state.generated_image = image
                    st.session_state.last_prompt = prompt

                    st.success("✅ Image generated successfully!")

                except Exception as e:
                    st.error(f"❌ Something went wrong: {e}")

    # ---- Display image outside the button block ----
    if st.session_state.generated_image is not None:
        st.image(
            st.session_state.generated_image,
            caption=f"Generated by VisionForge AI — Prompt: {st.session_state.last_prompt[:80]}",
            use_container_width=True
        )

        img_bytes = io.BytesIO()
        st.session_state.generated_image.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        st.download_button(
            label="⬇️ Download Image",
            data=img_bytes.getvalue(),
            file_name="visionforge_image.png",
            mime="image/png",
            use_container_width=True,
            key="download_btn"
        )




# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        VisionForge AI • Built with Python, Streamlit & Generative AI
        <br>
        © 2026 Aleesha Nadeem
    </div>
    """,
    unsafe_allow_html=True
)
