import os
import glob
import cv2

def main():
    # --- Configuration ---
    output_folder = "stop_motion_output"
    onion_skin_opacity = 0.4  # Transparency of the previous frame (0.0 to 1.0)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Automatically resume numbering based on existing files in the folder
    existing_files = glob.glob(os.path.join(output_folder, "frame_*.png"))
    if existing_files:
        # Extract numbers and find the maximum to avoid overwriting
        indices = [int(f.split("_")[-1].split(".")[0]) for f in existing_files]
        frame_count = max(indices) + 1
    else:
        frame_count = 0

    # Initialize the webcam (0 is usually the default built-in camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("--- Stop Motion Studio Started ---")
    print("Controls:")
    print("  [Spacebar] - Capture Frame")
    print("  [Q]        - Quit Studio")
    print("---------------------------------")

    prev_frame = None
    flash_frames = 0  # Used to create a visual feedback flash when capturing

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Flip horizontally for a mirror effect (optional, remove if not desired)
        frame = cv2.flip(frame, 1)
        
        # Create a copy for displaying (so UI/overlays aren't saved to the final image)
        display_frame = frame.copy()

        # 1. Apply Onion Skinning (Overlay of the past frame)
        if prev_frame is not None:
            # cv2.addWeighted blends two images: (img1, alpha, img2, beta, gamma)
            display_frame = cv2.addWeighted(
                frame, 1.0 - onion_skin_opacity, 
                prev_frame, onion_skin_opacity, 
                0
            )

        # 2. Extra Feature: Visual Capture Flash Feedback
        if flash_frames > 0:
            # Turn display completely white for a brief flash effect
            display_frame = cv2.bitwise_not(display_frame) * 0 + 255
            flash_frames -= 1

        # 3. UI Overlay text (Live Info)
        cv2.putText(display_frame, f"Next Frame Index: {frame_count:04d}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(display_frame, "Space: Capture | Q: Quit", (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        # Show the live feed window
        cv2.imshow("Stop Motion Studio", display_frame)

        # Key handling
        key = cv2.waitKey(1) & 0xFF

        # [Spacebar] to capture frame
        if key == ord(' '):
            filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
            # Save the clean frame (NOT the blended display_frame)
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            
            # Keep this frame as the background for the next shot
            prev_frame = frame.copy()
            frame_count += 1
            flash_frames = 2  # Triggers a 2-frame flash effect

        # [Q] to quit
        elif key == ord('q') or key == 27:  # 27 is the Escape key
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print(f"\nStudio closed. Total frames captured this session: {frame_count}")

if __name__ == "__main__":
    main()