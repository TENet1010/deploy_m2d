import torch
import torchvision.transforms as transforms
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "data/train"
VAL_DIR = "data/val"
BATCH_SIZE = 1
LEARNING_RATE = 1e-5
LAMBDA_IDENTITY = 0.0
LAMBDA_CYCLE = 10
NUM_WORKERS = 4
NUM_EPOCHS = 10
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_GEN_night = "genn.pth"
CHECKPOINT_GEN_day = "gend.pth"
CHECKPOINT_CRITIC_night = "criticn.pth"
CHECKPOINT_CRITIC_day = "criticd.pth"
MYTRANSFORMS_night   = transforms.Compose([transforms.ToPILImage(),
                                transforms.Resize((256,256)),
                                transforms.ToTensor(),
                                transforms.ColorJitter(contrast=(0.5,0.5),brightness=(1.2,1.4)),
                                ])

MYTRANSFORMS_day   = transforms.Compose([transforms.ToPILImage(),
                                transforms.Resize((256,256)),
                                transforms.ToTensor(),
                                transforms.RandomHorizontalFlip(p=0.5)])