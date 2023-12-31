# PetitTube Wrapper API

This Flask API provides an endpoint to retrieve PetitTube URL, YouTube title, and views for a video.

## Getting Started

Follow the instructions below to set up and run the API.

### Prerequisites

- Python 3.x
- Install required Python packages using the following command:

  ```bash
  pip install -r requirements.txt
  ```

### Running the API

1. Clone the repository:


2. Navigate to the project directory:

   ```bash
   cd petite-tube-wrapper-api
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

   The API will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. `/`

- **Method:** GET
- **Description:** Display documentation for the PetitTube API.
- **Example:**

  Open your web browser and navigate to `http://127.0.0.1:5000/` to view the documentation.

### 2. `/geturl`

- **Method:** GET
- **Description:** Retrieve PetitTube URL, YouTube title, and views.
- **Example:**

  Make a GET request to `http://127.0.0.1:5000/geturl` to get information about the PetitTube video.

  ```json
  {
    "petittube_url": "https://www.youtube.com/embed/example_video_id",
    "youtube_title": "Example YouTube Title",
    "views": 12345
  }
  ```

## Dependencies

- Flask: Web framework for building the API.
- Requests: HTTP library for making requests to external websites.
- BeautifulSoup4: HTML parsing library for extracting data from HTML content.
- pytube: Library for downloading YouTube videos and extracting information.

## Contributing

Feel free to contribute by opening issues or creating pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/): Web framework for Python.
- [Requests](https://docs.python-requests.org/en/master/): HTTP library for Python.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): HTML parsing library for Python.
- [pytube](https://github.com/pytube/pytube): Library for downloading YouTube videos.
- [PetitTube](https://petittube.com/index.php): Source of least interesting videos on YouTube.
