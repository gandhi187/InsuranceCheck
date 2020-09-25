# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:2.0.0rc1

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
# RUN pip install -r requirements-actions.txt
RUN pip install pycountry_convert
RUN pip install openpyxl
RUN pip install requests
RUN pip install psycopg2-binary
# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001