# Base image
FROM node:18

# Set working directory
WORKDIR /frontend

# Install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the app
RUN npm run build

# Expose the default Vite port
EXPOSE 5173

# Start the app
CMD ["npm", "run", "dev"]