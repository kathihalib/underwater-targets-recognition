import os
import xml.etree.ElementTree as ET

# 类别映射
label_map = {
    'holothurian': 0,
    'echinus': 1,
    'scallop': 2
}

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[2]) / 2.0
    y_center = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    return (x_center * dw, y_center * dh, w * dw, h * dh)

def convert_xml_to_txt(xml_path, save_txt_path, label_map):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)
    size = (width, height)

    lines = []
    for obj in root.findall('object'):
        label_name = obj.find('name').text
        if label_name not in label_map:
            continue  # 跳过未定义类别

        class_id = label_map[label_name]
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        bbox = (xmin, ymin, xmax, ymax)
        x, y, w, h = convert(size, bbox)
        lines.append(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}")

    if lines:  # 如果有标注才保存
        with open(save_txt_path, 'w') as f:
            f.write('\n'.join(lines))

def batch_convert(xml_dir, out_txt_dir):
    os.makedirs(out_txt_dir, exist_ok=True)
    xml_files = [f for f in os.listdir(xml_dir) if f.endswith('.xml')]

    for xml_file in xml_files:
        xml_path = os.path.join(xml_dir, xml_file)
        txt_path = os.path.join(out_txt_dir, xml_file.replace('.xml', '.txt'))
        convert_xml_to_txt(xml_path, txt_path, label_map)
        print(f"Converted: {xml_file} -> {txt_path}")

if __name__ == '__main__':
    xml_dir = r'F:\sea\test-B-box'   # 修改为你的 XML 文件夹路径
    out_txt_dir = r'F:\sea\label_B'    # 输出的 YOLO 标签路径

    batch_convert(xml_dir, out_txt_dir)
