# stopmotion-opencv
Want to create stop motion? Can do now without any bulky software package in 5 minutes

# 📸 OpenCV Stop-Motion Studio

A lightweight, punchy **5-minute weekend project** to create stop-motion animations using a standard webcam and Python. Engineered with built-in "onion skinning" to help you perfectly align frames and map out complex robot or object movements.

---

## ✨ Features

* **Smart Onion Skinning:** Blends your live camera feed with the previously captured frame using `cv2.addWeighted`, letting you see exactly how much your object has moved.
* **Visual Capture Flash:** Utilizes `cv2.bitwise_not` to invert pixels for a split second when you hit capture, giving you a satisfying visual confirmation.
* **Smart Overwrite Protection:** Automatically scans your output folder on startup and resumes numbering from your last saved frame.
* **One-Click Video Compiler:** Includes a secondary script to instantly stitch your captured images into a crisp, 12 FPS `.mp4` video.

---

## 🛠️ Prerequisites & Installation

Before running the studio, make sure you have Python installed along with the OpenCV library.

```bash
pip install opencv-python
```

🚀 How It Works
  1. Capture Your Frames
    Run the main script to open up the live Stop-Motion Studio window.

    [Spacebar]: Capture the current frame (saves a clean, un-overlayed image to disk).
    [Q] or [Esc]: Safely close the studio.

  Note: The UI text and the transparent onion skin are only visible on your live monitor; the script saves perfectly clean raw frames to your directory.

  2. Compile into a Video
    Once you've finished moving your robot/object through its sequence, run the compilation script. It automatically sorts your frames sequentially and exports them as a high-quality animation.

   ## 📁 Project Structure
    ├── stop_motion_studio.py   # The live capture & onion-skin engine
    ├── compile_video.py        # Stitches saved frames into an MP4
    └── stop_motion_output/     # Generated automatically (stores your frames)
        ├── frame_0000.png
        ├── frame_0001.png
        └── ...
  
  ## 💡 The "Why" Behind the Code
  This project highlights why foundational domain knowledge matters in the age of AI copilots. Instead of prompting an AI for a generic camera script, knowing that cv2.addWeighted handles pixel blending and cv2.bitwise_not handles color inversion allowed for precise, rapid engineering of the exact features needed for a fluid stop-motion workflow.
