Project Unknown: AI Filter Suite v1.0

Welcome to Project Unknown. This is a high-performance image processing application that bridges the gap between raw matrix mathematics and modern web architecture.

Core Engineering Concepts
This project isn't just about changing colors; it's about Vectorized Operations. By using NumPy, we avoid slow Python loops and perform calculations across the entire image grid (tensor) simultaneously.

Features
Night Vision: Isolation of the green channel with a $2\times$ gain boost and pixel clipping to prevent overflow.
Vintage Sepia: A professional-grade transformation using specific channel weighting:$R' = (0.393 \cdot R) + (0.769 \cdot G) + (0.189 \cdot B)
Noir (Grayscale): Luminance averaging across the RGB stack.
Color Pop: Direct channel swapping to demonstrate 3D array manipulation.

How to Run the Project

Follow these steps to get the suite running on your local machine:

Clone the Repository
git clone https://github.com/YOUR_USERNAME/Project_Unknown_Filters.git
cd Project_Unknown_Filters


Install Dependencies
Make sure you have Python installed, then run:
pip install -r requirements.txt

Start the Backend API
Run the FastAPI server using Uvicorn:
uvicorn main:app --reload



The API will be live at http://127.0.0.1:8000

Launch the Frontend
Simply open index.html in any modern web browser (Chrome, Edge, or Firefox).