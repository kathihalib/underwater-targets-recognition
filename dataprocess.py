import os

def remove_class_id_3_from_txt(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # 过滤掉class_id为3的行
            filtered_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id = parts[0]
                    if class_id != '3':
                        filtered_lines.append(line)
                else:
                    # 如果格式异常，直接保留该行（或根据需求处理）
                    print(1)
                    filtered_lines.append(line)

            # 写回文件
            with open(file_path, 'w') as f:
                f.writelines(filtered_lines)
            print(f"Processed {filename}")

if __name__ == "__main__":
    folder = r"F:\sea\label_B"
    remove_class_id_3_from_txt(folder)
