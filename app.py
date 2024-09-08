import streamlit as st
from yt_dlp import YoutubeDL
import os

# Set up the download directory
directory = 'downloads/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Streamlit page configuration
st.set_page_config(page_title="YouTube Video Downloader", page_icon="🎥", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    .stImage {
        border-radius: 10px;
    }
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
    }
    .stExpanderHeader {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to fetch video information using yt-dlp
def get_info(url):
    try:
        ydl_opts = {'quiet': True, 'no_warnings': True}
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_details = {
                "title": info_dict.get('title', 'No title available'),
                "thumbnail": info_dict.get('thumbnail', None),
                "duration": info_dict.get('duration', 0),
                "formats": info_dict.get('formats', [])
            }
            return video_details
    except Exception as e:
        st.error(f"Error retrieving video information: {e}")
        return None

# User interface
st.header("YouTube Video Downloader 🎥")
url = st.text_input("Paste YouTube URL here 👇", placeholder='https://www.youtube.com/')
if url:
    v_info = get_info(url)
    if v_info:
        # Layout with columns
        col1, col2 = st.columns([1, 2])
        
        # Show thumbnail in the first column
        with col1:
            if v_info['thumbnail']:
                st.image(v_info['thumbnail'], caption="Video Thumbnail", use_column_width=True)

        # Show video details in the second column
        with col2:
            st.subheader("Video Details ⚙️")
            st.write(f"**Title:** {v_info['title']}")
            st.write(f"**Duration:** {v_info['duration']} sec")

            # Expander for format selection
            with st.expander("Choose Format", expanded=True):
                format_options = [
                    f"{fmt['format_id']} | {fmt['format_note']} | {fmt['ext']} | {fmt.get('filesize', 'unknown size')} | {fmt.get('fps', 'unknown fps')}"
                    for fmt in v_info['formats']
                    if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none'  # Filters out video-only or audio-only formats
                ]
                format_choice = st.selectbox('Select Format', format_options)
                format_id = format_choice.split(" | ")[0]  # Extract format ID from selected option

            # Input for the file name
            file_name = st.text_input('Save as', placeholder=v_info['title'])
            if not file_name.endswith(".mp4"):
                file_name += ".mp4"

            # Download button with centered layout
            if st.button("Download Video"):
                with st.spinner('Downloading...'):
                    try:
                        ydl_opts = {
                            'format': format_id,  # Use the selected format ID
                            'outtmpl': os.path.join(directory, file_name),
                            'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}]  # Ensure it's saved as mp4
                        }
                        with YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])
                        st.success('Download Complete!', icon="✅")
                    except Exception as e:
                        st.error(f"Error during download: {e}", icon="🚨")

st.markdown("""
    <footer style="
        text-align: center; 
        padding: 20px; 
        font-size: 14px; 
        color: #555; 
        background-color: #f9f9f9; 
        border-top: 1px solid #ddd; 
        margin-top: 30px; 
        position: relative; 
        bottom: 0; 
        width: 100%;
        ">
        <p style="margin: 0;">Made with ❤️ by <strong>Akram Ullah</strong></p>
        <p style="margin: 5px 0 0; font-size: 12px; color: #777;">For any inquiries, contact me at <a href="mailto:akramullahkhan05@gmail.com" style="color: #007bff;">akramullahkhan05@gmail.com</a></p>
    </footer>
    """, unsafe_allow_html=True)

