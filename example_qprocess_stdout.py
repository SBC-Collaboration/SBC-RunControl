"""
Example showing how to use QProcess to read stdout from a process.
This demonstrates the key concepts you can apply to your project.
"""

import sys
from PySide6.QtCore import QProcess, QObject, Signal, Slot, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QLabel

class ProcessManager(QObject):
    """Example class showing QProcess stdout reading"""
    
    # Signals to communicate with UI
    stdout_received = Signal(str)
    stderr_received = Signal(str)
    process_finished = Signal(int, str)
    process_started = Signal()
    
    def __init__(self):
        super().__init__()
        self.process = None
    
    def start_process(self, command, arguments=None):
        """Start a process and capture its output"""
        if self.process is not None:
            if self.process.state() != QProcess.ProcessState.NotRunning:
                print("Process already running!")
                return False
        
        # Create new QProcess
        self.process = QProcess(self)
        
        # Connect all the important signals
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.handle_finished)
        self.process.started.connect(self.handle_started)
        self.process.errorOccurred.connect(self.handle_error)
        
        # Start the process
        if arguments:
            self.process.start(command, arguments)
        else:
            self.process.start(command)
        
        return True
    
    @Slot()
    def handle_stdout(self):
        """Handle stdout data - this is the key method for reading output"""
        if self.process:
            # Read all available stdout data
            data = self.process.readAllStandardOutput()
            
            # Convert bytes to string
            text = data.data().decode('utf-8', errors='replace')
            
            # Emit signal with the text (you could also process it here)
            self.stdout_received.emit(text)
            
            # You can also process the data line by line:
            lines = text.split('\n')
            for line in lines:
                if line.strip():  # ignore empty lines
                    print(f"STDOUT: {line}")
    
    @Slot()
    def handle_stderr(self):
        """Handle stderr data"""
        if self.process:
            data = self.process.readAllStandardError()
            text = data.data().decode('utf-8', errors='replace')
            self.stderr_received.emit(text)
            print(f"STDERR: {text}")
    
    @Slot()
    def handle_started(self):
        """Handle process start"""
        print("Process started successfully")
        self.process_started.emit()
    
    @Slot(int, QProcess.ExitStatus)
    def handle_finished(self, exit_code, exit_status):
        """Handle process completion"""
        status_str = "Normal" if exit_status == QProcess.ExitStatus.NormalExit else "Crashed"
        print(f"Process finished. Exit code: {exit_code}, Status: {status_str}")
        self.process_finished.emit(exit_code, status_str)
        
        # Clean up
        self.process = None
    
    @Slot(QProcess.ProcessError)
    def handle_error(self, error):
        """Handle process errors"""
        error_messages = {
            QProcess.ProcessError.FailedToStart: "Failed to start process",
            QProcess.ProcessError.Crashed: "Process crashed",
            QProcess.ProcessError.Timedout: "Process timed out", 
            QProcess.ProcessError.WriteError: "Write error",
            QProcess.ProcessError.ReadError: "Read error",
            QProcess.ProcessError.UnknownError: "Unknown error"
        }
        
        error_msg = error_messages.get(error, "Unknown error")
        print(f"Process error: {error_msg}")
    
    def stop_process(self):
        """Stop the running process"""
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            print("Terminating process...")
            
            # Try graceful termination first
            self.process.terminate()
            
            # Wait up to 5 seconds for graceful termination
            if not self.process.waitForFinished(5000):
                print("Process didn't terminate gracefully, killing it...")
                self.process.kill()
                self.process.waitForFinished(3000)
    
    def write_to_process(self, data):
        """Write data to the process stdin (if needed)"""
        if self.process and self.process.state() == QProcess.ProcessState.Running:
            self.process.write(data.encode('utf-8'))


class ProcessTestWindow(QWidget):
    """Simple UI to test the QProcess functionality"""
    
    def __init__(self):
        super().__init__()
        self.process_manager = ProcessManager()
        self.setup_ui()
        self.connect_signals()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Command input
        layout.addWidget(QLabel("Command to run:"))
        self.command_input = QLineEdit()
        self.command_input.setText("ping -c 5 google.com")  # Default command
        layout.addWidget(self.command_input)
        
        # Buttons
        self.start_button = QPushButton("Start Process")
        self.stop_button = QPushButton("Stop Process")
        self.stop_button.setEnabled(False)
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        # Output display
        layout.addWidget(QLabel("Process Output:"))
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(self.output_display)
        
        self.setLayout(layout)
        self.setWindowTitle("QProcess stdout Example")
        self.resize(600, 400)
    
    def connect_signals(self):
        # Connect UI signals
        self.start_button.clicked.connect(self.start_process)
        self.stop_button.clicked.connect(self.stop_process)
        
        # Connect process manager signals
        self.process_manager.stdout_received.connect(self.append_output)
        self.process_manager.stderr_received.connect(self.append_error)
        self.process_manager.process_started.connect(self.on_process_started)
        self.process_manager.process_finished.connect(self.on_process_finished)
    
    @Slot()
    def start_process(self):
        command = self.command_input.text().strip()
        if command:
            # Split command and arguments
            parts = command.split()
            cmd = parts[0]
            args = parts[1:] if len(parts) > 1 else None
            
            if self.process_manager.start_process(cmd, args):
                self.output_display.clear()
                self.output_display.append(f"Starting: {command}\n")
    
    @Slot()
    def stop_process(self):
        self.process_manager.stop_process()
    
    @Slot()
    def on_process_started(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.output_display.append("Process started...\n")
    
    @Slot(int, str)
    def on_process_finished(self, exit_code, status):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.output_display.append(f"\nProcess finished. Exit code: {exit_code}, Status: {status}")
    
    @Slot(str)
    def append_output(self, text):
        """Append stdout to the display"""
        self.output_display.insertPlainText(text)
        self.output_display.ensureCursorVisible()
    
    @Slot(str)
    def append_error(self, text):
        """Append stderr to the display with different formatting"""
        self.output_display.setTextColor(self.output_display.palette().color(self.output_display.palette().ColorRole.Highlight))
        self.output_display.insertPlainText(f"ERROR: {text}")
        self.output_display.setTextColor(self.output_display.palette().color(self.output_display.palette().ColorRole.Text))
        self.output_display.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessTestWindow()
    window.show()
    sys.exit(app.exec())
