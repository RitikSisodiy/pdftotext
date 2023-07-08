import os,datetime,time,threading
def cleanup_tmp_folder():
    while True:
        # Get the current time
        current_time = datetime.datetime.now()

        # Get the list of files in the tmp folder
        files = os.listdir('tmp')

        # Iterate over the files and delete the ones older than 1 hour
        for file in files:
            file_path = os.path.join('tmp', file)
            if os.path.isfile(file_path):
                file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                time_difference = current_time - file_modified_time

                # Delete the file if it is older than 1 hour
                if time_difference.total_seconds() > 3600:
                    os.remove(file_path)

        # Sleep for the desired interval (in seconds)
        time.sleep(3600)  # Cleanup every hour

cleanup_thread = threading.Thread(target=cleanup_tmp_folder)