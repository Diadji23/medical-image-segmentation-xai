import os
import shutil

def organize_from_separate_dirs(images_path, masks_path, output_images_dir, output_masks_dir):
    """
    Organise les images et masques extraits de deux dossiers différents
    """

    os.makedirs(output_images_dir, exist_ok=True)
    os.makedirs(output_masks_dir, exist_ok=True)

    # Copie les images
    for f in os.listdir(images_path):
        if f.endswith('.jpg'):
            shutil.copy(os.path.join(images_path, f), os.path.join(output_images_dir, f))

    # Copie les masques
    for f in os.listdir(masks_path):
        if f.endswith('.png'):
            shutil.copy(os.path.join(masks_path, f), os.path.join(output_masks_dir, f))

    print("✅ Organisation terminée.")
