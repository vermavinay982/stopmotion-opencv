import cv2
import glob
import os

def compile_video(folder="stop_motion_output", output_name="my_animation.mp4", fps=12):
    # Grab and sort all images sequentially
    images = sorted(glob.glob(os.path.join(folder, "frame_*.png")))
    
    if not images:
        print("No frames found to compile.")
        return

    # Read the first image to determine dimensions
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    # 'mp4v' works well universally for MP4 files
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_name, fourcc, fps, (width, height))

    print(f"Compiling {len(images)} frames at {fps} FPS...")
    for image in images:
        video.write(cv2.imread(image))

    video.release()
    print(f"Success! Video saved as {output_name}")

if __name__ == "__main__":
    # 12 frames per second is standard for classic stop-motion look
    compile_video(fps=5)