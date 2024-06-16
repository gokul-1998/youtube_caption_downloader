from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to get YouTube video title
def get_video_title(video_id):
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    return yt.title

# Function to fetch the transcript
def fetch_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

# Function to create a PDF from the transcript
def create_pdf(transcript, title):
    filename = f"{title}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    text_start_y = height - 40  # Start Y position for text
    line_height = 14  # Height of each line including spacing

    current_y = text_start_y
    for entry in transcript:
        lines = entry['text'].split('\n')
        for line in lines:
            if current_y < 40:  # Check if there's enough space for another line
                c.showPage()  # If not, create a new page
                c.setFont("Times-Roman", 12)
                current_y = text_start_y  # Reset Y position for new page
            c.drawString(40, current_y, line)  # Draw the line of text
            current_y -= line_height  # Move Y position down for next line

    c.save()
    print(f"PDF saved as {filename}")

# Main function to get the transcript and generate PDF
def main(video_id):
    title = get_video_title(video_id)
    transcript = fetch_transcript(video_id)
    create_pdf(transcript, title)

if __name__ == "__main__":
    video_id = "-C2olg3SfvU"  # Replace with your video ID
    main(video_id)
