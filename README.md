Python Project:

Author: Terry Sun

Date: 2019-09-23


FROM alpine/git as clone
WORKDIR /app
RUN git clone https://terrysun73:Su20181001@github.com/terrysun73/mypython.git

FROM python:3.7 as build
WORKDIR /usr/src/app
COPY --from=clone /app/* /usr/src/app
RUN pip install numpy scipy yfinance requests lxml
CMD [ "python", "/usr/src/app/d7.py" ]
