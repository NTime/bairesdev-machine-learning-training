# Transfer Learning project using Python

The project consists in applying Transfer Learning from a bigger dataset to a smaller one. Here [Cats vs Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) was chosen, freezing weights from [VGG16](https://www.google.com/url?q=https%3A%2F%2Farxiv.org%2Fpdf%2F1409.1556.pdf) and using only the last layer for training.

# Notebooks

Comments were kept on the new notebook, only code was changed to fit the new dataset

- Original: With instructions and examples
- New: With new dataset and new weights

# Results

The method of Transfer Learning was successfully achieved, but even though using only 10 epochs for the training it was enough to overfit. Maybe less would be better for this new dataset with only 2 classes
