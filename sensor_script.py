import subprocess
import json
import os

git_path = r"C:\\Program Files\\Git\\cmd\\git.exe"
GITHUB_REPO_PATH = "C:\\Users\\rayio\\render-api"
FILENAME = "sensor_data.json"

def save_sensor_data():
    # Simulating sensor data collection
    sensor_data = {"temperature": 22.5, "humidity": 60}
    
    with open(FILENAME, "w") as file:
        json.dump(sensor_data, file)
    
    print("✅ Data saved to sensor_data.json")

def push_to_github(repo_path, filename):
    try:
        # Change directory to repo
        os.chdir(repo_path)
        
        # Run Git commands with full path
        subprocess.run([git_path, "add", filename], check=True)
        subprocess.run([git_path, "commit", "-m", "Auto commit"], check=True)
        subprocess.run([git_path, "push"], check=True)
        
        print("✅ Pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    save_sensor_data()
    push_to_github(GITHUB_REPO_PATH, FILENAME)
