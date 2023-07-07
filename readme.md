# PDF to Text Project

This project aims to convert PDF files into text format using OCR (Optical Character Recognition) techniques. It provides a Flask API that accepts PDF files as input and returns the extracted text. The project includes Docker deployment instructions for easy setup and deployment.

## Features

- Converts PDF files into text format
- Supports OCR for images within PDF pages
- Provides a simple and intuitive Flask API
- Docker deployment for easy setup and portability

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
  ```
   git clone https://github.com/your-username/pdf-to-text-project.git
   cd pdf-to-text-project
   ```
2.  Install the required dependencies:
    
    
    ```
    pip install -r requirements.txt
    ``` 
    

## Usage

To use the PDF to Text project, follow these steps:

1.  Run the Flask application:
    
    
    ```
    python app.py
    ``` 
    
2.  Open your web browser and visit `http://localhost:5000` to access the API documentation and test the API endpoints.
    
3.  Use the API to upload a PDF file and receive the extracted text in response.
    

## Docker Deployment

To deploy the project using Docker, follow these steps:

1.  Make sure Docker is installed and running on your system.
    
2.  Build the Docker image:
    
    ```
    docker build -t pdf-to-text
    ``` 
    
3.  Run a Docker container based on the image:
    
    
    ```
    docker run -p 5000:5000 pdf-to-text
	``` 
    
4.  Open your web browser and visit `http://localhost:5000` to access the API documentation and test the API endpoints.
    

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow the guidelines outlined in the 

