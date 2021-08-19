# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
def reorganize(PATH, PATH_Save):
    df = pd.read_csv(PATH)
    data_array = pd.DataFrame(df).to_numpy()

    cam_data = data_array[:, 31:43]
    pos_data = data_array[:, 5:8]
    remaining = data_array[:, 43:-2]
    cropped_array = np.hstack((cam_data, pos_data, remaining))
    modified = cropped_array[1::7]
    frames = np.copy([i + 1 for i in range(len(modified))])
    final_array = np.hstack((frames.reshape((frames.shape[0], 1)), modified))
    pd.DataFrame(final_array).to_csv(PATH_Save, header=None, index=None)# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    dirname = os.path.dirname(file_path)
    Filename = input("Enter name of processed file: ")
    destination = dirname + '/' + Filename + '.csv'
    reorganize(file_path, destination)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
