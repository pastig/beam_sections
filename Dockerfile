# Python stage
FROM python:3.11.3-buster AS python-build

WORKDIR /app

# Install dependencies
ADD requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Add the rest of the code
ADD . /app

# MikTex stage
FROM miktex/miktex AS miktex-build

WORKDIR /miktex/work

# Final stage
FROM python:3.11.3-buster

# Copy Python dependencies
COPY --from=python-build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copy Django app
COPY --from=python-build /app/ /app/

# Copy MikTex
COPY --from=miktex-build /miktex /miktex

WORKDIR /app

# Expose the port that the Django development server will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
