# Hand Tracking Project

This project uses computer vision techniques to track hand movements and count the number of fingers being held up.

## Features

- Real-time hand tracking
- Finger counting (0-5)
- FPS display

## Requirements
 ```
pip install -r requirements.txt

 ```


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/hand-tracking-project.git
   ```


## Usage

Run the main script:

```
python hand_tracking.py
```

- Press 'q' to quit the application.

## How it works

1. The script captures video from your default camera.
2. It uses the HandDetector from CVZone to detect hands in each frame.
3. The program then analyzes the positions of key landmarks on the hand to determine which fingers are extended.
4. A count of extended fingers is displayed on the screen.
5. The current FPS (Frames Per Second) is also shown.

## Demo

![Hand Tracking Demo]()

In this demo, you can see the hand tracking in action. The green rectangle shows the finger count, and the FPS is displayed in the top-left corner.

