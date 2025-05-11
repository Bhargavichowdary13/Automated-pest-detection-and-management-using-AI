# Automated-pest-detection-and-management-using-AI
Automated Pest Detection using AI identifies and classifies pests in crops, enabling early detection and efficient management.

pest images:
[https://universe.roboflow.com/aimit-b7yve/pests-in-cucumber-plants-jegly](url)

Star method for this project:

Situation:
Agricultural productivity is significantly affected by pest infestations, leading to crop damage and financial losses. Traditional pest detection methods are manual, time-consuming, and require expert intervention, which is impractical for large-scale farming.

Task:
The goal was to develop an AI-based system that could automatically identify pests in cucumber plants and provide pesticide recommendations in real time. The system needed to be accurate, scalable, and easily accessible for farmers.

Action:
To achieve this, I followed a structured approach:

Data Collection & Preprocessing:

Gathered pest-infected cucumber plant images from Kaggle and research databases.

Applied preprocessing techniques like resizing, normalization, and data augmentation to enhance model performance.

Split data into training, validation, and test sets for better generalization.

Model Development & Training:

Built a CNN model for pest classification.

Implemented ResNet and VGG-16 architectures and fine-tuned them for improved accuracy.

Trained the models using TensorFlow & Keras, evaluating performance using accuracy, confusion matrix, precision, and recall.

Model Conversion & Deployment:

Saved the best-performing model in .h5 format and converted it to JSON for API integration.

Deployed the model on Hugging Face API, generating an API endpoint for easy access.

Frontend Development & System Execution:

Designed a user-friendly web interface using HTML & CSS, allowing users to upload images for pest detection.

Integrated the API to display real-time results with pesticide recommendations.

Tested the system with multiple pest images to ensure smooth end-to-end functionality.

Result:

Achieved 90% accuracy in pest detection.

Provided real-time pesticide recommendations, helping farmers take immediate action.

Created a scalable, user-friendly, and accessible solution for large-scale agricultural use.




