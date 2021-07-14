FROM rust:latest

WORKDIR /usr/src/api
COPY . .

RUN cargo install --path .

CMD ["api"]