# Username-Wordlist-Generator
This Python script automates the generation of various username variations using the crunch command. The script is designed to help with tasks such as wordlist generation for password cracking, specifically tailored to usernames. It processes multiple usernames in various formats and combines the results into final wordlist files.

Features

    Multiple Username Input: Accepts multiple usernames separated by commas and processes each individually.
    Username Variations: Supports generating wordlists for usernames in different formats, including:
        Lowercase
        Capitalized (First letter uppercase)
        Uppercase
        Last letter uppercase
        Both first and last letters uppercase
    Custom Options: Allows the user to choose which variations to generate or to generate all variations at once.
    Automated File Management: Concatenates intermediate files into a final wordlist file for each username and cleans up temporary files.
    Word Count and File Path Display: Provides a word count for the final wordlist and displays the full path to the generated file.
    User Interaction: Asks the user whether to remove previous final files and cleans up any cached files from previous runs.

How to Use

    1. Clone this repository to your local machine.
    2. Ensure that crunch is installed on your system (available on Kali Linux and other platforms).
    3. cd Username-Wordlist-Generator
    4. chmod +x username_wordlist_generator.py
    5. python3 username_wordlist_generator.py
    6. Follow the prompts to input usernames and select the desired options.

Example

 Enter the usernames separated by commas (e.g., user1,user2,user3): user1,user2
 Select Options (e.g., 1,2,3): 1,2,4

 This will generate wordlists for user1 and user2 in lowercase, capitalized, and with the last letter capitalized, then concatenate them into final files.

 Requirements

    Python 3.x
    crunch command-line tool
