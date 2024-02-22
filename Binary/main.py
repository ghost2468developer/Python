import tkinter as tk
from tkinter import messagebox
import logging
import time

# Set up logging
logging.basicConfig(filename='binary_search.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def binary_search(arr, low, high, x):
    """
    Standard binary search algorithm.
    """
    if high >= low:
        mid = (high + low) //  2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid -  1, x)
        else:
            return binary_search(arr, mid +  1, high, x)
    else:
        return -1

def get_user_input():
    """
    Prompt the user for the array and the target value.
    """
    arr = list(map(int, input("Enter the sorted array (comma-separated): ").split(',')))
    x = int(input("Enter the target value: "))
    return arr, x

def gui_start():
    """
    Start the GUI for a more interactive experience.
    """
    root = tk.Tk()
    root.title("Binary Search")

    def perform_search():
        arr, x = get_user_input()
        result = binary_search(arr,  0, len(arr) -  1, x)
        if result != -1:
            messagebox.showinfo("Result", f"Element found at index {result}")
            logging.info(f"Element found at index {result}")
        else:
            messagebox.showinfo("Result", "Element not found in array")
            logging.info("Element not found in array")

    search_button = tk.Button(root, text="Perform Binary Search", command=perform_search)
    search_button.pack()

    root.mainloop()

if __name__ == "__main__":
    gui_start()
