FROM python:3.7-slim AS build_env

ARG TVM_VERSION=v0.6.1

RUN apt-get update && apt install -y \
    build-essential \
    git \
    cmake \
    python3-dev \
    libsm6 \
    libxext6 \
    libxrender1 \
    libglib2.0-bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /opt

RUN git clone --recursive --branch ${TVM_VERSION} https://github.com/apache/incubator-tvm tvm
    
RUN cd tvm && \ 
    mkdir build && \
    cp cmake/config.cmake build && \
    cd build && \
    cmake .. && \
    make runtime -j && \
    cd ../python && \
    python setup.py install && \
    cd ../topi/python && \
    python setup.py install


RUN apt-get –purge remove \
    build-essential \
    git \
    cmake \
    python3-dev

RUN python3 -m pip install --upgrade --no-cache-dir \
    numpy \
    decorator \
    attrs \
    opencv-python \ 
    scipy \
    uvicorn \
    fastapi