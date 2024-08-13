import concurrent.futures
import subprocess


# Function to run the circularization.py script and save output to a file
def run(thread_id):
    try:
        output_filename = f'test_model_hd_t{thread_id}.txt'
        result = subprocess.run(['venv/Scripts/python', './test_model_hd.py', output_filename], capture_output=True, text=True)
        if result.returncode != 0:
            return f"An error occurred in thread {thread_id}: {result.stderr}"
        return output_filename
    except Exception as e:
        return f"An error occurred in thread {thread_id}: {e}"


# Main function to execute the script using multi-threading
def main():
    num_threads = 16

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(run, i) for i in range(num_threads)]

        for future in concurrent.futures.as_completed(futures):
            try:
                output_filename = future.result()
                print(f"Output saved to {output_filename}")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
