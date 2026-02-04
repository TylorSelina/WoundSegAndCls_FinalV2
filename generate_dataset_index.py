import os
import json
from pathlib import Path

def generate_dataset_index(dataset_root=r'F:\Dataset\WoundSeg&Cls\数据集\WoundSeg&Cls_Final'):
    # 类别映射
    class_mapping = {
        'no-infected': 0,
        'infected-Mildly': 1,
        'infected-Moderately': 2,
        'infected-Severely': 3
    }
    
    dataset = {
        'train': [],
        'test': []
    }
    
    # 支持的图片和掩码文件扩展名
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
    mask_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
    
    # 遍历所有类别文件夹
    for class_name, class_id in class_mapping.items():
        class_dir = Path(dataset_root) / class_name
        
        # 检查类别文件夹是否存在
        if not class_dir.exists():
            print(f"Warning: Directory {class_dir} does not exist")
            continue
        
        # 处理训练集和测试集
        for split in ['train', 'test']:
            images_dir = class_dir / split / 'images'
            masks_dir = class_dir / split / 'masks'
            
            if not images_dir.exists() or not masks_dir.exists():
                print(f"Warning: {split} directories for {class_name} are incomplete")
                continue
            
            # 获取所有图片文件
            image_files = []
            for ext in image_extensions:
                image_files.extend(images_dir.glob(f'*{ext}'))
            
            for image_file in image_files:
                # 获取不带后缀的文件名
                base_name = image_file.stem
                
                # 查找对应的掩码文件
                mask_file = None
                for ext in mask_extensions:
                    potential_mask = masks_dir / f"{base_name}{ext}"
                    if potential_mask.exists():
                        mask_file = potential_mask
                        break
                
                if mask_file is None:
                    print(f"Warning: No matching mask found for {image_file.name} in {class_name}/{split}")
                    continue
                
                # 使用相对路径，并确保使用正斜杠
                image_path = str(Path(class_name) / split / 'images' / image_file.name).replace('\\', '/')
                mask_path = str(Path(class_name) / split / 'masks' / mask_file.name).replace('\\', '/')
                
                # 添加到数据集
                dataset[split].append({
                    'image_path': image_path,
                    'mask_path': mask_path,
                    'class': class_id
                })
    
    # 打印统计信息
    print("\nDataset Statistics:")
    for split in ['train', 'test']:
        print(f"{split} set: {len(dataset[split])} samples")
        class_counts = {}
        for item in dataset[split]:
            class_counts[item['class']] = class_counts.get(item['class'], 0) + 1
        print(f"Class distribution in {split} set:")
        for class_id, count in class_counts.items():
            class_name = list(class_mapping.keys())[list(class_mapping.values()).index(class_id)]
            print(f"  {class_name}: {count} samples")
    
    # 保存到JSON文件
    output_file = 'dataset_index.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    print(f"\nDataset index has been saved to {output_file}")

if __name__ == '__main__':
    generate_dataset_index() 