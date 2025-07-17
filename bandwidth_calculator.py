import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BandwidthCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure the window
        self.title("Network Bandwidth Calculator")
        self.geometry("450x300")
        self.resizable(False, False)
        
        # Set up the main frame with padding
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        ttk.Label(main_frame, text="Bandwidth Calculator", font=("Arial", 16)).pack(pady=(0, 15))
        
        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        # File size input
        ttk.Label(input_frame, text="File Size:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.file_size = tk.DoubleVar()
        ttk.Entry(input_frame, textvariable=self.file_size).grid(row=0, column=1, padx=5)
        self.file_size_unit = tk.StringVar(value="MB")
        ttk.Combobox(input_frame, textvariable=self.file_size_unit, values=["Bytes", "KB", "MB", "GB"], width=5, state="readonly").grid(row=0, column=2)
        
        # Transfer time input
        ttk.Label(input_frame, text="Transfer Time:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.transfer_time = tk.DoubleVar()
        ttk.Entry(input_frame, textvariable=self.transfer_time).grid(row=1, column=1, padx=5)
        self.time_unit = tk.StringVar(value="seconds")
        ttk.Combobox(input_frame, textvariable=self.time_unit, values=["seconds", "minutes", "hours"], width=7, state="readonly").grid(row=1, column=2)
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate Bandwidth", command=self.calculate_bandwidth).pack(pady=15)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Results")
        results_frame.pack(fill=tk.X, pady=10)
        
        # Results labels
        ttk.Label(results_frame, text="Bandwidth:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.bandwidth_result = tk.StringVar(value="0 bps")
        ttk.Label(results_frame, textvariable=self.bandwidth_result, font=("Arial", 12, "bold")).grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
    def calculate_bandwidth(self):
        try:
            # Get file size and convert to bits based on the selected unit
            file_size = self.file_size.get()
            file_size_unit = self.file_size_unit.get()
            
            # Convert file size to bits
            # 1 byte = 8 bits
            if file_size_unit == "Bytes":
                file_size_bits = file_size * 8
            elif file_size_unit == "KB":
                file_size_bits = file_size * 8 * 1024
            elif file_size_unit == "MB":
                file_size_bits = file_size * 8 * 1024 * 1024
            elif file_size_unit == "GB":
                file_size_bits = file_size * 8 * 1024 * 1024 * 1024
            
            # Get transfer time and convert to seconds
            transfer_time = self.transfer_time.get()
            time_unit = self.time_unit.get()
            
            # Convert transfer time to seconds
            if time_unit == "seconds":
                transfer_time_seconds = transfer_time
            elif time_unit == "minutes":
                transfer_time_seconds = transfer_time * 60
            elif time_unit == "hours":
                transfer_time_seconds = transfer_time * 3600
            
            # Calculate bandwidth (bits per second)
            bandwidth = file_size_bits / transfer_time_seconds
            
            # Format the result with appropriate units
            if bandwidth < 1000:
                result = f"{bandwidth:.2f} bps"
            elif bandwidth < 1000000:
                result = f"{bandwidth/1000:.2f} Kbps"
            elif bandwidth < 1000000000:
                result = f"{bandwidth/1000000:.2f} Mbps"
            else:
                result = f"{bandwidth/1000000000:.2f} Gbps"
            
            # Update the result
            self.bandwidth_result.set(result)
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Transfer time cannot be zero.")
        except Exception as e:
            messagebox.showerror("Error", "Please enter valid numbers for file size and transfer time.")

if __name__ == "__main__":
    app = BandwidthCalculator()
    app.mainloop()
