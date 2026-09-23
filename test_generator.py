from generator import generate_image


prompt = """
A futuristic city on Mars at sunset,
with flying vehicles, glowing buildings,
cinematic lighting, highly detailed,
realistic science fiction environment.
"""


print("Generating image...")

image = generate_image(prompt)

image.save("test_output.png")

print("Image generated successfully!")
print("Saved as: test_output.png")