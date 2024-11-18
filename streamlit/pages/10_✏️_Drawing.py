import streamlit as st
# Install with : pip install Pillow
from PIL import Image, ImageDraw, ImageOps

size = st.number_input("size", min_value=300, max_value=1000, value=400, step=50)
im = Image.new('RGBA', (size, size), color="white") 
draw = ImageDraw.Draw(im) 
draw.line((100,200, 150,300), fill="black", width=3)
draw.line((200,100, 300,150), fill="red", width=3)
draw.arc((100,100, 200, 200), 10, 90, fill="blue", width=3)
draw.rectangle((250, 250, 350, 350), fill="magenta", width=5, outline="cyan")
draw.rectangle((350, 350, 450, 450), fill=None, width=5, outline=(0,255,0,255))
draw.text((200, 200), "Hello Pillow", fill="black")
draw.ellipse((0, 0, 100, 100), fill="darkred", width=2)
if( st.checkbox("Flip image ?")):
    im = ImageOps.flip(im)
im.save(R"image.png")
im.close()

st.image(R"image.png", caption='Sunrise by the mountains')
st.slider("Test slider", 0.0, 10.0, step=0.1)


