import os
import numpy as np
from PIL import Image

from django.shortcuts import render
from tensorflow.keras.models import load_model
from django.conf import settings

model = load_model("my_model.keras")


def home(request):

    prediction = None
    image_url = None

    if request.method == "POST":

        image = request.FILES["image"]

        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        image_path = os.path.join(settings.MEDIA_ROOT, image.name)

        with open(image_path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        image_url = settings.MEDIA_URL + image.name

        img = Image.open(image_path).convert("RGB")
        img = img.resize((256, 256))

        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        y = model.predict(img)

        if y[0][0] <= 0.5   :
            prediction = "Fake"
        else:
            prediction = "Real"

    return render(request, "index.html", {
        "prediction": prediction,
        "image_url": image_url
    })