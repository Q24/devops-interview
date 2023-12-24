FROM eclipse-temurin:17.0.8_7-jdk-alpine as build

WORKDIR /workspace/app
COPY . .
RUN ./gradlew clean build


FROM eclipse-temurin:17.0.8_7-jre-alpine as runtime

WORKDIR /app
COPY --from=build /workspace/app/build/libs/helloworld.jar .

ENTRYPOINT ["java", "-jar", "helloworld.jar"]
