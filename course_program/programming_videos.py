import os
from console_args import ConsoleArgs as c_args
import os_specific as os_spec        


class VideoTutorials:
    base_dir = "./video_tutorials/"

    @staticmethod
    def get_videos_folder_path():
        user_mode_name = c_args.get_user_mode_name()
        return VideoTutorials.base_dir + user_mode_name

    @staticmethod
    def get_video_count(video_name):
        splitter = video_name.split("_")
        first_num = int(splitter[0])
        second_num = 0
        if splitter[1].isdigit():
            second_num = int(splitter[1])
        return float(f"{first_num}.{second_num}")


    @staticmethod
    def print_available_videos():
        vid_folder_path = VideoTutorials.get_videos_folder_path()
        files_n_folders = os.listdir(vid_folder_path)
        vids = []

        for entry in files_n_folders:
            file_path = vid_folder_path +"/"+ entry
            if os.path.isfile(file_path) and entry.endswith(".txt"):
                vids.append(entry)

        user_mode_name = c_args.get_user_mode_name()
        print(f"Available Video Tutorials for {user_mode_name}:")
        vids.sort(key=VideoTutorials.get_video_count)
        for i, vid in enumerate(vids):
            print("", i, ":", vid)
        return vids

    @staticmethod
    def read_video_info(video_file_name):
        lines = []
        url = "URL_NOT_FOUND"

        vid_folder_path = VideoTutorials.get_videos_folder_path()
        vid_file_path = vid_folder_path + "/" + video_file_name
        if os.path.exists(vid_file_path) and os.path.isfile(vid_file_path):
            with open(vid_file_path) as f:
                data_len = 1
                while data_len > 0:
                    line = f.readline()
                    data_len = len(line)
                    if data_len > 0:
                        line_l = line.lower()
                        if line_l.startswith("video:") or line_l.startswith("link:"):
                            url = ":".join(line.split(":")[1:]).rstrip('\n').strip()
                        else:
                            lines.append(line.rstrip('\n'))

        return lines, url
                        

    @staticmethod
    def video_wheel():
        vids = VideoTutorials.print_available_videos()

        video_index = -1
        video_num = input("Select video [0]: ")
        if len(video_num) == 0:
            video_index = 0
        elif video_num == "q":
            return False
        
        if video_num.isdigit():
            video_index = int(video_num)

        if 0 <= video_index < len(vids):
            info_lines, url = VideoTutorials.read_video_info(vids[video_index])
            print()
            print("[Video] URL:", url)
            print("[Video] Info:")
            print()

            empty_start_line = True
            for line in info_lines:
                if empty_start_line:
                    empty_start_line = len(line.strip()) == 0
                if not empty_start_line:
                    print(line)
            
            if url != "URL_NOT_FOUND":
                print()
                os_spec.open_url(url)

            print()
        else:
            print("Invalid input! Please try again.")

        return True 

