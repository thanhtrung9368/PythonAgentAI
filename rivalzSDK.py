from rivalz_client.client import RivalzClient

# Initialize the client
client = RivalzClient('eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY2MGE4OTY1ZGQzYmJhZDUyNzIyYjM2NyIsImF1dGhUeXBlIjoiaXBmcy1zZWNyZXQtYXBpLWtleSIsImlhdCI6MTcyMTExMzM3MywiZXhwIjoxNzUyNjcwOTczfQ.T5UQdvTrdsgRgg5ppPlTnCPRBIoeus2I43FWQ2CkpZo')

def uploadFile(file_path, file_type='image'):
    try:
        if file_type == 'image':
            upload_response = client.upload_passport(file_path)
        else:
            upload_response = client.upload_file(file_path)
        
        # Extract the upload hash
        upload_hash = upload_response.get('uploadHash')
        if upload_hash:
            print(f"Upload Hash: {upload_hash}")
        else:
            print("Upload hash not found in response.")
        return upload_hash  # Return the upload hash

    except Exception as e:
        print(f"An error occurred during file upload: {e}")
        return None

# Download a file
def readFileFromHash(hash):
    # Download the file
    try:
        file_path = client.download(hash, 'save/directory')
        print(f"File downloaded to: {file_path}")
    except Exception as e:
        print(f"An error occurred during file download: {e}")

def deleteFileFromHash(hash):
    # Download the file
    try:
        delete_response = client.delete_file(hash)
        print(f"Delete File Response: {delete_response}")
    except Exception as e:
        print(f"An error occurred during file deletion: {e}")


# Example usage
if __name__ == "__main__":
    # Step 1: Upload the file and get the hash
    ipfs_hash = uploadFile("requirements.txt","file")
    print(f"{ipfs_hash}")
    # Step 2: Read from the hash
    readFileFromHash(ipfs_hash)
    # Step 3: Read from the hash
    deleteFileFromHash(ipfs_hash)