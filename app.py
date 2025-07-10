import streamlit as st
import tempfile
import os
from faster_whisper import WhisperModel
import time
import docx

# Set page configuration
st.set_page_config(
    page_title="Audio Transcription App",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS for modern UI
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .upload-box {
        border: 2px dashed #2196F3;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
        background-color: rgba(33, 150, 243, 0.05);
        transition: all 0.3s ease;
    }
    .upload-box:hover {
        border-color: #1976D2;
        background-color: rgba(33, 150, 243, 0.1);
    }
    .status-box {
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        background-color: #f8f9fa;
        border-left: 5px solid #2196F3;
    }
    .transcription-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    .button-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #2196F3 !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover {
        background-color: #1976D2 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
    }
    .header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }
    .stProgress > div > div {
        background-color: #2196F3 !important;
    }
    .summary-link {
        color: #2196F3;
        text-decoration: none;
        font-weight: 500;
        cursor: pointer;
    }
    .summary-link:hover {
        color: #1976D2;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

def initialize_model():
    """Initialize the Whisper model with tiny configuration"""
    model_size = "tiny"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    return model

def transcribe_audio(model, audio_path):
    """Transcribe audio file using the Whisper model"""
    segments, _ = model.transcribe(audio_path, beam_size=1)
    return " ".join([segment.text for segment in segments])

def save_as_docx(text, filename):
    """Save text as a Word document"""
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(filename)
    return filename

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return data

def main():
    # Header
    st.markdown("<div class='header'>", unsafe_allow_html=True)
    st.title("🎙️ Audio Transcription App")
    st.markdown("Transform your audio into text with AI-powered transcription")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Initialize session state for model
    if 'model' not in st.session_state:
        with st.spinner("Loading model... Please wait."):
            st.session_state.model = initialize_model()
        st.success("Model loaded successfully!")

    # Create two columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # File upload section
        st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload your audio file (WAV, MP3, M4A)",
            type=['wav', 'mp3', 'm4a']
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        # Instructions card
        st.markdown("""
        ### 📖 Quick Guide
        1. Upload your audio file
        2. Wait for transcription
        3. Download or summarize results
        """)

    if uploaded_file is not None:
        # Create a progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            audio_path = tmp_file.name

        try:
            # Update status
            status_text.markdown("<div class='status-box'>Starting transcription...</div>", unsafe_allow_html=True)
            progress_bar.progress(25)
            
            # Transcribe audio
            start_time = time.time()
            transcription = transcribe_audio(st.session_state.model, audio_path)
            end_time = time.time()
            
            # Update progress
            progress_bar.progress(100)
            status_text.markdown("<div class='status-box'>Transcription completed!</div>", unsafe_allow_html=True)
            
            # Save transcription to files
            with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as txt_file:
                txt_file.write(transcription)
                txt_path = txt_file.name

            docx_path = os.path.splitext(txt_path)[0] + '.docx'
            save_as_docx(transcription, docx_path)
            
            # Display metrics and action buttons first
            st.markdown("### ⚡ Processing Information")
            metrics_col1, metrics_col2 = st.columns(2)
            with metrics_col1:
                st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                st.metric("⏱️ Processing Time", f"{(end_time - start_time):.2f} seconds")
                st.markdown("</div>", unsafe_allow_html=True)
            with metrics_col2:
                st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                st.metric("📊 Word Count", f"{len(transcription.split())} words")
                st.markdown("</div>", unsafe_allow_html=True)

            # Action buttons
            st.markdown("### 🔄 Actions")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                txt_data = get_binary_file_downloader_html(txt_path, 'text')
                st.download_button(
                    label="📄 Download as TXT",
                    data=txt_data,
                    file_name="transcription.txt",
                    mime="text/plain",
                    key='txt_download'
                )
            
            with col2:
                docx_data = get_binary_file_downloader_html(docx_path, 'docx')
                st.download_button(
                    label="📑 Download as DOCX",
                    data=docx_data,
                    file_name="transcription.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key='docx_download'
                )
            
            with col3:
                st.markdown(
                    f'<a href="https://v0-javascript-text-summarizer.vercel.app/" target="_blank" class="summary-link">🔍 Click here to get summary</a>',
                    unsafe_allow_html=True
                )
            
            # Display transcription results
            st.markdown("### 📝 Transcription Results")
            st.markdown("<div class='transcription-box'>", unsafe_allow_html=True)
            st.write(transcription)
            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred during transcription: {str(e)}")
        
        finally:
            # Clean up temporary files
            os.unlink(audio_path)
            if 'txt_path' in locals():
                os.unlink(txt_path)
            if 'docx_path' in locals():
                os.unlink(docx_path)

    # Add instructions in the sidebar
    with st.sidebar:
        st.markdown("### 🎯 Features")
        st.markdown("""
        - Multiple audio format support
        - Fast AI-powered transcription
        - Download as TXT or DOCX
        - Get AI-powered summary
        - Real-time progress tracking
        
        **Supported Formats:**
        - WAV
        - MP3
        - M4A
        
        **Model Info:**
        Using the tiny Whisper model for fast processing.
        """)

if __name__ == "__main__":
    main() 