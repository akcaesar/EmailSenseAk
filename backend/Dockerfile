# Use a Conda-based image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the backend code to the container
COPY . .

# Create the Conda environment using the requirements.txt file
RUN conda create --name emailsense_env python=3.8 -y

# Activate the Conda environment and install dependencies
# Use `conda run` to execute commands within the Conda environment
RUN /bin/bash -c "source activate emailsense_env && pip install -r requirements.txt"

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["/bin/bash", "-c", "source activate emailsense_env && uvicorn main:app --host 0.0.0.0 --port 8000"]