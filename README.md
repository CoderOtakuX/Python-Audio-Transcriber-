# Audio Transcription App

A modern Streamlit application for transcribing audio files using the faster-whisper model. This application provides a user-friendly interface for audio transcription without requiring any API keys.

## Features

- 🎤 Support for multiple audio formats (WAV, MP3, M4A)
- ⚡ Fast transcription using the tiny Whisper model
- 📊 Real-time progress tracking
- 🎯 Processing time and word count metrics
- 💻 Modern and responsive UI

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Deployment

This application can be easily deployed to various platforms:

### Streamlit Cloud (Recommended)
1. Push your code to a GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy the app directly from your repository

### Alternative Deployment Options
- Heroku
- Google Cloud Platform
- AWS
- Azure

## Model Information

The application uses the `tiny` model from faster-whisper, which provides a good balance between speed and accuracy. The model runs entirely on CPU, making it suitable for deployment on most platforms without requiring GPU resources.

## Notes

- The application uses CPU-based inference, which is suitable for most deployment scenarios
- Larger audio files will take longer to process
- For better accuracy, you can modify the model size in the code (options: tiny, base, small, medium, large) 