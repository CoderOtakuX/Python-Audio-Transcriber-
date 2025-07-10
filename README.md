# 🎙️ Python Audio Transcriber

A modern Streamlit application that transcribes audio files to text using AI, featuring a clean interface and multiple export options.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🎤 Support for multiple audio formats (WAV, MP3, M4A)
- ⚡ Fast transcription using the tiny Whisper model
- 📊 Real-time progress tracking
- 💾 Export options (TXT, DOCX)
- 🔍 AI-powered text summarization
- 🎯 Processing time and word count metrics
- 💻 Modern and responsive UI

## 🚀 Live Demo

Try the app live at: [Python Audio Transcriber](https://python-audio-transcriber.streamlit.app)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/CoderOtakuX/Python-Audio-Transcriber-.git
cd Python-Audio-Transcriber-
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
- Local: http://localhost:8501
- Network: http://your-network-url:8501

3. Upload an audio file (WAV, MP3, or M4A)
4. Wait for the transcription to complete
5. Download the result or get an AI-powered summary

## 🔧 Technical Details

- **Model**: Uses the `faster-whisper` implementation with the 'tiny' model for optimal speed
- **CPU-Based**: Runs entirely on CPU, no GPU required
- **File Size Limit**: 200MB per file
- **Export Formats**: TXT and DOCX support
- **Summary Integration**: Links to AI text summarizer for additional analysis

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

- GitHub: [@CoderOtakuX](https://github.com/CoderOtakuX)

## 🙏 Acknowledgments

- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) for the efficient transcription model
- [Streamlit](https://streamlit.io/) for the awesome web framework
- [python-docx](https://python-docx.readthedocs.io/) for DOCX export functionality 