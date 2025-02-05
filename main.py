import os
import random
import string
import time
import base64
import json
import sys

num = random.randint(5, 10)

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
    "https://github.com/ExampleRepo/EncryptedFile1/raw/main/sensitive_data1.txt",
    "https://github.com/ExampleRepo/EncryptedFile2/raw/main/sensitive_data2.json",
    "https://github.com/ExampleRepo/EncryptedFile3/raw/main/sensitive_data3.env",
    "https://github.com/ExampleRepo/EncryptedFile4/raw/main/sensitive_data4.pem",
    "https://github.com/ExampleRepo/EncryptedFile5/raw/main/sensitive_data5.key",
] #* 12  # Repeat the list to simulate 60 files

# Step 3: Simulating data and file download
def download_and_decrypt_file(file_url, downloaded_files):
    """Simulate downloading and decrypting the file."""
    print(f"\nDownloading file from: {file_url}")
    
    # Simulate the download progress
    file_size = random.randint(50, 200)  # Random file size between 50MB and 200MB
    download_time = random.uniform(1, 3)  # Random download time per file between 1 and 3 seconds
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

    print(f"Files to download: ", num)
    print("Total data to exfiltrate: ~5000 MB")
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
    with open("decrypted_files_output.json_of_", num, "w") as json_file:
        json.dump(decrypted_files, json_file, indent=4)

    print("Decrypted data saved to 'decrypted_files_output.json'")

# Run the Hacking function
Hacking()
