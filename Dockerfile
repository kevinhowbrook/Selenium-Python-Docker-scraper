FROM ubuntu:14.04

ENV BROWSER Firefox
ENV DISPLAY :99

#================================================
# Installations
#================================================

RUN apt-get update && apt-get install -y $BROWSER \
        build-essential libssl-dev python-setuptools \
        vim xvfb xz-utils zlib1g-dev

RUN easy_install pip

RUN pip install selenium pyvirtualdisplay requests unittest-xml-reporting

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

