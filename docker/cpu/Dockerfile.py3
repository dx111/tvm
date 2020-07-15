FROM python:3.7-slim AS build_env

ARG TVM_VERSION=v0.6.1

RUN apt-get update && apt install -y build-essential git cmake

WORKDIR /workspace

RUN git clone --recursive --branch ${TVM_VERSION} https://github.com/apache/incubator-tvm tvm
    
RUN cd tvm && \ 
    mkdir build && \
    cp cmake/config.cmake build && \
    cd build && \
    cmake .. && \
    make runtime -j

FROM python:3.7-slim

COPY --from=build_env /workspace/tvm /usr/local/tvm

ENV TVM_HOME /usr/local/tvm

ENV PYTHONPATH=$TVM_HOME/python:$TVM_HOME/topi/python:${PYTHONPATH}
