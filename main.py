import os
import random
import string
import time
import base64
import json
import sys

num = random.randint(5, 10)
file_size = random.randint(50, 200)  # Random file size between 50MB and 200MB
download_time = random.uniform(1, 3)  # Random download time per file between 1 and 3 seconds

# Step 1: Helper functions for network simulation and progress
def simulate_progress_bar(iteration, total, bar_length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(bar_length * iteration // total)
    bar = "#" * filled_length + '_' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {percent}%')
    sys.stdout.flush()

def simulate_network_noise():
    if random.random() < 0.1:  # 10% chance of network noise
        print("\nWarning: Network instability detected. Retrying...")
        time.sleep(random.uniform(1, 3))
        print("Network stable. Resuming operation...")

# Step 2: Simulate data encryption and decryption
def encrypt_data(data):
    """Simulate file encryption by base64 encoding the content."""
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def decrypt_data(encrypted_data):
    """Simulate file decryption by base64 decoding the content."""
    return base64.b64decode(encrypted_data).decode('utf-8')

# Simulate some GitHub URLs containing encrypted files (for the purpose of this simulation, we use base64 encoding to "encrypt" the data)
github_repositories = [
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_1.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_2.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_3.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_4.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_5.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_6.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_7.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_8.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_9.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_10.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_11.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_12.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_13.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_14.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_15.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_16.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_17.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_18.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_19.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_20.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_21.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_22.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_23.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_24.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_25.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_26.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_27.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_28.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_29.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_30.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_31.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_32.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_33.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_34.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_35.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_36.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_37.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_38.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_39.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_40.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_41.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_42.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_43.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_44.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_45.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_46.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_47.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_48.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_49.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_50.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_51.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_52.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_53.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_54.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_55.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_56.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_57.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_58.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_59.txt",
    "https://raw.githubusercontent.com/smartshopia/Hacking_simulation/refs/heads/main/encrypted_files/encrypted_file_60.txt",

] #* 12  # Repeat the list to simulate 60 files

# Step 3: Simulating data and file download
def download_and_decrypt_file(file_url, downloaded_files):
    """Simulate downloading and decrypting the file."""
    print(f"\nDownloading file from: {file_url}")
    
    # Simulate the download progress
    
    for j in range(1, 11):  # Simulating a 10-step progress for each file
        simulate_progress_bar(j, 10)
        time.sleep(download_time / 10)  # Make the download progress

    print(f"\nFile downloaded: {file_url}")
    time.sleep(1)

    # Simulate encrypted content in the file using random data
    encrypted_data = encrypt_data(f"Encrypted data for {file_url} - {random.choice(github_repositories)}")
    
    # Store the downloaded files for decryption later
    downloaded_files.append({
        "url": file_url,
        "encrypted_data": encrypted_data
    })
    return encrypted_data

# Step 4: Main hacking program
def Hacking():
    downloaded_files = []  # To store downloaded file data
    print("Connecting to server...")
    time.sleep(2)
    print("Accessing network...")
    time.sleep(2)
    print("Bypassing security firewall...")
    time.sleep(2)
    print("Hacking...")
    time.sleep(1)

    print(f"Files to download: ", num, "Time Needed: ", download_time)
    print("Total data to exfiltrate: ~",(file_size * num) ," MB")
    time.sleep(1)

    # Simulating the download and decryption of 60 files
    for i in range(num):
        simulate_network_noise()  # Introduce network noise periodically
        file_url = random.choice(github_repositories)
        download_and_decrypt_file(file_url, downloaded_files)

    print("\nDownload Complete. Exfiltrating data...")
    time.sleep(1)
    
    print("Bypassing encryption layer...")  # Simulate bypassing an encryption layer
    time.sleep(2)
    print("Data decrypted successfully.")

    simulate_network_noise()  # Simulate network instability during exfiltration
    print("Sending data to backup server...")
    time.sleep(num)  # Simulate the exfiltration time based on the number of files
    print("Data sent successfully!")
    
    # Finalizing the hack with additional feedback
    print("Accessing secure folders...")  # Simulate accessing restricted files
    time.sleep(1.5)
    print("Secure files successfully downloaded.")
    print("Hacked Successfully!")
    
    # Step 5: Decrypt and output the data in a JSON file
    print("Decrypting downloaded files and saving to output file...")
    decrypted_files = []

    for downloaded_file in downloaded_files:
        file_url = downloaded_file["url"]
        encrypted_data = downloaded_file["encrypted_data"]
        
        # Simulate decryption of the file
        decrypted_data = decrypt_data(encrypted_data)
        decrypted_files.append({
            "url": file_url,
            "decrypted_content": decrypted_data
        })

    # Save the decrypted data to a JSON file
    with open("decrypted_files_output.json", "w") as json_file:
        json.dump(decrypted_files, json_file, indent=4)

    print("Decrypted data saved to 'decrypted_files_output.json'")

# Run the Hacking function
Hacking()
