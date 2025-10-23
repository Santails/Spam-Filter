# Spam Mail Classifier (from Scratch)

A spam mail classifier built using **only the Python Standard Library**. This project was a core assignment for the B4B33RPH course at ČVUT, where the use of external machine learning libraries like scikit-learn, pandas, or nltk was prohibited.

The primary goal was to implement a complete machine learning pipeline—from text processing to model training and evaluation—from first principles.

---

### ► Core Implementation Details

*   **Algorithm:** A custom implementation of the Naive Bayes classification algorithm.
*   **Text Processing:** Includes a self-built tokenizer to split emails into words and a vectorizer to count word frequencies (bag-of-words).
*   **Evaluation:** Measures filter quality based on a custom formula provided by the course, heavily penalizing false positives.

---

### ► Technologies Used

*   **Python 3 (Standard Library Only)**

---

### ► How to Use

1.  **Clone the repository:**
    ```bash
    git clone [your-repository-url.git]
    cd [repository-folder-name]
    ```

2.  **Run the classifier:**
    *(No installation is required as no external dependencies are used.)*
    ```bash
    python main.py "your sample email text here"
    ```
