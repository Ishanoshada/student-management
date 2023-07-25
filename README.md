**Student Management System**

This repository contains a Python-based Student Management System, which utilizes JSON for data storage. The system provides a simple command-line interface (CLI) to manage student records, including adding new students, viewing existing students, and performing basic operations on student data.

## Features

- Add a new student with name and age details.
- View the list of all students and their corresponding information.
- Search for a specific student by name.
- Update a student's details, such as name or age.
- Delete a student from the system.

## Requirements

To run the Student Management System, you will need the following:

- Python 3.x installed on your system.
- The system utilizes JSON for data storage, which is a standard Python library and does not require any additional installation.

## Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Ishanoshada/student-management-.git
```

2. Navigate to the project directory:

```bash
cd student-management-
```

3. Run the `student_management.py` script:

```bash
python student_management.py
```

## Usage

Upon running the script, you will be presented with a command-line menu providing options to interact with the student management system. Simply follow the on-screen instructions to perform various operations:

- To add a new student, select the appropriate option and provide the student's name and age when prompted.
- To view all students, choose the corresponding option to see a list of all registered students and their details.
- To search for a specific student by name, select the search option and enter the student's name to find their record.
- To update a student's information, choose the update option, and provide the student's name. You will then be prompted to update the name and/or age.
- To delete a student from the system, select the delete option and enter the name of the student you wish to remove.

## JSON Data Storage

The Student Management System uses JSON to store student records locally. The data is saved in a file named `grade/*.json` within the project directory. Each student record consists of a unique ID, name, and age.

**Note**: This is a basic command-line implementation of a student management system for educational purposes. In a real-world application, you would consider using a database for more robust and scalable data storage.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute to the project or use it as a starting point for your own student management system! Happy coding!
