# Transfer Learning project using Python

This project applies Transfer Learning from a bigger dataset to a smaller one. Here [Cats vs Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) was chosen, freezing weights from [VGG16](https://www.google.com/url?q=https%3A%2F%2Farxiv.org%2Fpdf%2F1409.1556.pdf) and using only the last layer for training.

# Notebooks

Comments were kept on the new notebook, only code was changed to fit the new dataset:

- [Original](original_transfer_learning.ipynb): Includes original instructions and examples for the task
- [New](new_transfer_learning.ipynb): Includes new dataset and weights

# Results

Transfer Learning was successfully implemented. However, even with just 10 epochs for the training it was enough to overfit. Maybe less would be better for this new dataset with only 2 classes
