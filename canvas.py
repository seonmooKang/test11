import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Drawing App")

st.sidebar.header("Configuration")
stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color", "#000000")
bg_color = st.sidebar.color_picker("Background color", "#FFFFFF")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

# Set up the canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color if not bg_image else None,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=True,
    height=500,
    width=700,
    drawing_mode="freedraw",
    key="canvas",
)

# Display the image data after drawing
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="Your Drawing")
