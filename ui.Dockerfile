FROM nikolaik/python-nodejs:python3.8-nodejs14

RUN pip install -U pip

COPY scripts/wait-for-it.sh .
RUN chmod 755 wait-for-it.sh

WORKDIR /ui

COPY ui/package.json .
COPY ui/package-lock.json .

RUN npm install
RUN npm install react-scripts@3.4.1 -g

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /ui

COPY ui /ui
RUN npm run build

WORKDIR /

COPY brain /brain
RUN mv /ui/build /brain/ui
