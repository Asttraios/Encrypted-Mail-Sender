# Encrypted Mail Sender 

## Description
Encrypted Mail Sender is a Python application that allows users to send encrypted emails using Google's Gmail API. The encryption is performed using a custom implementation of the Playfair Cipher, ensuring that messages remain secure.

This application seamlessly integrates with a Google account, validates recipient email addresses, and enables users to specify the recipient, subject, and body of their emails.

## Features
✅ Secure Email Sending – Encrypt messages using the Playfair Cipher before sending.<br/>
✅ Google Account Integration – Authenticate via Gmail API and send emails securely.<br/>
✅ Email Validation – Ensure recipient email addresses are correctly formatted.<br/>
✅ Interactive CLI Interface – Simple command-line prompts for user interaction.<br/>
✅ Checking for duplicate letters in Playfair Cipher matrix

## Installation
1. Clone the repository
```
git clone https://github.com/yourusername/encrypted-mail-sender.git
cd encrypted-mail-sender
```

2. Create virtual environment
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install dependencies
```
pip install -r requirements.txt
```

## Set up Google Credentials
To use Gmail API, follow these steps
1. Go to the [Google Cloud Console](https://console.developers.google.com/)
2. Create a new project.
3. Enable the Gmail API for your project.
4. Create OAuth 2.0 credentials and download credentials .json file.
5. Rename the file to credentials.json and place it in the root folder of the project.

## Run the application
```
python main.py

```

## Important
This implementation of Playfair Cipher was created for English language. Both the message and the key must be in English.
* The "j" letter is substituted with "i".
* If number of letters is odd, then "x" letter is added at the end of the word
* Spaces are deleted
* Punctuations are deleted
* Letters are converted to small ones
* The key should be shorter than 25 chars


## So, how does it work?
1. The application checks for existing OAuth2.0 cresentials - token.json. If not found, it prompts the user to log in with their Google account. The new token.json is created with credentials.json - now you don't have to log
in again to use application until token expires.
2. The user provides the recipient's email, subject, and message body. The message is then encrypted using the Playfair Cipher.
3. The application ensures the recipient's email is valid before sending.
4. The encrypted message is sent via the Gmail API.

## What is a Playfair Cipher?

It's a digraph substitution cipher.
* Empty 5x5 matrix is created and then filled with letters of a key. There mustn't be any duplicated letters.
* The rest of empty cells are filled with next letters of the alphabet. There mustn't be any duplicates.
* Letter "j" is replaced with "i" to fit 25 characters
* Now we prepare the message - we divide the sentence into pairs. If number of characters is odd we add "x" letter at the end of a sentence If there's a oair of two same letters . Example: Call me tomorrow -> CA LX LM ET OM OR RO WX
* If two letters in pair are in the same row, we replace those letters with letters to the right. Example: <br/>

```markdown
| A | S | F | C | H |
```

C becomes H, A becomes S<br/>

* If two letters in pair are in the same column, we replace those letters with letters below. Example: <br/>

```markdown
| A | G | Y | M | F |
| Z | W | R | T | U |
| C | X | B | L | P |
| D | S | K | I | O |
```

Here C becomes D and A becomes Z<br/>

* If two letters in pair are in the different row and column, a rectangle is formed and letters on opposite corners are swapped. Example: <br/>

```markdown
| A | G | Y | M | F |
| Z | W | R | T | U |
| L | X | B | C | P |
| D | S | K | I | O |
```

Here C becomes L and A becomes M

* After encrypting every pair we finally have fully encrypted message. Example what it may looks like: ISKYIQEWFQKC (HELXLOWORLDX)



  



