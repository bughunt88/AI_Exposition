import torch

torch.cuda.is_available()

torch.cuda.get_device_name(0)

torch.cuda.device_count()


print(torch.cuda.is_available())