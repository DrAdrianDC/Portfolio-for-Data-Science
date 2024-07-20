### Model



Split the file into smaller parts, upload them separately, and then combine them after downloading. Here’s how to split and recombine files:
* Splitting the File: 
split -b 20971520 cifar10_vgg16_model.h5 cifar10_vgg16_model_part_

This size is 20 MB in bytes (20 * 1024 * 1024).

* Recombining the File
After splitting the file, and downloading, you can recombine it using the cat command on Unix-like systems:

cat cifar10_vgg16_model_part_* > cifar10_vgg16_model.h5


