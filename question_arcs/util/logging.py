from pathlib import Path

def log_error(
        error: Exception,
        sentence: str,
        logs_path: str = './logs'
    ):
    """Appends potentially faulty sentences to the error log
    
    Args:
        error: The exception that ocurred.
        sentence: The sentence that was affected.

    """

    Path(logs_path).mkdir(parents=True, exist_ok=True)

    with open(f"{logs_path}/error.log", 'a+') as outfile:
        outfile.write(f"Error: {error}\n{sentence}\n")