import os
import subprocess
from termcolor import colored

def print_ascii_art():
    # Prints ASCII art for the tool's branding
    art = r"""
    ,---,                        ___                  ,---,.                       
    '  .' \                     ,--.'|_              ,'  .'  \                      
    /  ;    '.             ,--,  |  | :,'    ,---.  ,---.' .' |   ,---.              
    :  :       \          ,'_ /|  :  : ' :   '   ,'\ |   |  |: |  '   ,'\ ,--,  ,--,  
    :  |   /\   \    .--. |  | :.;__,'  /   /   /   |:   :  :  / /   /   ||'. \/ .`|  
    |  :  ' ;.   : ,'_ /| :  . ||  |   |   .   ; ,. ::   |    ; .   ; ,. :'  \/  / ;  
    |  |  ;/  \   \|  ' | |  . .:__,'| :   '   | |: :|   :     \'   | |: : \  \.' /   
    '  :  | \  \ ,'|  | ' |  | |  '  : |__ '   | .; :|   |   . |'   | .; :  \  ;  ;   
    |  |  '  '--'  :  | : ;  ; |  |  | '.'||   :    |'   :  '; ||   :    | / \  \  \  
    |  :  :        '  :  `--'   \ ;  :    ; \   \  / |   |  | ;  \   \  /./__;   ;  \ 
    |  | ,'        :  ,      .-./ |  ,   /   `----'  |   :   /    `----' |   :/\  \ ; 
    `--''           `--`----'      ---`-'            |   | ,'            `---'  `--`  
                                                   `----'                          
                                                   Created by @4rk4n3
    """
    print(colored(art, 'cyan'))

def print_notice():
    # Prints a notice to inform the user that the script must be run as root
    notice = """
    #############################################
    #            must run as root               #
    #############################################
    """
    print(colored(notice, 'red'))

def get_user_input(prompt):
    # Prompts the user for input and returns the response, colored for visibility
    return input(colored(prompt, 'cyan'))

def create_folder_structure(box_name):
    # Creates a folder structure for storing scan results
    try:
        # Create the main folder for the box name
        os.makedirs(box_name, exist_ok=True)
        print(colored(f"Folder '{box_name}' created or already exists.", 'green'))
        
        # Change the current directory to the box folder
        os.chdir(box_name)
        print(colored(f"Moved into folder '{box_name}'.", 'green'))
        
        # Create a subfolder for scans
        scans_folder = "scans"
        os.makedirs(scans_folder, exist_ok=True)
        print(colored(f"Folder '{scans_folder}' created or already exists inside '{box_name}'.", 'green'))
        
    except Exception as e:
        # Handle exceptions and print an error message
        print(colored(f"Error creating folder structure: {e}", 'red'))

def update_hosts_file(box_name, ip_address):
    # Updates the /etc/hosts file with the box name and IP address
    entry = f"{ip_address} {box_name}.htb\n"
    try:
        # Open the hosts file in append mode
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(entry)
        print(colored(f"Added '{entry.strip()}' to /etc/hosts.", 'green'))
    except PermissionError:
        # Handle permission errors specifically
        print(colored("Permission denied: You need to run this script with elevated privileges to modify /etc/hosts.", 'red'))
    except Exception as e:
        # Handle other exceptions
        print(colored(f"Error updating /etc/hosts: {e}", 'red'))

def run_nmap_scan(box_name, ip_address):
    # Executes an Nmap scan on the specified IP address
    scan_folder = "scans"
    output_base = os.path.join(scan_folder, box_name)
    nmap_command = [
        "nmap", "-sV", "-sC", "-p-", "--open",
        "-oA", output_base,
        ip_address
    ]
    
    try:
        # Print the banner before starting the Nmap scan
        banner = """
        *******************************
        *                             *
        *     NMAP SCAN ACTIVATED     *
        * PLEASE STAND BY FOR RESULTS *
        *                             *
        *******************************
        """
        print(colored(banner, 'cyan'))

        # Start the Nmap scan in a subprocess
        process = subprocess.Popen(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Indicate that the scan is completed
        print(colored(f"Nmap scan completed. Results saved in '{scan_folder}' folder.", 'green'))
        
        # Print Nmap scan results
        print(colored("\nNmap scan results:", 'yellow'))
        print(stdout.decode())

    except subprocess.CalledProcessError as e:
        # Handle errors from the Nmap process
        print(colored(f"Error running nmap: {e}", 'red'))

def main():
    # Main function to orchestrate the script's functionality
    print_ascii_art()  # Print ASCII art
    print_notice()     # Print notice about running as root
    box_name = get_user_input("Enter the box name: ")  # Get box name from user
    ip_address = get_user_input("Enter the IP address: ")  # Get IP address from user

    create_folder_structure(box_name)  # Create necessary folder structure
    update_hosts_file(box_name, ip_address)  # Update hosts file with the new entry
    run_nmap_scan(box_name, ip_address)  # Run the Nmap scan

if __name__ == "__main__":
    main()  # Execute the main function when the script is run
