from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI,UploadFile,File,Query
import io
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

# # Using the 'r' prefix to fix the path issue
# img_path = r"C:\Users\Milan Singh\Desktop\img.jpg"
# img = Image.open(img_path)


class PhotoFilter:
    def __init__(self, image):
        # We keep the original as float for math accuracy, processed as uint8 for display
        self.original = image.copy().astype(float)
        self.processed = image.copy().astype(np.uint8)

    def nightVision(self):
        nv = self.original.copy()
        nv[:,:,[0,2]] = 0 # Kill Red and Blue
        nv[:,:,1] = np.clip(nv[:,:,1] * 2, 0, 255) # Boost Green and CLIP!
        self.processed = nv.astype(np.uint8)
        return self.processed
    
    def noir(self):
        res = PhotoFilter.rgb(self.original.copy())
        average = (res["red"] + res["green"] + res["blue"]) / 3
        # Use our helper with Red, Green, Blue in order
        self.processed = PhotoFilter.rgbConversion(self.original.copy(), average, average, average)
        return self.processed
    
    def vintageSepia(self):
        res = PhotoFilter.rgb(self.original.copy())
        r, g, b = res["red"], res["green"], res["blue"]
        
        newRed = (0.393 * r) + (0.769 * g) + (0.189 * b)
        newGreen = (0.349 * r) + (0.686 * g) + (0.168 * b)
        newBlue = (0.272 * r) + (0.534 * g) + (0.131 * b)
        
        self.processed = PhotoFilter.rgbConversion(self.original.copy(), newRed, newGreen, newBlue)
        return self.processed

    @staticmethod
    def rgb(image):
        return {
            "red": image[:,:,0],
            "green": image[:,:,1],
            "blue": image[:,:,2]
        }

    @staticmethod
    def rgbConversion(image, r, g, b):
        # Correcting the index: Red=0, Green=1, Blue=2
        image[:,:,0] = np.clip(r, 0, 255)
        image[:,:,1] = np.clip(g, 0, 255)
        image[:,:,2] = np.clip(b, 0, 255)
        return image.astype(np.uint8)





app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all websites to talk to your API
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/filter")
async def photo_filter_api(
    # We change this to a Query parameter for easier browser testing
    filtername: str = Query(..., description="nightvision, noir, or vintagesepia"),
    file: UploadFile = File(...)
):
    # 1. READ the uploaded file
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    
    # 2. Convert and Process
    img_array = np.array(img)
    filter_engine = PhotoFilter(img_array)

    fname = filtername.lower()
    
    if fname == "nightvision":
        result = filter_engine.nightVision()
    elif fname == "noir":
        result = filter_engine.noir()
    elif fname == "vintagesepia":
        result = filter_engine.vintageSepia()
    else:
        return {"message": "Filter not available. Choose: nightvision, noir, or vintagesepia"}

    # 3. CONVERT back to image format to send to browser
    filtered_img = Image.fromarray(result)
    
    # Create a virtual file in RAM
    img_io = io.BytesIO()
    filtered_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0) # Go back to the start of the file

    # 4. Return the ACTUAL image file
    return StreamingResponse(img_io, media_type="image/jpeg")
