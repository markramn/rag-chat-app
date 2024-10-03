# Terminal Chat Interface

A modern, retro-styled chat interface that mimics a classic terminal experience. This project combines the nostalgia of old-school command-line interfaces with the power of modern web technologies and AI-driven conversations.

## Features

- Retro terminal-style user interface
- Dark and light mode toggle
- Real-time chat functionality
- AI-powered responses using OpenAI's GPT model
- Animated text display for a authentic terminal feel
- Responsive design for various screen sizes

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- AI Integration: OpenAI API
- Animation: Anime.js

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)
- An OpenAI API key

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/terminal-chat-interface.git
   cd terminal-chat-interface
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the Flask application:
   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000` to use the Terminal Chat Interface.

## Usage

- Type your message in the input field and press Enter or click the "Send" button to chat with the AI.
- Use the "Reset" button to start a new conversation.
- Toggle between light and dark modes using the "Toggle Mode" button.

## Contributing

Contributions to the Terminal Chat Interface project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you want to contact me, you can reach me at `<your_email@example.com>`.

## Acknowledgements

- OpenAI for providing the GPT model API
- Anime.js for smooth animations
- The Flask team for the lightweight WSGI web application framework