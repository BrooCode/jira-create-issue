import base64

def convert(ext,file_base64):

    decoded_bytes = base64.b64decode(file_base64)

    output_file_path = "issue"+ext  

    with open(output_file_path, "wb") as output_file:
        output_file.write(decoded_bytes)

    print(f"File '{output_file_path}' has been created with the decoded content.")
