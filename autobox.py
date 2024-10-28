import os
import subprocess
from termcolor import colored

def print_ascii_art():
    art = """
                                                                                   
 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    
█       █  █ █  █       █       █  ▄    █       █  █▄█  █   
█   ▄   █  █ █  █▄     ▄█   ▄   █ █▄█   █   ▄   █       █   
█  █▄█  █  █▄█  █ █   █ █  █ █  █       █  █ █  █       █   
█       █       █ █   █ █  █▄█  █  ▄   ██  █▄█  ██     █    
█   ▄   █       █ █   █ █       █ █▄█   █       █   ▄   █   
█▄▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█ v1.1
                                       Created by @4rk4n3
    """
    print(colored(art, 'cyan'))

def print_notice():
    notice = """
    #############################################
    #            must run as root               #
    #############################################
    """
    print(colored(notice, 'red'))

def get_user_input(prompt):
    return input(colored(prompt, 'cyan'))

def create_folder_structure(box_name):
    try:
        os.makedirs(box_name, exist_ok=True)
        print(colored(f"Folder '{box_name}' created or already exists.", 'green'))
        os.chdir(box_name)
        print(colored(f"Moved into folder '{box_name}'.", 'green'))
        
        scans_folder = "scans"
        os.makedirs(scans_folder, exist_ok=True)
        print(colored(f"Folder '{scans_folder}' created or already exists inside '{box_name}'.", 'green'))
        
    except Exception as e:
        print(colored(f"Error creating folder structure: {e}", 'red'))

def update_hosts_file(box_name, ip_address):
    entry = f"{ip_address} {box_name}.htb\n"
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(entry)
        print(colored(f"Added '{entry.strip()}' to /etc/hosts.", 'green'))
    except PermissionError:
        print(colored("Permission denied: You need to run this script with elevated privileges to modify /etc/hosts.", 'red'))
    except Exception as e:
        print(colored(f"Error updating /etc/hosts: {e}", 'red'))

def run_nmap_scan(box_name, ip_address):
    scan_folder = "scans"
    output_base = os.path.join(scan_folder, box_name)
    nmap_command = [
        "nmap", "-sV", "-sC", "-p-", "--open",
        "-oA", output_base,
        ip_address
    ]
    
    try:
        # Add the banner right before starting the Nmap scan
        banner = """
        *******************************
        *                             *
        *     NMAP SCAN ACTIVATED     *
        * PLEASE STAND BY FOR RESULTS *
        *                             *
        *******************************
        """
        print(colored(banner, 'cyan'))

        # Start the nmap scan in a subprocess
        process = subprocess.Popen(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        print(colored(f"Nmap scan completed. Results saved in '{scan_folder}' folder.", 'green'))
        
        # Print Nmap results
        print(colored("\nNmap scan results:", 'yellow'))
        print(stdout.decode())

    except subprocess.CalledProcessError as e:
        print(colored(f"Error running nmap: {e}", 'red'))

    except subprocess.CalledProcessError as e:
        print(colored(f"Error running nmap: {e}", 'red'))

def main():
    print_ascii_art()
    print_notice()
    box_name = get_user_input("Enter the box name: ")
    ip_address = get_user_input("Enter the IP address: ")

    create_folder_structure(box_name)
    update_hosts_file(box_name, ip_address)
    run_nmap_scan(box_name, ip_address)

if __name__ == "__main__":
    main()
