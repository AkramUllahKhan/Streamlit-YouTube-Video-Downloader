
# Streamlit YouTube Video Downloader

A simple YouTube video downloader built using Python's Streamlit library and `yt-dlp`. This application allows users to download YouTube videos by selecting the desired format.

## Features

- **Download YouTube Videos**: Enter a YouTube URL to get video details and download the video in the desired format.
- **Format Selection**: Choose from available video formats.
- **Thumbnail Display**: View the video's thumbnail before downloading.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/streamlit-youtube-downloader.git
   cd streamlit-youtube-downloader
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

2. **Access the App**

   Open your web browser and navigate to `http://localhost:8501` to use the application.

3. **Download a Video**

   - Paste a YouTube video URL into the input field.
   - Select the desired format from the dropdown menu.
   - Enter a filename and click the "Download Video" button.
   - The video will be downloaded to the `downloads/` directory.

## Requirements

- Python 3.x
- Streamlit
- yt-dlp
- ffmpeg (for handling multiple formats)

## Troubleshooting

- **FFmpeg Error**: Ensure that FFmpeg is installed and properly configured in your system's PATH.
- **Download Issues**: Check the URL and format options. Make sure the video URL is correct and the format is supported.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Made with ❤️ by [Akram Ullah](https://github.com/AkramUllahKhan)
```