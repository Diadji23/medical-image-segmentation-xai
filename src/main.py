from data_utils import organize_from_separate_dirs 


organize_from_separate_dirs(
    images_path="../data/zip_image/",
    masks_path="../data/raw/zip_mask/",
    output_images_dir="../data/raw/images/",
    output_masks_dir="../data/raw/masks/"
)