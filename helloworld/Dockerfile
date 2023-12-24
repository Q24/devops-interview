FROM eclipse-temurin:17.0.8_7-jdk-alpine

WORKDIR /app
COPY . .
RUN ./gradlew clean build

ENTRYPOINT ["java", "-jar", "/app/build/libs/helloworld.jar"]
