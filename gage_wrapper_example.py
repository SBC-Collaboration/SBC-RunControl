"""
Example showing how you could create a wrapper for your GaGe library
to use with QProcess if you wanted to capture stdout from it.
"""

import os
import sys
import ctypes
from PySide6.QtCore import QProcess, QObject, Signal, Slot

class GaGeProcessWrapper(QObject):
    """
    Wrapper to run your GaGe library through QProcess.
    This would require creating an executable wrapper for your shared library.
    """
    
    # Signals for communication
    stdout_received = Signal(str)
    stderr_received = Signal(str)
    acquisition_started = Signal()
    acquisition_finished = Signal(int)
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.process = None
    
    def start_acquisition(self):
        """Start the GaGe acquisition using QProcess"""
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            print("Acquisition already running")
            return False
        
        # Create the process
        self.process = QProcess(self)
        
        # Connect signals
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.handle_finished)
        self.process.started.connect(self.handle_started)
        
        # You would need to create a wrapper executable that:
        # 1. Loads your shared library
        # 2. Calls the main() function
        # 3. Prints status/progress to stdout
        # 4. Handles signals properly
        
        wrapper_executable = "gage_wrapper_executable"  # You'd need to create this
        config_file = "SBCAcquisition.ini"  # Your config file
        
        # Start the wrapper process
        self.process.start(wrapper_executable, [config_file])
        
        return True
    
    @Slot()
    def handle_stdout(self):
        """Process stdout from the GaGe wrapper"""
        if self.process:
            data = self.process.readAllStandardOutput()
            text = data.data().decode('utf-8')
            
            # Parse the output for specific information
            for line in text.split('\n'):
                line = line.strip()
                if not line:
                    continue
                
                # Example: parse status messages
                if line.startswith("GAGE_STATUS:"):
                    status = line.replace("GAGE_STATUS:", "").strip()
                    print(f"GaGe Status: {status}")
                elif line.startswith("GAGE_ERROR:"):
                    error = line.replace("GAGE_ERROR:", "").strip() 
                    print(f"GaGe Error: {error}")
                elif line.startswith("GAGE_PROGRESS:"):
                    progress = line.replace("GAGE_PROGRESS:", "").strip()
                    print(f"GaGe Progress: {progress}")
                
                # Emit the raw stdout for logging/display
                self.stdout_received.emit(line)
    
    @Slot()
    def handle_stderr(self):
        """Process stderr from the GaGe wrapper"""
        if self.process:
            data = self.process.readAllStandardError()
            text = data.data().decode('utf-8')
            self.stderr_received.emit(text)
    
    @Slot()
    def handle_started(self):
        """Handle process start"""
        print("GaGe acquisition started")
        self.acquisition_started.emit()
    
    @Slot(int, QProcess.ExitStatus)
    def handle_finished(self, exit_code, exit_status):
        """Handle process completion"""
        print(f"GaGe acquisition finished with exit code: {exit_code}")
        self.acquisition_finished.emit(exit_code)
        self.process = None
    
    def stop_acquisition(self):
        """Stop the acquisition"""
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            # Send a graceful stop signal (you'd implement this in your wrapper)
            self.process.write(b"STOP\n")
            
            # Wait for graceful shutdown
            if not self.process.waitForFinished(5000):
                self.process.terminate()
                if not self.process.waitForFinished(3000):
                    self.process.kill()
