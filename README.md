# Face Recognition Attendance System

This repository contains a face recognition-based attendance system developed during my Machine Learning Internship at Diffuse AI. The system automates attendance tracking using face recognition technology, with logs stored in datewise CSV files. It also includes a user-friendly GUI.

## Demo Images
1. **Home Page**:
   ![Home Page](path/to/Home%20Page.png)

2. **Login Page**:
   ![Login Page](path/to/Login%20Page%20for%20Admin%20page.png)

3. **Admin Page**:
   ![Admin Page](path/to/Admin%20Page.png)

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Contributing](#contributing)
7. [Guidelines](#guidelines)
8. [License](#license)
9. [Contact](#contact)
10. [Demo Images](#demo-images)

## Technologies
- **HTML**
- **CSS**
- **JavaScript**
- **Bootstrap**
- **Python**
- **Flask**

## Features
- Face recognition for attendance
- Automated attendance logging
- Datewise CSV storage
- User-friendly GUI with responsive design

## Requirements
The following Python packages are required:
- face_recognition 1.3.0
- dlib 19.22.1
- cmake 3.20.0
- Flask 2.3.2
- OpenCV 4.7.0
- NumPy 1.25.2
- Pandas 2.0.3
- scikit-learn 1.3.0
- joblib 1.3.2
- Werkzeug 2.3.4
- Jinja2 3.1.2

## Installation
To set up the project locally, follow these steps:
```bash
git clone https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec.git
cd REPO1.ANAND.Face_Dec_Rec
pip install face_recognition==1.3.0 dlib==19.22.1 cmake==3.20.0 Flask==2.3.2 OpenCV==4.7.0 NumPy==1.25.2 Pandas==2.0.3 scikit-learn==1.3.0 joblib==1.3.2 Werkzeug==2.3.4 Jinja2==3.1.2
```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Access the application via your local browser.

## Results
- Attendance logs are stored in CSV files named by date.
- The GUI displays real-time attendance tracking and logs.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Submit a pull request.

## Guidelines
If you encounter errors or issues running the project in VS Code, consider using a virtual environment:
**Note:** Before all of that, put the project folder in another folder and create a virtual environment in that folder.
1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Install Dependencies**:
   After activating the virtual environment, install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

This will help isolate dependencies and ensure compatibility across different environments.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
If you have any questions or would like to collaborate, feel free to reach out:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Face%20Recognition%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Face%20Recognition%20Projects%20you%20developed%20during%20your%20Machine%20Learning%20Internship%20at%20Diffuse%20AI.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])
- **LinkedIn**: [Anand's LinkedIn Profile](https://www.linkedin.com/in/anands37/)
