import concurrent.futures
import subprocess


# Function to run the circularization.py script and save output to a file
def run_circularization(thread_id, temp):
    try:
        if temp:  # concatemerization
            # output_filename = f'concat_thread_{thread_id}.txt'
            # result = subprocess.run(['python', 'concatemerization_length.py', output_filename], capture_output=True, text=True)
            # output_filename = f'concat_thread_{thread_id}_concentration.txt'
            # result = subprocess.run(['python', 'concatemerization_concentration.py', output_filename], capture_output=True, text=True)
            output_filename = f'random_concat_thread_{thread_id}.txt'
            result = subprocess.run(['python', './concatemerization/concatemerization_random.py', output_filename],
                                    capture_output=True, text=True)
        else:  # circularization
            output_filename = f'circle_thread_{thread_id}.txt'
            result = subprocess.run(['python', 'circularization.py', output_filename], capture_output=True, text=True)
        if result.returncode != 0:
            return f"An error occurred in thread {thread_id}: {result.stderr}"
        return output_filename
    except Exception as e:
        return f"An error occurred in thread {thread_id}: {e}"


# Main function to execute the script using multi-threading
def main():
    num_threads = 32
    temp = 1  # 0 for circularization 1 for concatemerization

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(run_circularization, i, temp) for i in range(num_threads)]

        for future in concurrent.futures.as_completed(futures):
            try:
                output_filename = future.result()
                print(f"Output saved to {output_filename}")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
