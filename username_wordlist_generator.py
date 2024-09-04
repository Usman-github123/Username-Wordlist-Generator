#!/usr/bin/env python3

import os
import subprocess
import multiprocessing

# Function to generate crunch commands
def generate_crunch_commands(username, username_length):
    commands = [
        f"crunch {username_length + 1} {username_length + 1} -t {username}% -o 1Auser4d #-----------------------------> 2%",
        f"crunch {username_length + 2} {username_length + 2} -t {username}%% -o 1Buser4d #-----------------------------> 6%",
        f"crunch {username_length + 3} {username_length + 3} -t {username}%%% -o 1Cuser4d #-----------------------------> 10%",
        f"crunch {username_length + 4} {username_length + 4} -t {username}%%%% -o 1Duser4d #-----------------------------> 15%",
        
        f"crunch {username_length + 5} {username_length + 5} -t {username}^%%%% -o 2Auser_Sym4d #-----------------------------> 17%",
        f"crunch {username_length + 4} {username_length + 4} -t {username}^%%% -o 2Buser_Sym4d #-----------------------------> 20%",
        f"crunch {username_length + 3} {username_length + 3} -t {username}^%% -o 2Cuser_Sym4d #-----------------------------> 25%",
        f"crunch {username_length + 2} {username_length + 2} -t {username}^% -o 2Duser_Sym4d #-----------------------------> 27%",
        
        f"crunch {username_length + 5} {username_length + 5} -t ^{username}%%%% -o 3ASym_user_4d #-----------------------------> 30%",
        f"crunch {username_length + 4} {username_length + 4} -t ^{username}%%% -o 3BSym_user_4d #-----------------------------> 32%",
        f"crunch {username_length + 3} {username_length + 3} -t ^{username}%% -o 3CSym_user_4d #-----------------------------> 35% ",
        f"crunch {username_length + 2} {username_length + 2} -t ^{username}% -o 3DSym_user_4d #-----------------------------> 37%",
        
        f"crunch {username_length + 4} {username_length + 4} -t {username}%%%% -o 4Auser4d #-----------------------------> 40%",
        f"crunch {username_length + 3} {username_length + 3} -t {username}%%% -o 4Buser4d #-----------------------------> 45%",
        f"crunch {username_length + 2} {username_length + 2} -t {username}%% -o 4Cuser4d #-----------------------------> 48%",
        f"crunch {username_length + 1} {username_length + 1} -t {username}% -o 4Duser4d #-----------------------------> 50%",
        
        f"crunch {username_length + 5} {username_length + 5} -t {username}^%%%% -o 5Auser_Sym4d #-----------------------------> 55%",
        f"crunch {username_length + 4} {username_length + 4} -t {username}^%%% -o 5Buser_Sym4d #-----------------------------> 60%",
        f"crunch {username_length + 3} {username_length + 3} -t {username}^%% -o 5Cuser_Sym4d #-----------------------------> 65%",
        f"crunch {username_length + 2} {username_length + 2} -t {username}^% -o 5Duser_Sym4d #-----------------------------> 70%",
        
        f"crunch {username_length + 5} {username_length + 5} -t ^{username}%%%% -o 6ASym_user_4d #-----------------------------> 75%",
        f"crunch {username_length + 4} {username_length + 4} -t ^{username}%%% -o 6BSym_user_4d #-----------------------------> 80%",
        f"crunch {username_length + 3} {username_length + 3} -t ^{username}%% -o 6CSym_user_4d #-----------------------------> 83%",
        f"crunch {username_length + 2} {username_length + 2} -t ^{username}% -o 6DSym_user_4d #-----------------------------> 85%",
        
        f"crunch {username_length + 6} {username_length + 6} -t ^{username}^%%%% -o 7ASym_user_Sym_4d #-----------------------------> 87%",
        f"crunch {username_length + 5} {username_length + 5} -t ^{username}^%%% -o 7BSym_user_Sym_4d #-----------------------------> 93%",
        f"crunch {username_length + 4} {username_length + 4} -t ^{username}^%% -o 7CSym_user_Sym_4d #-----------------------------> 95%",
        f"crunch {username_length + 3} {username_length + 3} -t ^{username}^% -o 7DSym_user_Sym_4d #-----------------------------> 99%",
        
        f"#crunch {username_length + 9} {username_length + 9} -t {username}^%%%%%%%% -o 8DSym_user_Sym_4d #-----------------------------> 100%"
    ]
    return commands

# Function to execute commands
def execute_commands(commands):
    for command in commands:
        print(f"Running command: {command}")
        subprocess.run(command, shell=True, check=True)

# Function to concatenate files
def concatenate_files(username):
    files = [
        "1Auser4d", "1Buser4d", "1Cuser4d", "1Duser4d",
        "2Auser_Sym4d", "2Buser_Sym4d", "2Cuser_Sym4d", "2Duser_Sym4d",
        "3ASym_user_4d", "3BSym_user_4d", "3CSym_user_4d", "3DSym_user_4d",
        "4Auser4d", "4Buser4d", "4Cuser4d", "4Duser4d",
        "5Auser_Sym4d", "5Buser_Sym4d", "5Cuser_Sym4d", "5Duser_Sym4d",
        "6ASym_user_4d", "6BSym_user_4d", "6CSym_user_4d",  "6DSym_user_4d", "7ASym_user_Sym_4d", "7BSym_user_Sym_4d", "7CSym_user_Sym_4d", "7DSym_user_Sym_4d", "8DSym_user_Sym_4d"
    ]
    final_file = f"_{username}.txt"
    try:
        with open(final_file, "wb") as outfile:
            for fname in files:
                with open(fname, "rb") as infile:
                    outfile.write(infile.read())
        print(f"Concatenated all files into {final_file}")
    except Exception as e:
        print(f"File Read Error: {e}")

