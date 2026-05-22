import subprocess

def install_libraries(libs):
    for lib in libs:
        subprocess.run(["pipx", "install", lib])

def main():
    required_libraries = [
        "requests",
        "schedule",
	"py2app",
        # Add more libraries as needed
    ]

    install_libraries(required_libraries)
    print("Libraries installed successfully.")

if __name__ == "__main__":
    main()

