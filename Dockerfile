FROM ubuntu:14.04

ENV BROWSER Firefox
ENV DISPLAY :99

#================================================
# Installations
#================================================

RUN apt-get update && apt-get install -y $BROWSER \
        build-essential libssl-dev python-setuptools \
        vim xvfb xz-utils zlib1g-dev wget

RUN easy_install pip
RUN sudo pip install -U selenium
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
RUN tar xvzf geckodriver-v0.19.0-linux64.tar.gz -C /usr/local/bin
CMD export PATH=$PATH:/usr/local/bin/geckodriver
RUN pip install pyvirtualdisplay requests unittest-xml-reporting

#==================
# Vim highlight
#==================

RUN echo "syntax on" >> /etc/vim/vimrc

#==================
# Xvfb + init scripts
#==================
ADD libs/xvfb_init /etc/init.d/xvfb
RUN chmod a+x /etc/init.d/xvfb

ADD libs/xvfb-daemon-run /usr/bin/xvfb-daemon-run
RUN chmod a+x /usr/bin/xvfb-daemon-run

#============================
# Clean up
#============================
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

