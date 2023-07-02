FROM eclipse-temurin:17.0.6_10-jdk-jammy

FROM gradle:6.8.3-jdk8 AS build

COPY build.gradle .

COPY settings.gradle

COPY src ./src

RUN gradle clean build -x test

FROM openjdk:8-jdk-alpine

LABEL maintainer="austinbreathesair@gmail.com"

VOLUME /tmp

EXPOSE 8080

# STEP 1: Add the executable jar file in this container

ARG JAR_FILE=build/libs/helloworld.jar

ADD ${JAR_FILE} helloworld.jar

# STEP 2: Run the application when the container starts

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/helloworld.jar"]