FROM eclipse-temurin:17.0.8_7-jdk-alpine as app-builder

# Build the app by using gradlew
RUN mkdir /app
WORKDIR /app
COPY  . .
WORKDIR /app/helloworld
RUN ./gradlew clean build

# Copy the created Jar file from previous build to new  
FROM openjdk:19-jdk-alpine
WORKDIR /app
COPY --from=app-builder /app/helloworld/build/libs/helloworld.jar .
# STEP 2: Run the application when the container starts
EXPOSE 8080
CMD ["java","-XX:+UseG1GC" ,"-Djava.security.egd=file:/dev/./urandom", "-jar", "helloworld.jar"]
