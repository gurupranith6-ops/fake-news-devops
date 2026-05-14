BEGIN

    // Load and Prepare Dataset
    LOAD dataset from "train.csv"
    EXTRACT columns: title, text, label
    FOR each record in dataset:
        COMBINE title and text into single field "content"
    END FOR

    // Preprocessing
    REMOVE empty or null entries
    SPLIT data into training set and testing set (80:20 ratio)

    // Feature Extraction using TF-IDF
    INITIALIZE TF-IDF Vectorizer with English stopwords
    FIT vectorizer on training content
    TRANSFORM training content into numerical vectors
    TRANSFORM testing content using the same vectorizer

    // Model Training
    INITIALIZE Logistic Regression model
    TRAIN model using training vectors and training labels

    // Model Evaluation
    PREDICT labels for test data
    COMPUTE accuracy, precision, recall (optional)

    // Save Model
    SAVE trained model as "model.pkl"
    SAVE fitted TF-IDF vectorizer as "vectorizer.pkl"

    // Begin Flask Application
    START Flask web server

    ON user accessing homepage:
        RENDER input interface

    ON user submitting news text:
        READ input text from form

        IF input text is empty THEN
            RETURN interface without prediction
        END IF

        // Process User Input
        TRANSFORM input text using saved vectorizer
        APPLY trained model to predict class

        IF predicted class = 1 THEN
            SET result = "FAKE NEWS"
        ELSE
            SET result = "REAL NEWS"
        END IF

        DISPLAY result on web interface
    END ON

END