# Function to remove individual files
def remove_files():
    files = [
        "1Auser4d", "1Buser4d", "1Cuser4d", "1Duser4d",
        "2Auser_Sym4d", "2Buser_Sym4d", "2Cuser_Sym4d", "2Duser_Sym4d",
        "3ASym_user_4d", "3BSym_user_4d", "3CSym_user_4d", "3DSym_user_4d",
        "4Auser4d", "4Buser4d", "4Cuser4d", "4Duser4d",
        "5Auser_Sym4d", "5Buser_Sym4d", "5Cuser_Sym4d", "5Duser_Sym4d",
        "6ASym_user_4d", "6BSym_user_4d", "6CSym_user_4d", "6DSym_user_4d", "7ASym_user_Sym_4d", "7BSym_user_Sym_4d", "7CSym_user_Sym_4d", "7DSym_user_Sym_4d", "8DSym_user_Sym_4d"
    ]
    try:
        for fname in files:
            if os.path.exists(fname):
                os.remove(fname)
                print(f"Removed file: {fname}")
            else:
                print(f"File {fname} does not exist. Skipping to Remove.")
    except Exception as e:
        print(f"File Remove Error: {e}")

# Function to concatenate both username files into one final file
def concatenate_final_files(username):
    final_files = [
    f"_{username.lower()}.txt", 
    f"_{username.capitalize()}.txt", 
    f"_{username.upper()}.txt" ,
    f"_{username[:-1] + username[-1].upper()}.txt",
     f"_{username[0].upper() + username[1:-1] + username[-1].upper()}.txt"
    ]
    final_done_file = f"Final_{username}.txt"
    
    try:
        with open(final_done_file, "wb") as outfile:
            for fname in final_files:
                if os.path.exists(fname):
                    with open(fname, "rb") as infile:
                        outfile.write(infile.read())
                else:
                    print(f"File {fname} does not exist. Skipping.")
        print(f"Concatenated both username files into {final_done_file}")
    except Exception as e:
        print(f"Error concatenating final files: {e}")

# Function to process username with the last letter capitalized
def process_username_last_letter_capital(username):
    if len(username) > 1:
        username_variation = username[:-1] + username[-1].upper()
    else:
        username_variation = username.upper()
    
    process_username_variation(username_variation)
    
# Function to process username with both first and last letter capitalized
def process_username_first_last_letter_capital(username):
    if len(username) > 1:
        username_variation = username[0].upper() + username[1:-1] + username[-1].upper()
    else:
        username_variation = username.upper()
    
    process_username_variation(username_variation)

# Function to process username variations
def process_username_variation(username):
    username_length = len(username)
    commands = generate_crunch_commands(username, username_length)
    execute_commands(commands)
    concatenate_files(username)
    remove_files()

#Main Script
def main():
    try:
        subprocess.run("rm [0-9]*  ", shell=True, check=True)
    except:
        print("\n")
        pass
    
    remove = input("Do you want to remove all Final_* Files 'y' or 'n':").strip().lower()
    if remove in ['y', 'yes']:
        try:
            subprocess.run("rm Final_* ", shell=True, check=True)
            print("Removed Successfull.")
        except:
            print("Final_ File didn't Exist!")
    elif remove in ['n', 'no']:
        pass
    else:
        print("Removed Error. Please Press y or n ")

    print("------------------------------------------------------------------")
    
    usernames = input("Enter the usernames separated by commas (e.g., user1,user2,user3): ").split(',')
    
    print("\n1. Lowercase")
    print("2. First Letter Capital")
    print("3. Uppercase")
    print("4. Last Letter Capital")
    print("5. First and Last Letter Capitalized")
    print("6. All")
    print("------------------------------------------------------------------")
    user_input = input("Select Options (e.g., 1,2,3): ")
    options = user_input.split(',')

    for username in usernames:
        username = username.strip()
        
        for option in options:
            option = option.strip()
            if option == "1":
                process_username_variation(username.lower())
            elif option == "2":
                process_username_variation(username.capitalize())
            elif option == "3":
                process_username_variation(username.upper())
            elif option == "4":
                process_username_last_letter_capital(username)
            elif option == "5":
                process_username_first_last_letter_capital(username)
            elif option == "6":
                process_username_variation(username.lower())
                process_username_variation(username.capitalize())
                process_username_variation(username.upper())
                process_username_last_letter_capital(username)
                process_username_first_last_letter_capital(username)
            else:
                print(f"Invalid option: {option}")
        
        concatenate_final_files(username)
        
    print("\n\nWord Count:")
    for username in usernames:
        username = username.strip()
        Word_Count = subprocess.run(f"wc -w Final_{username}.txt", shell=True, check=True)
        
        current_directory = os.getcwd()
        additional_string = f"Final_{username}.txt"
        full_path = os.path.join(current_directory, additional_string)
        print(f"Full path for {username}: ", full_path)
    
    print("Cleaning Cache")
    subprocess.run("rm _* ", shell=True, check=True)

if __name__ == "__main__":
    main()
