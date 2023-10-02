# The user provides a board of letters and the word they want to search for
# The word can formed from adjacent, non-repeated letters in neighboring cells
# If the word can be formed from adjacent neighboring cells, the word will be highlighted in green
# Other the board will turn red to indicate that the word cannot be found on the board

# Below are the important libraries needed to create the GUI
# pip install tkinter
import tkinter
import tkinter as tk
from tkinter import ttk

def loading_page(board, word, onBoard,seen):
    def close_loading():
        root.destroy()

    # Create a Tkinter loading screen (aesthetic purposes)
    root = tk.Tk()
    root.title("Loading Word Search GUI")
    width = 300 # width for the Tk root
    height = 200 # height for the Tk root

    screenWidth = root.winfo_screenwidth() # width of the screen
    screenHeight = root.winfo_screenheight() # height of the screen

    xPos = (screenWidth/2) - (width/2) # x position on the scree
    yPos = (screenHeight/2) - (height/2) # y position on the screen

    root.geometry('%dx%d+%d+%d' % (width, height, xPos, yPos)) # finalizes window information
    root.resizable(False, False)

    # Create a frame for the loading message
    loading_frame = ttk.Frame(root)
    loading_frame.pack(pady=50)

    # Create a label for the loading message
    loading_label = ttk.Label(loading_frame, text="Loading...", font=("Arial", 14))
    loading_label.pack()

    # Create a progress bar
    progress_bar = ttk.Progressbar(root, length=200, mode='indeterminate')
    progress_bar.pack()

    # Schedule closing the loading window after 5 seconds after the script is ran
    root.after(5000, close_loading)

    # Start the progress bar animation
    progress_bar.start(100000)
    root.mainloop()


    # After the loading screen completes, the GUI revealing the word board appears
    root = tk.Tk()
    root.title(f"Word Search GUI: {onBoard}") 
    width = 800 # width for the Tk root
    height = 600 # height for the Tk root

    # get screen width and height
    screenWidth = root.winfo_screenwidth() # width of the screen
    screenHeight = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    xPos = (screenWidth/2) - (width/2)
    yPos = (screenHeight/2) - (height/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (width, height, xPos, yPos))
    root.resizable(False, False)

    labels = []

    # create frame that will highlight the cells in either green, red, or white
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for i, row in enumerate(board):
        frame.grid_rowconfigure(i, weight=1) # makes the font larger within the cell
        row_labels = []
        for j, cell_value in enumerate(row):
            frame.grid_columnconfigure(j, weight=1)

            # if the word is not found (onBoard=False), make the cell color red
            # this will be done for every cell
            if not onBoard:
                bg_color = "red"

            # if the word is found, make the cells that are found in seen green
            # the cells in seen are the adjacent letters that make up the desired word
            elif ((i,j) in seen and onBoard):
                bg_color = "green"
            
            # the cells that do not make up the word are made white
            else:
                bg_color = "white"
            label = tk.Label(frame, text=cell_value, width=5, height=2, borderwidth=1, relief="solid", font=("Helvetica", 100), bg=bg_color)
            label.grid(row=i, column=j, sticky="nsew")
            row_labels.append((i, j))
        labels.append(row_labels)   


# The function below first determines whether or not the word is found on the board
# Then it passes its' results to the function above
def exist(board, word) -> bool:

    # We will check for the word by utilizing Depth First Search and Backtracking
    def dfs(r, c, word, index, seen, board):

        # If we have found all of the letters adjacently, we return True
        if index == len(word):
            return True
        
        # There are several conditions that will return False, and allow the script to backtrack out of that path
        # The first is first we are out of bounds, whether it be row or column wise
        # The second is if we reach a character than is not identical to the character we are searching for
        # The last is if we've seen the character (which is identified by its position) already
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index] or (r, c) in seen):
            return False
        
        # Add the letter to our set of seen letters based on position 
        seen.add((r,c))

        # Run Depth First Search on every direction once we reach a new position on the board
        # The goal is to find the next letter in the word we are searching for
        # If the next letter is found, we continue searching up,down,left,right for the next letter
        # This is done until we find the last letter of the word or determine the word cannot be found
        if (dfs(r+1,c,word,index+1,seen,board) or dfs(r-1,c,word,index+1,seen,board) or dfs(r,c-1,word,index+1,seen,board) or dfs(r,c+1,word,index+1,seen,board)):
            return True
        
        # If we encounter a position that does not have any adjacent links we are searching for, it is removed from the set
        seen.remove((r,c))

        # If the word cannot be formed using adjacent letters, return False
        return False


    row,col = len(board), len(board[0])
    seen = set()

    # Search every cell of the board until the first letter of the word is found
    # Once the first letter is found, Depth First Search begins from the position
    for r in range(0,row):
        for c in range(0,col):
            if board[r][c] == word[0]:
                if dfs(r,c,word,0,seen,board):

                    # If the word is found, two parameters are passed to the GUI functions
                    # One is the boolean, True, revealing that the word was found
                    # The other are the positions of the letters that will be highlighted
                    loading_page(board,word,True,seen)
                    return True
    
    # If the word is not found, the boolean False is passed
    loading_page(board,word,False,seen)
    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")