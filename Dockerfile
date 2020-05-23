FROM nikolaik/python-nodejs:python3.8-nodejs14

RUN pip install -U pip

WORKDIR /ui

COPY ui/package.json .
COPY ui/yarn.lock .

RUN npm install
RUN npm install react-scripts@3.4.1 -g

COPY ui /ui
RUN npm run build

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/wait-for-it.sh .
RUN chmod 755 wait-for-it.sh

COPY brain /brain

RUN mv /ui/build /brain/ui
