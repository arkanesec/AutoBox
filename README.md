![image](https://github.com/user-attachments/assets/fbb7e203-12b5-44bc-8bd0-bd7a45dfef00)

TLDR; 
This adds a folder for the box and adds it to your etc/host file then runs an intial nmap scans and saves them to a folder called scans in the folder named after the box.


This tool is a simple command-line script designed for Hackthebox it Automates the first steps you would normally take when staring a box on HTB. Here’s a brief description of its functionality:

Tool Overview
User Input: The script prompts the user for the target box name and its corresponding IP address.

Folder Structure Creation:

It creates a dedicated folder for the target box, including a subfolder for storing scan results.
The folder structure helps organize output files related to the specific target.
Hosts File Update:

The tool appends an entry to the /etc/hosts file, mapping the provided IP address to the specified box name. This allows for easier access during testing.
Nmap Scan:

It executes an Nmap scan to discover open ports and services on the target.
The results of the scan are saved in the created folder for further analysis.

**Use Cases**
Penetration Testing: Useful for security professionals conducting assessments on networks and systems.
Network Discovery: Helps in identifying services running on a machine, which is essential for vulnerability assessment.
Organizational Efficiency: By organizing results in a structured way, it aids in maintaining clear records of findings during security assessments.
Important Note
This tool is intended for use on systems for which the user has explicit permission to test. Unauthorized scanning of networks or systems is illegal and unethical.
