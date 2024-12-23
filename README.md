# Hate_Offensive_Speech_Detection
Detected toxic language with NLP preprocessing and Random Forest.

This project aims to detect hate and offensive speech in textual data. It includes a user-friendly interface and a machine learning model trained to classify input text as hate speech, offensive speech, or neither. The project is designed for educational and research purposes to promote a better understanding of hate speech detection systems.

## Project Features
- **Machine Learning Model**: A trained model to classify text into hate, offensive, or neutral categories.
- **Interactive User Interface**: A web-based UI to input text and visualize classification results.
- **Data**: Includes a labeled dataset used for training and testing the model.

---

## File Descriptions

### 1. **static/**
Contains static assets for the user interface, such as CSS, JavaScript, or images.

### 2. **templates/**
Holds HTML files used for rendering the user interface.

### 3. **Hate_Offensive_Speech_Detector.ipynb**
Jupyter Notebook containing the data preprocessing, model training, and evaluation process. It documents the step-by-step approach to building the hate and offensive speech detector.

### 4. **Hate_Speech_Detector_model.pkl**
Serialized (pickled) machine learning model trained for detecting hate and offensive speech.

### 5. **Hate_Speech_Detector_model_vectorizer.pkl**
Pickled vectorizer used to transform text data into a numerical format compatible with the machine learning model.

### 6. **Labeled_data.csv**
CSV file containing the labeled dataset used for training and testing the model.

### 7. **model.py**
Python script for loading the trained model and vectorizer, as well as handling predictions. It serves as the backend for the user interface.

---

## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd hate-offensive-speech-detector
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Install the required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Flask application by running:
   ```bash
   python model.py
   ```

4. **Access the UI**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

5. **Input Text**
   Use the interface to input text and receive predictions.

---

## Dataset
The dataset (`Labeled_data.csv`) contains labeled examples of text data categorized into hate, offensive, or neutral speech. 

---

## Future Improvements
- Enhance model accuracy with more data and advanced preprocessing.
- Expand the dataset to include more languages and diverse speech contexts.
- Add more features to the UI for improved user interaction.

---

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Special thanks to open-source contributors and datasets that made this project possible.

---

**Note:** This project is for educational purposes and should not be used in production without further testing and validation.
```

