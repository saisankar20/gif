from PIL import Image, ImageDraw, ImageFont
import imageio

# Text and settings
text = "Hi, I'm Sai Sankar Bhuvanapalli Welcome"
font_path = "C:/Windows/Fonts/arial.ttf"  # Path to Arial font
  # Adjust based on your system
font_size = 50
output_gif = "animated_text.gif"

# Image size
width, height = 800, 200
bg_color = (255, 255, 255)  # White background
text_color = (0, 0, 0)  # Black text

# Load font
font = ImageFont.truetype(font_path, font_size)

frames = []
for i in range(len(text) + 1):
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Calculate text position
    text_width, text_height = draw.textsize(text[:i], font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw text
    draw.text((x, y), text[:i], font=font, fill=text_color)

    # Append frame
    frames.append(img)

# Save as GIF
frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=100, loop=0)

print(f"GIF saved as {output_gif}")
