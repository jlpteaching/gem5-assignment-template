FROM gcr.io/gem5-test/ubuntu-20.04_all-dependencies:stable AS builder

RUN apt -y update
RUN apt -y install git

# Clone gem5
RUN git clone -b stable https://gem5.googlesource.com/public/gem5

# build gem5 ALL fast
WORKDIR /gem5
RUN scons -j`nproc` build/ALL/gem5.fast

# The actual container that we're going to use
FROM gcr.io/gem5-test/ubuntu-20.04_all-dependencies:stable

COPY --from=builder /gem5/build/ALL/gem5.fast /usr/local/bin/gem5

RUN pip install -r requirements.txt