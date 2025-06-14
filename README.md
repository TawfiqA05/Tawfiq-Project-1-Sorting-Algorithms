# Sorting Algorithms Project – CSCI-C310 Data Structures

**Name:** Tawfiq Abulail  
**Class:** CSCI-C310 Data Structures

**Project Goal:** Test and compare different sorting algorithms to see which ones are fastest.

---

## Algorithms Included

- Insertion Sort  
- Bubble Sort  
- Merge Sort  
- Quick Sort  
- Radix Sort  

Each one was written in Python and tested on random numbers to see how they perform.

---

## Files in This Project

- `sorting_algorithms.py` – This is the main code with all 5 sorting algorithms, plus code that runs tests and times them.
- `Sorting_Algorithms_Report.docx` – The report with a table, chart, and short write-up of what I found.
- `Updated_Sorting_Performance_Chart.png` – A chart that compares how fast each algorithm was.
- `output_screenshot.png` – A screenshot of my results from running the program.

---

## How to Run the Program

1. Make sure you have Python installed (version 3.6 or newer).
2. Open a terminal in the folder with the files.
3. Type:

```
python sorting_algorithms.py
```

4. The program will:
   - Make test files if they aren’t there
   - Run each algorithm 5 times per test
   - Drop the slowest result
   - Print the average time in seconds

---

## Example Output

```
Testing with dataset size: 1000
Insertion Sort: 0.0188 seconds
Bubble Sort: 0.0381 seconds
Merge Sort: 0.0014 seconds
Quick Sort: 0.0013 seconds
Radix Sort: 0.0010 seconds
```

Note: Insertion Sort and Bubble Sort are skipped for big inputs (100,000 numbers) because they take way too long.

---

## Summary

Radix Sort was the fastest overall. Merge Sort and Quick Sort also handled big data really well. Insertion and Bubble Sort are only good for small stuff — they’re too slow on big lists. This showed me how important algorithm choice is, especially when working with large files or data.
