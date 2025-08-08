FROM golang:1.23 AS build
WORKDIR /app
COPY go.mod .
RUN go mod download
COPY . .
RUN go build -o gateway .

FROM alpine:latest
COPY --from=build /app/gateway /gateway
CMD ["/gateway"]
