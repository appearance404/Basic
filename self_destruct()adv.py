import os
import sys

def self_destruct():
    try:
        file_path = os.path.abspath(__file__)
        os.remove(file_path)
        print(f"{file_path} successfully deleted.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    self_destruct()
'''
• Absolute Path Resolution:
The enhanced code uses os.path.abspath(__file__) to resolve the absolute path of the script file. 
This ensures that the correct file is targeted for deletion, regardless of the current working directory.

• Error Handling:
The try-except block in the enhanced code captures and prints any exceptions that occur during the file removal process. This makes the script more robust by handling potential issues such as file permission errors, file not found errors, or other OS-related errors.

• User Feedback:
The enhanced code provides clear feedback on whether the file was successfully deleted or if an error occurred. This can be useful for debugging and for users to understand the script's behavior.

• Cross-Platform Consistency:
While both versions are designed to be cross-platform, the enhanced code's use of absolute paths and error handling makes it more reliable in varied environments.
'''
