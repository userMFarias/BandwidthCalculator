# Network Bandwidth Calculator Exercise

## Overview
In this exercise, you will implement the calculation logic for a network bandwidth calculator application built with Python and Tkinter. The GUI (Graphical User Interface) has already been created for you - your task is to make it functional by writing the code that performs the bandwidth calculations.

## Learning Objectives
- Apply networking concepts in a practical scenario
- Understand how to work with an existing GUI application
- Practice handling user input and performing calculations
- Learn to convert between different data and time units

## Background
Bandwidth refers to the maximum rate of data transfer across a given path. In networking, it's commonly measured in bits per second (bps) and its multiples:
- Kilobits per second (Kbps) = 1,000 bps
- Megabits per second (Mbps) = 1,000,000 bps
- Gigabits per second (Gbps) = 1,000,000,000 bps

The formula for calculating bandwidth is:
```
Bandwidth = Data Volume (in bits) / Transfer Time (in seconds)
```

## About the Application
The application provides:
- An input field for file size with a dropdown to select units (Bytes, KB, MB, GB)
- An input field for transfer time with a dropdown to select units (seconds, minutes, hours)
- A "Calculate Bandwidth" button
- A results area that displays the calculated bandwidth

## Your Task
Complete the `calculate_bandwidth()` method in the provided code. This method is called when the user clicks the "Calculate Bandwidth" button.

### Step 1: Understand the Code
- Familiarise yourself with the existing code structure
- Identify the variables that store user inputs (`self.file_size`, `self.file_size_unit`, etc.)
- Understand how to update the result display (`self.bandwidth_result`)

### Step 2: Implement Unit Conversions
You need to convert:
- File size to bits (remember: 1 byte = 8 bits)
  - Bytes to bits: multiply by 8
  - KB to bits: multiply by 8 * 1024
  - MB to bits: multiply by 8 * 1024 * 1024
  - GB to bits: multiply by 8 * 1024 * 1024 * 1024
- Transfer time to seconds
  - Minutes to seconds: multiply by 60
  - Hours to seconds: multiply by 3600

### Step 3: Calculate Bandwidth
- Divide the file size (in bits) by the transfer time (in seconds)
- Determine the appropriate unit for the result:
  - < 1,000 bits/second: display as bps
  - < 1,000,000 bits/second: display as Kbps
  - < 1,000,000,000 bits/second: display as Mbps
  - >= 1,000,000,000 bits/second: display as Gbps

### Step 4: Implement Error Handling
- Check for invalid inputs (negative numbers, non-numeric values, etc.)
- Handle division by zero (when transfer time is 0)
- Display appropriate error messages using `messagebox.showerror()`

## Testing Your Implementation
To test your implementation:
1. Run the application
2. Enter different file sizes and transfer times
3. Verify that your calculations are correct
4. Test edge cases (very large files, very small transfer times, etc.)
5. Ensure error handling works properly

## Example Calculations
1. File size: 10 MB, Transfer time: 2 seconds
   - 10 MB = 10 * 8 * 1024 * 1024 = 83,886,080 bits
   - Bandwidth = 83,886,080 / 2 = 41,943,040 bps = 41.94 Mbps

2. File size: 1 GB, Transfer time: 5 minutes
   - 1 GB = 1 * 8 * 1024 * 1024 * 1024 = 8,589,934,592 bits
   - 5 minutes = 5 * 60 = 300 seconds
   - Bandwidth = 8,589,934,592 / 300 = 28,633,115.31 bps = 28.63 Mbps

