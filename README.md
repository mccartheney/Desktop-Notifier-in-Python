# Desktop-Notifier-in-Python

## Overview

The project utilizes the newsapi API to fetch TechCrunch updates . It then processes the retrieved data to extract relevant information . This information is then used to generate desktop notifications using the DesktopNotifier module, keeping users informed about the latest TechCrunch updates.

## Features (In development)

- Fetch TechCrunch updates from the Hindustan Times RSS feed API.
- Process the retrieved data to extract relevant TechCrunch information.
- Generate desktop notifications using the DesktopNotifier Python module.
- Customize notification settings such as title, message, and duration.

## Technologies Used

- Python
- newsapi feed API
- "DesktopNotifier" Python module

## Usage

1. Clone the repository:
```bash
  git clone https://github.com/MccartheneyMendes/Desktop-Notifier-in-Python
```

2. Navigate to the project directory:
```bash
  cd Desktop-Notifier-in-Python
```

3. Install the required Python packages:
```bash
  pip install -r requirements.txt
```

4. Add in .env file your api key from [newsapi](https://newsapi.org/)
```bash
    API_KEY = api_key
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Hindustan Times for providing the RSS feed API.
- Developers of the DesktopNotifier Python module for enabling desktop notifications.
