#THis is just for the extra credit

Step 1 - We should add a Shebang line like this: #!/usr/bin/env python3

Step 2: Set a standard location for the pickle file using OS package 

        Import OS
        os.chdir(r"C:\Users\16823\.todo.pickle") #This is specific to my desktop when I experimented with this implementation

Step 3: Ensure the code can be excuted

        in bash you can go to the path of the script and use chmod although I have a windows which uses a different command
        command to use: chmod +x todo.py
        This lets you run without using 'python' as a keyword

Step 4: Move the code to the main default path using below (#This is using Git Bash)

        Move your script to /usr/local/bin:
        sudo mv todo.py /usr/local/bin/todo
    
        Verify that the script is accessible:
        todo --help
