# MedVisioSphere - Secure Medical STL Visualization Web Application

MedVisioSphere is an advanced and secure web application tailored exclusively for medical students. It seamlessly combines the power of Django and Three.js to deliver an immersive and educational experience, allowing students to visualize real medical STL images. This application ensures the utmost security, preventing direct file access while providing an intuitive interface for exploring and learning from these intricate 3D models. MedVisioSphere utilizes SQLite for efficient data management, safeguarding sensitive medical information.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Secure Access:** MedVisioSphere restricts access to authorized medical students only, ensuring the privacy and integrity of sensitive medical data.
- **Immersive Visualization:** The integration of Three.js enables interactive and detailed rendering of medical STL images, offering a lifelike and informative visualization experience.
- **Efficient Data Handling:** The application utilizes SQLite, a lightweight and efficient database system, for seamless storage and retrieval of relevant data.
- **User-Centric Design:** MedVisioSphere boasts a user-friendly interface, designed to facilitate ease of navigation and interaction, making it accessible to users with varying technical backgrounds.
- **Cross-Platform Compatibility:** Users can access MedVisioSphere from any modern web browser, making it adaptable to a range of devices.

## Technologies Used

- Django
- Three.js
- SQLite

## Getting Started

To set up and run the MedVisioSphere application, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/MedVisioSphere.git
    cd MedVisioSphere
    ```

2. **Setup Virtual Environment:**
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    python manage.py runserver
    ```

5. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8000`.

## Usage

- Register a new user or log in with existing credentials.
- Upload and manage your encrypted medical STL content.
- Explore detailed 3D visualizations using the integrated Three.js renderer.
- Use the intuitive interface to navigate and interact with the medical images.
- Ensure to follow best practices for security and data privacy.

## Contributing

We welcome contributions to enhance MedVisioSphere. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to your fork: `git push origin feature-name`.
5. Create a pull request with detailed explanations of changes.

## License

MedVisioSphere is released under the MIT License. For details, see the [LICENSE](LICENSE) file.

## Contact

For inquiries or feedback, please contact us at naveenad260@gmail.com.
