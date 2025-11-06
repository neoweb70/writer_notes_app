# Writer Notes App

A simple note-taking app built with Python and Kivy, designed to run on Android devices.

## Features

- Create new notes
- Edit existing notes
- Save notes automatically to JSON file
- Delete notes
- Clean, user-friendly interface
- Persistent storage

## Setup

### 1. Install Dependencies

First, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Test on Desktop

You can test the app on your desktop before building for Android:

```bash
python3 main.py
```

### 3. Build for Android

To build an APK for Android, you'll need to install buildozer and its dependencies:

```bash
# Install buildozer dependencies (Debian/Ubuntu)
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install buildozer
pip install buildozer cython

# Build the APK (this will take a while the first time)
cd writer_notes_app
buildozer android debug
```

The APK file will be created in `bin/` directory.

### 4. Install on Android

Transfer the APK file to your Android device and install it. You may need to enable "Install from Unknown Sources" in your device settings.

## Usage

- Click **"+ New Note"** to create a new note
- Enter a title and content for your note
- Click **"Save"** to save your note
- Click on any note in the left panel to view/edit it
- Click **"Delete"** to remove the current note

## Project Structure

```
writer_notes_app/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── buildozer.spec      # Android build configuration
└── README.md           # This file
```

## Notes

- Notes are saved in `notes_data.json` in the app's directory
- The app works on both desktop (for testing) and Android devices
- Building for Android requires significant disk space and may take 15-30 minutes the first time
