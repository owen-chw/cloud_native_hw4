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

## 設計邏輯
- 只要push to  main branch或pull request to main branch就會觸發github action
- tag為當下github action被觸發當下的日期時間
- github action的設計邏輯:
  1. checkout code
  2. setup Buildx
  3. put the timestamp into environment
  4. login Dockerhub
  5. build and push imge
  ```
    build-and-push:

    runs-on: ubuntu-latest
    environment: env

    steps:
    - name: checkout code
      uses: actions/checkout@v4

    - name: setup Docker Buildx
      uses: docker/setup-buildx-action@v3
      
    - name: set tag as timestamp
      run: echo "IMAGE_TAG=$(date +'%Y%m%d-%H%M%S')" >> $GITHUB_ENV


    - name: login Dockerhub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: build and push image
      uses: docker/build-push-action@v5
      with:
         context: .
         file: ./Dockerfile
         push: true
         tags: owen2chw/2025cloud:${{ env.IMAGE_TAG }}
  ```
