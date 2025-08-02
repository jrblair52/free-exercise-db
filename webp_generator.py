from PIL import Image
import os

EXERCISE_DIR = "exercises"  # change as needed

for exercise_name in os.listdir(EXERCISE_DIR):
    exercise_path = os.path.join(EXERCISE_DIR, exercise_name)
    # Check if 0.jpg and 1.jpg exist
    frame0 = os.path.join(exercise_path, "0.jpg")
    frame1 = os.path.join(exercise_path, "1.jpg")
    output_path = os.path.join(exercise_path, "0.webp")

    if not os.path.isdir(exercise_path):
        continue
    if not (os.path.exists(frame0) and os.path.exists(frame1)):
        print(f"Skipping {exercise_name}, missing images")
        continue

    # Optional: Convert to 'P' mode (palette) with adaptive palette
    img0 = Image.open(frame0).convert("RGB")
    img1 = Image.open(frame1).convert("RGB")

    try:
        # Create a forward and reverse loop
        frames = [img0, img1, img0]
         # Save as animated WebP
        img0.save(
            output_path,
            format="WEBP",
            save_all=True,
            append_images=[img1],
            duration=700,  # 500ms per frame = 1s total loop
            loop=0,
            quality=85  # adjust for size vs quality
        )
        #print(f"Saved WEBP for {exercise_name}")
        #os.remove(img0)
        #os.remove(img1)
    except Exception as e:
        print(f"❌ Failed to create GIF for {exercise_name}: {e}")    
