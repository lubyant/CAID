class image_demo_config():
    def __init__(self, img_folder, config_file, checkpoint_file, output_folder, \
        img_suffix = 'png', opacity = 1, device = 'cuda:0', with_labels = False, title = "result"):
        self.img_folder = img_folder
        self.config = config_file
        self.checkpoint = checkpoint_file
        self.out_folder = output_folder
        self.img_suffix = img_suffix
        self.opacity = opacity
        self.device = device
        self.with_labels = with_labels
        self.title = title