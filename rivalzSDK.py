from rivalz_client.client import RivalzClient

# Initialize the client
def initAndupload():
    client = RivalzClient('eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY2MGE4OTY1ZGQzYmJhZDUyNzIyYjM2NyIsImF1dGhUeXBlIjoiaXBmcy1zZWNyZXQtYXBpLWtleSIsImlhdCI6MTcyMTExMzM3MywiZXhwIjoxNzUyNjcwOTczfQ.T5UQdvTrdsgRgg5ppPlTnCPRBIoeus2I43FWQ2CkpZo')

    # Upload a file
    upload_response = client.upload_file('requirements.txt')
    print(f"Uploaded File Response: {upload_response}")

# # Upload a passport image
# passport_response = client.upload_passport('path/to/your/passport_image.jpg')
# print(f"Uploaded Passport Response: {passport_response}")

# Download a file
def readFromHash(hash):
    ipfs_hash = 'hash'  # Replace with the actual IPFS hash
        # Download the file
    try:
        file,filename = client.download(ipfs_hash)
        print(f"File downloaded to: {file}, filename: {filename}")
    except Exception as e:
        print(f"An error occurred during file download: {e}")
# Delete a file
# delete_response = client.delete_file('QmSampleHash')
# print(f"Delete File Response: {delete_response}")