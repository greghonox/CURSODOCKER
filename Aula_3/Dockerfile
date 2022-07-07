FROM kasmweb/core-ubuntu-bionic:1.10.0
USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########

# Install Google Chrome
COPY ./src/ubuntu/install/chrome $INST_SCRIPTS/chrome/
RUN bash $INST_SCRIPTS/chrome/install_chrome.sh  && rm -rf $INST_SCRIPTS/chrome/

# Install VLC
RUN apt-get update && apt-get install -y vlc

# Install Shotcut
COPY ./src/ubuntu/install/shotcut/Shotcut.desktop $HOME/Desktop/
WORKDIR /tmp
RUN wget https://github.com/mltframework/shotcut/releases/download/v21.10.31/shotcut-linux-x86_64-211031.txz && \
    tar -xf shotcut-linux-x86_64-211031.txz -C /opt

######### End Customizations ###########

RUN chown 1000:0 $HOME
RUN $STARTUPDIR/set_user_permission.sh $HOME

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000
