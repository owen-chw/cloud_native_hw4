# Simple calculator
This is the assignment 4 for NTU cloud native-class to demo the intergration of Github Action and Docker Hub

## Build the image
Before this step, you need to have installed docker in your host
Then, run the following command in the working directory:
```
docker build . -t calculator
```

## Run the application container
After building the image, run the following command to run the calculator!
```
docker run -it calculator
```