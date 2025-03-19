# filepath: /workspaces/codespaces-blank/EmailSense_cp/backend/Dockerfile
# Use a Conda-based image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the backend code to the container
COPY . .

# Create the Conda environment using the requirements.txt file
RUN conda create --name emailsense_env --file requirements.txt python=3.10 -y

# Activate the Conda environment and install Uvicorn
RUN echo "conda activate emailsense_env" > ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc && conda activate emailsense_env && pip install uvicorn"

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["/bin/bash", "-c", "source ~/.bashrc && conda activate emailsense_env && uvicorn main:app --host 0.0.0.0 --port 8000"]