# WhatsApp Message Sender

This project automates sending messages via WhatsApp using Python and Selenium. It controls a browser to send messages to specific phone numbers through WhatsApp Web.

## Features

- Automated message sending through WhatsApp Web
- Reads phone numbers from a CSV file
- Loads message content from a text file

## Requirements

- Python 3.x
- The following Python libraries:

  - `selenium`
  - `webdriver-manager`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/qiyascc/whatsapp-marketing-automation.git wma
   cd wma
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Settings**

   - Update the `config.py` file with your `ABS_PATH`, `IMAGE_PATH`, and `CHROME_PROFILE_PATH` settings.
   - Specify the message content in `message.txt`.

4. **Prepare the CSV File**

   Create a `numbers.csv` file with phone numbers. The file should have the following format:

   ```plaintext
   numbers,
   393518285322,
   994518774569,
   ```

## Usage

1. **Launch the Browser and Log into WhatsApp Web**

   Before running the script, you need to manually log into WhatsApp Web in the browser.

2. **Run the Script**

   ```bash
   python main.py
   ```

   The script will read phone numbers from `numbers.csv` and send the message to each number.

## File Structure

- `config.py`: Configuration settings.
- `browser.py`: Browser setup and control.
- `messenger.py`: Message sending functionality.
- `message.txt`: Text file containing the message to be sent.
- `numbers.csv`: CSV file with phone numbers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
